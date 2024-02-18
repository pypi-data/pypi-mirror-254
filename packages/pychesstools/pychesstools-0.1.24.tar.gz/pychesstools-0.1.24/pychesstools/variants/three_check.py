"""Three-check chess."""

import re
from typing import Literal, overload

from ..game import ChessGame
from ..position import ChessPosition
from ..types import COLORS, Color, GameStatus, PieceType, Side
from ..utils import other_color


class ThreeCheckGame(ChessGame[ChessPosition]):
    """Three-check chessboard."""

    def __init__(
        self,
        pgn: str | None = None,
        *,
        fen: str | None = None,
        epd: str | None = None,
        empty: bool = False,
        import_fields: bool = True,
    ) -> None:
        """Create a ThreeCheckBoard."""
        self._checks: dict[Color, int] = {"white": 0, "black": 0}
        super().__init__(
            fen=fen, epd=epd, pgn=pgn, empty=empty, import_fields=import_fields
        )
        self.fields["Variant"] = "Three-check"

    def is_three_check(self) -> bool:
        """Whether a win by three checks has occurred."""
        for color in COLORS:
            if self._checks[color] >= 3:
                self._status = GameStatus(
                    game_over=True,
                    winner=other_color(color),
                    description="three_check",
                )
                return True
        return False

    @property
    def status(self) -> GameStatus:
        """Check the board for a checkmate or draw."""
        if self.is_three_check():
            return self._status
        return super().status

    def _check_game_over(self, *, check_insufficient_material: bool = True) -> bool:
        if self.is_three_check():
            return True
        return super()._check_game_over(
            check_insufficient_material=check_insufficient_material
        )

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
        return_val = super()._move_piece(
            initial_square,
            final_square,
            allow_castle_and_en_passant=allow_castle_and_en_passant,
            skip_checks=skip_checks,
            no_disambiguator=no_disambiguator,
            return_metadata=return_metadata,
            game_over_checked=game_over_checked,
            seconds_elapsed=seconds_elapsed,
            glyphs=glyphs,
        )
        if self.board.king_is_in_check(self.board.turn):
            self._checks[self.board.turn] += 1
        if self.is_three_check():
            self._moves[-1] = f"{self._moves[-1].replace('+', '').replace('#', '')}#"
        return return_val

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
        super()._en_passant(
            initial_square,
            final_square,
            skip_checks=skip_checks,
            game_over_checked=game_over_checked,
            seconds_elapsed=seconds_elapsed,
            glyphs=glyphs,
        )
        if self.board.king_is_in_check(self.board.turn):
            self._checks[self.board.turn] += 1
        if self.is_three_check():
            self._moves[-1] = f"{re.sub(r'[+#?!]', '', self._moves[-1])}#"

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
        """
        Move the king two spaces right or left and move the closest rook to its
        other side.
        """
        super()._castle(
            color,
            side,
            skip_checks=skip_checks,
            game_over_checked=game_over_checked,
            seconds_elapsed=seconds_elapsed,
            glyphs=glyphs,
        )
        if self.board.king_is_in_check(self.board.turn):
            self._checks[self.board.turn] += 1
        if self.is_three_check():
            self._moves[-1] = f"{self._moves[-1].replace('+', '').replace('#', '')}#"

    def promote_pawn(self, square: str, piece_type: PieceType) -> None:
        """Promote a pawn on the farthest rank from where it started."""
        super().promote_pawn(square, piece_type)
        if self.board.king_is_in_check(self.board.turn):
            self._checks[self.board.turn] += 1
        if self.is_three_check():
            self._moves[-1] = f"{self._moves[-1].replace('+', '').replace('#', '')}#"
