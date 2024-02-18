"""Data structures for JSON tree of openings."""

from __future__ import annotations

import json
from collections import UserDict
from collections.abc import MutableMapping, Sequence
from contextlib import suppress
from io import TextIOWrapper
from typing import NamedTuple, TypedDict, Union, cast, overload

from .pgn import moves_list_from_pgn


class Opening(NamedTuple):
    """An ECO game opening."""

    eco: str
    name: str
    moves: str


class OpeningDict(TypedDict):
    """An ECO opening dict as read from an OpeningTree."""

    eco: str
    moves: str
    name: str


class OpeningTree(UserDict[str | None, Union[OpeningDict, "OpeningTree"]]):
    """A tree of OpeningDicts nested by moves."""

    @overload
    def __getitem__(self, key: None) -> OpeningDict:
        ...

    @overload
    def __getitem__(self, key: str) -> OpeningTree:
        ...

    @overload
    def __getitem__(self, key: str | None) -> OpeningDict | OpeningTree:
        ...

    def __getitem__(self, key: str | None) -> OpeningDict | OpeningTree:
        return super().__getitem__(key)

    @staticmethod
    def _replace_null_str_with_none(
        mapping: MutableMapping[str | None, OpeningTree | OpeningDict]
    ) -> None:
        """Replace 'null' string keys with None recursively."""
        for k, v in mapping.items():
            if k == "null":
                mapping[None] = mapping.pop(k)
            else:
                v = cast(OpeningTree, v)
                OpeningTree._replace_null_str_with_none(v)

    @staticmethod
    def _to_dicts(tree: OpeningTree) -> list[OpeningDict]:
        """Create a list of OpeningDicts from tree, suitable for JSON export."""
        openings = []
        for k, v in tree.items():
            if k is None:
                v = cast(OpeningDict, v)
                openings.append(v)
            else:
                v = cast(OpeningTree, v)
                openings.extend(OpeningTree._to_dicts(v))
        return openings

    @classmethod
    def load_json_tree(cls, file: TextIOWrapper) -> OpeningTree:
        """Load an OpeningTree from a JSON file."""
        tree = json.load(file)
        cls._replace_null_str_with_none(tree)
        return cls(tree)

    @classmethod
    def load_json_book(cls, file: TextIOWrapper) -> OpeningTree:
        """Load an OpeningTree from a JSON list of OpeningDicts."""
        book = json.load(file)
        return cls.from_dicts(book)

    @classmethod
    def from_dicts(cls, openings: list[OpeningDict]) -> OpeningTree:
        """Make an OpeningTree from a list of OpeningDicts."""
        tree = cls()
        for opening in openings:
            bare_moves = moves_list_from_pgn(opening["moves"])
            cursor = tree
            for move in bare_moves:
                if move not in cursor:
                    cursor[move] = cls()
                cursor = cursor[move]
            cursor[None] = opening
        return tree

    def to_dicts(self) -> list[OpeningDict]:
        """Create a list of OpeningDicts from tree, suitable for JSON export."""
        return self._to_dicts(self)

    def get_opening(self, moves: Sequence[str]) -> Opening | None:
        """Get the ECO opening for a sequence of moves."""
        cursor = self
        last_matched_opening: OpeningDict | None = None
        for move in moves:
            try:
                cursor = cursor[move]
            except KeyError:
                break
            else:
                with suppress(KeyError):
                    last_matched_opening = cursor[None]
        if None in cursor:
            return Opening(**cursor[None])
        elif last_matched_opening is not None:
            return Opening(**last_matched_opening)
        else:
            return None
