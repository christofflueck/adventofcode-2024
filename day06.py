from run_util import run_puzzle


def parse_data(data: str):
    obstacles = set()
    player = None
    max_x = None
    max_y = None
    for y, row in enumerate(data.splitlines()):
        for x, char in enumerate(row):
            if char == '#':
                obstacles.add((x, y))
            elif char == '^':
                player = (x, y)
            max_x = x
        max_y = y

    return obstacles, player, max_x, max_y


DIRECTIONS = [
    (0, -1), (1, 0), (0, 1), (-1, 0)
]


def part_a(data: str) -> int:
    obstacles, player, max_x, max_y = parse_data(data)
    visited = set()
    facing = 0
    x, y = player
    while 0 <= x < max_x and 0 <= y < max_y:
        next_x = x + DIRECTIONS[facing][0]
        next_y = y + DIRECTIONS[facing][1]

        if (next_x, next_y) in obstacles:
            facing = (facing + 1) % len(DIRECTIONS)
            continue

        x, y = next_x, next_y
        visited.add((x, y))

    return len(visited)


def part_b(data: str) -> int:
    obstacles, player, max_x, max_y = parse_data(data)
    loops = 0
    for test_x in range(max_x + 1):
        for test_y in range(max_y + 1):
            if (test_x, test_y) in obstacles:
                continue
            x, y = player
            visited = set()
            facing = 0
            loop = False

            while 0 <= x < max_x and 0 <= y < max_y:
                next_x = x + DIRECTIONS[facing][0]
                next_y = y + DIRECTIONS[facing][1]

                if (next_x, next_y) in obstacles or next_x == test_x and next_y == test_y:
                    facing = (facing + 1) % len(DIRECTIONS)
                    continue
                x, y = next_x, next_y
                if (x, y, facing) in visited:
                    loop = True
                    break
                visited.add((x, y, facing))

            if loop:
                loops = loops + 1
    return loops


def main():
    examples = [
        ("""....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""", 41, 6)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
