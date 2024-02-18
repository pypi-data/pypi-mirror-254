from __future__ import annotations

import random
import re
from collections import UserDict
from collections.abc import Iterator
from contextlib import contextmanager, suppress
from typing import ClassVar, Final, Literal, overload

from . import RICH_AVAILABLE, WORKING_DIRECTORY
from .types import (
    BLACK_SQUARES,
    CASTLING_DEFAULT_CHARS,
    CASTLING_FINAL_SQUARES,
    COLORS,
    FEN_REPRESENTATIONS,
    FILES,
    PIECE_SYMBOLS,
    PIECE_VALUES,
    PIECES_TO_TRACK,
    PLAINTEXT_ABBRS,
    PLAINTEXT_ABBRS_BY_TYPE_AND_COLOR,
    SIDES,
    SQUARES,
    WHITE_SQUARES,
    Color,
    GameStatus,
    Piece,
    PieceType,
    Side,
)
from .utils import (
    _COLORS_AND_RANKS,
    _GENERATORS_AND_TYPES,
    _PAWN_RANK_BY_COLOR,
    BISHOP_GENERATORS,
    FORWARD_STEP_FUNCTIONS_BY_PAWN_COLOR,
    GENERATORS_BY_PIECE_TYPE,
    ROOK_GENERATORS,
    en_passant_final_square_from_file,
    en_passant_final_square_from_pawn_square,
    get_adjacent_files,
    get_adjacent_squares,
    get_squares_between,
    king_navigable_squares,
    knight_navigable_squares,
    other_color,
    pawn_capturable_squares,
    squares_in_rank,
    step_right,
)

if RICH_AVAILABLE:
    from rich.console import Console


with (WORKING_DIRECTORY / "data" / "fischer_fens.fen").open() as file:
    FISCHER_SETUPS: list[str] = file.readlines()


