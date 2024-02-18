"""An incremental chess clock."""

from __future__ import annotations

import re
from collections.abc import Callable
from typing import Final, Literal

from .types import Color


class IncrementalTimer:
    """A chess clock with support for incremental and sudden death time controls."""

    def __init__(self, controls: str, remaining: float | None = None) -> None:
        """Create an IncrementalClock object."""
        if match := re.search(r"(\d+)(?:\+(\d+))?", controls):
            groups = match.groups()
            self.allocated: Final = int(groups[0])
            self.increment: Final = int(grp) if (grp := groups[1]) else 0
            self.seconds_remaining: float = (
                float(self.allocated) if remaining is None else remaining
            )
            self.controls = controls
            self.history: dict[str, float] = {}  # move number: time elapsed
        else:
            raise ValueError(
                "Failed to parse time controls. Give the number of seconds allocated "
                "for the player and the number of seconds to add after each turn, "
                "separated by a plus ('+') sign. Examples: '300+0', '720+15'."
            )

    def __repr__(self) -> str:
        """IncrementalTimer string representation."""
        return (
            f"{self.__class__.__name__}(controls='{self.allocated}+{self.increment}', "
            f"seconds_remaining={self.seconds_remaining:.2f})"
        )

    @property
    def out_of_time(self) -> bool:
        """Whether the clock has run out."""
        return self.seconds_remaining == 0.0

    @out_of_time.setter
    def out_of_time(self, value: Literal[True]) -> None:
        if value is True:
            self.seconds_remaining = 0.0
        else:
            raise ValueError("Can only set out_of_time to True.")

    def add_move(self, move_no: str, seconds_elapsed: float) -> None:
        """Update the timer after a move."""
        self.seconds_remaining -= seconds_elapsed
        if self.seconds_remaining > 0.0:
            self.seconds_remaining += self.increment
        elif self.seconds_remaining < 0.0:
            self.seconds_remaining = 0.0
        self.history[move_no] = self.seconds_remaining

    @staticmethod
    def read_annotation(annotation: str) -> float:
        """Read clock value from move annotation in [%clk 0:00:00.0] format."""
        if match := re.search(
            r"(?P<hours>\d+):(?P<minutes>\d+):(?P<seconds>[\d\.]+)", annotation
        ):
            hours, minutes, seconds = (float(group) for group in match.groups())
            return (3600 * hours) + (60 * minutes) + seconds
        else:
            raise ValueError("Could not read timestamp.")

    @staticmethod
    def format_annotation(seconds_remaining: float) -> str:
        """Format [%clk 0:00:00.0] move annotation."""
        parts = seconds_remaining
        hours = int(parts // 3600)
        parts %= 3600
        minutes = int(parts // 60)
        parts %= 60
        seconds = int(parts // 1)
        parts %= 1
        return f"[%clk {hours}:{minutes:02}:{seconds:04.1f}]"

    @classmethod
    def from_pgn(cls, pgn: str, player_color: Color) -> IncrementalTimer:
        """Create a clock for a player from a PGN string."""
        if match := re.search(r"\[TimeControl \"(.+?)\"\]", pgn):
            time_control = match.group(1)
        else:
            raise ValueError("PGN is missing TimeControl tag.")
        clock = cls(time_control)
        move_no_condition: Callable[[str], bool] = (
            (lambda k: "..." in k)
            if player_color == "black"
            else (lambda k: "..." not in k)
        )
        matches = re.findall(r"(\d+\.+)[^\.\{]+?\{(.+?)\}", pgn)
        clock.history = {
            k: (last := cls.read_annotation(v))
            for k, v in matches
            if move_no_condition(k)
        }
        clock.seconds_remaining = float(last)
        return clock
