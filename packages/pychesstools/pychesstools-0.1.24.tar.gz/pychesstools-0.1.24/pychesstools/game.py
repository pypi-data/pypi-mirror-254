"""A game of chess."""

from __future__ import annotations

import re
from collections import Counter
from contextlib import suppress
from typing import ClassVar, Final, Generic, Literal, TypeVar, cast, overload

from . import WORKING_DIRECTORY
from .openings import Opening, OpeningTree
from .position import ChessPosition
from .timer import IncrementalTimer
from .types import (
    ALGEBRAIC_PIECE_ABBRS,
    CASTLING_FINAL_SQUARES,
    COLORS,
    PGN_HEADER_FIELDS,
    PGN_RESULT_BY_WINNER,
    PLAINTEXT_ABBRS,
    WINNER_BY_PGN_RESULT,
    Color,
    GameOverError,
    GameStatus,
    MoveError,
    Piece,
    PieceType,
    Side,
)
from .utils import (
    _TERMINATION_BY_STATUS_DESCRIPTION,
    FORWARD_STEP_FUNCTIONS_BY_PAWN_COLOR,
    GENERATORS_BY_PIECE_TYPE,
    en_passant_initial_square,
    knight_navigable_squares,
    other_color,
    pawn_capturable_squares,
)

with (WORKING_DIRECTORY / "data" / "book.json").open() as file:
    OPENINGS = OpeningTree.load_json_book(file)

T = TypeVar("T", bound=ChessPosition)


