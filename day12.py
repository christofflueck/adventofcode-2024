from collections import Counter, defaultdict

from run_util import run_puzzle

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1), ]
TRAVEL_DIRECTION = [(0, 1), (1, 0), (0, 1), (1, 0)]


def parse_data(data: str):
    coords = dict()
    lookup = defaultdict(list)
    for y, row in enumerate(data.splitlines()):
        for x, plant in enumerate(row):
            coords[(x, y)] = plant
            lookup[plant].append((x, y))

    regions = []
    in_region = set()
    for coord in coords.keys():
        if coord in in_region:
            continue
        x, y = coord
        plant = coords[coord]
        neighbors = {(x + dx, y + dy) for dx, dy in DIRECTIONS}
        region = [coord]
        while neighbors:
            neighbor = neighbors.pop()
            if neighbor not in coords or neighbor in in_region or coords[neighbor] != plant or neighbor in region:
                continue
            region.append(neighbor)
            in_region.add(neighbor)
            x, y = neighbor
            neighbors |= {(x + dx, y + dy) for dx, dy in DIRECTIONS}
        regions.append(region)

    return regions


def part_a(data: str) -> int:
    regions = parse_data(data)
    total = 0
    for region in regions:
        perimeter = 0

        for plant in region:
            for dx, dy in DIRECTIONS:
                adjacent = (plant[0] + dx, plant[1] + dy)
                if adjacent not in region:
                    perimeter += 1
        total += perimeter * len(region)

    return total


def part_b(data: str) -> int:
    regions = parse_data(data)
    total = 0

    for region in regions:
        visited = set()
        sides = []

        for plant in region:
            for i, direction in enumerate(DIRECTIONS):
                if (plant, direction) in visited:
                    continue
                tx, ty = TRAVEL_DIRECTION[i]
                dx, dy = direction
                curr = plant
                adjacent = (plant[0] + dx, plant[1] + dy)
                side = set()
                while adjacent not in region and curr in region:
                    if (curr, direction) in visited:
                        side.clear()
                        break
                    side.add(curr)
                    visited.add((curr, direction))

                    curr = (curr[0] + tx, curr[1] + ty)
                    adjacent = (curr[0] + dx, curr[1] + dy)
                if len(side) > 0:
                    sides.append(side)
        total += len(sides) * len(region)

    return total


def main():
    examples = [
        ("""AAAA
BBCD
BBCC
EEEC""", 140, 80),

        ("""RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE""", 1930, 1206)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
