from typing import Generator


def move_rope(lines, rope_coords: list):
    visits = set()
    visits.add(rope_coords[-1])

    for line in lines:
        direction, steps = line.split(' ')
        for _ in range(int(steps)):
            # head
            if direction == "R":
                rope_coords[0] = (rope_coords[0][0], rope_coords[0][1] + 1)
            elif direction == "L":
                rope_coords[0] = (rope_coords[0][0], rope_coords[0][1] - 1)
            elif direction == "U":
                rope_coords[0] = (rope_coords[0][0] - 1, rope_coords[0][1])
            elif direction == "D":
                rope_coords[0] = (rope_coords[0][0] + 1, rope_coords[0][1])

            # tail
            for knot_i in range(1, len(rope_coords)):
                row_d = rope_coords[knot_i - 1][0] - rope_coords[knot_i][0]
                col_d = rope_coords[knot_i - 1][1] - rope_coords[knot_i][1]

                if row_d != 0:
                    row_d -= 1 if row_d > 0 else -1

                if col_d != 0:
                    col_d -= 1 if col_d > 0 else -1

                if row_d or col_d:
                    rope_coords[knot_i] = (rope_coords[knot_i - 1][0] - row_d, rope_coords[knot_i - 1][1] - col_d)

            visits.add(rope_coords[-1])

    return len(visits)


def part_1(lines: Generator[str, None, None]):
    return move_rope(lines, [(10, 10)] * 2)


def part_2(lines: Generator[str, None, None]):
    return move_rope(lines, [(10, 10)] * 10)
