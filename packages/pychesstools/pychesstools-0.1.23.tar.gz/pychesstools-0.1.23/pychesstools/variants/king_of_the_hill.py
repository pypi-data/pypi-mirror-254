"""King of the hill chess."""

from ..game import ChessGame
from ..position import ChessPosition
from ..types import COLORS, GameStatus


class KingOfTheHillGame(ChessGame[ChessPosition]):
    """King of the hill chessboard."""

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
        """Create a KingOfTheHillBoard."""
        super().__init__(
            fen=fen, epd=epd, pgn=pgn, empty=empty, import_fields=import_fields
        )
        self.fields["Variant"] = "King of the Hill"

    @property
    def moves(self) -> str:
        """Export moves as string."""
        for i in range(len(self._moves[:-1])):
            self._moves[i] = self._moves[i].replace("#", "")
        return super().moves

    def king_reached_hill(self) -> bool:
        """Whether a player's king has reached the hill."""
        for color in COLORS:
            if self.board.kings[color] in ("d4", "d5", "e4", "e5"):
                self._moves[-1] = (
                    self._moves[-1].replace("+", "").replace("#", "") + "#"
                )
                self._status = GameStatus(
                    game_over=True, winner=color, description="king_reached_hill"
                )
                return True
        return False

    @property
    def status(self) -> GameStatus:
        """Check the board for a checkmate or draw."""
        if self.king_reached_hill():
            return self._status
        return super().status

    def _check_game_over(self, *, check_insufficient_material: bool = True) -> bool:
        if self.king_reached_hill():
            return True
        return super()._check_game_over(
            check_insufficient_material=check_insufficient_material
        )
