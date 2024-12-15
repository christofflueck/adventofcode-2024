import math
from run_util import run_puzzle

import re


def parse_data(data: str):
    return [list(map(int, re.findall(r"-?\d+", row))) for row in data.splitlines()]


def part_a(data: str) -> int:
    data = parse_data(data)
    max_x, max_y = (101, 103) if len(data) > 12 else (11, 7)

    quadrants = [0, 0, 0, 0]

    for x, y, vx, vy in data:
        x = (x + vx * 100) % max_x
        y = (y + vy * 100) % max_y
        if x < max_x // 2 and y < max_y // 2:
            quadrants[0] += 1
        elif x > max_x // 2 and y < max_y // 2:
            quadrants[1] += 1
        elif x < max_x // 2 and y > max_y // 2:
            quadrants[2] += 1
        elif x > max_x // 2 and y > max_y // 2:
            quadrants[3] += 1

    return math.prod(quadrants)


def part_b(data: str) -> int:
    data = parse_data(data)

    max_x, max_y = (101, 103) if len(data) > 12 else (11, 7)
    iterations = 0
    while True:
        iterations += 1
        for tree in data:
            tree[0] = (tree[0] + tree[2]) % max_x
            tree[1] = (tree[1] + tree[3]) % max_y

        clustered = False   
        for x in range(max_x):
            if sum(1 if tx == x else 0 for tx, ty, _, _ in data) > 20:
                clustered = True
                break
        if not clustered:
            continue
                
        for y in range(103):
            row = ""
            for x in range(101):
                row = row + (
                    "*" if any(tx == x and ty == y for tx, ty, _, _ in data) else " "
                )
            if '*******************************' in row:
                return iterations


def main():
    examples = [
        (
            """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3""",
            12,
            None,
        )
    ]
    day = int(__file__.split("/")[-1].split(".")[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == "__main__":
    main()
