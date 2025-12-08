from functools import cache
import math
import sys

import heapq

path, count = sys.argv[1], int(sys.argv[2])

with open(path) as file:
    boxes = [tuple(map(int, x.strip().split(","))) for x in file.readlines()]

    N = len(boxes)
    seen: set[tuple[int, int]] = set()
    heap: list[tuple[float, int, int]] = []

    junctions: list[list[int]] = [[i] for i in range(N)]

    for i in range(N):
        for j in range(i + 1, N):
            b1, b2 = boxes[i], boxes[j]

            x1, y1, z1 = b1
            x2, y2, z2 = b2

            if (i, j) in seen or (j, i) in seen:
                continue

            seen.add((i, j))

            dist = math.sqrt(
                math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2) + math.pow(z1 - z2, 2)
            )

            heapq.heappush(heap, (dist, i, j))
    heap2 = heap[::]

    cnt = 0
    while cnt < count:
        cnt += 1
        _, i, j = heapq.heappop(heap)
        j1, j2 = junctions[i], junctions[j]

        if j1 == j2:
            continue

        for item in j2:
            j1.append(item)

        for item in j2:
            junctions[item] = j1

    lengths = [-x for x in list(map(len, set([tuple(x) for x in junctions if x])))]
    heapq.heapify(lengths)
    x1, x2, x3 = heapq.heappop(lengths), heapq.heappop(lengths), heapq.heappop(lengths)
    part_one = -x1 * -x2 * -x3

    junctions2: list[list[int]] = [[i] for i in range(N)]
    part_two = 0

    while heap2:
        _, i, j = heapq.heappop(heap2)
        j1, j2 = junctions2[i], junctions2[j]

        if j1 == j2:
            continue

        for item in j2:
            j1.append(item)

        for item in j2:
            junctions2[item] = j1

        if len(set([tuple(x) for x in junctions2])) == 1:
            part_two = boxes[i][0] * boxes[j][0]

    print(f"part one answer is {part_one}")
    print(f"part one answer is {part_two}")
