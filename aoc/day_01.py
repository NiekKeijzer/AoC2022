def part_1(lines: list[str]):
    result = 0
    tmp = []
    for line in lines:
        if line:
            tmp.append(int(line))
        else:
            # empty line
            tmp_calories = sum(tmp)
            tmp = []
            if tmp_calories > result:
                result = tmp_calories

    return result


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
