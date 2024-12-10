from typing import Optional

from run_util import run_puzzle

# Please dont judge me based of this solution. I know its bad


class Block:
    def __init__(self, id: int, length: int, value: Optional[int]):
        self.id = id
        self.length = length
        self.value = value

    def __str__(self):
        return f"{'.' if self.value is None else str(self.value)}" * self.length


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


def parse_data_b(data: str):
    blocks = []
    for i, char in enumerate(data):
        blocks.append(Block(i, int(char), i // 2 if i % 2 == 0 else None))
    return blocks


def part_b(data: str) -> int:
    blocks = parse_data_b(data)

    i = len(blocks) - 1
    changed = False
    while True:
        if i < 0:
            if changed:
                i = len(blocks) - 1
                changed = False
            else:
                break

        block = blocks[i]
        if block.value is None:
            i -= 1
            continue

        for j in range(i):
            if blocks[j].value is None:
                if blocks[j].length == block.length:
                    blocks[j].value = block.value
                    block.value = None
                    changed = True
                    break
                elif blocks[j].length > block.length:
                    blocks[j].length -= block.length
                    blocks.insert(i + 1, Block(-1, block.length, None))
                    blocks.insert(j, blocks.pop(i))
                    changed = True
                    i += 1
                    break
        i -= 1

    result = 0
    i = 0
    for block in blocks:
        for _ in range(block.length):
            if block.value is not None:
                result += i * block.value
            i += 1
    return result


def main():
    examples = [("""2333133121414131402""", 1928, 2858)]
    day = int(__file__.split("/")[-1].split(".")[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == "__main__":
    main()
