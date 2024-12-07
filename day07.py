from typing import List, Tuple
from run_util import run_puzzle


def parse_data(data: str) -> List[Tuple[int, List[int]]]:
    equations = []
    for row in data.splitlines():
        result, values = row.split(": ")
        equations.append((int(result), list(map(int, values.split()))))
    return equations


def part_a(data: str) -> int:
    equations = parse_data(data)
    total = 0
    for result, components in equations:
        prev = set([components[0]])
        next = set()
        for i in range(1, len(components)):
            for num in prev:
                next.add(num + components[i])
                next.add(num * components[i])
            prev = next
            next = set()
        if result in prev:
            total += result
        
    return total


def part_b(data: str) -> int:
    equations = parse_data(data)
    total = 0
    for result, components in equations:
        prev = set([components[0]])
        next = set()
        for i in range(1, len(components)):
            for num in prev:
                next.add(num + components[i])
                next.add(num * components[i])
                next.add(int(str(num) + str(components[i])))
            prev = next
            next = set()
        if result in prev:
            total += result
        
    return total


def main():
    examples = [
        (
            """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""",
            3749,
            11387,
        )
    ]
    day = int(__file__.split("/")[-1].split(".")[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == "__main__":
    main()
