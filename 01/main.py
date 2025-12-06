import sys
from typing import Callable

path = sys.argv[1]

with open(path) as file:
    entries = [x.strip() for x in file.readlines()]
    curr = 50
    part_one = 0
    part_two = 0

    op_codes: dict[str, Callable[[int], int]] = {
        "R": lambda x: (curr + x) % 100,
        "L": lambda x: (curr - x) % 100,
    }

    for entry in entries:
        code, arg = entry[0], int(entry[1:])
        cache = part_two

        if code == "L" and curr - arg <= 0:
            part_two = part_two + 1 + (abs(curr - arg) // 100)

            if curr == 0:
                part_two -= 1

        if code == "R" and curr + arg >= 100:
            part_two = part_two + (abs(curr + arg) // 100)

        curr = op_codes[code](arg)

        if curr == 0:
            part_one += 1

    print(f"part one answer is {part_one}")
    print(f"part two answer is {part_two}")