class ChessGame(Generic[T]):
    """A game of chess."""

    AUTOPRINT: ClassVar[bool] = False
    """Print board upon `__repr__` call."""

    ARBITER_DRAW_AFTER_THREEFOLD_REPETITION: ClassVar[bool] = False
    """Do not require claim to draw after threefold repetition."""

    AUTOMATIC_DRAW_AFTER_FIVEFOLD_REPETITION: ClassVar[bool] = True
    """Call a draw immediately upon fivefold repetition."""

    ARBITER_DRAW_AFTER_100_HALFMOVE_CLOCK: ClassVar[bool] = False
    """Do not require claim to draw after halfmove clock hits 100."""

    BLOCK_IF_GAME_OVER: ClassVar[bool] = True
    """Prevent attempts to move if game has already ended."""

    CHECK_FOR_INSUFFICIENT_MATERIAL: ClassVar[bool] = True
    """Perform draw by insufficient material checks (uses Lichess rules)."""

    def __init__(
        self,
        pgn: str | None = None,
        *,
        fen: str | None = None,
        epd: str | None = None,
        empty: bool = False,
        import_fields: bool = True,
        time_control: str | None = None,
        position_cls: type[T] = ChessPosition,  # type: ignore
    ) -> None:
        """Create a chess board object."""
        self.halfmove_clock = 0
        self.initial_fen: str | None = None
        self.fields: Final[dict[str, str]] = {}
        self.clocks: dict[Color, IncrementalTimer] | None = (
            {color: IncrementalTimer(time_control) for color in COLORS}
            if time_control
            else None
        )
        self._status = GameStatus(game_over=False)
        self._moves: Final[list[str]] = []
        self._moves_before_fen_import = 0
        self._hashes: Final[Counter[int]] = Counter()
        self._must_promote_pawn: str | None = None
        self._move_annotations: dict[str, str] = {}
        self._position_cls = position_cls
        self.board: T
        if not empty and fen is None and pgn is None:
            self.board = self._position_cls.with_staunton_pattern()  # type: ignore
        else:
            self.board = self._position_cls()
        if fen is not None and epd is None:
            self.import_fen(fen)
        if fen is None and epd is not None:
            self.import_epd(epd)
        if pgn is not None:
            return self.import_pgn(pgn, import_fields=import_fields)
        with suppress(StopIteration):
            self.board.set_initial_positions()

    def __repr__(self) -> str:
        """Represent ChessBoard as string."""
        if self.AUTOPRINT:
            self.board.print()
        return f"{self.__class__.__name__}(fen='{self.fen}')"

    @staticmethod
    def _wrap_moves(moves: str, width: int = 80) -> str:
        if width < 8:
            raise ValueError("Width must be at least 8.")
        output = ""
        while len(moves) > width:
            i = width
            line = moves[:i]
            while line[-1] != " ":
                i -= 1
                line = line[:-1]
            output += f"{line.strip()}\n"
            moves = moves[i:]
        output += moves
        return output

    def import_fen(self, fen: str) -> None:
        """Import Forsyth-Edwards Notation to board."""
        self.board = self._position_cls.import_bare_fen(fen)  # type: ignore
        if match := re.search(r" (?P<halfmove>\d+) (?P<fullmove>\d+)$", fen):
            halfmove, fullmove = match.groups()
            self.halfmove_clock = int(halfmove)
            self._moves_before_fen_import = int(fullmove) - 1
            if self.board.turn == "black":
                self._moves.append("_")
        self.initial_fen = fen

    def import_epd(self, epd: str) -> None:
        """Import Extended Position Description to board."""
        self.board.import_bare_fen(epd)
        for opcode, operand in re.findall(r"(hmvc|fmvn) (\d+);", epd):
            match opcode:
                case "hmvc":
                    self.halfmove_clock = int(operand)
                case "fmvn":
                    self._moves_before_fen_import = int(operand) - 1
                    if self.board.turn == "black":
                        self._moves.append("_")
        self.initial_fen = self.fen

    def _annotate_clk(self) -> None:
        if self.clocks is not None:
            for clock in self.clocks.values():
                for move_no, seconds_remaining in clock.history.items():
                    if existing_annotation := self._move_annotations.get(move_no):
                        existing_annotation = re.sub(
                            r"\[%clk.+?\]", "", existing_annotation
                        ).strip()
                        self._move_annotations[move_no] = (
                            IncrementalTimer.format_annotation(seconds_remaining)
                            + (" " if len(existing_annotation) > 0 else "")
                            + existing_annotation
                        )
                    else:
                        self._move_annotations[
                            move_no
                        ] = IncrementalTimer.format_annotation(seconds_remaining)

    def export_pgn(
        self,
        fields: dict[str, str] | None = None,
        *,
        wrap: int | None = None,
        include_annotations: bool = True,
        include_current_position: bool = False,
        include_opening: bool = True,
        include_termination: bool = True,
    ) -> str:
        """Export game in Portable Game Notation."""
        fields_ = self.fields if fields is None else self.fields | fields
        status = (
            GameStatus(
                game_over=True,
                winner=WINNER_BY_PGN_RESULT[res] if res in ("1-0", "0-1") else None,
                description="imported",
            )
            if (res := fields_.get("Result")) and not self._status.game_over
            else self._status
        )
        output = ""
        for field in PGN_HEADER_FIELDS:
            if field in fields_:
                output += f'[{field} "{fields_[field]}"]\n'
            elif field == "Date":
                output += '[Date "????.??.??"]\n'
            else:
                output += f'[{field} "?"]\n'
        if not status.game_over:
            output += '[Result "*"]\n'
        else:
            output += f'[Result "{PGN_RESULT_BY_WINNER[status.winner]}"]\n'
        if self.initial_fen is not None:
            if "SetUp" not in fields_:
                output += '[SetUp "1"]\n'
            if "FEN" not in fields_:
                output += f'[FEN "{self.initial_fen}"]\n'
        if (
            include_termination
            and "Termination" not in fields_
            and (termination := self._termination(fields_)) is not None
        ):
            output += f'[Termination "{termination}"]\n'
        if include_current_position:
            output += f'[CurrentPosition "{self.fen}"]\n'
        if (
            include_opening
            and (opening := self.opening) is not None
            and "ECO" not in fields_
        ):
            if "Opening" not in fields_:
                output += f'[Opening "{opening.name}"]\n'
            output += f'[ECO "{opening.eco}"]\n'
        for name, value in fields_.items():
            if name not in PGN_HEADER_FIELDS and name != "Result":
                output += f'[{name} "{value}"]\n'
        output += "\n"
        output += self.export_moves(include_annotations=include_annotations, wrap=wrap)
        output += "\n"
        return output

    def export_epd(
        self,
        fields: dict[str, str] | None = None,
        *,
        include_hmvc: bool = False,
        include_fmvn: bool = False,
    ) -> str:
        """Return Extended Position Description (EPD) as string."""
        output = self.board.export_bare_fen()
        if include_hmvc:
            output += f" hmvc {self.halfmove_clock};"
        if include_fmvn:
            output += f" fmvn {self.fullmove_clock};"
        if fields is not None:
            for field in fields:
                output += f" {field} {fields[field]};"
        return output

    def export_moves(
        self,
        *,
        include_annotations: bool = False,
        wrap: int | None = None,
        include_status: bool = True,
    ) -> str:
        """Export moves to string."""
        if include_annotations:
            self._annotate_clk()
        i = self._moves_before_fen_import
        output = ""
        moves = self._moves
        while True:
            i += 1
            if len(moves) == 1:
                move_no = f"{i}."
                move_annotation = f"{move_no} {moves[0]}"
                output += move_annotation
                if include_annotations and (
                    annotation := self._move_annotations.get(move_no)
                ):
                    output += f" {{{annotation}}} "
            if len(moves) < 2:
                break
            move_no = f"{i}."
            output += f"{move_no} {moves[0]} "
            if include_annotations and (
                annotation := self._move_annotations.get(move_no)
            ):
                output += f"{{{annotation}}} {i}... "
            output += f"{moves[1]} "
            if include_annotations and (
                annotation := self._move_annotations.get(f"{i}...")
            ):
                output += f"{{{annotation}}} "
            moves = moves[2:]
        if include_status:
            status = self.status
            output += (
                f" {PGN_RESULT_BY_WINNER[status.winner] if status.game_over else '*'}"
            )
        output = output.replace(". _", "...").strip().replace("  ", " ")
        return self._wrap_moves(output, wrap) if wrap else output

    def _block_if_game_over(self) -> None:
        """Raise an exception if the game is already over."""
        if not self.BLOCK_IF_GAME_OVER:
            return None
        if self._check_game_over():
            raise GameOverError("The game has already ended.")

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
        self._block_if_game_over()
        self._handle_missing_clock_update(seconds_elapsed)
        if "O-O" in notation:
            side: Side = "queenside" if "O-O-O" in notation else "kingside"
            glyphs = (
                match.group(1) if (match := re.search(r"([?!]*)", notation)) else ""
            )
            self._castle(
                self.board.turn,
                side,
                game_over_checked=True,
                seconds_elapsed=seconds_elapsed,
                glyphs=glyphs,
            )
            return (
                {"move_type": "castle", "side": side, "capture": False}
                if return_metadata
                else None
            )
        elif match := re.search(
            r"([KQRBN]?)([a-h1-8]{,2})x?([a-h][1-8])=?([KQRBN]?)([?!]*)",
            notation,
        ):
            pt_abbr, disambiguator, final_square, promotion, glyphs = match.groups()
            piece_type = ALGEBRAIC_PIECE_ABBRS[pt_abbr]
            pawn_promotion = (
                ALGEBRAIC_PIECE_ABBRS[promotion] if promotion != "" else None
            )
            initial_square, legality_checked = self._read_disambiguator(
                notation, piece_type, disambiguator, final_square
            )
            if "x" in notation and self.board[final_square] is None:
                with suppress(MoveError):
                    self._en_passant(
                        initial_square,
                        final_square,
                        game_over_checked=True,
                        skip_checks=legality_checked,
                        seconds_elapsed=seconds_elapsed,
                        glyphs=glyphs,
                    )
                    return (
                        {
                            "move_type": "en_passant",
                            "capture": True,
                            "capture_piece_type": "pawn",
                            "capture_piece_is_promoted": False,
                        }
                        if return_metadata
                        else None
                    )
            if (
                piece_type == "pawn"
                and final_square[1] in ("1", "8")
                and pawn_promotion is None
            ):
                msg = "Must promote pawn upon move to final rank."
                raise MoveError(msg)
            return_val = self._move_piece(
                initial_square,
                final_square,
                allow_castle_and_en_passant=False,
                no_disambiguator=(disambiguator == ""),
                return_metadata=return_metadata,
                game_over_checked=True,
                skip_checks=legality_checked,
                seconds_elapsed=seconds_elapsed,
                glyphs=glyphs,
            )
            if pawn_promotion is not None:
                self.promote_pawn(final_square, pawn_promotion)
                if return_val is not None:
                    return_val["promote_pawn"] = True
            return return_val
        else:
            msg = f"Could not read notation '{notation}'."
            raise MoveError(msg)

    def _check_turn(self, color: Color, *, ignore_pawn_promotion: bool = False) -> None:
        if color != self.board.turn:
            raise MoveError(f"It is {self.board.turn}'s turn.")
        if not ignore_pawn_promotion and self._must_promote_pawn is not None:
            raise MoveError(
                f"Must promote pawn at square '{self._must_promote_pawn}'"
                " before next move."
            )

    def promote_pawn(self, square: str, piece_type: PieceType) -> None:
        """Promote a pawn on the farthest rank from where it started."""
        piece = self.board._get_piece_at_non_empty_square(square)
        self._check_turn(piece.color, ignore_pawn_promotion=True)
        if (piece.color == "white" and square[1] != "8") or (
            piece.color == "black" and square[1] != "1"
        ):
            msg = f"Cannot promote pawn at square '{square}'."
            raise MoveError(msg)
        self.board[square] = Piece(
            piece_type, piece.color, promoted=True, has_moved=True
        )
        self._double_forward_last_move = None
        self._must_promote_pawn = None
        notation = f"{self._moves[-1]}={PLAINTEXT_ABBRS[piece_type]}"
        if self.board.king_is_in_check(oc := other_color(self.board.turn)):
            notation += (
                "#" if self.board.is_checkmate(kings_known_in_check=(oc,)) else "+"
            )
        self._moves[-1] = notation
        self._alternate_turn(reset_halfmove_clock=True, reset_hashes=True)

    @property
    def move_number(self) -> str:
        """Get move number in PGN format (i.e. '32.', '32...')."""
        num = self.fullmove_clock
        suffix = "." if self.board.turn == "white" else "..."
        return f"{num}{suffix}"

    def _alternate_turn(
        self,
        *,
        reset_halfmove_clock: bool = False,
        reset_hashes: bool = False,
        seconds_elapsed: float | None = None,
    ) -> None:
        """Alternate turn, update halfmove clock, and hash position."""
        if self.clocks is not None:
            if seconds_elapsed is not None:
                self.clocks[self.board.turn].add_move(self.move_number, seconds_elapsed)
            else:
                raise ValueError("Expected seconds_elapsed parameter for timed game.")
        self.board.turn = other_color(self.board.turn)
        if reset_hashes:
            self._hashes.clear()
        else:
            self._hashes.update((hash(self.board),))
        self.halfmove_clock = 0 if reset_halfmove_clock else self.halfmove_clock + 1

    def is_draw_by_fivefold_repetition(self) -> bool:
        """Check if any position has repeated 5 times or more."""
        if len(self._moves) < 10:
            return False
        with suppress(IndexError):
            if self._hashes.most_common(1)[0][1] >= 5:
                self._status = GameStatus(
                    game_over=True, description="fivefold_repetition"
                )
                return True
        return False

    def is_draw_by_75_move_rule(self) -> bool:
        """Check if draw by 75 moves without pawn move or capture."""
        if self.halfmove_clock >= 150:
            self._status = GameStatus(game_over=True, description="75move")
            return True
        return False

    def can_claim_draw(self) -> bool:
        """Whether draw can be claimed without agreement."""
        return (
            self.can_claim_draw_by_halfmove_clock()
            or self.can_claim_draw_by_threefold_repetition()
        )

    def can_claim_draw_by_halfmove_clock(self) -> bool:
        """Whether draw can be claimed due to 50 moves without pawn move or capture."""
        can_claim = self.halfmove_clock >= 100
        if can_claim and self.ARBITER_DRAW_AFTER_100_HALFMOVE_CLOCK:
            self._status = GameStatus(game_over=True, description="50move")
        return can_claim

    def can_claim_draw_by_threefold_repetition(self) -> bool:
        """Whether draw can be claimed due to threefold repetition."""
        try:
            can_claim = self._hashes.most_common(1)[0][1] >= 3
        except IndexError:
            return False
        else:
            if can_claim and self.ARBITER_DRAW_AFTER_THREEFOLD_REPETITION:
                self._status = GameStatus(
                    game_over=True, description="threefold_repetition"
                )
            return can_claim

    def resign(self, color: Color | None = None) -> GameStatus:
        """Resign instead of moving."""
        self._status = GameStatus(
            game_over=True,
            winner=other_color(self.board.turn if color is None else color),
            description="resignation",
        )
        return self._status

    def draw(self) -> GameStatus:
        """Draw instead of moving."""
        if self.can_claim_draw():
            return self.claim_draw()
        self._status = GameStatus(game_over=True, description="agreement")
        return self._status

    def claim_draw(self) -> GameStatus:
        """Claim a draw due to 50 moves without a capture or pawn move."""
        if self._status.game_over:
            return self._status
        if (move_rule := self.halfmove_clock >= 100) or (
            self._hashes.most_common(1)[0][1] >= 3
        ):
            self._status = GameStatus(
                game_over=True,
                description="50move" if move_rule else "threefold_repetition",
            )
            return self._status
        return GameStatus(game_over=False)

    def submit_moves(self, *notations: str) -> None:
        """Submit multiple moves at once with algebraic notation."""
        if len(notations) == 1 and " " in notations[0]:
            notations = tuple(
                re.sub(
                    r"\[.+?\]|\{.+?\}|\d+\.+|[10]-[10]|\*|1/2-1/2|[?!]",
                    "",
                    notations[0],
                ).split()
            )
            if len(notations) == 1 and notations[0] == "":
                return None
        for notation in notations:
            self.move(notation)

    def import_pgn(self, pgn: str, *, import_fields: bool = True) -> None:
        """Import a game by PGN string."""
        pgn = pgn.replace("\n", " ")
        pgn = re.sub(r"(?m)^%.+", "", pgn)
        if "[FEN " in pgn and (match := re.search(r"\[FEN \"(.+?)\"\]", pgn)):
            fen = match.group(1)
            self.import_fen(fen)
        else:
            self.board = self._position_cls.with_staunton_pattern()  # type: ignore
        self.board.set_initial_positions()
        self.submit_moves(pgn)
        if import_fields:
            self.fields.update(dict(re.findall(r"\[([^\s]+) \"(.+?)\"\]", pgn)))
            self._move_annotations = dict(
                re.findall(r"(\d+\.+)[^\.\{]+?\{(.+?)\}", pgn)
            )
        if (  # Import result (and clocks if game is timed and still in progress).
            not self.status.game_over
            and (result := re.search(r"([10]-[10]|1/2-1/2|\*)$", pgn))
        ):
            match result.group(1):
                case "1/2-1/2":
                    self.draw()
                case "1-0" | "0-1" as res:
                    self._status = GameStatus(
                        game_over=True,
                        winner=WINNER_BY_PGN_RESULT[res],
                        description="imported",
                    )
                case _:
                    if "[TimeControl " in pgn:
                        self.clocks = {}
                        for color in COLORS:
                            self.clocks[color] = IncrementalTimer.from_pgn(pgn, color)

    @property
    def fen(self) -> str:
        """Export the board in Forsyth-Edwards Notation."""
        return self.export_fen()

    def export_fen(self) -> str:
        """Export the board in Forsyth-Edwards Notation."""
        return (
            self.board.export_bare_fen()
            + f" {self.halfmove_clock} {self.fullmove_clock}"
        )

    def _termination(self, fields: dict[str, str]) -> str | None:
        if not self.status.game_over:
            return None
        desc = cast(str, self._status.description)
        template = _TERMINATION_BY_STATUS_DESCRIPTION.get(desc)
        if template is None:
            return None
        if (winning_color := self._status.winner) is None:
            return template
        losing_color = other_color(winning_color)
        winner = (
            fld if (fld := fields.get(winning_color.title())) else winning_color.title()
        )
        loser = (
            fld if (fld := fields.get(losing_color.title())) else losing_color.title()
        )
        return template.replace("[WINNER]", winner).replace("[LOSER]", loser)

    @property
    def fullmove_clock(self) -> int:
        """Return the current move number, as it appears in FEN notation."""
        return self._moves_before_fen_import + (len(self._moves) // 2) + 1

    @property
    def pgn(self) -> str:
        """Export game in Portable Game Notation."""
        return self.export_pgn()

    @property
    def epd(self) -> str:
        """Return Extended Position Description (EPD) as string."""
        return self.export_epd()

    @property
    def moves(self) -> str:
        """Export moves to string."""
        return self.export_moves()

    @property
    def opening(self) -> Opening | None:
        """Get ECO opening."""
        return OPENINGS.get_opening(self._moves)

    @property
    def status(self) -> GameStatus:
        """Check the board for a checkmate or draw."""
        if self._status.game_over:
            return self._status
        pieces = self.board.pieces
        if (
            (status := self.board.is_checkmate())
            or (status := self.board.is_stalemate(pieces))
            or (
                self.CHECK_FOR_INSUFFICIENT_MATERIAL
                and (status := self.board.is_draw_by_insufficient_material(pieces))
            )
        ):
            self._status = status
            return status
        elif (
            self.is_timeout()
            or (
                self.ARBITER_DRAW_AFTER_THREEFOLD_REPETITION
                and self.can_claim_draw_by_threefold_repetition()
            )
            or (
                self.AUTOMATIC_DRAW_AFTER_FIVEFOLD_REPETITION
                and self.is_draw_by_fivefold_repetition()
            )
            or (
                self.ARBITER_DRAW_AFTER_100_HALFMOVE_CLOCK
                and self.can_claim_draw_by_halfmove_clock()
            )
            or self.is_draw_by_75_move_rule()
        ):
            return self._status
        return GameStatus(game_over=False)

    def is_timeout(self) -> bool:
        """Whether a player's clock has run out."""
        if self.clocks is None:
            return False
        for color, clock in self.clocks.items():
            if clock.out_of_time:
                oc = other_color(color)
                if not self.board.player_has_sufficient_material(oc):
                    self._status = GameStatus(
                        game_over=True, winner=None, description="timeoutvsinsufficient"
                    )
                    return True
                self._status = GameStatus(
                    game_over=True, winner=oc, description="timeout"
                )
                return True
        return False

    def _check_game_over(self, *, check_insufficient_material: bool = True) -> bool:
        """Check if game is over without checking for stalemate or checkmate."""
        return bool(
            self._status.game_over
            or self.is_timeout()
            or (
                self.ARBITER_DRAW_AFTER_THREEFOLD_REPETITION
                and self.can_claim_draw_by_threefold_repetition()
            )
            or (
                self.AUTOMATIC_DRAW_AFTER_FIVEFOLD_REPETITION
                and self.is_draw_by_fivefold_repetition()
            )
            or (
                check_insufficient_material
                and self.CHECK_FOR_INSUFFICIENT_MATERIAL
                and self.board.is_draw_by_insufficient_material()
            )
            or (
                self.ARBITER_DRAW_AFTER_100_HALFMOVE_CLOCK
                and self.can_claim_draw_by_halfmove_clock()
            )
            or self.is_draw_by_75_move_rule()
        )

    def _handle_missing_clock_update(self, seconds_elapsed: float | None) -> None:
        if self.clocks is not None and seconds_elapsed is None:
            raise ValueError("Expected seconds_elapsed parameter for timed game.")

    def _castle(
        self,
        color: Color,
        side: Side,
        *,
        skip_checks: bool = False,
        game_over_checked: bool = False,
        seconds_elapsed: float | None = None,
        glyphs: str = "",
    ) -> None:
        """Move the king and rook at once."""
        if not game_over_checked:
            self._block_if_game_over()
            self._handle_missing_clock_update(seconds_elapsed)
        if not skip_checks:
            can_move, explanation = self.board.can_castle(
                color, side, return_explanation_if_false=True
            )
            if not can_move:
                raise MoveError(explanation)
        king_final_sq, rook_final_sq = CASTLING_FINAL_SQUARES[color, side]
        rook_init_sq = self.board.initial_squares["rook", color, side]
        self.board[self.board.kings[color]] = None
        self.board[rook_init_sq] = None
        self.board[king_final_sq] = Piece("king", color)
        self.board[rook_final_sq] = Piece("rook", color)
        self.board.has_moved["king", color, None] = True
        self.board.has_moved["rook", color, side] = True
        self._double_forward_last_move = None
        notation = "O-O" if side == "kingside" else "O-O-O"
        if self.board.king_is_in_check(oc := other_color(self.board.turn)):
            notation += (
                "#" if self.board.is_checkmate(kings_known_in_check=(oc,)) else "+"
            )
        self._moves.append(notation + glyphs)
        self._must_promote_pawn = None
        self._alternate_turn(reset_hashes=True, seconds_elapsed=seconds_elapsed)

    def _read_disambiguator(
        self,
        notation: str,
        piece_type: PieceType,
        disambiguator: str,
        final_square: str,
    ) -> tuple[str, bool]:
        """Determine moving piece from notation. Returns (square, legality_checked)."""
        candidates = []
        match piece_type:  # Ignoring check, get candidate pieces.
            case "rook" | "bishop" | "queen" as pt:
                for generator in GENERATORS_BY_PIECE_TYPE[pt]:
                    for sq in generator(final_square):
                        if (piece := self.board[sq]) is not None:
                            if (
                                disambiguator in sq
                                and piece.piece_type == piece_type
                                and piece.color == self.board.turn
                            ):
                                candidates.append(sq)
                            else:
                                break
            case "pawn":
                # If capturing but moving to an empty square, it must be an en passant.
                # For en passant moves, the file must also be specified (e.g. "exf6").
                # We know the initial rank by color, so there is only one candidate.
                if "x" in notation and self.board[final_square] is None:
                    candidates = [
                        en_passant_initial_square(disambiguator, self.board.turn)
                    ]
                # If no piece at final square, it must be a forward advance.
                elif self.board[final_square] is None:
                    step_func = FORWARD_STEP_FUNCTIONS_BY_PAWN_COLOR[
                        other_color(self.board.turn)
                    ]
                    if (
                        (square := step_func(final_square, 1)) is not None
                        and disambiguator in square
                        and (pc := self.board[square]) is not None
                        and pc.piece_type == "pawn"
                        and pc.color == self.board.turn
                    ) or (
                        (square := step_func(final_square, 2)) is not None
                        and disambiguator in square
                        and (pc := self.board[square]) is not None
                        and pc.piece_type == "pawn"
                        and pc.color == self.board.turn
                    ):
                        candidates = [square]
                else:  # Otherwise, it's a capture.
                    candidates = [
                        square
                        for square in pawn_capturable_squares(
                            other_color(self.board.turn), final_square
                        )
                        if (
                            square is not None
                            and disambiguator in square
                            and (pc := self.board[square]) is not None
                            and pc.piece_type == "pawn"
                            and pc.color == self.board.turn
                        )
                    ]
            case "knight":
                candidates = [
                    sq
                    for sq in knight_navigable_squares(final_square)
                    if disambiguator in sq
                    and (pc := self.board[sq]) is not None
                    and pc.piece_type == "knight"
                    and pc.color == self.board.turn
                ]
            case "king":
                candidates = (
                    [king_sq]
                    if (king_sq := self.board.kings[self.board.turn]) is not None
                    else []
                )
        if len(candidates) == 1:
            return candidates[0], False
        elif len(candidates) == 0:
            raise MoveError(f"'{notation}' is not allowed.")
        else:  # Attempt to disambiguate by testing legality of each piece moving.
            successful_candidates = [
                candidate
                for candidate in candidates
                if self.board.can_move_piece(candidate, final_square)
            ]
            if len(successful_candidates) == 1:
                initial_square = successful_candidates[0]
            elif len(candidates) == 0:
                raise MoveError(f"'{notation}' is not allowed.")
            else:
                raise MoveError(
                    f"Must disambiguate moving pieces: {successful_candidates}"
                )
        return initial_square, True

    def _en_passant(
        self,
        initial_square: str,
        final_square: str,
        *,
        skip_checks: bool = False,
        game_over_checked: bool = False,
        seconds_elapsed: float | None = None,
        glyphs: str = "",
    ) -> None:
        """Capture an adjacent file pawn that has just made a double forward advance."""
        if not game_over_checked:
            self._block_if_game_over()
        piece = self.board._get_piece_at_non_empty_square(initial_square)
        if not skip_checks:
            can_move, explanation = self.board.can_en_passant(
                initial_square, return_explanation_if_false=True
            )
            if not can_move:
                raise MoveError(explanation)
        double_forward = self.board._get_double_forward_last_move_strict()
        self.board[double_forward] = None
        self.board[initial_square] = None
        self.board[final_square] = piece
        self.board._double_forward_last_move = None
        self.board._piece_count -= 1
        notation = f"{initial_square[0]}x{final_square}"
        if self.board.king_is_in_check(oc := other_color(self.board.turn)):
            notation += (
                "#" if self.board.is_checkmate(kings_known_in_check=(oc,)) else "+"
            )
        self._moves.append(notation + glyphs)
        self._must_promote_pawn = None
        self._alternate_turn(reset_halfmove_clock=True, seconds_elapsed=seconds_elapsed)

    @overload
    def _move_piece(
        self,
        initial_square: str,
        final_square: str,
        *,
        allow_castle_and_en_passant: bool = True,
        skip_checks: bool = False,
        no_disambiguator: bool = False,
        return_metadata: Literal[False],
        game_over_checked: bool = False,
        seconds_elapsed: float | None = None,
        glyphs: str = "",
    ) -> None:
        ...

    @overload
    def _move_piece(
        self,
        initial_square: str,
        final_square: str,
        *,
        allow_castle_and_en_passant: bool = True,
        skip_checks: bool = False,
        no_disambiguator: bool = False,
        return_metadata: Literal[True],
        game_over_checked: bool = False,
        seconds_elapsed: float | None = None,
        glyphs: str = "",
    ) -> dict[str, str | bool]:
        ...

    @overload
    def _move_piece(
        self,
        initial_square: str,
        final_square: str,
        *,
        allow_castle_and_en_passant: bool = True,
        skip_checks: bool = False,
        no_disambiguator: bool = False,
        return_metadata: bool = False,
        game_over_checked: bool = False,
        seconds_elapsed: float | None = None,
        glyphs: str = "",
    ) -> dict[str, str | bool] | None:
        ...

    def _move_piece(
        self,
        initial_square: str,
        final_square: str,
        *,
        allow_castle_and_en_passant: bool = True,
        skip_checks: bool = False,
        no_disambiguator: bool = False,
        return_metadata: bool = False,
        game_over_checked: bool = False,
        seconds_elapsed: float | None = None,
        glyphs: str = "",
    ) -> dict[str, str | bool] | None:
        """Move a game piece."""
        if not game_over_checked:
            self._block_if_game_over()
            self._handle_missing_clock_update(seconds_elapsed)
        piece = self.board._get_piece_at_non_empty_square(initial_square)
        if allow_castle_and_en_passant:
            # Try to castle if king is moving to a final castling square, or if rook is
            # jumping over a king.
            castle_side: Side = "queenside" if final_square[0] in "cd" else "kingside"
            if (
                piece.piece_type == "king"
                and final_square in ("c1", "c8", "g1", "g8")
                and self.board.can_castle(piece.color, castle_side)
            ):
                self._castle(
                    piece.color,
                    castle_side,
                    skip_checks=True,
                    game_over_checked=True,
                    seconds_elapsed=seconds_elapsed,
                    glyphs=glyphs,
                )
                return (
                    {"move_type": "castle", "side": castle_side}
                    if return_metadata
                    else None
                )
            # Reroute to self.en_passant if pawn captures on empty final square.
            if (
                piece.piece_type == "pawn"
                and initial_square[0] != final_square[0]
                and self.board[final_square] is None
            ):
                self._en_passant(
                    initial_square,
                    final_square,
                    game_over_checked=True,
                    seconds_elapsed=seconds_elapsed,
                    glyphs=glyphs,
                )
                return (
                    {"move_type": "en_passant", "capture": True}
                    if return_metadata
                    else None
                )
        if not skip_checks:
            success, explanation = self.board.can_move_piece(
                initial_square, final_square, return_explanation_if_false=True
            )
            if not success:
                raise MoveError(explanation)
        # Add piece type notation, disambiguating if necessary.
        piece_at_final_square = self.board[final_square]
        notation = PLAINTEXT_ABBRS[pt] if (pt := piece.piece_type) != "pawn" else ""
        notation += self._write_disambiguator(
            initial_square,
            final_square,
            piece,
            piece_at_final_square,
            no_disambiguator=no_disambiguator,
        )
        # Update clocks, notation, has_moved to reflect capture.
        if piece_at_final_square is not None:
            if piece.piece_type == "pawn" and len(notation) == 0:
                notation += initial_square[0]
            notation += "x"
            is_capture = True
            self.board._piece_count -= 1
            oc = piece_at_final_square.color
            if piece_at_final_square.piece_type == "rook" and (
                (
                    qns := final_square
                    == self.board.initial_squares.get(("rook", oc, "queenside"))
                )
                or final_square
                == self.board.initial_squares.get(("rook", oc, "kingside"))
            ):
                self.board.has_moved[
                    "rook", oc, "queenside" if qns else "kingside"
                ] = True
        else:
            is_capture = False
        notation += final_square
        # Update has_moved variables for castling/en passant.
        if piece.piece_type == "king":
            self.board.has_moved["king", piece.color, None] = True
        elif piece.piece_type == "rook":
            if initial_square == self.board.initial_squares.get(
                ("rook", piece.color, "kingside")
            ):
                side: Side | None = "kingside"
            elif initial_square == self.board.initial_squares.get(
                ("rook", piece.color, "queenside")
            ):
                side = "queenside"
            else:
                side = None
            if side is not None:
                self.board.has_moved["rook", piece.color, side] = True
        self.board._double_forward_last_move = (
            final_square
            if piece.piece_type == "pawn"
            and abs(int(initial_square[1]) - int(final_square[1])) == 2
            else None
        )
        # Move piece.
        self.board[initial_square] = None
        if not piece.has_moved and piece.piece_type == "pawn":
            piece.has_moved = True
        self.board[final_square] = piece
        # If pawn moving to final rank, require pawn promotion. Else, check for
        # check / checkmate, append moves, and return.
        if piece.piece_type == "pawn" and final_square[1] in ("1", "8"):
            self._must_promote_pawn = final_square
        else:
            self._must_promote_pawn = None
            if self.board.king_is_in_check(oc := other_color(self.board.turn)):
                notation += (
                    "#" if self.board.is_checkmate(kings_known_in_check=(oc,)) else "+"
                )
            self._alternate_turn(
                reset_halfmove_clock=(rs := piece.piece_type == "pawn" or is_capture),
                reset_hashes=rs,
                seconds_elapsed=seconds_elapsed,
            )
        self._moves.append(notation + glyphs)
        return (
            (
                {
                    "move_type": "normal",
                    "capture": is_capture,
                    "capture_piece_type": piece_at_final_square.piece_type,
                    "capture_piece_is_promoted": piece_at_final_square.promoted,
                }
                if piece_at_final_square is not None
                else {"move_type": "normal", "capture": is_capture}
            )
            if return_metadata
            else None
        )

    def _write_disambiguator(
        self,
        initial_square: str,
        final_square: str,
        piece: Piece,
        piece_at_final_square: Piece | None,
        *,
        no_disambiguator: bool = False,
    ) -> str:
        if no_disambiguator:
            return ""
        disambiguator = ""
        ambiguous_pieces: list[str] = []
        match piece.piece_type:
            case "rook" | "bishop" | "queen" as pt:
                for generator in GENERATORS_BY_PIECE_TYPE[pt]:
                    for sq in generator(final_square):
                        if (pc := self.board[sq]) == piece:
                            if sq != initial_square and self.board.can_move_piece(
                                sq, final_square
                            ):
                                ambiguous_pieces.append(sq)
                            break
                        elif pc is not None:
                            break
            case "pawn":
                # Forward moves are unambiguous by nature.
                if piece_at_final_square is not None:
                    for square in pawn_capturable_squares(
                        piece_at_final_square.color, final_square
                    ):
                        if (
                            square is not None
                            and square != initial_square
                            and self.board[square] is not None
                            and self.board.can_move_piece(square, final_square)
                        ):
                            ambiguous_pieces = [square]
                            break
            case "knight":
                ambiguous_pieces = [
                    sq
                    for sq in knight_navigable_squares(final_square)
                    if self.board[sq] == piece
                    and sq != initial_square
                    and self.board.can_move_piece(sq, final_square)
                ]
            case "king":
                ambiguous_pieces = []
        if len(ambiguous_pieces) > 0:
            possible_disambiguators = (
                initial_square[0],
                initial_square[1],
                initial_square,
            )
            for possible_disambiguator in possible_disambiguators:
                still_ambiguous_pieces = [
                    sq
                    for sq in ambiguous_pieces
                    if possible_disambiguator in sq and sq != initial_square
                ]
                if len(still_ambiguous_pieces) == 0:
                    disambiguator = possible_disambiguator
                    break
        return disambiguator

    def print(self, *, plaintext: bool = False) -> None:
        """Print the board."""
        self.board.print(plaintext=plaintext)
