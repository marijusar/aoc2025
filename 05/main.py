from re import L
import sys


path = sys.argv[1]

with open(path) as file:
    part_one = 0
    part_two = 0
    ranges, ingredients = [x.strip().split("\n") for x in file.read().split("\n\n")]

    ingredients = list(map(int, ingredients))
    ranges = [[int(y) for y in x.split("-")] for x in ranges]

    for i in ingredients:
        spoiled = True

        for x, y in ranges:
            if x <= i <= y:
                spoiled = False

        if not spoiled:
            part_one += 1

    ranges.sort()

    merged: list[list[int]] = []

    for x, y in ranges:
        if y < x:
            print("here")
        if merged and merged[-1][1] >= x:
            px, py = merged.pop()

            merged.append([px, max(y, py)])
        else:
            merged.append([x, y])

    for i, p in enumerate(merged):
        x, y = p
        part_two += y - x + 1

    print(f"part one answer is {part_one}")
    print(f"part two answer is {part_two}")
