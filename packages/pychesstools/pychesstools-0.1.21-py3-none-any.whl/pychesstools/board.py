"""A chess board."""

import platform
import random
import re
from collections import Counter
from collections.abc import Iterator
from contextlib import contextmanager, suppress
from dataclasses import dataclass
from typing import ClassVar, Final, Literal, NamedTuple, cast, overload

from mypy_extensions import mypyc_attr

from . import RICH_AVAILABLE, WORKING_DIRECTORY
from ._cache import cache
from .openings import Opening, OpeningTree
from .timer import IncrementalTimer
from .types import Color, PieceType, Side, SquareGenerator, StepFunction

if RICH_AVAILABLE:
    from rich.console import Console


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


with (WORKING_DIRECTORY / "data" / "fischer_fens.fen").open() as file:
    FISCHER_SETUPS: list[str] = file.readlines()

with (WORKING_DIRECTORY / "data" / "book.json").open() as file:
    # Uses Lichess Openings (retrieved 2024.01.23).
    # https://github.com/lichess-org/chess-openings
    OPENINGS = OpeningTree.load_json_book(file)

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


@cache
def other_color(color: Color) -> Color:
    """Get white if black, or black if white."""
    return "black" if color == "white" else "white"


@cache
def get_adjacent_files(square: str) -> tuple[str, ...]:
    """Get files adjacent to square."""
    adjacent_files: list[str] = []
    match square[0]:
        case "a":
            adjacent_files = ["b"]
        case "h":
            adjacent_files = ["g"]
        case _:
            for index in FILES.index(square[0]) + 1, FILES.index(square[0]) - 1:
                with suppress(IndexError):
                    adjacent_files.append(FILES[index])
    return tuple(adjacent_files)


@cache
def get_adjacent_squares(square: str) -> tuple[str, ...]:
    """Get squares to left and right of square."""
    return tuple(f"{file}{square[1]}" for file in get_adjacent_files(square))


@cache
def get_squares_between(
    square_1: str, square_2: str, *, strict: bool = False
) -> tuple[str, ...]:
    """Get the squares between two other squares on the board."""
    if square_1 == square_2:
        return ()
    if square_1[0] == square_2[0] and square_1[1] != square_2[1]:
        if int(square_1[1]) < int(square_2[1]):
            iterator = iter_to_top
        else:
            iterator = iter_to_bottom
    elif square_1[0] != square_2[0] and square_1[1] == square_2[1]:
        if FILES.index(square_1[0]) < FILES.index(square_2[0]):
            iterator = iter_to_right
        else:
            iterator = iter_to_left
    elif square_1[0] != square_2[0] and square_1[1] != square_2[1]:
        if int(square_1[1]) < int(square_2[1]) and FILES.index(
            square_1[0]
        ) < FILES.index(square_2[0]):
            iterator = iter_top_right_diagonal
        elif int(square_1[1]) < int(square_2[1]):
            iterator = iter_top_left_diagonal
        elif int(square_1[1]) > int(square_2[1]) and FILES.index(
            square_1[0]
        ) < FILES.index(square_2[0]):
            iterator = iter_bottom_right_diagonal
        else:
            iterator = iter_bottom_left_diagonal
    squares_between = []
    met_square_2 = False
    for sq in iterator(square_1):
        if sq == square_2:
            met_square_2 = True
            break
        squares_between.append(sq)
    if met_square_2:
        return tuple(squares_between)
    else:
        if strict:
            raise ValueError(
                "Squares must be directly diagonal, horizontal, "
                "or vertical to each other."
            )
        else:
            return ()


@cache
def squares_in_rank(rank: int | str) -> tuple[str, ...]:
    """Get all squares in rank."""
    return tuple(f"{file}{rank}" for file in FILES)


@cache
def squares_in_file(file: str) -> tuple[str, ...]:
    """Get all squares in file."""
    return tuple(f"{file}{rank}" for rank in range(1, 9))


@cache
def en_passant_initial_square(disambiguator: str, color: Color) -> str:
    """Get en passant initial square from disambiguator and moving piece color."""
    return f"{disambiguator}{'5' if color == 'white' else '4'}"


@cache
def en_passant_final_square_from_pawn_square(
    double_forward_last_move: str, color: Color
) -> str:
    """En passant final square from ChessBoard._double_forward_last_move."""
    final_rank = (
        int(double_forward_last_move[1]) + 1
        if color == "white"
        else int(double_forward_last_move[1]) - 1
    )
    return f"{double_forward_last_move[0]}{final_rank}"


@cache
def en_passant_final_square_from_file(capture_file: str, color: Color) -> str:
    """En passant final square from capture file (i.e. exd6: 'e')."""
    return f"{capture_file}{6 if color == 'white' else 3}"


@cache
def iter_to_top(square: str) -> tuple[str, ...]:
    """Get board squares up to the top (rank 8)."""
    return tuple(f"{square[0]}{rank}" for rank in range(int(square[1]) + 1, 9))


@cache
def iter_to_bottom(square: str) -> tuple[str, ...]:
    """Get board squares down to the bottom (rank 1)."""
    return tuple(f"{square[0]}{rank}" for rank in range(int(square[1]) - 1, 0, -1))


@cache
def iter_to_right(square: str) -> tuple[str, ...]:
    """Get board squares to the right (file h)."""
    return tuple(f"{file}{square[1]}" for file in FILES[FILES.index(square[0]) + 1 :])


@cache
def iter_to_left(square: str) -> tuple[str, ...]:
    """Get board squares to the left (file a)."""
    return tuple(
        f"{file}{square[1]}" for file in reversed(FILES[: FILES.index(square[0])])
    )


@cache
def iter_top_right_diagonal(square: str) -> tuple[str, ...]:
    """Get board squares diagonally upward and to the right from square."""
    return tuple(
        f"{file}{rank}"
        for file, rank in zip(
            FILES[FILES.index(square[0]) + 1 :],
            range(int(square[1]) + 1, 9),
            strict=False,
        )
    )


