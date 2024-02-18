"""Atomic chess."""

from collections.abc import Iterator
from typing import Literal, overload

from ..game import ChessGame
from ..position import ChessPosition
from ..types import (
    CASTLING_FINAL_SQUARES,
    COLORS,
    PLAINTEXT_ABBRS,
    SIDES,
    Color,
    GameStatus,
    MoveError,
    Piece,
    PieceType,
    Side,
)
from ..utils import (
    en_passant_final_square_from_file,
    get_adjacent_squares,
    king_navigable_squares,
    other_color,
)


class AtomicPosition(ChessPosition):
    """Atomic chess position."""

    def king_is_in_check(self, color: Color) -> bool | None:
        """Whether king is in check."""
        if self.kings.get(color) is None:
            return None
        if self.king_exploded():
            return False
        if any(
            (pc := self[sq]) is not None
            and pc.piece_type == "king"
            and pc.color == other_color(color)
            for sq in king_navigable_squares(self.kings[color])
        ):
            return False
        return super().king_is_in_check(color)

    def is_checked_square(self, color: Color, square: str) -> bool:
        """Whether a square is threatened by an opposite color piece."""
        return (
            False
            if square in king_navigable_squares(self.kings[other_color(color)])
            else super().is_checked_square(color, square)
        )

    def _explosion_dict(self, final_square: str) -> dict[str, Piece | None]:
        """Return dict of explosion changes without actually exploding."""
        return {
            sq: None
            for sq in (final_square, *king_navigable_squares(final_square))
            if sq == final_square
            or ((pc := self[sq]) is not None and pc.piece_type != "pawn")
        }

    def king_exploded(self, color: Color | None = None) -> GameStatus | None:
        """Whether a king has exploded (ending the game)."""
        colors_ = COLORS if color is None else (color,)
        for color in colors_:
            if self[self.kings[color]] is None:
                return GameStatus(
                    game_over=True, winner=other_color(color), description="explosion"
                )
        return None

    def can_explode_opponent_king(self, color: Color) -> bool:
        """Whether color can indirectly explode opponent's king."""
        return self.can_explode_piece(self.kings[other_color(color)])

    def can_explode_piece(self, square: str) -> bool:
        """Whether a piece can be removed by capturing an adjacent piece."""
        piece = self._get_piece_at_non_empty_square(square)
        unsafe_to_capture = [
            sq
            for sq in king_navigable_squares(self.kings[other_color(piece.color)])
            if (pc := self[sq]) is not None
        ]
        if_captured_then_piece_explodes = (
            [
                sq
                for sq in king_navigable_squares(square)
                if (pc := self[sq]) is not None
                and pc.color == piece.color
                and sq not in unsafe_to_capture
            ]
            if piece.piece_type != "pawn"
            else []
        )
        other_color_pieces = [
            sq
            for sq in self
            if (pc := self[sq]) is not None and pc.color == other_color(piece.color)
        ]
        for square_ in other_color_pieces:
            if any(
                sq in if_captured_then_piece_explodes
                for sq in self._pseudolegal_squares(square_, capture_only=True)
                if self.can_move_piece(square_, sq)
            ):
                return True
        return False

    def _king_pseudolegal_squares(
        self,
        initial_square: str,
        piece: Piece,
        *,
        check_castle: bool = False,
    ) -> Iterator[str]:
        """Get king pseudolegal squares (ignores king capture rules)."""
        yield from (
            sq for sq in king_navigable_squares(initial_square) if self[sq] is None
        )
        if check_castle:
            yield from (
                CASTLING_FINAL_SQUARES[piece.color, side][1]
                for side in SIDES
                if self.can_castle(piece.color, side)
            )

    def can_explode_out_of_check(self, color: Color) -> bool:
        """Whether check can be resolved by exploding a threatening piece."""
        return all(
            self.can_explode_piece(sq)
            for sq, _ in self.get_threatening_pieces(self.kings[color], color).items()
        )

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
            (
                piece_at_final_square.piece_type == "king"
                and piece_at_final_square.color == piece.color
            )
            or piece.piece_type == "king"
        ):
            return (
                (False, "Cannot capture king.")
                if return_explanation_if_false
                else False
            )
        changes = {final_square: piece, initial_square: None}
        if piece_at_final_square is not None:
            changes.update(self._explosion_dict(final_square))
        with self.test_position(changes):
            if self.king_is_in_check(piece.color) or self.king_exploded(piece.color):
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
                and not self.can_explode_opponent_king(color)
                and not self.can_explode_out_of_check(color)
            ):
                return GameStatus(
                    game_over=True, winner=other_color(color), description="checkmate"
                )
        return None

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
        changes = {
            initial_square: None,
            (final_sq := en_passant_final_square_from_file(capture_file, color)): Piece(
                "pawn", color
            ),
            self._double_forward_last_move: None,
        }
        changes.update(self._explosion_dict(final_sq))
        with self.test_position(changes):
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


