import time

from aocd import get_data, submit


def _run_part(day, description, fn, data):
    start = time.perf_counter_ns()
    result = fn(data)
    end = time.perf_counter_ns()
    print(f"day {day} - {description} -> result [{result}], duration {(end - start) / 1E6} ms")
    return result


def run_puzzle(day, part_a, part_b, examples):
    day = int(day)
    data = get_data(day=day)

    start = time.perf_counter_ns()

    if part_a is not None:
        for example_data, example_solution_a, _ in examples:
            if example_solution_a is not None:
                example_answer_a = _run_part(day, 'example part_a', part_a, example_data)
                assert example_answer_a == example_solution_a, f"example_data did not match for part_a: {example_answer_a} != {example_solution_a}"

        answer_a = _run_part(day, 'puzzle part_a', part_a, data)
        submit(answer=answer_a, day=day, part="a")

    if part_b is not None:
        for example_data, _, example_solution_b in examples:
            if example_solution_b is not None:
                example_answer_b = _run_part(day, 'example part_b', part_b, example_data)
                assert example_answer_b == example_solution_b, f"example_data did not match for part_b: {example_answer_b} != {example_solution_b}"

        answer_b = _run_part(day, 'puzzle part_b', part_b, data)
        submit(answer=answer_b, day=day, part="b")

    end = time.perf_counter_ns()
    print(f'total duration: {(end - start) / 1E6} ms')