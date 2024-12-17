import math

from tqdm import tqdm
from run_util import run_puzzle


def parse_data(data: str):
    data = data.splitlines()
    ra = int(data[0].split(": ")[1])
    rb = int(data[1].split(": ")[1])
    rc = int(data[2].split(": ")[1])

    program = list(map(int, data[4].split(": ")[1].split(",")))

    return program, ra, rb, rc


def compute(program, ra, rb, rc):
    instruction = 0
    output = []

    while instruction < len(program):
        opcode = program[instruction]
        operand = program[instruction + 1]
        combo = operand
        match operand:
            case 4:
                combo = ra
            case 5:
                combo = rb
            case 6:
                combo = rc

        match opcode:
            case 0:
                ra = int(ra // (2**combo))
            case 1:
                rb = int(rb ^ operand)
            case 2:
                rb = combo % 8
            case 3:
                if ra != 0:
                    instruction = operand
                    continue
            case 4:
                rb = int(rb ^ rc)
            case 5:
                output.append(combo % 8)
            case 6:
                rb = int(ra // (2**combo))
            case 7:
                rc = int(ra // (2**combo))

        instruction += 2
    return output


def part_a(data: str) -> int:
    program, ra, rb, rc = parse_data(data)

    return ",".join(map(str, map(int, compute(program, ra, rb, rc))))


def part_b(data: str) -> int:
    program, _, _, _ = parse_data(data)
    
    possible_ra = {0}

    for p in range(1, len(program) + 1):
        next_ras = set()
        for ra in possible_ra:
            for i in range(8):
                next_ra = (ra << 3) + i
                output = compute(program, next_ra, 0, 0)
                if output == program[len(program) - p :]:
                    next_ras.add(next_ra)
        possible_ra = next_ras
    return min(possible_ra)


def main():
    examples = [
        (
            """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0""",
            "4,6,3,5,6,3,5,2,1,0",
            None,
        ),
        (
            """Register A: 10
Register B: 0
Register C: 0

Program: 5,0,5,1,5,4""",
            "0,1,2",
            None,
        ),
        (
            """Register A: 2024
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0""",
            "4,2,5,6,7,7,7,7,3,1,0",
            None,
        ),
    ]
    day = int(__file__.split("/")[-1].split(".")[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == "__main__":
    main()