@cache
def iter_bottom_left_diagonal(square: str) -> tuple[str, ...]:
    """Get board squares diagonally downward and to the left from square."""
    return tuple(
        f"{file}{rank}"
        for file, rank in zip(
            reversed(FILES[: FILES.index(square[0])]),
            range(int(square[1]) - 1, 0, -1),
            strict=False,
        )
    )


@cache
def iter_top_left_diagonal(square: str) -> tuple[str, ...]:
    """Get board squares diagonally upward and to the left from square."""
    return tuple(
        f"{file}{rank}"
        for file, rank in zip(
            reversed(FILES[: FILES.index(square[0])]),
            range(int(square[1]) + 1, 9),
            strict=False,
        )
    )


@cache
def iter_bottom_right_diagonal(square: str) -> tuple[str, ...]:
    """Get board squares diagonally to the bottom and right from square."""
    return tuple(
        f"{file}{rank}"
        for file, rank in zip(
            FILES[FILES.index(square[0]) + 1 :],
            range(int(square[1]) - 1, 0, -1),
            strict=False,
        )
    )


@cache
def step_up(square: str, steps: int) -> str | None:
    """Get square `steps` up from `square`."""
    return (
        f"{square[0]}{rank}"
        if (rank := int(square[1]) + steps) > 0 and rank < 9
        else None
    )


@cache
def step_down(square: str, steps: int) -> str | None:
    """Get square `steps` down from `square`."""
    return (
        f"{square[0]}{rank}"
        if (rank := int(square[1]) - steps) > 0 and rank < 9
        else None
    )


@cache
def step_right(square: str, steps: int) -> str | None:
    """Get square `steps` right from `square`."""
    return (
        f"{FILES[col_index]}{square[1]}"
        if (col_index := FILES.index(square[0]) + steps) >= 0 and col_index <= 7
        else None
    )


@cache
def step_left(square: str, steps: int) -> str | None:
    """Get square `steps` left from `square`."""
    return (
        f"{FILES[col_index]}{square[1]}"
        if (col_index := FILES.index(square[0]) - steps) >= 0 and col_index <= 7
        else None
    )


@cache
def step_diagonal_up_right(square: str, steps: int) -> str | None:
    """Step diagonally to the top and right from square."""
    cursor: str | None = square
    for _ in range(steps):
        cursor = cast(str, cursor)
        cursor = step_up(cursor, 1)
        if cursor is None:
            return None
        cursor = step_right(cursor, 1)
        if cursor is None:
            return None
    return cursor


@cache
def step_diagonal_up_left(square: str, steps: int) -> str | None:
    """Step diagonally to the top and left from square."""
    cursor: str | None = square
    for _ in range(steps):
        cursor = cast(str, cursor)
        cursor = step_up(cursor, 1)
        if cursor is None:
            return None
        cursor = step_left(cursor, 1)
        if cursor is None:
            return None
    return cursor


@cache
def step_diagonal_down_right(square: str, steps: int) -> str | None:
    """Step diagonally to the bottom and right from square."""
    cursor: str | None = square
    for _ in range(steps):
        cursor = cast(str, cursor)
        cursor = step_down(cursor, 1)
        if cursor is None:
            return None
        cursor = step_right(cursor, 1)
        if cursor is None:
            return None
    return cursor


@cache
def step_diagonal_down_left(square: str, steps: int) -> str | None:
    """Step diagonally to the bottom and left from square."""
    cursor: str | None = square
    for _ in range(steps):
        cursor = cast(str, cursor)
        cursor = step_down(cursor, 1)
        if cursor is None:
            return None
        cursor = step_left(cursor, 1)
        if cursor is None:
            return None
    return cursor


@cache
def step(square: str, file_offset: int = 0, rank_offset: int = 0) -> str | None:
    """Step multiple directions at once."""
    with suppress(IndexError):
        if (file_idx := FILES.index(square[0]) + file_offset) >= 0 and (
            square := f"{FILES[file_idx]}{int(square[1]) + rank_offset}"
        ) in SQUARES:
            return square
    return None


DIRECTION_GENERATORS: Final[dict[tuple[str, str], SquareGenerator]] = {
    ("up", "right"): iter_top_right_diagonal,
    ("up", "inline"): iter_to_top,
    ("up", "left"): iter_top_left_diagonal,
    ("inline", "right"): iter_to_right,
    ("inline", "left"): iter_to_left,
    ("down", "right"): iter_bottom_right_diagonal,
    ("down", "inline"): iter_to_bottom,
    ("down", "left"): iter_bottom_left_diagonal,
}
STEP_FUNCTIONS_BY_DIRECTION: Final[dict[str, StepFunction]] = {
    "up": step_up,
    "right": step_right,
    "left": step_left,
    "down": step_down,
    "up_right": step_diagonal_up_right,
    "up_left": step_diagonal_up_left,
    "down_right": step_diagonal_down_right,
    "down_left": step_diagonal_down_left,
}
ROOK_GENERATORS: Final[tuple[SquareGenerator, ...]] = (
    iter_to_top,
    iter_to_bottom,
    iter_to_right,
    iter_to_left,
)
BISHOP_GENERATORS: Final[tuple[SquareGenerator, ...]] = (
    iter_bottom_left_diagonal,
    iter_bottom_right_diagonal,
    iter_top_left_diagonal,
    iter_top_right_diagonal,
)
QUEEN_GENERATORS: Final[tuple[SquareGenerator, ...]] = (
    ROOK_GENERATORS + BISHOP_GENERATORS
)
GENERATORS_BY_PIECE_TYPE: Final[dict[PieceType, tuple[SquareGenerator, ...]]] = {
    "rook": ROOK_GENERATORS,
    "bishop": BISHOP_GENERATORS,
    "queen": QUEEN_GENERATORS,
}
FORWARD_STEP_FUNCTIONS_BY_PAWN_COLOR: Final[dict[Color, StepFunction]] = {
    "white": step_up,
    "black": step_down,
}
_TERMINATION_BY_STATUS_DESCRIPTION: dict[str, str | None] = {
    "50move": "Game drawn by 50 move rule",
    "75move": "Game drawn by 75 move rule",
    "checkmate": "[WINNER] won by checkmate",
    "stalemate": "Game drawn by stalemate",
    "threefold_repetition": "Game drawn by threefold repetition",
    "fivefold_repetition": "Game drawn by fivefold repetition",
    "agreement": "Game drawn by agreement",
    "resignation": "[LOSER] resigned",
    "insufficient_material": "Game drawn due to insufficient material",
    "timeout": "[WINNER] won on time",
    "timeoutvsinsufficient": "Game drawn by timeout vs insufficient material",
    "king_reached_hill": "[WINNER]'s king reached the hill",  # King of the Hill
    "explosion": "[WINNER] won by exploding [LOSER]'s king",  # Atomic
    "all_pieces_captured": "[WINNER] won by capturing all of [LOSER]'s pieces",  # Horde
    "three_check": "[WINNER] won by checking [LOSER]'s king three times",  # Three-check
}
_GENERATORS_AND_TYPES: Final[
    tuple[tuple[tuple[SquareGenerator, ...], tuple[PieceType, ...]], ...]
] = (ROOK_GENERATORS, ("rook", "queen")), (BISHOP_GENERATORS, ("bishop", "queen"))
_COLORS_AND_RANKS: Final[tuple[tuple[Color, int, int], ...]] = (
    ("white", 1, 2),
    ("black", 8, 7),
)
_PAWN_RANK_BY_COLOR: dict[Color, str] = {"white": "2", "black": "7"}


