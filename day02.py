from run_util import run_puzzle


def parse_data(data: str):
    return [[int(x) for x in row.split()] for row in data.split('\n')]


def part_a(data: str) -> int:
    data = parse_data(data)
    safe = 0

    for row in data:
        increasing = True
        is_unsafe = False
        prev = None
        for num in row:
            if prev is None:
                if row[0] > row[1]:
                    increasing = False
                if row[0] == row[1]:
                    is_unsafe = True
                    break
                prev = num
                continue

            if prev == num or (prev > num and increasing) or (prev < num and not increasing) or 1 < abs(prev - num) > 3:
                is_unsafe = True
                break
            prev = num

        if not is_unsafe:
            safe = safe + 1

    return safe


def part_b(data: str) -> int:
    data = parse_data(data)
    return 0


def main():
    examples = [
        ("""7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""", 2, 4)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
