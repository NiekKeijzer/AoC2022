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


def count_until(seq: list[int], until: int) -> int:
    i = 0
    for j in seq:
        i += 1
        if j >= until:
            break

    return i


def part_2(lines: Generator[str, None, None]):
    forest = list(lines)

    highest = 0
    for row_idx, row in enumerate(forest):
        for col_idx, tree in enumerate(row):
            column = get_column(forest, col_idx)

            up = count_until(list(reversed(column[:row_idx])), tree)
            left = count_until(list(reversed(row[:col_idx])), tree)
            right = count_until(row[col_idx + 1:], tree)
            down = count_until(column[row_idx + 1:], tree)

            score = up * left * down * right
            if score > highest:
                highest = score

    return highest
