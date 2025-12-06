import sys

path = sys.argv[1]

with open(path) as file:
    grid = [[y for y in x.strip()] for x in file.readlines()]
    m, n = len(grid), len(grid[0])

    positions = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    part_one = 0
    part_two = 0

    for x in range(m):
        for y in range(n):
            curr = 0

            if grid[x][y] == ".":
                continue

            for dx, dy in positions:
                nx, ny = x + dx, y + dy

                if nx < 0 or nx == m or ny < 0 or ny == n or grid[nx][ny] == ".":
                    continue

                curr += 1

            if curr < 4:
                part_one += 1

    removed = True

    while removed:
        removed = False
        for x in range(m):
            for y in range(n):
                curr = 0

                if grid[x][y] == ".":
                    continue

                for dx, dy in positions:
                    nx, ny = x + dx, y + dy

                    if nx < 0 or nx == m or ny < 0 or ny == n or grid[nx][ny] == ".":
                        continue

                    curr += 1

                if curr < 4:
                    part_two += 1
                    removed = True
                    grid[x][y] = "."

    print(f"part one answer is {part_one}")
    print(f"part two answer is {part_two}")
