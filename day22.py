from collections import defaultdict

from run_util import run_puzzle


def parse_data(data: str):
    return [int(x) for x in data.split("\n")]


def compute_next_number(secret: int) -> int:
    secret = (secret ^ (secret << 6)) % 16777216
    secret = (secret ^ (secret >> 5)) % 16777216
    return (secret ^ (secret << 11)) % 16777216


def part_a(data: str) -> int:
    secret_numbers = parse_data(data)

    new_secret_numbers = []
    for secret in secret_numbers:
        for _ in range(2000):
            secret = compute_next_number(secret)
        new_secret_numbers.append(secret)
    return sum(new_secret_numbers)


def part_b(data: str) -> int:
    secret_numbers = parse_data(data)

    sequence_sales = defaultdict(int)
    sequence_seller = defaultdict(int)

    for buyer, secret in enumerate(secret_numbers):
        secret = compute_next_number(secret)
        last_price = secret % 10

        window = [None] * 4

        for i in range(1, 2000):
            secret = compute_next_number(secret)
            price = secret % 10

            window[0] = window[1]
            window[1] = window[2]
            window[2] = window[3]
            window[3] = price - last_price

            fluct = tuple(window)
            if sequence_seller[fluct] != buyer:
                sequence_sales[fluct] += price
                sequence_seller[fluct] = buyer
            last_price = price

    return max(sequence_sales.values())


def main():
    examples = [
        (
            """1
10
100
2024""",
            37327623,
            None,
        ),
        (
            """1
2
3
2024""",
            None,
            None,
        ),
    ]
    day = int(__file__.split("/")[-1].split(".")[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == "__main__":
    main()
