import dataclasses
import functools
from typing import Generator, Union, Optional


@dataclasses.dataclass
class File:
    name: str
    size: int


@dataclasses.dataclass
class Directory:
    name: str
    parent: Optional['Directory']
    children: list[Union[File, 'Directory']] = dataclasses.field(default_factory=list)

    @functools.cached_property
    def size(self) -> int:
        return sum(c.size for c in self.children)

    def total(self) -> int:
        total = sum(d.size for d in self.directories) + sum(f.size for f in self.files)

        return total

    @property
    def directories(self) -> list['Directory']:
        return list(filter(lambda c: isinstance(c, Directory), self.children))

    @property
    def files(self) -> list['Directory']:
        return list(filter(lambda c: isinstance(c, File), self.children))


def build_tree(lines: Generator[str, None, None]):
    current = Directory('/', None)
    root = current

    for i, line in enumerate(lines):
        if i == 0:
            continue

        if line.startswith('$ ls'):
            # Noop; implied
            continue
        elif line.startswith('$ cd'):
            _, target = line.rsplit(' ', 1)
            if target == '..':
                current = current.parent
            else:
                for d in current.directories:
                    if d.name == target:
                        current = d

                        break
        elif line.startswith('dir'):
            _, name = line.split(' ')
            current.children.append(Directory(name, current))
        else:
            size, name = line.split(' ')
            current.children.append(File(name, int(size)))

    return root


def smaller_than(directory: Directory, max_size: int = 100_000):
    if directory.size < max_size:
        yield directory

    for sub in directory.directories:
        yield from smaller_than(sub, max_size)


def part_1(lines: Generator[str, None, None]):
    tree = build_tree(lines)

    return sum(d.size for d in smaller_than(tree))


def part_2(lines: Generator[str, None, None]):
    result = None

    return result
