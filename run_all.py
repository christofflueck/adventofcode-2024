import importlib
import itertools
import time

from aocd import get_data, submit

days_solved = 14

from multiprocessing import Pool


def solve_day_part(day_and_part):
    day, part = day_and_part
    title = f'day {day} - part {part}'

    if day == 12:
        return title, 0

    if day == 25 and part != 'a':
        return title, None

    data = get_data(day=day)

    d = importlib.import_module(f'day{str(day).zfill(2)}')

    if part == 'a':
        fn = d.part_a
    else:
        fn = d.part_b

    start = time.perf_counter_ns()
    answer_a = fn(data)
    end = time.perf_counter_ns()
    timing = end - start
    submit(answer_a, day=day, part=part, quiet=True, reopen=False)

    return title, timing


def main():
    days_and_parts = itertools.product(range(1, days_solved + 1), ['a', 'b'])

    with Pool(processes=32) as pool:
        start = time.perf_counter_ns()
        results = pool.map(solve_day_part, days_and_parts)
        end = time.perf_counter_ns()

    for idx, (title, duration) in enumerate(results):
        if duration is not None:
            duration /= 1E6
        print(f'{title}: {duration} ms')

    print(f'solved all {days_solved} days in {(end - start) / 1E6} ms, sum of parts {sum(timing for _, timing in results)/1E6} ms')


if __name__ == '__main__':
    main()