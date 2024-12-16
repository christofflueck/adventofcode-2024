import heapq
from run_util import run_puzzle


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def parse_data(data: str):
    grid = [list(row) for row in data.splitlines()]

    start = None
    end = None

    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == "S":
                start = (y, x)
            elif char == "E":
                end = (y, x)

    return grid, start, end


def part_a(data: str) -> int:
    grid, start, end = parse_data(data)

    costs = [
        [[float("inf") for _ in range(len(DIRECTIONS))] for _ in range(len(grid[0]))]
        for _ in range(len(grid))
    ]

    heap = []
    heapq.heappush(heap, (0, start[0], start[1], 1))

    while heap:
        curr_cost, y, x, dir = heapq.heappop(heap)
        if (y, x) == end:
            return curr_cost

        if curr_cost > costs[y][x][dir]:
            continue

        costs[y][x][dir] = curr_cost

        dy, dx = DIRECTIONS[dir]
        if (
            grid[y + dy][x + dx] in [".", "E"]
            and costs[y + dy][x + dx][dir] > curr_cost + 1
        ):
            heapq.heappush(heap, (curr_cost + 1, y + dy, x + dx, dir))

        if costs[y][x][(dir + 1) % 4] > curr_cost + 1000:
            heapq.heappush(heap, (curr_cost + 1000, y, x, (dir + 1) % 4))

        if costs[y][x][(dir - 1) % 4] > curr_cost + 1000:
            heapq.heappush(heap, (curr_cost + 1000, y, x, (dir - 1) % 4))

    return 0


def part_b(data: str) -> int:
    grid, start, end = parse_data(data)

    costs = [
        [[float("inf") for _ in range(len(DIRECTIONS))] for _ in range(len(grid[0]))]
        for _ in range(len(grid))
    ]

    history = [
        [[set() for _ in range(len(DIRECTIONS))] for _ in range(len(grid[0]))]
        for _ in range(len(grid))
    ]

    heap = []
    heapq.heappush(heap, (0, start[0], start[1], 1, set()))

    while heap:
        curr_cost, y, x, dir, curr_history = heapq.heappop(heap)
        if (y, x) == end:
            if curr_cost > costs[y][x][dir]:
                continue
            if curr_cost < costs[y][x][dir]:
                costs[y][x][dir] = curr_cost
                history[y][x][dir] = curr_history
            else:
                total_history = history[y][x][dir]
                total_history.update(curr_history)
                total_history.add((y, x))

            continue

        if curr_cost > costs[y][x][dir]:
            continue
        lowest_cost_dir = min(costs[end[0]][end[1]])
        if curr_cost > lowest_cost_dir:
            continue
        costs[y][x][dir] = curr_cost

        total_history = history[y][x][dir]
        total_history.update(curr_history)

        next_history = total_history.copy()
        next_history.add((y, x))

        dy, dx = DIRECTIONS[dir]
        if (
            grid[y + dy][x + dx] in [".", "E"]
            and costs[y + dy][x + dx][dir] > curr_cost + 1
        ):
            heapq.heappush(heap, (curr_cost + 1, y + dy, x + dx, dir, next_history))

        if costs[y][x][(dir + 1) % 4] > curr_cost + 1000:
            heapq.heappush(heap, (curr_cost + 1000, y, x, (dir + 1) % 4, next_history))

        if costs[y][x][(dir - 1) % 4] > curr_cost + 1000:
            heapq.heappush(heap, (curr_cost + 1000, y, x, (dir - 1) % 4, next_history))

    lowest_cost_dir = min(
        range(len(costs[end[0]][end[1]])), key=costs[end[0]][end[1]].__getitem__
    )
    return len(history[end[0]][end[1]][lowest_cost_dir])


def main():
    examples = [
        (
            """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############""",
            7036,
            45,
        ),
        (
            """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################""",
            11048,
            64,
        ),
    ]
    day = int(__file__.split("/")[-1].split(".")[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == "__main__":
    main()
