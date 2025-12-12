from functools import cache
import sys
from collections import defaultdict, deque
from typing import cast

path = sys.argv[1]

with open(path) as file:
    part_one = 0
    nested = [[y.strip() for y in line.split(":")] for line in file.readlines()]

    lines = [[x[0], x[1].split(" ")] for x in nested]
    adj_list: defaultdict[str, list[str]] = defaultdict(list)

    for line in lines:
        source, targets = cast(str, line[0]), cast(list[str], line[1])

        for target in targets:
            adj_list[source].append(target)

    q: deque[str] = deque()
    q2: deque[tuple[int, str]] = deque()

    q.append("you")
    q2.append((0, "svr"))

    while q:
        node = q.popleft()

        if node == "out":
            part_one += 1
        else:
            for next in adj_list[node]:
                q.append(next)

    @cache
    def dfs(node: str, count: int):
        if node == "out" and count == 2:
            return 1
        if node == "out":
            return 0

        if node == "fft" or node == "dac":
            count += 1

        ans = 0

        for nn in adj_list[node]:
            ans += dfs(nn, count)

        return ans

    part_two = dfs("svr", 0)

    print(f"part one answer is {part_one}")
    print(f"part one answer is {part_two}")