class AtomicGame(ChessGame[AtomicPosition]):
    """Atomic chess game."""

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
            position_cls=AtomicPosition,
        )
        self.fields["Variant"] = "Atomic"

    def promote_pawn(self, square: str, piece_type: PieceType) -> None:
        """Promote a pawn on the farthest rank from where it started."""
        if self.board[square] is None:
            self._double_forward_last_move = None
            self._must_promote_pawn = None
            updated_notation = f"{self._moves[-1]}={PLAINTEXT_ABBRS[piece_type]}"
            if self.board.king_is_in_check(oc := other_color(self.board.turn)):
                if (
                    self.board.is_checkmate(kings_known_in_check=(oc,))
                    or self.board.king_exploded()
                ):
                    updated_notation += "#"
                else:
                    updated_notation += "+"
            self._moves[-1] = updated_notation
            self._alternate_turn(reset_halfmove_clock=True)
        else:
            super().promote_pawn(square, piece_type)

    def _explode(self, final_square: str) -> None:
        """Create an atomic "explosion" after a capture."""
        for sq in self.board._explosion_dict(final_square):
            if (pc := self.board[sq]) is not None and pc.piece_type == "king":
                self._status = GameStatus(
                    game_over=True,
                    winner=other_color(pc.color),
                    description="explosion",
                )
            self.board[sq] = None

    @overload
    def _move_piece(
        self,
        initial_square: str,
        final_square: str,
        *,
        allow_castle_and_en_passant: bool = True,
        ignore_turn: bool = False,
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
        ignore_turn: bool = False,
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
        ignore_turn: bool = False,
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
        ignore_turn: bool = False,
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
        piece = self.board._get_piece_at_non_empty_square(initial_square)
        if not skip_checks and self._must_promote_pawn is not None:
            msg = (
                f"Must promote pawn at square '{self._must_promote_pawn}' "
                "before next move."
            )
            raise MoveError(msg)
        assert piece is not None
        if (
            not skip_checks
            and self.board[final_square] is not None
            and (
                piece.piece_type == "king"
                or self.board.kings[piece.color] in king_navigable_squares(final_square)
            )
        ):
            msg = "Suicidal capture not allowed."
            raise MoveError(msg)
        if allow_castle_and_en_passant:
            # Try to castle if king is moving to a final castling square, or if rook is
            # jumping over a king.
            castle_side: Side = (
                "queenside" if final_square[0] in ("c", "d") else "kingside"
            )
            if (
                piece.piece_type == "king"
                and final_square in ("c1", "c8", "g1", "g8")
                and self.board.can_castle(piece.color, castle_side)
            ):
                self._castle(
                    piece.color,
                    castle_side,
                    skip_checks=True,
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
                    seconds_elapsed=seconds_elapsed,
                    glyphs=glyphs,
                )
                return (
                    {"move_type": "en_passant", "capture": True}
                    if return_metadata
                    else None
                )

        if not skip_checks:
            # Check correct player's piece is being moved.
            if not ignore_turn and piece.color != self.board.turn:
                msg = f"It is {self.board.turn}'s turn."
                raise MoveError(msg)
            # Check piece can navigate to square.
            if final_square not in self.board._pseudolegal_squares(
                initial_square, check_castle=False
            ):
                msg = "Not a valid move."
                raise MoveError(msg)
            # Test if king would be in check if moved.
            king_would_be_in_check = False
            changes = {final_square: piece, initial_square: None}
            if self.board[final_square] is not None:
                changes.update(self.board._explosion_dict(final_square))
            with self.board.test_position(changes):
                if self.board.king_is_in_check(self.board.turn):
                    king_would_be_in_check = True
            if king_would_be_in_check:
                msg = "Cannot move piece because king would be in check."
                raise MoveError(msg)

        # Add piece type notation, disambiguating if necessary.
        piece_at_final_square = self.board[final_square]
        notation = (
            PLAINTEXT_ABBRS[piece.piece_type] if piece.piece_type != "pawn" else ""
        )
        notation += self._write_disambiguator(
            initial_square,
            final_square,
            piece,
            piece_at_final_square,
            no_disambiguator=no_disambiguator,
        )

        # Update clocks and notation to denote capture, and raise exceptions for illegal
        # captures.
        if piece_at_final_square is not None:
            if piece.piece_type == "pawn" and len(notation) == 0:
                notation += initial_square[0]
            notation += "x"
            is_capture = True
            if piece_at_final_square.color == piece.color:
                msg = "Cannot place piece at square occupied by same color piece."
                raise MoveError(msg)
            elif piece_at_final_square.piece_type == "king":
                msg = "Cannot capture king."
                raise MoveError(msg)
        else:
            is_capture = False
        notation += final_square

        # Update has_moved variables (used to determine castling availability).
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
            piece = Piece(
                piece_type=piece.piece_type,
                color=piece.color,
                promoted=piece.promoted,
                has_moved=True,
            )
        self.board[final_square] = piece
        if is_capture:
            self._explode(final_square)

        # If pawn moving to final rank, require pawn promotion. Else, check for
        # check / checkmate, append moves, and return.
        if piece.piece_type == "pawn" and final_square[1] in ("1", "8"):
            self._must_promote_pawn = final_square
        else:
            self._must_promote_pawn = None
            if self.board.king_is_in_check(oc := other_color(self.board.turn)):
                if (
                    self.board.is_checkmate(kings_known_in_check=(oc,))
                    or self.board.king_exploded()
                ):
                    notation += "#"
                else:
                    notation += "+"
            self._alternate_turn(
                reset_halfmove_clock=(piece.piece_type == "pawn" or is_capture),
                seconds_elapsed=seconds_elapsed,
            )
        self._moves.append(notation)
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
        self._explode(final_square)
        self._moves[-1] = self._moves[-1].replace("+", "").replace("#", "")
        if self.board.king_is_in_check(self.board.turn):
            if (
                self.board.is_checkmate(kings_known_in_check=(self.board.turn,))
                or self.board.king_exploded()
            ):
                self._moves[-1] += "#"
            else:
                self._moves[-1] += "+"

    @property
    def status(self) -> GameStatus:
        """Check the board for a checkmate or draw."""
        if self.board.king_exploded():
            return self._status
        return super().status

    @property
    def moves(self) -> str:
        """Export moves to string."""
        if self.board.is_checkmate() or self.board.king_exploded():
            self._moves[-1] = f"{self._moves[-1].replace('+', '').replace('#', '')}#"
        return super().moves
