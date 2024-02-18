"""Horde variant of chess."""

from collections.abc import Iterator

from ..game import ChessGame
from ..position import ChessPosition
from ..types import Color, GameStatus, Piece
from ..utils import FORWARD_STEP_FUNCTIONS_BY_PAWN_COLOR


class HordePosition(ChessPosition):
    """A position in a game of horde chess."""

    def _pawn_pseudolegal_squares(
        self,
        initial_square: str,
        piece: Piece,
        *,
        capture_only: bool = False,
    ) -> Iterator[str]:
        yield from super()._pawn_pseudolegal_squares(
            initial_square, piece, capture_only=capture_only
        )
        if not capture_only and not piece.has_moved:
            step_func = FORWARD_STEP_FUNCTIONS_BY_PAWN_COLOR[piece.color]
            if (
                (sq := step_func(initial_square, 1)) is not None
                and self[sq] is None
                and (sq := step_func(initial_square, 2)) is not None
                and self[sq] is None
            ):
                yield sq

    def is_checkmate(
        self, *, kings_known_in_check: tuple[Color, ...] | None = None
    ) -> GameStatus | None:
        """Check if either color's king is checkmated."""
        if (
            (
                (kings_known_in_check is not None and "black" in kings_known_in_check)
                or self.king_is_in_check("black")
            )
            and not self.can_block_or_capture_check("black")
            and not self.king_can_escape_check("black")
        ):
            return GameStatus(
                game_over=True,
                winner="white",
                description="checkmate",
            )
        return None


class HordeGame(ChessGame[HordePosition]):
    """A chess board to play Horde."""

    BLOCK_IF_GAME_OVER = False
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
        """Create a HordeBoard."""
        fen_ = (
            "rnbqkbnr/pppppppp/8/1PP2PP1/PPPPPPPP/PPPPPPPP/PPPPPPPP/PPPPPPPP w qk - 0 1"
            if fen is None and not empty
            else fen
        )
        super().__init__(
            fen=fen_,
            epd=epd,
            pgn=pgn,
            empty=True,
            import_fields=import_fields,
            position_cls=HordePosition,
        )
        self.fields["Variant"] = "Horde"

    def all_pawns_captured(self) -> bool:
        """Whether all white pieces have been captured."""
        if all(pc.color == "black" for pc in self.board.pieces.values()):
            self._moves[-1] = f"{self._moves[-1].replace('+', '').replace('#', '')}#"
            self._status = GameStatus(
                game_over=True, winner="black", description="all_pieces_captured"
            )
            return True
        return False

    @property
    def status(self) -> GameStatus:
        """Check the board for a checkmate or draw."""
        if self.all_pawns_captured():
            return self._status
        return super().status

    def _check_game_over(self, *, check_insufficient_material: bool = True) -> bool:
        """Check if game is over without checking for stalemate or checkmate."""
        if self.all_pawns_captured():
            return True
        return super()._check_game_over(
            check_insufficient_material=check_insufficient_material
        )
