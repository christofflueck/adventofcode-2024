from collections import Counter
from typing import List, Tuple

from run_util import run_puzzle


def parse_data(data: str):
    return data.split('\n')


DIRECTIONS = [
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]

SEARCH = 'XMAS'


def check_for_xmas(data: List[str], x: int, y: int, direction: Tuple[int, int]):
    for match in SEARCH:
        if y < 0 or y >= len(data) or x < 0 or x >= len(data[0]):
            return False
        char = data[y][x]
        if char != match:
            return False
        x = x + direction[0]
        y = y + direction[1]
    return True


def part_a(data: str) -> int:
    data = parse_data(data)
    total = 0
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char == 'X':
                for direction in DIRECTIONS:
                    if check_for_xmas(data, x, y, direction):
                        total = total + 1

    return total


def check_for_mas(data: List[str], x: int, y: int):
    corners = data[y - 1][x - 1] + data[y - 1][x + 1] + data[y + 1][x + 1] + data[y + 1][x - 1]
    chars = Counter(corners)
    return chars.get('M') == 2 and chars.get('S') == 2 and corners[0] != corners[2] and corners[1] != corners[3]


def part_b(data: str) -> int:
    data = parse_data(data)
    total = 0
    for y, row in enumerate(data):
        if y < 1 or y >= len(data) - 1:
            continue
        for x, char in enumerate(row):
            if x < 1 or x >= len(row) - 1:
                continue
            if char == 'A':
                if check_for_mas(data, x, y):
                    total = total + 1

    return total


def main():
    examples = [
        ("""MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""", 18, 9)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
