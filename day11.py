from collections import Counter, defaultdict

from run_util import run_puzzle


def parse_data(data: str):
    numerics = map(int, data.split(" "))
    counts = Counter(numerics)
    values = defaultdict(int)
    values.update(counts)
    return values


def blinks(data, iterations):
    values = parse_data(data)
    curr = values
    for _ in range(iterations):
        next = defaultdict(int)
        for num, count in curr.items():
            str_num = str(num)
            if num == 0:
                next[1] += count
            elif len(str_num) % 2 == 0:
                next[int(str_num[:len(str_num) // 2])] += count
                next[int(str_num[len(str_num) // 2:])] += count
            else:
                next[num * 2024] += count
        curr = next
    return sum(curr.values())


def part_a(data: str) -> int:
    return blinks(data, 25)


def part_b(data: str) -> int:
    return blinks(data, 75)


def main():
    examples = [
        ("""125 17""", 55312, None)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
