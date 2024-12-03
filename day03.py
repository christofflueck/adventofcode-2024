from run_util import run_puzzle
import re


def parse_data_a(data: str):
    regex = r"(mul\(\d+,\d+\))"
    matches = re.findall(regex, data)
    return [[int(x) for x in match[4:-1].split(",")] for match in matches]


def part_a(data: str) -> int:
    data = parse_data_a(data)

    return sum([x * y for x, y in data])


def parse_data_b(data: str):
    regex = r"(mul\(\d+,\d+\))|(do\(\))|(don't\(\))"
    matches = re.findall(regex, data)
    muls = []
    disabled = False

    for mul, do, dont in matches:
        if do:
            disabled = False
            continue
        if dont:
            disabled = True
            continue
        if disabled:
            continue
        if mul:
            muls.append([int(x) for x in mul[4:-1].split(",")])

    return muls


def part_b(data: str) -> int:
    data = parse_data_b(data)

    return sum([x * y for x, y in data])


def main():
    examples = [
        (
            """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))""",
            161,
            48,
        )
    ]
    day = int(__file__.split("/")[-1].split(".")[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == "__main__":
    main()
