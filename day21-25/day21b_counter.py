from functools import cache
import numpy as np


def get_end_positions(data):
    start = [(index, row.index('S')) for index, row in enumerate(data) if 'S' in row]
    data[start[0][0]][start[0][1]] = '.'
    data = tuple([tuple(row) for row in data])
    new_starts = start
    outputs = []
    for i in range(500):
        new_starting = []
        for coord in new_starts:
            new_starting.extend(get_next(data, coord))
        new_starts = set(new_starting)
        if (i+1) % 131 == 65:
            if len(outputs) == 3:
                break
            else:
                outputs.append(len(new_starts))

    inputs = [[0, 0, 1], [1, 1, 1], [4, 2, 1]]
    a, b, c = np.linalg.solve(inputs, outputs)

    x = (26501365 - (len(data)//2)) / len(data)
    result = a * (x ** 2) + b * x + c
    return int(result)


@cache
def get_next(data, start_pos):
    next_pos = []
    x, y = start_pos
    steps = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    for step in steps:
        step_x, step_y = step
        if data[step_x % len(data)][step_y % len(data[0])] == '.':
            next_pos.append(step)
    return next_pos


def main():
    with open('day21_input.txt') as file:
        data = []
        for line in file:
            data.append([char for char in line.strip()])

    print(get_end_positions(data))


if __name__ == '__main__':
    main()
