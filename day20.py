from collections import defaultdict, deque
from run_util import run_puzzle



DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def parse_data(data: str):
    paths = []
    start = None
    end = None

    for y, row in enumerate(data.splitlines()):
        for x, char in enumerate(row):
            if char != '#':
                paths.append((x, y))
            if char == 'S':
                start = (x, y)
            elif char == 'E':
                end = (x, y)

    path = [start]

    while path[-1] != end:
        for dx, dy in DIRECTIONS:
            next_pos = (path[-1][0] + dx, path[-1][1] + dy)
            if next_pos in paths and next_pos not in path:
                path.append(next_pos)
                break


    return path

def part_a(data: str) -> int:
    path = parse_data(data)
    lookup = set(path)
    index = {pos: i for i, pos in enumerate(path)}

    possible_cheats = defaultdict(int)

    for cheat_start in path:
        for dx, dy in DIRECTIONS:
            skipped = (cheat_start[0] + dx, cheat_start[1] + dy)
            target = (cheat_start[0] + 2 * dx, cheat_start[1] + 2 * dy)
            if skipped in lookup or target not in lookup:
                continue
            if index[target] < index[cheat_start]:
                continue
            else:
                possible_cheats[index[target] - index[cheat_start] - 2] += 1


    return sum(possible_cheats[saved] if saved >= 100 else 0 for saved in possible_cheats)

CHEATING_MOVES = set()

for y in range(-20, 21):
    width = 20 - abs(y)
    for x in range(-width, width + 1):
        if abs(x) + abs(y) < 2:
            continue
        CHEATING_MOVES.add((x, y))

def part_b(data: str) -> int:
    path = parse_data(data)
    lookup = set(path)
    index = {pos: i for i, pos in enumerate(path)}

    possible_cheats = defaultdict(int)


    for cheat_start in path:
        for dx, dy in CHEATING_MOVES:
            target = (cheat_start[0] + dx, cheat_start[1] + dy)
            if target not in lookup or index[target] < index[cheat_start]:
                continue
            
            possible_cheats[index[target] - index[cheat_start] - abs(dx) - abs(dy)] += 1

    return sum(possible_cheats[saved] if saved >= 100 else 0 for saved in possible_cheats)


def main():
    examples = [
        ("""###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############""", 0, 0)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
