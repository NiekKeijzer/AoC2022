import collections

from aoc.const import INPUT_DIR
from aoc.utils import clean


def part_1(lines: list[str]):
    calories = 0
    tmp = []
    for line in lines:
        if line:
            tmp.append(int(line))
        else:
            # empty line
            tmp_calories = sum(tmp)
            tmp = []
            if tmp_calories > calories:
                calories = tmp_calories

    return calories


def part_2(lines: list[str]):
    top_3, tmp = [0, 0, 0], []

    for line in lines:
        if line:
            tmp.append(int(line))
        else:
            # empty line
            tmp_calories = sum(tmp)
            tmp = []
            top_3.sort(reverse=True)
            lowest = min(top_3)
            if tmp_calories > lowest:
                top_3.pop(2)
                top_3.append(tmp_calories)

    return sum(top_3)


if __name__ == '__main__':
    INPUT = INPUT_DIR / "01.txt"
    with INPUT.open() as fh:
        lines = clean(fh.readlines())
        print(f"1: {part_1(lines)}")
        print(f"2: {part_2(lines)}")
