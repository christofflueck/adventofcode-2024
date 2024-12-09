from typing import List, Optional, Tuple
from run_util import run_puzzle


class Block:
    def __init__(self, id: int, length: int, value: Optional[int]):
        self.id = id
        self.length = length
        self.value = value


def parse_data(data: str):
    blocks = []
    empty = []
    for i, char in enumerate(data):
        if i % 2 == 0:
            blocks.append(Block(i, int(char), i // 2))
        else:
            empty.append(Block(i, int(char), None))
    return blocks, empty


def part_a(data: str) -> int:
    data, empties = parse_data(data)
    result = []
    for i in range(len(data)):
        block = data[i]
        for _ in range(block.length):
            result.append(block.value)
        block.length = 0
        if len(empties) <= i:
            break
        empty = empties[i]
        for block in reversed(data):
            if block.length > 0:
                if block.length <= empty.length:
                    empty.length -= block.length
                    for _ in range(block.length):
                        result.append(block.value)
                    block.length = 0
                else:
                    for _ in range(empty.length):
                        result.append(block.value)
                    block.length -= empty.length
                    empty.length = 0
            if empty.length == 0:
                break
            if empty.length < 0:
                print("Error: Negative empty length")

    return sum([i * val for i, val in enumerate(result)])


# 0099811188827773336446555566
# 009981118882777333644655556665


def parse_data_b(data: str):
    blocks = []
    for i, char in enumerate(data):
        blocks.append(Block(i, int(char), i // 2 if i % 2 == 0 else None))
    return blocks


def part_b(data: str) -> int:
    blocks = parse_data_b(data)

    for i in range(len(blocks) - 1, -1, -1):
        block = blocks[i]
        if block.value is None:
            continue
        # I  got a headache and a fever. continuing later
    return 0


def main():
    examples = [("""2333133121414131402""", 1928, 2858)]
    day = int(__file__.split("/")[-1].split(".")[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == "__main__":
    main()