@cache
def knight_navigable_squares(square: str) -> tuple[str, ...]:
    """Get knight navigable squares on board."""
    squares = []
    for (dir_1, step_1), (dir_2, step_2) in (
        ((dir_1, step_1), (dir_2, step_2))
        for dir_1 in ("up", "down")
        for dir_2 in ("left", "right")
        for step_1, step_2 in ((1, 2), (2, 1))
    ):
        cursor: str | None = square
        cursor = cast(str, cursor)
        for dir, step in ((dir_1, step_1), (dir_2, step_2)):
            cursor = STEP_FUNCTIONS_BY_DIRECTION[dir](cursor, step)
            if cursor is None:
                break
        if cursor is not None:
            squares.append(cursor)
    return tuple(squares)


@cache
def king_navigable_squares(square: str) -> tuple[str, ...]:
    """Get king navigable squares on board."""
    return tuple(
        sq
        for func in STEP_FUNCTIONS_BY_DIRECTION.values()
        if (sq := func(square, 1)) is not None
    )


@cache
def pawn_capturable_squares(color: Color, square: str) -> tuple[str, ...]:
    """Get squares a pawn can capture on."""
    pawn_sq_funcs = (
        (step_diagonal_up_left, step_diagonal_up_right)
        if color == "white"
        else (step_diagonal_down_left, step_diagonal_down_right)
    )
    return tuple(sq for func in pawn_sq_funcs if (sq := func(square, 1)) is not None)


