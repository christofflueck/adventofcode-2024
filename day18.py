from collections import deque
from run_util import run_puzzle


def parse_data(data: str):
    grid = []
    for row in data.split("\n"):
        c = row.split(",")
        grid.append((int(c[0]), int(c[1])))
    return grid


DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def get_shortest_path(grid, fallen_bytes):
    grid_size = 6 if len(grid) < 30 else 70

    relevant_grid = set(grid[:fallen_bytes])
    start = (0, 0)
    end = (grid_size, grid_size)

    visited = set()
    stack = deque([(start, set())])

    while stack:
        pos, history = stack.popleft()
        x, y = pos
        if pos == end:
            return history
        if pos in visited:
            continue
        visited.add(pos)

        new_history = history.copy()
        new_history.add(pos)
        for dx, dy in DIRECTIONS:
            next_x = x + dx
            next_y = y + dy
            if next_x < 0 or next_x > grid_size or next_y < 0 or next_y > grid_size:
                continue
            next_pos = (x + dx, y + dy)
            if next_pos not in relevant_grid and next_pos not in visited:
                stack.append((next_pos, new_history))
    return None


def part_a(data: str) -> int:
    grid = parse_data(data)
    fallen_bytes = 12 if len(grid) < 30 else 1024
    return len(get_shortest_path(grid, fallen_bytes))


def part_b(data: str) -> str:
    grid = parse_data(data)
    fallen_bytes = 12 if len(grid) < 30 else 1024

    path = get_shortest_path(grid, fallen_bytes)

    while path is not None:
        fallen_bytes += 1
        while grid[fallen_bytes] not in path:
            fallen_bytes += 1

        path = get_shortest_path(grid, fallen_bytes + 1)

    return ",".join(map(str, grid[fallen_bytes]))


def main():
    examples = [
        (
            """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0""",
            22,
            "6,1",
        )
    ]
    day = int(__file__.split("/")[-1].split(".")[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == "__main__":
    main()
