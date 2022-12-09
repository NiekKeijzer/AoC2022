import functools
from typing import Generator


def get_column(rows: list, idx: int):
    return [row[idx] for row in rows]


def part_1(lines: Generator[str, None, None]):
    forest = list(lines)

    visible = 0
    edges = (0, 98)
    for row_idx, row in enumerate(forest):
        for col_idx, tree in enumerate(row):
            column = get_column(forest, col_idx)
            if row_idx in edges or col_idx in edges:
                visible += 1
            elif max(row[col_idx + 1:]) < tree:
                # Right
                visible += 1
            elif max(row[:col_idx]) < tree:
                # Left
                visible += 1
            elif max(column[row_idx + 1:]) < tree:
                # Bottom
                visible += 1
            elif max(column[:row_idx]) < tree:
                # Top
                visible += 1

    return visible


def part_2(lines: Generator[str, None, None]):
    result = None

    return result
