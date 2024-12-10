from run_util import run_puzzle


def parse_data(data: str):
    values = {}
    starting_positions = []
    for y, row in enumerate(data.splitlines()):
        for x, char in enumerate(row):
            int_val = int(char)
            values[(x, y)] = int_val
            if int_val == 0:
                starting_positions.append((x, y))

    return values, starting_positions


DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def part_a(data: str) -> int:
    values, starting_positions = parse_data(data)

    score = 0
    for x, y in starting_positions:
        neighbors = [(x + dx, y + dy, 1) for dx, dy in DIRECTIONS]
        nines = set()
        while neighbors:
            nx, ny, required_val = neighbors.pop(0)
            if values.get((nx, ny)) == required_val:
                if required_val == 9:
                    nines.add((nx, ny))
                else:
                    neighbors.extend(
                        [(nx + dx, ny + dy, required_val + 1) for dx, dy in DIRECTIONS]
                    )
        score += len(nines)

    return score


def part_b(data: str) -> int:
    values, starting_positions = parse_data(data)

    score = 0
    for x, y in starting_positions:
        neighbors = [(x + dx, y + dy, 1) for dx, dy in DIRECTIONS]
        while neighbors:
            nx, ny, required_val = neighbors.pop(0)
            if values.get((nx, ny)) == required_val:
                if required_val == 9:
                    score += 1
                else:
                    neighbors.extend(
                        [(nx + dx, ny + dy, required_val + 1) for dx, dy in DIRECTIONS]
                    )

    return score


def main():
    examples = [
        (
            """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""",
            36,
            81,
        )
    ]
    day = int(__file__.split("/")[-1].split(".")[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == "__main__":
    main()
