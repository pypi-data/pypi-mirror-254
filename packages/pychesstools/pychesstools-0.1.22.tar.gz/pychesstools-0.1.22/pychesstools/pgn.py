"""Utilities for managing PGN files."""

import re
from collections.abc import Iterable, Iterator
from datetime import datetime
from pathlib import Path


def get_pgn_field(pgn: str, name: str) -> str | None:
    """Get PGN field by field name and PGN text."""
    return mat.group(1) if (mat := re.search(rf"\[{name} \"(.+?)\"\]", pgn)) else None


def pgn_database_to_dicts(path: Path | str) -> list[dict[str, int | str | None]]:
    """Read a .pgn file to a list of dicts."""
    return [
        {
            "game_no": i,
            "variant": get_pgn_field(pgn, "Variant"),
            "imported_pgn": pgn,
            "imported_bare_moves": strip_bare_moves_from_pgn(pgn),
            "imported_result": get_pgn_field(pgn, "Result"),
            "imported_termination": get_pgn_field(pgn, "Termination"),
            "imported_initial_fen": get_pgn_field(pgn, "FEN"),
        }
        for i, pgn in enumerate(iter_pgn_file(path))
    ]


def read_pgn_file(path: Path | str) -> list[str]:
    """Read a .pgn file to a list of PGN strings."""
    with Path(path).open() as file:
        text = file.read()
    return [f"[{pgn}" for pgn in text.split("\n\n[") if len(pgn) > 0 and pgn[0] != "["]


def write_pgn_file(
    pgns: Iterable[str], path: Path | str, *, overwrite: bool = False
) -> None:
    """Write a PGN file from a sequence of PGN strings."""
    path = Path(path)
    exception: Exception | None = None
    with path.open("w" if overwrite else "x") as file:
        try:
            file.write("\n".join(pgns))
        except Exception as exc:  # noqa: BLE001
            exception = exc
    if exception is None:
        return None
    elif not overwrite:
        path.unlink(missing_ok=True)
    raise exception


def iter_pgn_file(db: Path | str) -> Iterator[str]:
    """Iterate through PGN strings in file."""
    output = ""
    with Path(db).open() as file:
        for line in file:
            if output != "" and "[Event " in line:
                yield re.sub(r"\n+$", "\n", output)
                output = ""
            output += line


def strip_bare_moves_from_pgn(pgn: str, *, strip_numbers: bool = True) -> str:
    """Strip the SAN tokens from a PGN string."""
    pattern = (
        r"\[.+?\]|\{.+?\}|\d+\.+|[10]-[10]|\*|1/2-1/2|[?!]"
        if strip_numbers
        else r"\[.+?\]|\{.+?\}|[10]-[10]|\*|1/2-1/2|[?!]"
    )
    return re.sub(r"[\n\s]+", " ", re.sub(pattern, "", pgn)).replace("P@", "@").strip()


def moves_list_from_pgn(pgn: str) -> list[str]:
    """Get list of SAN tokens from a PGN string."""
    return re.sub(r"\[.+?\]|\{.+?\}|\d+\.+|[10]-[10]|\*|1/2-1/2|[?!]", "", pgn).split()


def date_to_pgn_format(date: datetime) -> str:
    """Convert a date into a PGN format string (YYYY-MM-DD)."""
    return date.strftime("%Y.%m.%d")
