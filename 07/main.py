from functools import cache
import sys


path = sys.argv[1]

with open(path) as file:
    grid = [x.strip() for x in file.readlines()]
    start = grid[0].index("S")
    beams: set[int] = set()
    beams.add(start)
    part_one = 0

    N, M = len(grid), len(grid[0])

    for i in range(1, N):
        for j in range(M):
            if grid[i][j] == "^" and j in beams:
                part_one += 1
                beams.remove(j)
                if j + 1 < M:
                    beams.add(j + 1)

                if j - 1 > 0:
                    beams.add(j - 1)

    cache = [[0] * M for _ in range(N + 1)]

    for i in range(M):
        cache[-1][i] = 1

    for i in range(N - 1, -1, -1):
        for j in range(M - 1, -1, -1):
            if grid[i][j] == "^" or grid[i][j] == "S":
                if j - 1 >= 0:
                    cache[i][j] += cache[i + 1][j - 1]
                if j + 1 < M:
                    cache[i][j] += cache[i + 1][j + 1]
            else:
                cache[i][j] = cache[i + 1][j]

    part_two = cache[0][start]

    print(f"part one answer is {part_one}")
    print(f"part two answer is {part_two}")
