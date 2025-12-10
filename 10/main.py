import collections
import sys
import scipy


path = sys.argv[1]

with open(path) as file:
    lines = [x.strip().split(" ") for x in file.readlines()]
    part_one = 0
    part_two = 0
    for line in lines:
        target, buttons, joltage = (
            line[0][1:-1],
            [list(map(int, x[1:-1].split(","))) for x in line[1:-1]],
            [list(map(int, x[1:-1].split(","))) for x in line[-1:]][0],
        )

        start: collections.deque[tuple[str, int]] = collections.deque()
        start.append(("." * len(target), 0))
        seen: set[str] = set()

        found = False

        while not found:
            state, count = start.popleft()
            for b in buttons:
                if state == target:
                    found = True
                    part_one += count
                    break

                array = [char for char in state]

                for i in b:
                    if array[i] == "#":
                        array[i] = "."
                    else:
                        array[i] = "#"

                string = "".join(array)
                if string in seen:
                    continue

                seen.add(string)
                start.append((string, count + 1))

            count += 1

        # Obviously not my solution, but it was fun learning about math.
        A = [[0 for _ in range(len(buttons))] for j in range(len(joltage))]

        for j, b in enumerate(buttons):
            for light in b:
                A[light][j] = 1

        c = [1 for _ in range(len(buttons))]

        res = scipy.optimize.linprog(c, A_eq=A, b_eq=joltage, integrality=1)

        part_two += sum(res.x)

    print(f"part one answer is {part_one}")
    print(f"part two answer is {part_two}")
