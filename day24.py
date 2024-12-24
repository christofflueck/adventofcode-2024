from collections import deque

from run_util import run_puzzle


def parse_data(data: str):
    initials, rules_rows = data.split("\n\n")

    values = dict()

    for row in initials.splitlines():
        key, value = row.split(": ")
        values[key] = int(value)

    rules = deque([])
    for row in rules_rows.splitlines():
        left, op, right, _, target = row.split()
        rules.append((left, right, op, target))

    return values, rules


def part_a(data: str) -> int:
    values, rules = parse_data(data)

    return run_rules(values, rules)


def run_rules(values, rules):
    iterations = 0
    while rules:
        rule = rules.popleft()
        left, right, op, target = rule
        if left not in values or right not in values:
            rules.append(rule)
            iterations += 1
            if iterations == len(rules):
                return 0
            continue
        match op:
            case "AND":
                values[target] = values[left] & values[right]
            case "OR":
                values[target] = values[left] | values[right]
            case "XOR":
                values[target] = values[left] ^ values[right]
        iterations = 0
    return get_value(values, "z")


def get_value(values, prefix):
    z = sorted([key for key in values if key.startswith(prefix)], reverse=True)

    result = 0
    for key in z:
        result = result << 1
        result += values[key]
    return result


def part_b(data: str) -> int:
    _, rules = parse_data(data)

    wrong = set()
    for left, right, op, target in rules:
        # Every Z is set using an XOR gate except the last one
        if target[0] == "z" and op != "XOR" and target != "z45":
            wrong.add(target)
        # XOR is only used when reading from x or y or setting z
        if (
            op == "XOR"
            and target[0] not in ["z"]
            and left[0] not in ["x", "y"]
            and right[0] not in ["x", "y"]
        ):
            wrong.add(target)
        # After every AND should follow an OR gate
        if op == "AND" and left != "x00" and right != "x00":
            for next_left, next_right, next_op, _ in rules:
                if (target == next_left or target == next_right) and next_op != "OR":
                    wrong.add(target)
        # After every XOR should follow an OR gate
        if op == "XOR":
            for next_left, next_right, next_op, _ in rules:
                if (target == next_left or target == next_right) and next_op == "OR":
                    wrong.add(target)

    return ",".join(sorted(wrong))


def swap_rules(rules, pair):
    rule_1 = rules[pair[0]]
    rule_2 = rules[pair[1]]
    rules[pair[0]] = (rule_1[0], rule_1[1], rule_1[2], rule_2[3])
    rules[pair[1]] = (rule_2[0], rule_2[1], rule_2[2], rule_1[3])


def main():
    examples = [
        (
            """x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02""",
            4,
            None,
        ),
        (
            """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj""",
            2024,
            None,
        ),
    ]
    day = int(__file__.split("/")[-1].split(".")[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == "__main__":
    main()
