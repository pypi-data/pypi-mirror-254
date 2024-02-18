"""Basic types for ChessBoard and subclasses."""

import platform
from collections.abc import Callable
from dataclasses import dataclass
from typing import Final, Literal, NamedTuple

from . import RICH_AVAILABLE

PieceType = Literal["king", "queen", "rook", "bishop", "knight", "pawn"]
Color = Literal["white", "black"]
Side = Literal["kingside", "queenside"]
SquareGenerator = Callable[[str], tuple[str, ...]]
StepFunction = Callable[[str, int], str | None]


class MoveError(Exception):
    """Raised when an invalid move is played."""


class GameOverError(Exception):
    """Raised when player attempts to move after game has ended."""


@dataclass
class Piece:
    """A piece on a chess board."""

    piece_type: PieceType
    color: Color
    promoted: bool = False
    has_moved: bool = False

    def __eq__(self, other: object) -> bool:
        """Check if two pieces are of the same type and color."""
        return (
            self.piece_type == other.piece_type and self.color == other.color
            if isinstance(other, Piece)
            else False
        )

    def __hash__(self) -> int:
        """Hash piece."""
        return id(self)


class GameStatus(NamedTuple):
    """Status of the game."""

    game_over: bool
    winner: Color | None = None
    description: str | None = None


COLORS: Final[tuple[Color, ...]] = "white", "black"
SIDES: Final[tuple[Side, ...]] = "queenside", "kingside"
FILES: Final = tuple("abcdefgh")
PIECE_TYPES: Final[tuple[PieceType, ...]] = (
    "rook",
    "bishop",
    "knight",
    "queen",
    "king",
    "pawn",
)
SQUARES: Final = tuple(f"{file}{rank}" for rank in range(1, 9) for file in FILES)
PIECE_SYMBOLS: Final[dict[PieceType, str]] = {
    "king": "♚",
    "queen": "♛",
    "rook": "♜",
    "bishop": "♝",
    "knight": "♞",
    "pawn": "♟︎"
    if "Windows" not in platform.system() and RICH_AVAILABLE
    else ":chess_pawn:",
}
BLACK_SQUARES: Final = tuple(
    [f"{file}{rank}" for file in "aceg" for rank in (1, 3, 5, 7)]
    + [f"{file}{rank}" for file in "bdfh" for rank in (2, 4, 6, 8)]
)
WHITE_SQUARES: Final = tuple(sq for sq in SQUARES if sq not in BLACK_SQUARES)
PLAINTEXT_ABBRS: Final[dict[PieceType, str]] = {
    "knight": "N",
    "rook": "R",
    "bishop": "B",
    "pawn": "P",
    "queen": "Q",
    "king": "K",
}
PLAINTEXT_ABBRS_BY_TYPE_AND_COLOR: Final[dict[tuple[PieceType, Color], str]] = {
    (pt, color): PLAINTEXT_ABBRS[pt]
    if color == "white"
    else PLAINTEXT_ABBRS[pt].lower()
    for pt in PIECE_TYPES
    for color in COLORS
}
ALGEBRAIC_PIECE_ABBRS: Final[dict[str, PieceType]] = {
    "K": "king",
    "Q": "queen",
    "R": "rook",
    "B": "bishop",
    "N": "knight",
    "": "pawn",
    "P": "pawn",
}
FEN_REPRESENTATIONS: Final = {
    v: k for k, v in PLAINTEXT_ABBRS_BY_TYPE_AND_COLOR.items()
}
CASTLING_FINAL_SQUARES: Final[dict[tuple[Color, Side], tuple[str, str]]] = {
    ("white", "kingside"): ("g1", "f1"),
    ("white", "queenside"): ("c1", "d1"),
    ("black", "kingside"): ("g8", "f8"),
    ("black", "queenside"): ("c8", "d8"),
}
CASTLING_DEFAULT_CHARS: Final[tuple[tuple[Side, str], ...]] = (
    ("queenside", "q"),
    ("kingside", "k"),
)
PIECES_TO_TRACK: Final[tuple[tuple[PieceType, Color, Side | None], ...]] = (
    ("king", "white", None),
    ("rook", "white", "kingside"),
    ("rook", "white", "queenside"),
    ("king", "black", None),
    ("rook", "black", "kingside"),
    ("rook", "black", "queenside"),
)
WINNER_BY_PGN_RESULT: Final[dict[str, Color | None]] = {
    "1-0": "white",
    "0-1": "black",
    "1/2-1/2": None,
}
PGN_RESULT_BY_WINNER: Final = {v: k for k, v in WINNER_BY_PGN_RESULT.items()}
PGN_HEADER_FIELDS: Final = "Event", "Site", "Date", "Round", "White", "Black"
PIECE_VALUES: Final[dict[PieceType, int]] = {
    "queen": 9,
    "rook": 5,
    "bishop": 3,
    "knight": 3,
    "pawn": 1,
    "king": 0,  # Kings do not have a point value.
}
