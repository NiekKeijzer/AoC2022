import collections
from typing import Generator


def marker(inp: str, size: int):
    buffer = collections.deque([], size)
    for i, char in enumerate(inp):
        buffer.append(char)
        if len(set(buffer)) == size:
            return i + 1


def part_1(lines: Generator[str, None, None]):
    return marker(next(lines), 4)


def part_2(lines:  Generator[str, None, None]):
    return marker(next(lines), 14)
