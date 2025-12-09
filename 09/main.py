import sys
from shapely.geometry.polygon import Polygon
from shapely.geometry.point import Point


path = sys.argv[1]

with open(path) as file:
    coords = [tuple(map(int, x.strip().split(","))) for x in file.readlines()]
    N = len(coords)

    part_one = 0
    part_two = 0

    polygon = Polygon([(x, y) for x, y in coords])

    for i in range(N):
        for j in range(i + 1, N):
            x1, y1 = coords[i]
            x2, y2 = coords[j]
            points = list(map(Point, [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]))
            rectangle = Polygon(points)

            area = abs(max(x1, x2) - min(x2, x1) + 1) * abs(
                max(y1, y2) - min(y2, y1) + 1
            )

            if polygon.contains(rectangle):
                part_two = max(part_two, area)

            part_one = max(part_one, area)

    print(f"part one answer is {part_one}")
    print(f"part two answer is {part_two}")
