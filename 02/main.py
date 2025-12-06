import math
import sys


path = sys.argv[1]

with open(path) as file:
    ranges = [x.split("-") for x in file.readline().strip().split(",")]
    part_one = 0
    part_two = 0
    acc: list[int] = []

    for x, y in ranges:
        x1, y1 = int(x), int(y)

        while x1 <= y1:
            s = str(x1)
            omit = False

            for i in range(1, len(s)):
                if s.replace(s[:i], "") == "":
                    omit = True
                    break

            if omit:
                part_two += x1
            if len(s) % 2 == 1:
                x1 += 1
                continue

            if s[len(s) // 2 :] == s[: len(s) // 2]:
                part_one += x1

            x1 += 1

    print(f"part one answer is {part_one}")
    print(f"part two answer is {part_two}")
