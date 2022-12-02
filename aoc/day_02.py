# A : Rock
# B : Paper
# C : Scissor


# X : Rock
# Y : Paper
# Z : Scissor

POINTS_TABLE = {
    "A": ["Z", "X", "Y"],
    "B": ["X", "Y", "Z"],
    "C": ["Y", "Z", "X"]
}
FACTOR = {
    'X': 1,
    'Y': 2,
    'Z': 3
}
OUTCOME_POINTS = [0, 3, 6]

GUIDE = {
    'X': 0,
    'Y': 1,
    'Z': 2,
}


def score(x, y) -> int:
    points_idx = POINTS_TABLE[x].index(y)

    return FACTOR[y] + OUTCOME_POINTS[points_idx]


def part_1(lines: list[str]):
    result = 0

    for line in lines:
        x, y = line.split(' ')
        result += score(x, y)

    return result


def part_2(lines: list[str]):
    result = 0

    for line in lines:
        x, y = line.split(' ')

        # Override y with what we're supposed to choose
        g = GUIDE[y]
        y = POINTS_TABLE[x][g]

        result += score(x, y)

    return result