class ChessPosition(UserDict[str, Piece | None]):
    """A standard chess position."""

    AUTOPRINT: ClassVar[bool] = False
    """Print board upon `__repr__` call."""

    def __init__(
        self, __dict: dict[str, Piece | None] | None = None, /, **kwargs: Piece | None
    ) -> None:
        if __dict is None:
            __dict = {square: None for square in SQUARES}
        super().__init__(__dict, **kwargs)
        self.turn: Color = "white"
        self.initial_squares: Final[
            dict[tuple[PieceType, Color, Side | None], str]
        ] = {}
        self.has_moved: Final[dict[tuple[PieceType, Color, Side | None], bool]] = {
            piece_tuple: False for piece_tuple in PIECES_TO_TRACK
        }
        self.kings: Final[dict[Color, str]] = {}
        self._double_forward_last_move: str | None = None
        self._piece_count: int = 0

    def __setitem__(self, key: str, value: Piece | None) -> None:
        """Set a square to a piece or None if setting to empty."""
        if value is not None and value.piece_type == "king":
            self.kings[value.color] = key
        super().__setitem__(key, value)

    def __repr__(self) -> str:
        """Represent position as string."""
        if self.AUTOPRINT:
            self.print()
        return f"{self.__class__.__name__}('{self.export_bare_fen()}')"

    def __hash__(self) -> int:
        """Hash position."""
        return hash(
            (
                (black_king_has_moved := self.has_moved["king", "black", None])
                or self.has_moved["rook", "black", "kingside"],
                black_king_has_moved or self.has_moved["rook", "black", "queenside"],
                (white_king_has_moved := self.has_moved["king", "white", None])
                or self.has_moved["rook", "white", "kingside"],
                white_king_has_moved or self.has_moved["rook", "white", "queenside"],
                self._double_forward_last_move if self.can_en_passant() else None,
                self.turn,
                *self.values(),
            )
        )

    @classmethod
    def with_staunton_pattern(cls) -> ChessPosition:
        """Set Staunton pattern (initial piece squares)."""
        board = cls()
        for color, pc_rank, pawn_rank in _COLORS_AND_RANKS:
            for file in FILES:
                board[f"{file}{pawn_rank}"] = Piece("pawn", color)
            board[f"a{pc_rank}"] = Piece("rook", color)
            board[f"b{pc_rank}"] = Piece("knight", color)
            board[f"c{pc_rank}"] = Piece("bishop", color)
            board[f"d{pc_rank}"] = Piece("queen", color)
            board[f"e{pc_rank}"] = Piece("king", color)
            board[f"f{pc_rank}"] = Piece("bishop", color)
            board[f"g{pc_rank}"] = Piece("knight", color)
            board[f"h{pc_rank}"] = Piece("rook", color)
        return board

    @classmethod
    def with_fischer_random_pattern(cls) -> ChessPosition:
        """Set board for Fischer random chess / Chess960."""
        board = cls()
        fen = random.choice(FISCHER_SETUPS)
        board.import_bare_fen(fen)
        return board

    @property
    def pieces(self) -> dict[str, Piece]:
        """Get all pieces on the board."""
        return {sq: piece for sq, piece in self.items() if piece is not None}

    @contextmanager
    def test_position(self, changes: dict[str, Piece | None]) -> Iterator[None]:
        """
        Make temporary changes to the board to test properties of a position.
        Warning: Do not raise exceptions within a `test_position` context manager.
        """
        original_contents = {sq: self[sq] for sq in changes}
        for sq in changes:
            self[sq] = changes[sq]
        yield
        for sq in original_contents:
            self[sq] = original_contents[sq]

    def print(self, *, plaintext: bool = False) -> None:
        """Print the ChessBoard to console."""
        if not plaintext and RICH_AVAILABLE:
            Console().print(self._rich_renderable())
        else:
            print(self._ascii())

    def _ascii(self) -> str:
        """Get an ASCII representation of the board."""
        winning_king_sq = None
        output = ""
        for rank in range(8, 0, -1):
            output += f"{rank} "
            for sq in squares_in_rank(rank):
                if (piece := self[sq]) is None:
                    output += ". "
                else:
                    output += (
                        f"{PLAINTEXT_ABBRS[piece.piece_type].upper()}"
                        f"{'#' if sq == winning_king_sq else ' '}"
                        if piece.color == "white"
                        else f"{PLAINTEXT_ABBRS[piece.piece_type].lower()} "
                    )
            output += "\n"
        output += "  a b c d e f g h "
        return output

    def _rich_renderable(self) -> str:
        """Get a Rich renderable representation of the board."""
        rank_renderable = "\n"
        for rank in range(8, 0, -1):
            rank_renderable += f"[white]{rank}[/white] "
            for sq in squares_in_rank(rank):
                piece = self[sq]
                if piece is not None:
                    color_tags = (
                        ("[reverse][#ffffff]", "[/#ffffff][/reverse]")
                        if piece.color == "white"
                        else ("[white]", "[/white]")
                    )
                    rank_renderable += (
                        f"{color_tags[0]}{PIECE_SYMBOLS[piece.piece_type]}"
                        f" {color_tags[1]}"
                    )
                else:
                    rank_renderable += (
                        "[reverse][#789656]  [/reverse][/#789656]"
                        if sq in BLACK_SQUARES
                        else "[reverse][#f0edd1]  [/reverse][/#f0edd1]"
                    )
            rank_renderable += "\n"
        rank_renderable += "[bold][white]  a b c d e f g h [/bold][/white]\n"
        return rank_renderable

    def king_is_in_check(self, color: Color) -> bool | None:
        """Whether the king is in check."""
        return (
            None
            if (king_sq := self.kings.get(color)) is None
            else self.is_checked_square(color, king_sq)
        )

    def _is_checked_by_rook_bishop_queen(self, color: Color, king_sq: str) -> bool:
        for generator_list, types in _GENERATORS_AND_TYPES:
            for generator in generator_list:
                for sq in generator(king_sq):
                    if (
                        (pc := self[sq]) is not None
                        and pc.color != color
                        and pc.piece_type in types
                    ):
                        return True
                    elif pc is not None:
                        break
        return False

    def _is_checked_by_pawn(self, color: Color, king_sq: str) -> bool:
        return any(
            (pc := self[sq]) is not None
            and pc.piece_type == "pawn"
            and pc.color == other_color(color)
            for sq in pawn_capturable_squares(color, king_sq)
        )

    def _is_checked_by_king(self, color: Color, king_sq: str) -> bool | None:
        return (
            king in king_navigable_squares(king_sq)
            if (king := self.kings.get(other_color(color))) is not None
            else None
        )

    def _is_checked_by_knight(self, color: Color, king_sq: str) -> bool:
        return any(
            (pc := self[sq]) is not None
            and pc.piece_type == "knight"
            and pc.color == other_color(color)
            for sq in knight_navigable_squares(king_sq)
        )

    def _pseudolegal_squares(
        self,
        initial_square: str,
        *,
        capture_only: bool = False,
        check_castle: bool = True,
    ) -> Iterator[str]:
        """
        Get all pseudolegal squares for a given piece. This includes squares occupied by
        the opponent king or which, if moved to, would put the king in check. Use
        ChessBoard.legal_moves() to only include legal moves.

        If capture_only is True, only include squares which are eligible for capture.
        In other words, pawn forward moves will not be included in return list.

        If check_castle is True, yield post-castling positions for kings.
        """
        piece = self._get_piece_at_non_empty_square(initial_square)
        match piece.piece_type:
            case "pawn":
                return self._pawn_pseudolegal_squares(
                    initial_square, piece, capture_only=capture_only
                )
            case "rook" | "queen" | "bishop":
                return self._queen_rook_bishop_pseudolegal_squares(
                    initial_square, piece
                )
            case "knight":
                return self._knight_pseudolegal_squares(initial_square, piece)
            case "king":
                return self._king_pseudolegal_squares(
                    initial_square,
                    piece,
                    check_castle=(check_castle and not capture_only),
                )

    def _get_piece_at_non_empty_square(self, square: str) -> Piece:
        if (piece := self[square]) is None:
            raise ValueError(f"No piece at square '{square}'.")
        return piece

    def _pawn_pseudolegal_squares(
        self,
        initial_square: str,
        piece: Piece,
        *,
        capture_only: bool = False,
    ) -> Iterator[str]:
        step_func = FORWARD_STEP_FUNCTIONS_BY_PAWN_COLOR[piece.color]
        # forward and double forward advance
        if (
            not capture_only
            and (sq := step_func(initial_square, 1)) is not None
            and self[sq] is None
        ):
            yield sq
            if (
                initial_square[1] == _PAWN_RANK_BY_COLOR[piece.color]
                and (sq := step_func(initial_square, 2)) is not None
                and self[sq] is None
            ):
                yield sq
        # diagonal capture
        yield from (
            sq
            for sq in pawn_capturable_squares(piece.color, initial_square)
            if (pc := self[sq]) is not None and pc.color != piece.color
        )
        # en passant capture
        if self._double_forward_last_move in get_adjacent_squares(initial_square):
            yield en_passant_final_square_from_pawn_square(
                self._double_forward_last_move, piece.color
            )

    def _queen_rook_bishop_pseudolegal_squares(
        self, initial_square: str, piece: Piece
    ) -> Iterator[str]:
        for generator in GENERATORS_BY_PIECE_TYPE[piece.piece_type]:
            for sq in generator(initial_square):
                if (other_piece := self[sq]) is None:
                    yield sq
                else:
                    if other_piece.color != piece.color:
                        yield sq
                    break

    def _knight_pseudolegal_squares(
        self, initial_square: str, piece: Piece
    ) -> Iterator[str]:
        return (
            sq
            for sq in knight_navigable_squares(initial_square)
            if (pc := self[sq]) is None or pc.color != piece.color
        )

    def _king_pseudolegal_squares(
        self,
        initial_square: str,
        piece: Piece,
        *,
        check_castle: bool = False,
    ) -> Iterator[str]:
        yield from (
            sq
            for sq in king_navigable_squares(initial_square)
            if (pc := self[sq]) is None or pc.color != piece.color
        )
        if check_castle:
            yield from (
                CASTLING_FINAL_SQUARES[piece.color, side][0]
                for side in SIDES
                if self.can_castle(piece.color, side)
            )

    def is_checked_square(self, color: Color, square: str) -> bool:
        """Whether a square is threatened by an opposite color piece."""
        return (
            self._is_checked_by_rook_bishop_queen(color, square)
            or self._is_checked_by_pawn(color, square)
            or self._is_checked_by_king(color, square)
            or self._is_checked_by_knight(color, square)
        )

    def checked_squares(self, color: Color) -> Iterator[str]:
        """Get all checked squares for a color."""
        oc = other_color(color)
        other_color_pieces = [
            sq for sq, pc in self.items() if pc is not None and pc.color == oc
        ]
        already_yielded: list[str] = []
        for init_sq in other_color_pieces:
            for sq in self._pseudolegal_squares(
                init_sq, capture_only=True, check_castle=False
            ):
                if sq not in already_yielded:
                    yield sq
                    already_yielded.append(sq)

    def get_threatening_pieces(
        self,
        square: str,
        color: Color | None = None,
        *,
        square_is_empty: bool = False,
    ) -> dict[str, Piece]:
        """
        Get pieces threatening a square. If include_all_pawn_moves, includes forward
        move to tile.
        """
        threatening_pieces: list[tuple[str, Piece]] = []
        color_ = (
            self._get_piece_at_non_empty_square(square).color
            if color is None
            else color
        )
        for generator_list, types in (
            (ROOK_GENERATORS, ("rook", "queen")),
            (BISHOP_GENERATORS, ("bishop", "queen")),
        ):
            for generator in generator_list:
                for sq in generator(square):
                    if (
                        (pc := self[sq]) is not None
                        and pc.color != color_
                        and pc.piece_type in types
                    ):
                        threatening_pieces.append((sq, pc))
                        break
                    elif pc is not None:
                        break
        oc = other_color(color_)
        if (other_king := self.kings.get(oc)) in king_navigable_squares(square):
            pc = self._get_piece_at_non_empty_square(other_king)
            threatening_pieces.append((other_king, pc))
        sq_iterators: list[tuple[PieceType, tuple[str, ...]]] = [
            ("knight", knight_navigable_squares(square))
        ]
        if not square_is_empty:
            sq_iterators.append(("pawn", pawn_capturable_squares(color_, square)))
        threatening_pieces.extend(
            (sq, pc)
            for pt, iterator in sq_iterators
            for sq in iterator
            if (pc := self[sq]) is not None and pc.piece_type == pt and pc.color == oc
        )
        if square_is_empty and (
            (
                (sq_ := FORWARD_STEP_FUNCTIONS_BY_PAWN_COLOR[color_](square, 1))
                is not None
                and (pc := self[sq_]) is not None
                and pc.piece_type == "pawn"
                and pc.color == oc
            )
            or (
                pc is None
                and (sq_ := FORWARD_STEP_FUNCTIONS_BY_PAWN_COLOR[color_](square, 2))
                is not None
                and sq_[1] in ("2", "7")
                and (pc := self[sq_]) is not None
                and pc.piece_type == "pawn"
                and pc.color == oc
            )
        ):
            threatening_pieces.append((sq_, pc))
        return dict(threatening_pieces)

    def _infer_en_passant_initial_square(self) -> str | None:
        double_forward = self._get_double_forward_last_move_strict()
        candidates = [
            sq
            for sq in get_adjacent_squares(double_forward)
            if (pc := self[sq]) is not None
            and pc.piece_type == "pawn"
            and pc.color == self.turn
        ]
        match len(candidates):
            case 1:
                return candidates[0]
            case 2:
                candidates = [cand for cand in candidates if self.can_en_passant(cand)]
                return candidates[0] if len(candidates) == 1 else None
            case _:
                return None

    def _get_double_forward_last_move_strict(self) -> str:
        if (result := self._double_forward_last_move) is None:
            raise ValueError("No pawn can be captured by en passant.")
        return result

    def _can_drop_out_of_check(
        self,
        drop_pool: list[PieceType] | None,
        checks: dict[str, Piece],
        squares_that_would_block_check: list[str],
    ) -> bool:
        """
        In variants like Crazyhouse, a piece can be dropped on the board to block
        checkmate. Returns True if player can drop a piece to escape check.
        """
        if drop_pool is not None and drop_pool != [] and len(checks) == 1:
            for sq in squares_that_would_block_check:
                if sq not in checks and not (
                    set(drop_pool) == {"pawn"} and sq[1] in ("1", "8")
                ):
                    return True
        return False

    def _en_passant_can_block_check(self, color: Color) -> bool:
        if self._double_forward_last_move is not None:
            for square in get_adjacent_squares(self._double_forward_last_move):
                if (
                    (piece := self[square]) is not None
                    and piece.piece_type == "pawn"
                    and piece.color == color
                    and self.can_en_passant(square)
                ):
                    with self.test_position(
                        {
                            self._double_forward_last_move: None,
                            square: None,
                            en_passant_final_square_from_pawn_square(
                                self._double_forward_last_move, color
                            ): Piece("pawn", color),
                        }
                    ):
                        if not self.king_is_in_check(color):
                            return True
        return False

    def set_initial_positions(self) -> None:
        """Set initial positions of pieces used for castling."""
        for color in COLORS:
            rooks = [
                sq
                for sq, pc in self.items()
                if pc is not None and pc.piece_type == "rook" and pc.color == color
            ]
            match len(rooks):
                case 2:
                    (
                        self.initial_squares["rook", color, "queenside"],
                        self.initial_squares["rook", color, "kingside"],
                    ) = (
                        (rooks[0], rooks[1])
                        if FILES.index(rooks[0][0]) < FILES.index(rooks[1][0])
                        else (rooks[1], rooks[0])
                    )
                case 1:
                    for side in SIDES:
                        self.initial_squares["rook", color, side] = rooks[0]
            if self.kings.get(color) is None:
                with suppress(StopIteration):
                    self.kings[color] = next(
                        sq
                        for sq, pc in self.items()
                        if pc is not None
                        and pc.piece_type == "king"
                        and pc.color == color
                    )
            with suppress(KeyError):
                self.initial_squares["king", color, None] = self.kings[color]
        self._piece_count = len(self.pieces)

    @classmethod
    def import_bare_fen(cls, epd: str) -> ChessPosition:
        """Import FEN to board (move clocks are ignored)."""
        board = cls()
        if match := re.search(
            r"(?P<R8>[^/]+)/(?P<R7>[^/]+)/(?P<R6>[^/]+)/(?P<R5>[^/]+)/"
            r"(?P<R4>[^/]+)/(?P<R3>[^/]+)/(?P<R2>[^/]+)/(?P<R1>[^/\s]+) "
            r"(?P<turn>[wb]) (?P<castling>[KQkqA-Ha-h-]+) (?P<enpassant>[a-h1-8-]+)",
            epd,
        ):
            groups = match.groups()
        else:
            raise ValueError("Could not read notation.")
        for rank, group in zip(range(8, 0, -1), groups[:8], strict=True):
            cursor = f"a{rank}"
            for char in group:
                if char.isalpha():
                    board[cursor] = Piece(*FEN_REPRESENTATIONS[char])
                    if (cur := step_right(cursor, 1)) is not None:
                        cursor = cur
                elif char.isnumeric():
                    board[cursor] = None
                    if (cur := step_right(cursor, int(char))) is not None:
                        cursor = cur
        board.turn = "white" if groups[8] == "w" else "black"
        if groups[10] != "-":
            board._double_forward_last_move = (
                f"{groups[10][0]}{5 if groups[10][1] == 6 else 4}"
            )
        board.set_initial_positions()
        # Set castling availability.
        if groups[9] == "-":
            for color in COLORS:
                board.has_moved["king", color, None] = True
        else:
            for color in COLORS:
                chars_defined = False
                with suppress(KeyError):
                    queenside_rook_char, kingside_rook_char = (
                        sq[0]
                        if (sq := board.initial_squares["rook", color, side])
                        is not None
                        else default_char
                        for side, default_char in CASTLING_DEFAULT_CHARS
                    )
                    # mypyc doesn't support break statements inside try blocks.
                    # chars_defined is used to prevent this from becoming a problem.
                    chars_defined = True
                if chars_defined:
                    has_moved_vars: tuple[tuple[str, str, Color, Side], ...] = (
                        ("K", kingside_rook_char.upper(), "white", "kingside"),
                        ("Q", queenside_rook_char.upper(), "white", "queenside"),
                        ("k", kingside_rook_char, "black", "kingside"),
                        ("q", queenside_rook_char, "black", "queenside"),
                    )
                    for default_char, rook_char, color_, side in has_moved_vars:
                        if all(
                            char not in groups[9] for char in (default_char, rook_char)
                        ):
                            board.has_moved["rook", color_, side] = True
                    break
        return board

    def legal_moves(self, square: str) -> Iterator[str]:
        """Get legal moves for a piece."""
        piece = self._get_piece_at_non_empty_square(square)
        for sq in self._pseudolegal_squares(square):
            # If the piece is a pawn diagonal to the pseudolegal square, and the square
            # at pseudolegal square is None, it must be an en passant.
            if (
                (pt := piece.piece_type) == "pawn"
                and sq[0] in get_adjacent_files(square)
                and self[sq] is None
            ):
                if self.can_en_passant(square):
                    yield sq
            # If the piece is a king, it could be a castle.
            elif (
                pt == "king"
                and (
                    (sq in ("c1", "g1", "c8", "g8") and self.can_castle(piece.color))
                    or self.can_move_piece(
                        square,
                        sq,
                        navigability_already_checked=True,
                    )
                )
            ) or self.can_move_piece(
                square,
                sq,
                navigability_already_checked=True,
            ):
                yield sq

    @overload
    def can_move_piece(
        self,
        initial_square: str,
        final_square: str,
        *,
        navigability_already_checked: bool = False,
        return_explanation_if_false: Literal[False] = False,
    ) -> bool:
        ...

    @overload
    def can_move_piece(
        self,
        initial_square: str,
        final_square: str,
        *,
        navigability_already_checked: bool = False,
        return_explanation_if_false: Literal[True],
    ) -> tuple[bool, str | None]:
        ...

    def can_move_piece(
        self,
        initial_square: str,
        final_square: str,
        *,
        navigability_already_checked: bool = False,
        return_explanation_if_false: bool = False,
    ) -> bool | tuple[bool, str | None]:
        """Check if a piece can be moved to final_square without castling/en passant."""
        piece = self._get_piece_at_non_empty_square(initial_square)
        piece_at_final_square = self[final_square]
        if (
            not navigability_already_checked
            and final_square
            not in self._pseudolegal_squares(initial_square, check_castle=False)
        ):
            return (
                (
                    False,
                    f"Piece at '{initial_square}' cannot navigate to '{final_square}'.",
                )
                if return_explanation_if_false
                else False
            )
        if piece_at_final_square is not None and (
            piece_at_final_square.piece_type == "king"
            or piece_at_final_square.color == piece.color
        ):
            return (
                (False, "Cannot capture king.")
                if return_explanation_if_false
                else False
            )
        with self.test_position({final_square: piece, initial_square: None}):
            if self.king_is_in_check(piece.color):
                return (
                    (
                        False,
                        f"Cannot move piece from '{initial_square}' to '{final_square}'"
                        " because player's king would be put in check.",
                    )
                    if return_explanation_if_false
                    else False
                )
        return (True, None) if return_explanation_if_false else True

    @overload
    def can_castle(
        self,
        color: Color,
        side: Side | None = None,
        *,
        return_explanation_if_false: Literal[False] = False,
    ) -> bool:
        ...

    @overload
    def can_castle(
        self,
        color: Color,
        side: Side | None = None,
        *,
        return_explanation_if_false: Literal[True],
    ) -> tuple[bool, str | None]:
        ...

    def can_castle(
        self,
        color: Color,
        side: Side | None = None,
        *,
        return_explanation_if_false: bool = False,
    ) -> bool | tuple[bool, str | None]:
        """Check if a player can castle. Optionally specify side."""
        if self.has_moved["king", color, None]:
            return (
                (False, "Cannot castle because king has already moved.")
                if return_explanation_if_false
                else False
            )
        if (king_sq := self.initial_squares.get(("king", color, None))) is None:
            return (
                (False, "Could not determine castling availability.")
                if return_explanation_if_false
                else True
            )
        squares_by_side = [
            (
                self.initial_squares.get(("rook", color, side_)),
                self.has_moved["rook", color, side_],
                CASTLING_FINAL_SQUARES[color, side_],
            )
            for side_ in ([side] if side is not None else SIDES)
        ]
        for rook_init_sq, rook_has_moved, (king_final, rook_final) in squares_by_side:
            if rook_init_sq is None:
                return (
                    (
                        False,
                        "Cannot castle because rook's initial square could not be "
                        "determined.",
                    )
                    if return_explanation_if_false
                    else False
                )
            if rook_has_moved:
                return (
                    (False, "Cannot castle because rook has moved.")
                    if return_explanation_if_false
                    else False
                )
            if not all(
                self[sq] is None for sq in get_squares_between(king_sq, rook_init_sq)
            ):
                return (
                    (
                        False,
                        "Cannot castle because all squares between king and rook must "
                        "be empty.",
                    )
                    if return_explanation_if_false
                    else False
                )
            if not all(
                (pc := self[sq]) is None
                or (pc.color == color and pc.piece_type in ("rook", "king"))
                for sq in (king_final, rook_final)
            ):
                return (
                    (
                        False,
                        "Cannot castle because final squares must be empty or occupied "
                        "by moving pieces.",
                    )
                    if return_explanation_if_false
                    else False
                )
            if self.king_is_in_check(color):
                return (
                    (False, "Cannot castle because king would be put in check.")
                    if return_explanation_if_false
                    else False
                )
            if any(
                self.is_checked_square(color, sq)
                for sq in get_squares_between(king_sq, king_final)
            ):
                return (
                    (
                        False,
                        "Cannot castle because king would pass over a checked square.",
                    )
                    if return_explanation_if_false
                    else False
                )
        return (True, None) if return_explanation_if_false else True

    @overload
    def can_en_passant(
        self,
        initial_square: str | None = None,
        *,
        return_explanation_if_false: Literal[False] = False,
    ) -> bool:
        ...

    @overload
    def can_en_passant(
        self,
        initial_square: str | None = None,
        *,
        return_explanation_if_false: Literal[True],
    ) -> tuple[bool, str | None]:
        ...

    def can_en_passant(
        self,
        initial_square: str | None = None,
        *,
        return_explanation_if_false: bool = False,
    ) -> bool | tuple[bool, str | None]:
        """Check if an en passant capture is possible."""
        if self._double_forward_last_move is None:
            return (
                False
                if not return_explanation_if_false
                else (
                    False,
                    "En passant must follow a double forward pawn advance.",
                )
            )
        if initial_square is None:
            initial_square = self._infer_en_passant_initial_square()
            if initial_square is None:
                if return_explanation_if_false:
                    oc = other_color(
                        self._get_piece_at_non_empty_square(
                            self._double_forward_last_move
                        ).color
                    )
                    return False, f"No {oc} pawns are able to capture by en passant."
                else:
                    return False
        capture_file = self._double_forward_last_move[0]
        piece = self._get_piece_at_non_empty_square(initial_square)
        if self._double_forward_last_move not in get_adjacent_squares(initial_square):
            return (
                False
                if not return_explanation_if_false
                else (
                    False,
                    "Capturing pawn must be directly adjacent to captured pawn.",
                )
            )
        color = piece.color
        with self.test_position(
            {
                initial_square: None,
                en_passant_final_square_from_file(capture_file, color): Piece(
                    "pawn", color
                ),
                self._double_forward_last_move: None,
            }
        ):
            if self.king_is_in_check(color):
                return (
                    False
                    if not return_explanation_if_false
                    else (
                        False,
                        "Cannot move because player's king would be put in check.",
                    )
                )
        return (True, None) if return_explanation_if_false else True

    def is_checkmate(
        self, *, kings_known_in_check: tuple[Color, ...] | None = None
    ) -> GameStatus | None:
        """Check if either color's king is checkmated."""
        for color in COLORS:
            if (
                (
                    (kings_known_in_check is not None and color in kings_known_in_check)
                    or self.king_is_in_check(color)
                )
                and not self.can_block_or_capture_check(color)
                and not self.king_can_escape_check(color)
            ):
                return GameStatus(
                    game_over=True, winner=other_color(color), description="checkmate"
                )
        return None

    def is_stalemate(self, pieces: dict[str, Piece] | None = None) -> GameStatus | None:
        """Check if the game is a stalemate."""
        pieces_ = self.pieces if pieces is None else pieces
        if all(
            len(tuple(self.legal_moves(sq))) == 0
            for sq, pc in pieces_.items()
            if pc.color == self.turn
        ) and not self.can_castle(self.turn):
            return GameStatus(game_over=True, description="stalemate")
        return None

    def player_has_sufficient_material(self, color: Color) -> bool:
        """Whether a player has sufficient material to check the opponent's king."""
        pieces = self.pieces
        color_pieces: list[str] = []
        other_color_pieces: list[str] = []
        for pc in pieces.values():
            if pc.color == color:
                color_pieces.append(pc.piece_type)
            else:
                other_color_pieces.append(pc.piece_type)
        if len(color_pieces) > 3:
            return True
        if (
            any(pt in color_pieces for pt in ("rook", "pawn", "queen"))
            or color_pieces.count("knight") + color_pieces.count("bishop") > 1
            or (
                "knight" in color_pieces
                and any(
                    pt in other_color_pieces
                    for pt in ("rook", "knight", "bishop", "pawn")
                )
            )
            or (
                "bishop" in color_pieces
                and ("knight" in other_color_pieces or "pawn" in other_color_pieces)
            )
        ):
            return True
        if "bishop" in color_pieces:
            bishops = [sq for sq, pc in pieces.items() if pc.piece_type == "bishop"]
            bishop_square_colors = {
                ("white" if bishop in WHITE_SQUARES else "black") for bishop in bishops
            }
            if len(bishop_square_colors) == 2:
                return True
        return False

    def is_draw_by_insufficient_material(
        self, pieces: dict[str, Piece] | None = None
    ) -> GameStatus | None:
        """Check if board has insufficient material."""
        if self._piece_count > 4:
            return None
        pieces_ = self.pieces if pieces is None else pieces
        white_pieces: list[str] = []
        black_pieces: list[str] = []
        for pc in pieces_.values():  # Sort pieces by color.
            if pc.color == "white":
                white_pieces.append(pc.piece_type)
            else:
                black_pieces.append(pc.piece_type)
        is_sufficient = False
        pieces_by_color = white_pieces, black_pieces
        for color_pieces, other_color_pieces in (
            pieces_by_color,
            pieces_by_color[::-1],
        ):  # Check for sufficient material by Lichess definition as summarized
            # here: https://www.reddit.com/r/chess/comments/se89db/a_writeup_on_definitions_of_insufficient_material/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
            if (
                any(pt in color_pieces for pt in ("rook", "pawn", "queen"))
                or color_pieces.count("knight") + color_pieces.count("bishop") > 1
                or (
                    "knight" in color_pieces
                    and any(
                        pt in other_color_pieces
                        for pt in ("rook", "knight", "bishop", "pawn")
                    )
                )
                or (
                    "bishop" in color_pieces
                    and ("knight" in other_color_pieces or "pawn" in other_color_pieces)
                )
            ):
                is_sufficient = True
                break
            if "bishop" in color_pieces:
                bishops = [
                    sq for sq, pc in pieces_.items() if pc.piece_type == "bishop"
                ]
                bishop_square_colors = {
                    ("white" if bishop in WHITE_SQUARES else "black")
                    for bishop in bishops
                }
                if len(bishop_square_colors) == 2:
                    is_sufficient = True
                    break
        if not is_sufficient:
            return GameStatus(game_over=True, description="insufficient_material")
        return None

    def evaluate(self) -> int:
        """Evaluate position based on piece values."""
        pieces_by_color = self.pieces_by_color()
        white_score, black_score = (
            sum(PIECE_VALUES[pc.piece_type] for pc in pieces_by_color[color].values())
            for color in COLORS
        )
        return white_score - black_score

    def pieces_by_color(self) -> dict[Color, dict[str, Piece]]:
        """Sort pieces on board by color."""
        result: dict[Color, dict[str, Piece]] = {color: {} for color in COLORS}
        for sq, pc in self.items():
            if pc is not None:
                result[pc.color][sq] = pc
        return result

    def king_can_escape_check(self, color: Color) -> bool | None:
        """Whether a king can escape check (assuming it is in check)."""
        return (
            len(tuple(self.legal_moves(king))) > 0
            if self[king := self.kings[color]] is not None
            else None
        )

    def can_block_or_capture_check(
        self,
        color: Color,
        *,
        drop_pool: list[PieceType] | None = None,
    ) -> bool | None:
        """
        Return True if a check can be blocked by another piece or if the threatening
        piece can be captured.
        """
        # Sort pieces.
        same_color_pieces_except_king = []
        other_color_pieces = []
        king_sq: str | None = None
        for sq, check_pc in self.items():
            if check_pc is None:
                continue
            if check_pc.color == color:
                if check_pc.piece_type == "king":
                    king_sq = sq
                else:
                    same_color_pieces_except_king.append(sq)
            else:
                other_color_pieces.append(sq)
        if king_sq is None:
            return None
        # Find checks and squares that could block each.
        checks = self.get_threatening_pieces(self.kings[color], color)
        squares_that_would_block_check = []
        for check_sq, check_pc in checks.items():
            if (pt := check_pc.piece_type) in ("knight", "pawn"):
                squares_that_would_block_check.append(check_sq)
                continue
            if pt in ("rook", "bishop", "queen"):
                squares_that_would_block_check.extend(
                    (*get_squares_between(check_sq, king_sq), check_sq)
                )
        if self._can_drop_out_of_check(
            drop_pool, checks, squares_that_would_block_check
        ):
            return True
        if self._en_passant_can_block_check(color):
            return True
        # Check for a possible block, and test its legality.
        oc = other_color(color)
        for final_square in squares_that_would_block_check:
            for initial_square, pc in self.get_threatening_pieces(
                final_square, oc, square_is_empty=final_square not in checks
            ).items():
                if pc.piece_type == "king":
                    continue
                if self.can_move_piece(
                    initial_square,
                    final_square,
                    navigability_already_checked=True,
                ):
                    return True
        return False

    def export_bare_fen(self, *, clocks: bool = False) -> str:
        """Export FEN with no clocks."""
        epd = ""
        # Concatenate piece placement data.
        for rank in range(8, 0, -1):
            blank_sq_counter = 0
            for sq in squares_in_rank(rank):
                if (piece := self[sq]) is None:
                    blank_sq_counter += 1
                    continue
                if blank_sq_counter > 0:
                    epd += str(blank_sq_counter)
                    blank_sq_counter = 0
                epd += PLAINTEXT_ABBRS_BY_TYPE_AND_COLOR[piece.piece_type, piece.color]
            if blank_sq_counter > 0:
                epd += str(blank_sq_counter)
            if rank > 1:
                epd += "/"
        # Concatenate active color.
        epd += f" {self.turn[0]} "
        # Concatenate castling availability.
        symbols: dict[tuple[Color, Side], str] = {
            ("white", "kingside"): "K",
            ("black", "kingside"): "k",
            ("white", "queenside"): "Q",
            ("black", "queenside"): "q",
        }
        any_castles_possible = False
        for color in COLORS:
            for side in SIDES:
                if (
                    not self.has_moved["king", color, None]
                    and not self.has_moved["rook", color, side]
                ):
                    epd += symbols[color, side]
                    any_castles_possible = True
        if not any_castles_possible:
            epd += "-"
        epd += " "
        # Concatenate en passant target square.
        if self._double_forward_last_move is not None:
            epd += self._double_forward_last_move[0]
            if (char := self._double_forward_last_move[1]) == "4":
                epd += "3"
            elif char == "5":
                epd += "6"
        else:
            epd += "-"
        return epd
