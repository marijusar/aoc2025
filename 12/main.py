import sys

path = sys.argv[1]

with open(path) as file:
    areas = [7, 7, 7, 5, 6, 7]
    lines = file.readlines()
    part_one = 0
    for line in lines:
        space, items = line.split(":")
        space = list(map(int, space.strip().split("x")))
        items = list(map(int, items.strip().split(" ")))

        area = space[0] * space[1]

        shapes_area = sum([x * areas[i] for i, x in enumerate(items)])

        if shapes_area <= area:
            part_one += 1

    print(f"part one answer is {part_one}")
