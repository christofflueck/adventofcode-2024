from collections import defaultdict
from functools import cmp_to_key

from run_util import run_puzzle


def parse_data(data: str):
    rules, updates = data.split("\n\n")
    rules = [(int(row[0:2]), int(row[3:5])) for row in rules.split('\n')]
    rule_lookup = defaultdict(list)
    for before, after in rules:
        rule_lookup[before].append(after)
    updates = [[int(x) for x in row.split(',')] for row in updates.split('\n')]
    return updates, rule_lookup


def is_update_valid(update, rules):
    before = []
    for page in update:
        for prev in before:
            if prev in rules[page]:
                return False
        before.append(page)
    return True


def part_a(data: str) -> int:
    updates, rules = parse_data(data)

    total = 0
    for book in updates:
        if is_update_valid(book, rules):
            total = total + book[len(book) // 2]

    return total


def part_b(data: str) -> int:
    updates, rules = parse_data(data)

    def compare_page(a, b):
        if a in rules[b]:
            return 1
        if b in rules[a]:
            return -1
        return 0

    total = 0
    for update in updates:
        if not is_update_valid(update, rules):
            sorted_update = sorted(update, key=cmp_to_key(compare_page))
            total = total + sorted_update[len(sorted_update) // 2]

    return total


def main():
    examples = [
        ("""47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""", 143, 123)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
