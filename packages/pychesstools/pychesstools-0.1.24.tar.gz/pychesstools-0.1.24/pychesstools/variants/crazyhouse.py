"""Crazyhouse chess."""

import re
from typing import Literal, overload

from ..game import ChessGame
from ..position import ChessPosition
from ..types import (
    ALGEBRAIC_PIECE_ABBRS,
    COLORS,
    PLAINTEXT_ABBRS,
    Color,
    GameStatus,
    MoveError,
    Piece,
    PieceType,
)
from ..utils import other_color


class CrazyhousePosition(ChessPosition):
    """A board position in crazyhouse chess."""

    def __init__(
        self, __dict: dict[str, Piece | None] | None = None, /, **kwargs: Piece | None
    ) -> None:
        self._pools: dict[Color, list[PieceType]] = {"white": [], "black": []}
        super().__init__(__dict, **kwargs)

    def __hash__(self) -> int:
        """Hash position."""
        return hash(
            (
                *(tuple(self._pools[color]) for color in COLORS),
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

    def can_drop_piece(
        self,
        square: str,
        piece: Piece,
        *,
        ignore_turn: bool = False,
    ) -> bool:
        """Check if a piece can be dropped to a certain square."""
        with self.test_position({square: piece}):
            if self.king_is_in_check(piece.color):
                return False
        return (
            piece.piece_type in self._pools[piece.color]
            and self[square] is None
            and not (piece.piece_type == "pawn" and square[1] in ("1", "8"))
            and (ignore_turn or self.turn == piece.color)
        )

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
                and not self.can_block_or_capture_check(
                    color, drop_pool=self._pools[color]
                )
                and not self.king_can_escape_check(color)
            ):
                return GameStatus(
                    game_over=True, winner=other_color(color), description="checkmate"
                )
        return None


class CrazyhouseGame(ChessGame[CrazyhousePosition]):
    """A game of Crazyhouse chess."""

    CHECK_FOR_INSUFFICIENT_MATERIAL = False

    def __init__(
        self,
        pgn: str | None = None,
        *,
        fen: str | None = None,
        epd: str | None = None,
        empty: bool = False,
        import_fields: bool = True,
    ) -> None:
        """Create a Crazyhouse board."""
        super().__init__(
            fen=fen,
            epd=epd,
            pgn=pgn,
            empty=empty,
            import_fields=import_fields,
            position_cls=CrazyhousePosition,
        )
        self.fields["Variant"] = "Crazyhouse"

    def drop_piece(
        self,
        square: str,
        piece: Piece,
        *,
        skip_checks: bool = False,
        seconds_elapsed: float | None = None,
    ) -> None:
        """Drop a piece from a player's pool onto the board."""
        if not (skip_checks or self.board.can_drop_piece(square, piece)):
            return None
        self.board[square] = piece
        abbr = PLAINTEXT_ABBRS[piece.piece_type] if piece.piece_type != "pawn" else ""
        notation = f"{abbr}@{square}"
        if self.board.king_is_in_check(oc := other_color(self.board.turn)):
            notation += (
                "#" if self.board.is_checkmate(kings_known_in_check=(oc,)) else "+"
            )
        self._moves.append(notation)
        self.board._pools[piece.color].remove(piece.piece_type)
        self.board._piece_count += 1
        self._alternate_turn(seconds_elapsed=seconds_elapsed)

    def is_draw_by_insufficient_material(
        self, pieces: dict[str, Piece] | None = None
    ) -> GameStatus | None:
        """Check if board has insufficient material."""
        if any(len(self.board._pools[color]) > 0 for color in COLORS):
            return None
        return super().board.is_draw_by_insufficient_material(pieces)

    @overload
    def move(
        self,
        notation: str,
        *,
        return_metadata: Literal[False] = False,
        seconds_elapsed: float | None = None,
    ) -> None:
        ...

    @overload
    def move(
        self,
        notation: str,
        *,
        return_metadata: Literal[True],
        seconds_elapsed: float | None = None,
    ) -> dict[str, str | bool]:
        ...

    def move(
        self,
        notation: str,
        *,
        return_metadata: bool = False,
        seconds_elapsed: float | None = None,
    ) -> dict[str, str | bool] | None:
        """Make a move using algebraic notation."""
        if "@" in notation:
            if match := re.search(r"(.?)@([a-h][1-8])", notation):
                piece_type = ALGEBRAIC_PIECE_ABBRS[match.group(1)]
                square = match.group(2)
                if self.board.can_drop_piece(
                    square, (pc := Piece(piece_type, self.board.turn))
                ):
                    self.drop_piece(square, pc, seconds_elapsed=seconds_elapsed)
                    return {"move_type": "drop"} if return_metadata else None
                else:
                    msg = "Cannot drop piece."
                    raise MoveError(msg)
            else:
                msg = f"Could not read move notation '{notation}'."
                raise MoveError(msg)
        move_output = super().move(
            notation, return_metadata=True, seconds_elapsed=seconds_elapsed
        )
        if (
            move_output is not None
            and "capture" in move_output
            and move_output["capture"]
        ):
            self.board._pools[other_color(self.board.turn)].append(
                "pawn"
                if move_output["capture_piece_is_promoted"]
                else move_output["capture_piece_type"]  # type: ignore
            )
        return move_output if return_metadata else None

    def can_block_or_capture_check(
        self,
        color: Color,
        *,
        drop_pool: list[PieceType] | None = None,
    ) -> bool | None:
        """Return True if a check can be blocked by another piece."""
        return super().board.can_block_or_capture_check(
            color,
            drop_pool=self.board._pools[color] if drop_pool is None else drop_pool,
        )
