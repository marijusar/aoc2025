import functools
import math
import sys


path = sys.argv[1]


with open(path) as file:
    banks = [[int(y) for y in x.strip()] for x in file.readlines()]
    part_one = 0
    part_two = 0
    diff = [0] * len(banks)

    for j, bank in enumerate(banks):
        sorted_bank = sorted(bank)
        index = (
            bank.index(sorted_bank[-1])
            if bank.index(sorted_bank[-1]) < len(bank) - 1
            else bank.index(sorted_bank[-2])
        )

        max_digit = bank[index]

        curr = max_digit * 10

        for i in range(index + 1, len(bank)):
            curr = max(max_digit * 10 + bank[i], curr)

        diff[j] = curr
        part_one += curr

    for i, bank in enumerate(banks):

        @functools.cache
        def dfs(i: int, j: int) -> int | float:
            if i == len(bank):
                return float("-inf")

            if j == 0:
                return max(bank[i], dfs(i + 1, j))

            p = math.pow(10, j)
            take = int(bank[i] * p)
            v1, v2 = dfs(i + 1, j), take + dfs(i + 1, j - 1)
            value = max(v1, v2)

            return value

        v = dfs(0, 11)

        part_two += v

    print(f"part one answer is {part_one}")
    print(f"part two answer is {part_two}")
