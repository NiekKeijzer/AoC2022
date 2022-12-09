def prio(char: str) -> int:
    if char.islower():
        return ord(char) - 96
    return ord(char) - 64 + 26


def part_1(lines: list[str]):
    result = 0
    for line in lines:
        first, second = set(line[:len(line) // 2]), set(line[len(line) // 2:])
        common = first.intersection(second)

        result += sum(prio(c) for c in common)

    return result


def part_2(lines: list[str]):
    result = 0
    group = []
    for line in lines:
        group.append(set(line))

        if len(group) == 3:
            common = group[0].intersection(group[1]).intersection(group[2])
            result += sum(prio(c) for c in common)
            group = []

    return result
