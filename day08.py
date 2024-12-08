from typing import Tuple
from run_util import run_puzzle


def parse_data(data: str) -> Tuple[dict[Tuple[int, int], str], int, int]:
    antennas = {}
    max_x = 0
    max_y = 0
    for y, row in enumerate(data.splitlines()):
        max_y = max(max_y, y)
        for x, char in enumerate(row):
            max_x = max(max_x, x)
            if char != ".":
                antennas[(x, y)] = char

    return antennas, max_x, max_y


def part_a(data: str) -> int:
    antennas, max_x, max_y = parse_data(data)

    antinodes = set()

    for antenna in antennas:
        for other in antennas:
            if antenna == other or antennas[antenna] != antennas[other]:
                continue
            antinode_x = other[0] + (other[0] - antenna[0])
            antinode_y = other[1] + (other[1] - antenna[1])
            
            if 0 <= antinode_x <= max_x and 0 <= antinode_y <= max_y not in antinodes:
                antinodes.add((antinode_x, antinode_y))

    return len(antinodes)


def part_b(data: str) -> int:
    antennas, max_x, max_y = parse_data(data)

    antinodes = set()

    for antenna in antennas:
        for other in antennas:
            if antenna == other or antennas[antenna] != antennas[other]:
                continue
            diff_x = other[0] - antenna[0]
            diff_y = other[1] - antenna[1]
            
            antinode_x = other[0]
            antinode_y = other[1]
            
            while 0 <= antinode_x <= max_x and 0 <= antinode_y <= max_y not in antinodes:
                antinodes.add((antinode_x, antinode_y))
                antinode_x += diff_x
                antinode_y += diff_y

    return len(antinodes)


def main():
    examples = [
        (
            """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............""",
            14,
            34,
        )
    ]
    day = int(__file__.split("/")[-1].split(".")[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == "__main__":
    main()