@mypyc_attr(allow_interpreted_subclasses=True)
class ChessBoard:
    """A chess board."""

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
        fen: str | None = None,
        epd: str | None = None,
        pgn: str | None = None,
        *,
        empty: bool = False,
        import_fields: bool = True,
        time_control: str | None = None,
    ) -> None:
        """Create a chess board object."""
        self.halfmove_clock = 0
        self.turn: Color = "white"
        self.initial_fen: str | None = None
        self.fields: Final[dict[str, str]] = {}
        self.clocks: dict[Color, IncrementalTimer] | None = (
            {color: IncrementalTimer(time_control) for color in COLORS}
            if time_control
            else None
        )
        self._grid: Final[dict[str, Piece | None]] = {sq: None for sq in SQUARES}
        self._initial_squares: Final[
            dict[tuple[PieceType, Color, Side | None], str]
        ] = {}
        self._has_moved: Final[dict[tuple[PieceType, Color, Side | None], bool]] = {
            piece_tuple: False for piece_tuple in PIECES_TO_TRACK
        }
        self._kings: Final[dict[Color, str]] = {}
        self._double_forward_last_move: str | None = None
        self._status = GameStatus(game_over=False)
        self._moves: Final[list[str]] = []
        self._moves_before_fen_import = 0
        self._hashes: Final[Counter[int]] = Counter()
        self._must_promote_pawn: str | None = None
        self._move_annotations: dict[str, str] = {}
        self._piece_count: int = 0
        if not empty and fen is None and pgn is None:
            self.set_staunton_pattern()
        if fen is not None and epd is None:
            self.import_fen(fen)
        if fen is None and epd is not None:
            self.import_epd(epd)
        if pgn is not None:
            return self.import_pgn(pgn, import_fields=import_fields)
        with suppress(StopIteration):
            self.set_initial_positions()

    def __getitem__(self, index: str) -> Piece | None:
        """Get a square's current piece, or None if empty."""
        return self._grid[index]

    def __setitem__(self, index: str, value: Piece | None) -> None:
        """Set a square to a piece or None if setting to empty."""
        if value is not None and value.piece_type == "king":
            self._kings[value.color] = index
        self._grid[index] = value

    def __iter__(self) -> Iterator[str]:
        """Iterate through board."""
        return iter(self._grid)

    def __repr__(self) -> str:
        """Represent ChessBoard as string."""
        if self.AUTOPRINT:
            self.print()
        return f"{self.__class__.__name__}('{self.fen}')"

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

    def _is_checked_by_rook_bishop_queen(self, color: Color, king_sq: str) -> bool:
        for generator_list, types in _GENERATORS_AND_TYPES:
            for generator in generator_list:
                for sq in generator(king_sq):
                    if (
                        (pc := self._grid[sq]) is not None
                        and pc.color != color
                        and pc.piece_type in types
                    ):
                        return True
                    elif pc is not None:
                        break
        return False

    def _is_checked_by_pawn(self, color: Color, king_sq: str) -> bool:
        return any(
            (pc := self._grid[sq]) is not None
            and pc.piece_type == "pawn"
            and pc.color == other_color(color)
            for sq in pawn_capturable_squares(color, king_sq)
        )

    def _is_checked_by_king(self, color: Color, king_sq: str) -> bool | None:
        return (
            king in king_navigable_squares(king_sq)
            if (king := self._kings.get(other_color(color))) is not None
            else None
        )

    def _is_checked_by_knight(self, color: Color, king_sq: str) -> bool:
        return any(
            (pc := self._grid[sq]) is not None
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
            and self._grid[sq] is None
        ):
            yield sq
            if (
                initial_square[1] == _PAWN_RANK_BY_COLOR[piece.color]
                and (sq := step_func(initial_square, 2)) is not None
                and self._grid[sq] is None
            ):
                yield sq
        # diagonal capture
        yield from (
            sq
            for sq in pawn_capturable_squares(piece.color, initial_square)
            if (pc := self._grid[sq]) is not None and pc.color != piece.color
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
                if (other_piece := self._grid[sq]) is None:
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
            if (pc := self._grid[sq]) is None or pc.color != piece.color
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
            if (pc := self._grid[sq]) is None or pc.color != piece.color
        )
        if check_castle:
            yield from (
                CASTLING_FINAL_SQUARES[piece.color, side][0]
                for side in SIDES
                if self.can_castle(piece.color, side, check_turn=False)
            )

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
                self.clocks[self.turn].add_move(self.move_number, seconds_elapsed)
            else:
                raise ValueError("Expected seconds_elapsed parameter for timed game.")
        self.turn = other_color(self.turn)
        if reset_hashes:
            self._hashes.clear()
        else:
            self._hashes.update((self._hash_position(),))
        self.halfmove_clock = 0 if reset_halfmove_clock else self.halfmove_clock + 1

    def _handle_missing_clock_update(self, seconds_elapsed: float | None) -> None:
        if self.clocks is not None and seconds_elapsed is None:
            raise ValueError("Expected seconds_elapsed parameter for timed game.")

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
                        if (piece := self._grid[sq]) is not None:
                            if (
                                disambiguator in sq
                                and piece.piece_type == piece_type
                                and piece.color == self.turn
                            ):
                                candidates.append(sq)
                            else:
                                break
            case "pawn":
                # If capturing but moving to an empty square, it must be an en passant.
                # For en passant moves, the file must also be specified (e.g. "exf6").
                # We know the initial rank by color, so there is only one candidate.
                if "x" in notation and self._grid[final_square] is None:
                    candidates = [en_passant_initial_square(disambiguator, self.turn)]
                # If no piece at final square, it must be a forward advance.
                elif self._grid[final_square] is None:
                    step_func = FORWARD_STEP_FUNCTIONS_BY_PAWN_COLOR[
                        other_color(self.turn)
                    ]
                    if (
                        (square := step_func(final_square, 1)) is not None
                        and disambiguator in square
                        and (pc := self._grid[square]) is not None
                        and pc.piece_type == "pawn"
                        and pc.color == self.turn
                    ) or (
                        (square := step_func(final_square, 2)) is not None
                        and disambiguator in square
                        and (pc := self._grid[square]) is not None
                        and pc.piece_type == "pawn"
                        and pc.color == self.turn
                    ):
                        candidates = [square]
                else:  # Otherwise, it's a capture.
                    candidates = [
                        square
                        for square in pawn_capturable_squares(
                            other_color(self.turn), final_square
                        )
                        if (
                            square is not None
                            and disambiguator in square
                            and (pc := self._grid[square]) is not None
                            and pc.piece_type == "pawn"
                            and pc.color == self.turn
                        )
                    ]
            case "knight":
                candidates = [
                    sq
                    for sq in knight_navigable_squares(final_square)
                    if disambiguator in sq
                    and (pc := self._grid[sq]) is not None
                    and pc.piece_type == "knight"
                    and pc.color == self.turn
                ]
            case "king":
                candidates = (
                    [king_sq] if (king_sq := self._kings[self.turn]) is not None else []
                )
        if len(candidates) == 1:
            return candidates[0], False
        elif len(candidates) == 0:
            raise MoveError(f"'{notation}' is not allowed.")
        else:  # Attempt to disambiguate by testing legality of each piece moving.
            successful_candidates = [
                candidate
                for candidate in candidates
                if self.can_move_piece(candidate, final_square, check_turn=False)
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
                        if (pc := self._grid[sq]) == piece:
                            if sq != initial_square and self.can_move_piece(
                                sq,
                                final_square,
                                check_turn=False,
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
                            and self._grid[square] is not None
                            and self.can_move_piece(
                                square,
                                final_square,
                                check_turn=False,
                            )
                        ):
                            ambiguous_pieces = [square]
                            break
            case "knight":
                ambiguous_pieces = [
                    sq
                    for sq in knight_navigable_squares(final_square)
                    if self._grid[sq] == piece
                    and sq != initial_square
                    and self.can_move_piece(
                        sq,
                        final_square,
                        check_turn=False,
                    )
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
        piece = self._get_piece_at_non_empty_square(initial_square)
        if allow_castle_and_en_passant:
            # Try to castle if king is moving to a final castling square, or if rook is
            # jumping over a king.
            castle_side: Side = "queenside" if final_square[0] in "cd" else "kingside"
            if (
                piece.piece_type == "king"
                and final_square in ("c1", "c8", "g1", "g8")
                and self.can_castle(piece.color, castle_side, check_turn=False)
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
                and self._grid[final_square] is None
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
            success, explanation = self.can_move_piece(
                initial_square, final_square, return_explanation_if_false=True
            )
            if not success:
                raise MoveError(explanation)
        # Add piece type notation, disambiguating if necessary.
        piece_at_final_square = self._grid[final_square]
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
            self._piece_count -= 1
            oc = piece_at_final_square.color
            if piece_at_final_square.piece_type == "rook" and (
                (
                    qns := final_square
                    == self._initial_squares.get(("rook", oc, "queenside"))
                )
                or final_square == self._initial_squares.get(("rook", oc, "kingside"))
            ):
                self._has_moved["rook", oc, "queenside" if qns else "kingside"] = True
        else:
            is_capture = False
        notation += final_square
        # Update has_moved variables for castling/en passant.
        if piece.piece_type == "king":
            self._has_moved["king", piece.color, None] = True
        elif piece.piece_type == "rook":
            if initial_square == self._initial_squares.get(
                ("rook", piece.color, "kingside")
            ):
                side: Side | None = "kingside"
            elif initial_square == self._initial_squares.get(
                ("rook", piece.color, "queenside")
            ):
                side = "queenside"
            else:
                side = None
            if side is not None:
                self._has_moved["rook", piece.color, side] = True
        self._double_forward_last_move = (
            final_square
            if piece.piece_type == "pawn"
            and abs(int(initial_square[1]) - int(final_square[1])) == 2
            else None
        )
        # Move piece.
        self[initial_square] = None
        if not piece.has_moved and piece.piece_type == "pawn":
            piece.has_moved = True
        self[final_square] = piece
        # If pawn moving to final rank, require pawn promotion. Else, check for
        # check / checkmate, append moves, and return.
        if piece.piece_type == "pawn" and final_square[1] in ("1", "8"):
            self._must_promote_pawn = final_square
        else:
            self._must_promote_pawn = None
            if self.king_is_in_check(oc := other_color(self.turn)):
                notation += (
                    "#" if self.is_checkmate(kings_known_in_check=(oc,)) else "+"
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

    def _block_if_game_over(self) -> None:
        """Raise an exception if the game is already over."""
        if not self.BLOCK_IF_GAME_OVER:
            return None
        if self._check_game_over():
            raise GameOverError("The game has already ended.")

    def _hash_position(self) -> int:
        return hash(
            (
                (black_king_has_moved := self._has_moved["king", "black", None])
                or self._has_moved["rook", "black", "kingside"],
                black_king_has_moved or self._has_moved["rook", "black", "queenside"],
                (white_king_has_moved := self._has_moved["king", "white", None])
                or self._has_moved["rook", "white", "kingside"],
                white_king_has_moved or self._has_moved["rook", "white", "queenside"],
                self._double_forward_last_move if self.can_en_passant() else None,
                self.turn,
                *self._grid.values(),
            )
        )

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
            can_move, explanation = self.can_castle(
                color, side, check_turn=True, return_explanation_if_false=True
            )
            if not can_move:
                raise MoveError(explanation)
        king_final_sq, rook_final_sq = CASTLING_FINAL_SQUARES[color, side]
        rook_init_sq = self._initial_squares["rook", color, side]
        self[self._kings[color]] = None
        self._grid[rook_init_sq] = None
        self[king_final_sq] = Piece("king", color)
        self._grid[rook_final_sq] = Piece("rook", color)
        self._has_moved["king", color, None] = True
        self._has_moved["rook", color, side] = True
        self._double_forward_last_move = None
        notation = "O-O" if side == "kingside" else "O-O-O"
        if self.king_is_in_check(oc := other_color(self.turn)):
            notation += "#" if self.is_checkmate(kings_known_in_check=(oc,)) else "+"
        self._moves.append(notation + glyphs)
        self._must_promote_pawn = None
        self._alternate_turn(reset_hashes=True, seconds_elapsed=seconds_elapsed)

    def _get_piece_at_non_empty_square(self, square: str) -> Piece:
        if (piece := self._grid[square]) is None:
            raise ValueError(f"No piece at square '{square}'.")
        return piece

    def _check_turn(self, color: Color, *, ignore_pawn_promotion: bool = False) -> None:
        if color != self.turn:
            raise MoveError(f"It is {self.turn}'s turn.")
        if not ignore_pawn_promotion and self._must_promote_pawn is not None:
            raise MoveError(
                f"Must promote pawn at square '{self._must_promote_pawn}'"
                " before next move."
            )

    def _get_double_forward_last_move_strict(self) -> str:
        if (result := self._double_forward_last_move) is None:
            raise ValueError("No pawn can be captured by en passant.")
        return result

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
        piece = self._get_piece_at_non_empty_square(initial_square)
        if not skip_checks:
            can_move, explanation = self.can_en_passant(
                initial_square, return_explanation_if_false=True
            )
            if not can_move:
                raise MoveError(explanation)
        double_forward = self._get_double_forward_last_move_strict()
        self._grid[double_forward] = None
        self._grid[initial_square] = None
        self._grid[final_square] = piece
        self._double_forward_last_move = None
        self._piece_count -= 1
        notation = f"{initial_square[0]}x{final_square}"
        if self.king_is_in_check(oc := other_color(self.turn)):
            notation += "#" if self.is_checkmate(kings_known_in_check=(oc,)) else "+"
        self._moves.append(notation + glyphs)
        self._must_promote_pawn = None
        self._alternate_turn(reset_halfmove_clock=True, seconds_elapsed=seconds_elapsed)

    def _infer_en_passant_initial_square(self) -> str | None:
        double_forward = self._get_double_forward_last_move_strict()
        candidates = [
            sq
            for sq in get_adjacent_squares(double_forward)
            if (pc := self._grid[sq]) is not None
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

    def _check_game_over(self, *, check_insufficient_material: bool = True) -> bool:
        """Check if game is over without checking for stalemate or checkmate."""
        return (
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
            or (check_insufficient_material and self.is_draw_by_insufficient_material())
            or (
                self.ARBITER_DRAW_AFTER_100_HALFMOVE_CLOCK
                and self.can_claim_draw_by_halfmove_clock()
            )
            or self.is_draw_by_75_move_rule()
        )

    def is_timeout(self) -> bool:
        """Whether a player's clock has run out."""
        if self.clocks is None:
            return False
        for color, clock in self.clocks.items():
            if clock.out_of_time:
                oc = other_color(color)
                if not self.player_has_sufficient_material(oc):
                    self._status = GameStatus(
                        game_over=True, winner=None, description="timeoutvsinsufficient"
                    )
                    return True
                self._status = GameStatus(
                    game_over=True, winner=oc, description="timeout"
                )
                return True
        return False

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
                    (piece := self._grid[square]) is not None
                    and piece.piece_type == "pawn"
                    and piece.color == color
                    and self.can_en_passant(square, check_turn=False)
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
    def fen(self) -> str:
        """Export the board in Forsyth-Edwards Notation."""
        return self.export_fen()

    @property
    def epd(self) -> str:
        """Return Extended Position Description (EPD) as string."""
        return self.export_epd()

    @property
    def moves(self) -> str:
        """Export moves to string."""
        return self.export_moves()

    @property
    def pieces(self) -> dict[str, Piece]:
        """Get all pieces on the board."""
        return {sq: piece for sq, piece in self._grid.items() if piece is not None}

    @property
    def opening(self) -> Opening | None:
        """Get ECO opening."""
        return OPENINGS.get_opening(self._moves)

    @property
    def status(self) -> GameStatus:
        """Check the board for a checkmate or draw."""
        if self._status.game_over:
            return self._status
        pieces = self.pieces
        if (
            self.is_checkmate()
            or self.is_stalemate(pieces)
            or self.is_timeout()
            or (
                self.ARBITER_DRAW_AFTER_THREEFOLD_REPETITION
                and self.can_claim_draw_by_threefold_repetition()
            )
            or (
                self.AUTOMATIC_DRAW_AFTER_FIVEFOLD_REPETITION
                and self.is_draw_by_fivefold_repetition()
            )
            or self.is_draw_by_insufficient_material(pieces)
            or (
                self.ARBITER_DRAW_AFTER_100_HALFMOVE_CLOCK
                and self.can_claim_draw_by_halfmove_clock()
            )
            or self.is_draw_by_75_move_rule()
        ):
            return self._status
        return GameStatus(game_over=False)

    @property
    def ascii(self) -> str:
        """Get an ASCII representation of the board."""
        winning_king_sq = None
        if self.status.description == "checkmate":
            winner = cast(Color, self._status.winner)
            winning_king_sq = self._kings[winner]
        output = ""
        for rank in range(8, 0, -1):
            output += f"{rank} "
            for sq in squares_in_rank(rank):
                if (piece := self._grid[sq]) is None:
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

    @contextmanager
    def test_position(self, changes: dict[str, Piece | None]) -> Iterator[None]:
        """
        Make temporary changes to the board to test properties of a position.
        Warning: Do not raise exceptions within a `test_position` context manager.
        """
        original_contents = {sq: self._grid[sq] for sq in changes}
        for sq in changes:
            self[sq] = changes[sq]
        yield
        for sq in original_contents:
            self[sq] = original_contents[sq]

    def set_staunton_pattern(self) -> None:
        """Add Staunton pattern (initial piece squares)."""
        for color, pc_rank, pawn_rank in _COLORS_AND_RANKS:
            for file in FILES:
                self[f"{file}{pawn_rank}"] = Piece("pawn", color)
            self[f"a{pc_rank}"] = Piece("rook", color)
            self[f"b{pc_rank}"] = Piece("knight", color)
            self[f"c{pc_rank}"] = Piece("bishop", color)
            self[f"d{pc_rank}"] = Piece("queen", color)
            self[f"e{pc_rank}"] = Piece("king", color)
            self[f"f{pc_rank}"] = Piece("bishop", color)
            self[f"g{pc_rank}"] = Piece("knight", color)
            self[f"h{pc_rank}"] = Piece("rook", color)

    def set_random(self) -> None:
        """Set board for Fischer random chess / Chess960."""
        fen = random.choice(FISCHER_SETUPS)
        self.import_fen(fen)
        self.fields["Variant"] = "Chess960"

    def set_initial_positions(self) -> None:
        """Set initial positions of pieces used for castling."""
        for color in COLORS:
            rooks = [
                sq
                for sq, pc in self._grid.items()
                if pc is not None and pc.piece_type == "rook" and pc.color == color
            ]
            match len(rooks):
                case 2:
                    (
                        self._initial_squares["rook", color, "queenside"],
                        self._initial_squares["rook", color, "kingside"],
                    ) = (
                        (rooks[0], rooks[1])
                        if FILES.index(rooks[0][0]) < FILES.index(rooks[1][0])
                        else (rooks[1], rooks[0])
                    )
                case 1:
                    for side in SIDES:
                        self._initial_squares["rook", color, side] = rooks[0]
            if self._kings.get(color) is None:
                with suppress(StopIteration):
                    self._kings[color] = next(
                        sq
                        for sq, pc in self._grid.items()
                        if pc is not None
                        and pc.piece_type == "king"
                        and pc.color == color
                    )
            with suppress(KeyError):
                self._initial_squares["king", color, None] = self._kings[color]
        self._piece_count = len(self.pieces)

    def import_pgn(self, pgn: str, *, import_fields: bool = True) -> None:
        """Import a game by PGN string."""
        pgn = pgn.replace("\n", " ")
        pgn = re.sub(r"(?m)^%.+", "", pgn)
        if "[FEN " in pgn and (match := re.search(r"\[FEN \"(.+?)\"\]", pgn)):
            fen = match.group(1)
            self.import_fen(fen)
        else:
            self.set_staunton_pattern()
        self.set_initial_positions()
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

    def _players_last_move(self, color: Color) -> tuple[str, str]:
        move = self._moves[-2 if self.turn == color else -1]
        move_no = self.fullmove_clock
        if self.turn == "white" or (self.turn == "black" and color == "black"):
            move_no -= 1
        return f"{move_no}{'...' if color == 'black' else '.'}", move

    @property
    def move_number(self) -> str:
        """Get move number in PGN format (i.e. '32.', '32...')."""
        num = self.fullmove_clock
        suffix = "." if self.turn == "white" else "..."
        return f"{num}{suffix}"

    def import_epd(self, epd: str) -> None:
        """Import Extended Position Description to board."""
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
                    self[cursor] = Piece(*FEN_REPRESENTATIONS[char])
                    if (cur := step_right(cursor, 1)) is not None:
                        cursor = cur
                elif char.isnumeric():
                    self[cursor] = None
                    if (cur := step_right(cursor, int(char))) is not None:
                        cursor = cur
        self.turn = "white" if groups[8] == "w" else "black"
        if groups[10] != "-":
            self._double_forward_last_move = (
                f"{groups[10][0]}{5 if groups[10][1] == 6 else 4}"
            )
        self.set_initial_positions()
        # Set castling availability.
        if groups[9] == "-":
            for color in COLORS:
                self._has_moved["king", color, None] = True
        else:
            for color in COLORS:
                chars_defined = False
                with suppress(KeyError):
                    queenside_rook_char, kingside_rook_char = (
                        sq[0]
                        if (sq := self._initial_squares["rook", color, side])
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
                            self._has_moved["rook", color_, side] = True
                    break
        # Set hmvc, fmvn.
        for opcode, operand in re.findall(r"(hmvc|fmvn) (\d+);", epd):
            match opcode:
                case "hmvc":
                    self.halfmove_clock = int(operand)
                case "fmvn":
                    self._moves_before_fen_import = int(operand) - 1
                    if self.turn == "black":
                        self._moves.append("_")
        self.initial_fen = self.fen

    def import_fen(self, fen: str) -> None:
        """Import Forsyth-Edwards Notation to board."""
        self.import_epd(fen)
        if match := re.search(r" (?P<halfmove>\d+) (?P<fullmove>\d+)$", fen):
            halfmove, fullmove = match.groups()
            self.halfmove_clock = int(halfmove)
            self._moves_before_fen_import = int(fullmove) - 1
            if self.turn == "black":
                self._moves.append("_")
        self.initial_fen = fen

    def export_fen(self, *, no_clocks: bool = False, shredder: bool = False) -> str:
        """Export the board in Forsyth-Edwards Notation."""
        fen = ""
        # Concatenate piece placement data.
        for rank in range(8, 0, -1):
            blank_sq_counter = 0
            for sq in squares_in_rank(rank):
                if (piece := self._grid[sq]) is None:
                    blank_sq_counter += 1
                    continue
                if blank_sq_counter > 0:
                    fen += str(blank_sq_counter)
                    blank_sq_counter = 0
                fen += PLAINTEXT_ABBRS_BY_TYPE_AND_COLOR[piece.piece_type, piece.color]
            if blank_sq_counter > 0:
                fen += str(blank_sq_counter)
            if rank > 1:
                fen += "/"
        # Concatenate active color.
        fen += f" {self.turn[0]} "
        # Concatenate castling availability.
        symbols: dict[tuple[Color, Side], str] = {
            ("white", "kingside"): "K",
            ("black", "kingside"): "k",
            ("white", "queenside"): "Q",
            ("black", "queenside"): "q",
        }
        if shredder:
            for color, side in symbols:
                char = self._initial_squares["rook", color, side][0]
                symbols[color, side] = char.upper() if color == "white" else char
        any_castles_possible = False
        for color in COLORS:
            for side in SIDES:
                if (
                    not self._has_moved["king", color, None]
                    and not self._has_moved["rook", color, side]
                ):
                    fen += symbols[color, side]
                    any_castles_possible = True
        if not any_castles_possible:
            fen += "-"
        fen += " "
        # Concatenate en passant target square.
        if self._double_forward_last_move is not None:
            fen += self._double_forward_last_move[0]
            if (char := self._double_forward_last_move[1]) == "4":
                fen += "3"
            elif char == "5":
                fen += "6"
        else:
            fen += "-"
        # Concatenate halfmove and fullmove clocks.
        if not no_clocks:
            fen += f" {self.halfmove_clock} {self.fullmove_clock}"
        return fen

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
        output = self.export_fen(no_clocks=True)
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
        status = self.status
        output += f" {PGN_RESULT_BY_WINNER[status.winner] if status.game_over else '*'}"
        output = output.replace(". _", "...").strip().replace("  ", " ")
        return self._wrap_moves(output, wrap) if wrap else output

    def legal_moves(self, square: str) -> Iterator[str]:
        """Get legal moves for a piece."""
        piece = self._get_piece_at_non_empty_square(square)
        for sq in self._pseudolegal_squares(square):
            # If the piece is a pawn diagonal to the pseudolegal square, and the square
            # at pseudolegal square is None, it must be an en passant.
            if (
                (pt := piece.piece_type) == "pawn"
                and sq[0] in get_adjacent_files(square)
                and self._grid[sq] is None
            ):
                if self.can_en_passant(square, check_turn=False):
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
                        check_turn=False,
                    )
                )
            ) or self.can_move_piece(
                square,
                sq,
                navigability_already_checked=True,
                check_turn=False,
            ):
                yield sq

    @overload
    def can_move_piece(
        self,
        initial_square: str,
        final_square: str,
        *,
        check_turn: bool = True,
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
        check_turn: bool = True,
        navigability_already_checked: bool = False,
        return_explanation_if_false: Literal[True],
    ) -> tuple[bool, str | None]:
        ...

    def can_move_piece(
        self,
        initial_square: str,
        final_square: str,
        *,
        check_turn: bool = True,
        navigability_already_checked: bool = False,
        return_explanation_if_false: bool = False,
    ) -> bool | tuple[bool, str | None]:
        """Check if a piece can be moved to final_square without castling/en passant."""
        piece = self._get_piece_at_non_empty_square(initial_square)
        piece_at_final_square = self._grid[final_square]
        if check_turn:
            self._check_turn(piece.color)
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
                self.turn,
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
            if "x" in notation and self._grid[final_square] is None:
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

    @overload
    def can_castle(
        self,
        color: Color,
        side: Side | None = None,
        *,
        check_turn: bool = False,
        return_explanation_if_false: Literal[False] = False,
    ) -> bool:
        ...

    @overload
    def can_castle(
        self,
        color: Color,
        side: Side | None = None,
        *,
        check_turn: bool = False,
        return_explanation_if_false: Literal[True],
    ) -> tuple[bool, str | None]:
        ...

    def can_castle(
        self,
        color: Color,
        side: Side | None = None,
        *,
        check_turn: bool = False,
        return_explanation_if_false: bool = False,
    ) -> bool | tuple[bool, str | None]:
        """Check if a player can castle. Optionally specify side."""
        if check_turn:
            self._check_turn(color)
        if self._has_moved["king", color, None]:
            return (
                (False, "Cannot castle because king has already moved.")
                if return_explanation_if_false
                else False
            )
        if (king_sq := self._initial_squares.get(("king", color, None))) is None:
            return (
                (False, "Could not determine castling availability.")
                if return_explanation_if_false
                else True
            )
        squares_by_side = [
            (
                self._initial_squares.get(("rook", color, side_)),
                self._has_moved["rook", color, side_],
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
                self._grid[sq] is None
                for sq in get_squares_between(king_sq, rook_init_sq)
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
                (pc := self._grid[sq]) is None
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
        check_turn: bool = True,
        return_explanation_if_false: Literal[False] = False,
    ) -> bool:
        ...

    @overload
    def can_en_passant(
        self,
        initial_square: str | None = None,
        *,
        check_turn: bool = True,
        return_explanation_if_false: Literal[True],
    ) -> tuple[bool, str | None]:
        ...

    def can_en_passant(
        self,
        initial_square: str | None = None,
        *,
        check_turn: bool = True,
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
        if check_turn:
            self._check_turn(piece.color)
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

    def promote_pawn(self, square: str, piece_type: PieceType) -> None:
        """Promote a pawn on the farthest rank from where it started."""
        piece = self._get_piece_at_non_empty_square(square)
        self._check_turn(piece.color, ignore_pawn_promotion=True)
        if (piece.color == "white" and square[1] != "8") or (
            piece.color == "black" and square[1] != "1"
        ):
            msg = f"Cannot promote pawn at square '{square}'."
            raise MoveError(msg)
        self._grid[square] = Piece(
            piece_type, piece.color, promoted=True, has_moved=True
        )
        self._double_forward_last_move = None
        self._must_promote_pawn = None
        notation = f"{self._moves[-1]}={PLAINTEXT_ABBRS[piece_type]}"
        if self.king_is_in_check(oc := other_color(self.turn)):
            notation += "#" if self.is_checkmate(kings_known_in_check=(oc,)) else "+"
        self._moves[-1] = notation
        self._alternate_turn(reset_halfmove_clock=True, reset_hashes=True)

    def is_checkmate(
        self, *, kings_known_in_check: tuple[Color, ...] | None = None
    ) -> bool:
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
                self._status = GameStatus(
                    game_over=True, winner=other_color(color), description="checkmate"
                )
                return True
        return False

    def is_stalemate(self, pieces: dict[str, Piece] | None = None) -> bool:
        """Check if the game is a stalemate."""
        pieces_ = self.pieces if pieces is None else pieces
        if all(
            len(tuple(self.legal_moves(sq))) == 0
            for sq, pc in pieces_.items()
            if pc.color == self.turn
        ) and not self.can_castle(self.turn):
            self._status = GameStatus(game_over=True, description="stalemate")
            return True
        return False

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

    def player_has_sufficient_material(self, color: Color) -> bool:
        """Whether a player has sufficient material to check the opponent's king."""
        if not self.CHECK_FOR_INSUFFICIENT_MATERIAL:
            return False
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
    ) -> bool:
        """Check if board has insufficient material."""
        if not self.CHECK_FOR_INSUFFICIENT_MATERIAL:
            return False
        if self._piece_count > 4:
            return False
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
            self._status = GameStatus(
                game_over=True, description="insufficient_material"
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
        for sq, pc in self._grid.items():
            if pc is not None:
                result[pc.color][sq] = pc
        return result

    def king_is_in_check(self, color: Color) -> bool | None:
        """Whether the king is in check."""
        return (
            None
            if (king_sq := self._kings.get(color)) is None
            else self.is_checked_square(color, king_sq)
        )

    def king_can_escape_check(self, color: Color) -> bool | None:
        """Whether a king can escape check (assuming it is in check)."""
        return (
            len(tuple(self.legal_moves(king))) > 0
            if self._grid[king := self._kings[color]] is not None
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
        for sq, check_pc in self._grid.items():
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
        checks = self.get_threatening_pieces(self._kings[color], color)
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
                    check_turn=False,
                    navigability_already_checked=True,
                ):
                    return True
        return False

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
            sq for sq, pc in self._grid.items() if pc is not None and pc.color == oc
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
                        (pc := self._grid[sq]) is not None
                        and pc.color != color_
                        and pc.piece_type in types
                    ):
                        threatening_pieces.append((sq, pc))
                        break
                    elif pc is not None:
                        break
        oc = other_color(color_)
        if (other_king := self._kings.get(oc)) in king_navigable_squares(square):
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
            if (pc := self._grid[sq]) is not None
            and pc.piece_type == pt
            and pc.color == oc
        )
        if square_is_empty and (
            (
                (sq_ := FORWARD_STEP_FUNCTIONS_BY_PAWN_COLOR[color_](square, 1))
                is not None
                and (pc := self._grid[sq_]) is not None
                and pc.piece_type == "pawn"
                and pc.color == oc
            )
            or (
                pc is None
                and (sq_ := FORWARD_STEP_FUNCTIONS_BY_PAWN_COLOR[color_](square, 2))
                is not None
                and sq_[1] in ("2", "7")
                and (pc := self._grid[sq_]) is not None
                and pc.piece_type == "pawn"
                and pc.color == oc
            )
        ):
            threatening_pieces.append((sq_, pc))
        return dict(threatening_pieces)

    def resign(self, color: Color | None = None) -> GameStatus:
        """Resign instead of moving."""
        self._status = GameStatus(
            game_over=True,
            winner=other_color(self.turn if color is None else color),
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

    def print(self, *, plaintext: bool = False) -> None:
        """Print the ChessBoard to console."""
        if not plaintext and RICH_AVAILABLE:
            Console().print(self._rich_renderable())
        else:
            print(self.ascii)
