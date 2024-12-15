from run_util import run_puzzle


def parse_data(data: str):
    boxes_str, moves_str = data.split("\n\n")
    moves = moves_str.replace("\n", "")
    border = set()

    robot = None
    boxes = set()

    for y, row in enumerate(boxes_str.splitlines()):
        for x, char in enumerate(row):
            if char == "O":
                boxes.add((x, y))
            elif char == "@":
                robot = (x, y)
            elif char == "#":
                border.add((x, y))

    return robot, boxes, moves, border


def part_a(data: str) -> int:
    robot, boxes, moves, border = parse_data(data)

    for move in moves:
        x, y = robot
        dx, dy = 0, 0
        if move == "<":
            dx -= 1
        elif move == ">":
            dx += 1
        elif move == "^":
            dy -= 1
        elif move == "v":
            dy += 1

        if (x + dx, y + dy) in border:
            continue

        if (x + dx, y + dy) not in boxes:
            robot = (x + dx, y + dy)
            continue

        next_robot = (x + dx, y + dy)

        while True:
            x += dx
            y += dy

            if (x, y) in border:
                break

            if (x, y) not in boxes:
                robot = next_robot
                boxes.remove(robot)
                boxes.add((x, y))
                break
    return sum(x + (y * 100) for x, y in boxes)


def parse_data_b(data: str):
    boxes_str, moves_str = data.split("\n\n")
    moves = moves_str.replace("\n", "")
    border = set()

    robot = None
    boxes = set()

    for y, row in enumerate(boxes_str.splitlines()):
        for x, char in enumerate(row):
            if char == "O":
                boxes.add((x * 2, y))
            elif char == "@":
                robot = (x * 2, y)
            elif char == "#":
                border.add((x * 2, y))
                border.add((x * 2 + 1, y))

    return robot, boxes, moves, border


def can_i_move_box(
    boxes: set, border: set, x: int, y: int, dx: int, dy: int, needs_to_move: set
) -> bool:
    my_pos = (x, y)
    my_left_pos = (x - 1, y)
    if my_pos not in boxes and my_left_pos not in boxes:
        return True

    if my_pos in needs_to_move:
        return True

    box_hitbox = [(x + dx, y + dy)] if dx != -1 else []
    if my_pos in boxes:
        if dx != 1:
            box_hitbox.append((x + dx + 1, y + dy))
        needs_to_move.add(my_pos)
    else:
        if dx != 1:
            box_hitbox.append((x + dx - 1, y + dy))
        needs_to_move.add(my_left_pos)

    for box in box_hitbox:
        if box in border:
            return False

        if not can_i_move_box(boxes, border, box[0], box[1], dx, dy, needs_to_move):
            return False

    return True


def part_b(data: str) -> int:
    robot, boxes, moves, border = parse_data_b(data)

    for move in moves:
        x, y = robot
        dx, dy = 0, 0
        if move == "<":
            dx -= 1
        elif move == ">":
            dx += 1
        elif move == "^":
            dy -= 1
        elif move == "v":
            dy += 1

        if (x + dx, y + dy) in border:
            continue

        if (x + dx, y + dy) not in boxes and (x + dx - 1, y + dy) not in boxes:
            robot = (x + dx, y + dy)
            continue

        needs_to_move = set()
        if can_i_move_box(boxes, border, x + dx, y + dy, dx, dy, needs_to_move):
            for box in needs_to_move:
                boxes.remove(box)
            for box in needs_to_move:
                boxes.add((box[0] + dx, box[1] + dy))
            robot = (x + dx, y + dy)

    return sum(x + (y * 100) for x, y in boxes)


# My lord and saviour
def print_layout(robot, boxes, border):
    max_x = max(x for x, _ in border)
    max_y = max(y for _, y in border)
    print(" " + "".join(map(str, range(10))))
    for y in range(max_y + 1):
        row = ""
        for x in range(max_x + 1):
            if (x, y) in border:
                row += "#"
            elif (x, y) == robot:
                row += "@"
            elif (x, y) in boxes:
                row += "["
            elif (x - 1, y) in boxes:
                row += "]"
            else:
                row += "."
        print(str(y % 10) + row)
    print("---")


def main():
    examples = [
        (
            """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<""",
            2028,
            None,
        ),
        (
            """#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^""",
            None,
            618,
        ),
        (
            """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^""",
            10092,
            9021,
        ),
    ]
    day = int(__file__.split("/")[-1].split(".")[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == "__main__":
    main()
