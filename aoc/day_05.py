def build_stacks(lines: list[str]):
    stacks = []
    for i in range(9):
        stacks.append([])

    for line in lines:
        for i, char in enumerate(line):
            if char.isalpha():
                stacks[i // 4].append(char)

    for i, stack in enumerate(stacks):
        stacks[i] = list(reversed(stack))

    return stacks


def part_1(lines: list[str]):
    inp = list(lines)
    stacks = build_stacks(inp[:8])

    for instruction in inp[10:]:
        _, count, _, source, _, target = instruction.split()
        count, source, target = int(count), int(source) - 1, int(target) - 1

        for _ in range(count):
            stacks[target].append(stacks[source].pop())

    return "".join(x[-1] for x in stacks)


def part_2(lines: list[str]):
    result = None

    return result
