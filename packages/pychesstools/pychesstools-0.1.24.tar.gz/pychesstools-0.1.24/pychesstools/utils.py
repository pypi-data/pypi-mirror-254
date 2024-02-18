"""Board navigation utilities."""

from contextlib import suppress
from typing import Final, cast

from ._cache import cache
from .types import FILES, SQUARES, Color, PieceType, SquareGenerator, StepFunction


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
