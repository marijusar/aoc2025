import sys
from typing import Callable


path = sys.argv[1]

with open(path) as file:
    part_one = 0
    part_two = 0
    lines = [x.rstrip() for x in file.readlines()]
    grid = [[y for y in x.strip().split(" ") if y != ""] for x in lines]
    bps = [i - 1 for i, x in enumerate(lines[-1]) if x != " "]

    m, n = len(grid), len(grid[0])
    x, y = len(lines), len(lines[0])
    print(lines)

    ops: dict[str, Callable[[int, int], int]] = {
        "*": lambda x, y: x * y,
        "+": lambda x, y: x + y,
    }

    problems: list[list[str]] = [list(reversed(x)) for x in zip(*grid)]

    for j in range(y):
        for i in range(x):
            print(lines[i][j])

    for problem in problems:
        op = problem[0]
        k = len(problem)

        curr = 1 if op == "*" else 0

        fn = ops[op]

        for i in range(1, k):
            curr = fn(curr, int(problem[i]))

        part_one += curr

    print(f"part one answer is {part_one}")
    print(f"part two answer is {part_two}")
