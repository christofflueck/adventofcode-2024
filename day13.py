import re

from run_util import run_puzzle


def parse_data(data: str):
    return [list(map(int, re.findall(r"(\d+)", machine))) for machine in data.split('\n\n')]


def calculate_cost(a_x, a_y, b_x, b_y, prize_x, prize_y):
    a = (b_x * prize_y - b_y * prize_x) / (a_y * b_x - a_x * b_y)
    b = (prize_x - a * a_x) / b_x
    if a.is_integer() and b.is_integer():
        return 3 * a + b
    return 0


def part_a(data: str) -> int:
    machines = parse_data(data)

    return sum([calculate_cost(*machine) for machine in machines])


def part_b(data: str) -> int:
    machines = parse_data(data)

    return sum([calculate_cost(a_x, a_y, b_x, b_y, prize_x + 10000000000000, prize_y + 10000000000000) for a_x, a_y, b_x, b_y, prize_x, prize_y in machines])


def main():
    examples = [
        ("""Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279""", 480, None)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
