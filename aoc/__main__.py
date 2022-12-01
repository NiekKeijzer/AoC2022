import importlib
import shutil

import click
import requests

from aoc.const import COOKIE_FILE, INPUT_DIR, SHIM_FILE, AOC_DIR


@click.group
def aoc():
    pass


@aoc.command()
@click.argument('day')
def gen(day: str):
    with COOKIE_FILE.open('r') as cookie:
        response = requests.get(f'https://adventofcode.com/2022/day/{day}/input', headers={
            'cookie': cookie.read()
        })

    filename = f"day_{day.zfill(2)}"
    input_file = INPUT_DIR / f"{filename}.txt"
    with input_file.open('wb+') as out:
        out.write(response.content)

    day_py = AOC_DIR / ""
    shutil.copy(SHIM_FILE, day_py / f"{filename}.py")


@aoc.command()
@click.argument('day')
def solve(day: str):
    module_name = f"day_{day.zfill(2)}"
    module = importlib.import_module(f'aoc.{module_name}')

    input_file = INPUT_DIR / f"{module_name}.txt"
    with input_file.open('r') as input_fh:
        lines = [line.strip() for line in input_fh.readlines()]

        click.echo(f'Part 1: {module.part_1(lines)}')
        click.echo(f'Part 2: {module.part_2(lines)}')


if __name__ == '__main__':
    aoc()
