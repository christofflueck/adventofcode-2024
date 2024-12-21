import functools

from run_util import run_puzzle


def parse_data(data: str):
    return data.splitlines()


NUM_POS = {
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "0": (1, 3),
    "A": (2, 3),
}

DIR_POS = {"^": (1, 0), "A": (2, 0), "<": (0, 1), "v": (1, 1), ">": (2, 1)}


def part_a(data: str) -> int:
    data = parse_data(data)
    outputs = 0

    for code in data:
        possible_dir_2_inputs = 0
        prev = "A"
        for x in code:
            possible_dir_2_inputs += upcycle_char(x, prev, 2, "num")
            prev = x
        outputs += possible_dir_2_inputs * int(code[:3])
    return outputs


@functools.cache
def upcycle_char(c, pos, level, type="dir"):
    lookup = DIR_POS if type == "dir" else NUM_POS
    inputs = click_one(lookup[pos], lookup[c], (0, 0) if type == "dir" else (0, 3))
    if level <= 0:
        return len(inputs)
    total = 0
    prev = "A"
    for c in inputs:
        total += upcycle_char(c, prev, level - 1)
        prev = c

    return total


@functools.cache
def click_one(curr_pos, target_pos, disallowed):
    tx, ty = target_pos

    history = ""
    while curr_pos != target_pos:
        x, y = curr_pos

        diff_x = abs(tx - x)
        diff_y = abs(ty - y)
        if x > tx and (x - diff_x, y) != disallowed:
            curr_pos = (x - diff_x, y)
            history += "<" * diff_x
        elif y > ty and (x, y - diff_y) != disallowed:
            curr_pos = (x, y - diff_y)
            history += "^" * diff_y
        elif y < ty and (x, y + diff_y) != disallowed:
            curr_pos = (x, y + diff_y)
            history += "v" * diff_y
        elif x < tx and (x + diff_x, y) != disallowed:
            curr_pos = (x + diff_x, y)
            history += ">" * diff_x
    return history + "A"


def part_b(data: str) -> int:
    data = parse_data(data)
    outputs = 0

    for code in data:
        possible_dir_2_inputs = 0
        prev = "A"
        for x in code:
            possible_dir_2_inputs += upcycle_char(x, prev, 25, "num")
            prev = x
        outputs += possible_dir_2_inputs * int(code[:3])
    return outputs


def main():
    examples = [
        (
            """029A
980A
179A
456A
379A
""",
            126384,
            None,
        )
    ]
    day = int(__file__.split("/")[-1].split(".")[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == "__main__":
    main()
