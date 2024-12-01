from collections import Counter
from run_util import run_puzzle


def parse_data(data: str):
    rows = [(int(row.split()[0]), int(row.split()[1])) for row in data.split('\n')]
    transposed_data = list(zip(*rows))
    
    return transposed_data[0], transposed_data[1]


def part_a(data: str) -> int:
    first_column_unsorted, second_column_unsorted = parse_data(data)
    
    first_column = sorted(first_column_unsorted)
    second_column = sorted(second_column_unsorted)
    
    sum = 0
    for i in range(len(first_column)):
        sum = sum + abs(first_column[i] - second_column[i])
        
    return sum


def part_b(data: str) -> int:
    first_column, second_column = parse_data(data)
    
    lookups = Counter(second_column)
    
    total = 0
    for num in first_column:
        total = total + num * lookups[num]
    
    return total


def main():
    examples = [
        ("""3   4
4   3
2   5
1   3
3   9
3   3""", 11, 31)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
