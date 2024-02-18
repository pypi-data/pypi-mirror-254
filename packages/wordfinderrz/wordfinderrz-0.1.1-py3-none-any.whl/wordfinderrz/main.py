"""Make a word search."""

import functools
import random
import string
import operator
from collections.abc import Callable, Iterable, Iterator
from typing import Annotated, Literal, Final, overload

Direction = Literal[
    "up", "down", "left", "right", "down-left", "down-right", "up-left", "up-right"
]
GridIndex = tuple[Annotated[int, "row"], Annotated[int, "col"]]
StartingPositionGenerator = Callable[[int, int, int], Iterator[tuple[int, int]]]
Operator = Callable[[int, int], int]
ALPHABET = tuple(string.ascii_uppercase)
STEP_OPERATORS: Final[dict[Direction, tuple[Operator | None, Operator | None]]] = {
    "up": (operator.sub, None),
    "down": (operator.add, None),
    "left": (None, operator.sub),
    "right": (None, operator.add),
    "down-left": (operator.add, operator.sub),
    "down-right": (operator.add, operator.add),
    "up-left": (operator.sub, operator.sub),
    "up-right": (operator.sub, operator.add),
}
STARTING_POSITION_GENERATORS: Final[dict[Direction, StartingPositionGenerator]] = {
    "right": lambda w, h, len: ((r, c) for r in range(h) for c in range(w - len + 1)),
    "left": lambda w, h, len: ((r, c) for r in range(h) for c in range(len - 1, w)),
    "down": lambda w, h, len: ((r, c) for r in range(h - len + 1) for c in range(w)),
    "up": lambda w, h, len: ((r, c) for r in range(len - 1, h) for c in range(w)),
    "up-right": lambda w, h, len: (
        (r, c) for r in range(len - 1, h) for c in range(w - len + 1)
    ),
    "up-left": lambda w, h, len: (
        (r, c) for r in range(len - 1, h) for c in range(len - 1, w)
    ),
    "down-right": lambda w, h, len: (
        (r, c) for r in range(h - len + 1) for c in range(w - len + 1)
    ),
    "down-left": lambda w, h, len: (
        (r, c) for r in range(h - len + 1) for c in range(len - 1, w)
    ),
}


class PlacementError(Exception):
    """Raised when a word cannot be placed on the grid."""


class WordSearch:
    """
    A word search, like the one that that sub for Mrs. Morris's class yelled at me for
    striking through the words instead of circling them in fourth grade.
    """

    def __init__(
        self,
        bank: Iterable[str],
        width: int,
        height: int,
        max_attempts: int = 2000,
        _fill_empty: bool = True,
    ) -> None:
        """Create a word search of a specified size from a bank of terms."""
        self.bank = [word.upper() for word in bank]
        self.grid = self._make_grid(width, height)
        self.width = width
        self.height = height
        self.indexes: Final = [
            (row, col) for row in range(height) for col in range(width)
        ]
        self.populate_grid(max_attempts)
        if _fill_empty:
            self._fill_empty_with_random()

    def __repr__(self) -> str:
        """Represent WordSearch as a string."""
        result = ""
        for row in self.grid:
            for char in row:
                result += f" {char}" if char is not None else " -"
            result += " \n"
        return result

    @overload
    def __getitem__(self, idx: int) -> list[str | None]: ...

    @overload
    def __getitem__(self, idx: GridIndex) -> str | None: ...

    def __getitem__(self, idx: int | GridIndex) -> list[str | None] | str | None:
        """Fetch a row or cell."""
        return self.grid[idx[0]][idx[1]] if isinstance(idx, tuple) else self.grid[idx]

    @overload
    def __setitem__(self, idx: int, val: list[str | None]) -> None: ...

    @overload
    def __setitem__(self, idx: GridIndex, val: str | None) -> None: ...

    def __setitem__(
        self, idx: int | GridIndex, val: list[str | None] | str | None
    ) -> None:
        """Set a row or cell."""
        if isinstance(idx, tuple) and not isinstance(val, list):
            self.grid[idx[0]][idx[1]] = val
        elif isinstance(idx, int) and isinstance(val, list):
            self.grid[idx] = val
        else:
            raise ValueError(
                "must set `int` index to `list[str | None]` or `GridIndex` "
                "to `str | None`"
            )

    @staticmethod
    def _make_grid(width: int, height: int) -> list[list[str | None]]:
        """Make an empty grid (a list of lists of chars)."""
        return [[None for _ in range(width)] for _ in range(height)]

    def _fill_empty_with_random(self) -> None:
        """Fill all grid values set to None to a random letter."""
        for i_r, row in enumerate(self.grid):
            for i_c, cell in enumerate(row):
                if cell is None:
                    self.grid[i_r][i_c] = random.choice(ALPHABET)

    def _place_word(
        self,
        word: str,
        starting_position: GridIndex,
        direction: Direction,
        *,
        force: bool = False,
    ) -> None:
        """Place a word on the grid."""
        indexes = tuple(self._iter_idxs(starting_position, direction))
        if len(indexes) < len(word):
            raise PlacementError("word does not fit in grid")
        for idx, char in zip(indexes, word, strict=False):
            if force or self[idx] in (None, char):
                self[idx] = char
            else:
                raise PlacementError("failed to place word")

    def _can_place_word(
        self, word: str, starting_position: GridIndex, direction: Direction
    ) -> bool:
        """Whether a word can be placed at a certain position."""
        indexes = tuple(self._iter_idxs(starting_position, direction))
        if len(indexes) < len(word):
            return False
        for idx, char in zip(indexes, word, strict=False):
            if self[idx] not in (None, char):
                return False
        return True

    def _iter_idxs(
        self, starting_position: GridIndex, direction: Direction
    ) -> Iterator[GridIndex]:
        operators = STEP_OPERATORS[direction]
        if not self._grid_index_is_in_bounds(starting_position):
            raise ValueError(f"starting_position {starting_position} is out of bounds")
        cursor = starting_position
        while self._grid_index_is_in_bounds(cursor):
            yield cursor
            if (op := operators[0]) is not None:
                cursor = op(cursor[0], 1), cursor[1]
            if (op := operators[1]) is not None:
                cursor = cursor[0], op(cursor[1], 1)

    def _grid_index_is_in_bounds(self, index: GridIndex) -> bool:
        return 0 <= index[0] < self.height and 0 <= index[1] < self.width

    @functools.cache
    @staticmethod
    def _starting_positions(
        width: int, height: int, length: int
    ) -> list[tuple[GridIndex, Direction]]:
        """Get starting positions on an empty grid for a word of a certain length."""
        result: list[tuple[GridIndex, Direction]] = []
        for direction, generator in STARTING_POSITION_GENERATORS.items():
            result.extend((idx, direction) for idx in generator(width, height, length))
        return result

    def populate_grid(self, max_attempts: int) -> None:
        """Populate the grid with the words in the bank."""
        if max(len(word) for word in self.bank) > min((self.height, self.width)):
            raise ValueError("max word length cannot exceed height or width")
        for _ in range(max_attempts):
            failed = False
            for word in self.bank:
                starting_positions = WordSearch._starting_positions(
                    self.width, self.height, len(word)
                )
                random.shuffle(starting_positions)
                successfully_placed_word = False
                for position in starting_positions:
                    if self._can_place_word(word, *position):
                        successfully_placed_word = True
                        self._place_word(word, *position, force=True)
                        break
                if not successfully_placed_word:
                    failed = True
                    break
            if not failed:
                break
        if failed:
            raise PlacementError(
                f"failed to create word search in {max_attempts} attempts"
            )
