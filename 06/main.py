import sys
from typing import Callable


path = sys.argv[1]

with open(path) as file:
    part_one = 0
    part_two = 0
    lines = [x.rstrip('\n') for x in file.readlines()]
    grid = [[y for y in x.strip().split(" ") if y != ""] for x in lines]
    bps = [i - 1 for i, x in enumerate(lines[-1]) if x != " "]

    m, n = len(grid), len(grid[0])
    x, y = len(lines), len(lines[0])

    ops: dict[str, Callable[[int, int], int]] = {
        "*": lambda x, y: x * y,
        "+": lambda x, y: x + y,
    }

    problems: list[list[str]] = [list(reversed(x)) for x in zip(*grid)]

    total = 0
    base = 0
    fn = ops["+"]

    for j in range(y):
        num = ""
        if lines[-1][j] == "*" or lines[-1][j] == "+" :
            fn = ops[lines[-1][j]]
            part_two += base
            base = 1 if lines[-1][j] == "*" else 0

        for i in range(x - 1):
            if lines[i][j] != " " :
                num += lines[i][j]

        if num :
            base = fn(base, int(num))

    part_two += base


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
