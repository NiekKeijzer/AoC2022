def contained(a, b):
    return (b[0] <= a[0] <= b[1] and b[0] <= a[1] <= b[1]) or (a[0] <= b[0] <= a[1] and a[0] <= b[1] <= a[1])


def overlap(a, b):
    return (b[0] <= a[0] <= b[1]) or (b[0] <= a[1] <= b[1]) or (a[0] <= b[0] <= a[1]) or (a[0] <= b[1] <= a[1])


def part_1(lines: list[str]):
    result = 0
    for line in lines:
        a, b = line.split(',')
        a = [int(x) for x in a.split('-')]
        b = [int(x) for x in b.split('-')]

        if contained(a, b):
            result += 1

    return result


def part_2(lines: list[str]):
    result = 0
    for line in lines:
        a, b = line.split(',')
        a = [int(x) for x in a.split('-')]
        b = [int(x) for x in b.split('-')]

        if overlap(a, b):
            result += 1

    return result
