import numpy as np


def get_adjacent(matrix, start):
    start_row, start_column = start
    rows, columns = matrix.shape
    adjacent = [(start_row + x, start_column + y) for x in range(-1, 2) for y in range(-1, 2) if (start_row + x in range(rows) and start_column + y in range(columns) and abs(x) != abs(y))]
    return adjacent


def get_next_element(current, previous, matrix):
    if matrix[current[0][0]][current[0][1]] == '-':
        return get_next_horizontal(current, previous)
    elif matrix[current[0][0]][current[0][1]] == '|':
        return get_next_vertical(current, previous)
    elif matrix[current[0][0]][current[0][1]] == 'L':
        return get_next_l(current, previous)
    elif matrix[current[0][0]][current[0][1]] == 'F':
        return get_next_f(current, previous)
    elif matrix[current[0][0]][current[0][1]] == 'J':
        return get_next_j(current, previous)
    elif matrix[current[0][0]][current[0][1]] == '7':
        return get_next_7(current, previous)


def get_next_horizontal(current, previous):
    if current[0][1] > previous[0][1]:
        next_el = ((current[0][0], current[0][1] + 1), current[1] + 1)
    else:
        next_el = ((current[0][0], current[0][1] - 1), current[1] + 1)
    return next_el


def get_next_vertical(current, previous):
    if current[0][0] > previous[0][0]:
        next_el = ((current[0][0] + 1, current[0][1]), current[1] + 1)
    else:
        next_el = ((current[0][0] - 1, current[0][1]), current[1] + 1)
    return next_el


def get_next_l(current, previous):
    if current[0][0] > previous[0][0]:
        next_el = ((current[0][0], current[0][1] + 1), current[1] + 1)
    else:
        next_el = ((current[0][0] - 1, current[0][1]), current[1] + 1)
    return next_el


def get_next_f(current, previous):
    if current[0][1] < previous[0][1]:
        next_el = ((current[0][0] + 1, current[0][1]), current[1] + 1)
    else:
        next_el = ((current[0][0], current[0][1] + 1), current[1] + 1)
    return next_el


def get_next_j(current, previous):
    if current[0][0] > previous[0][0]:
        next_el = ((current[0][0], current[0][1] - 1), current[1] + 1)
    else:
        next_el = ((current[0][0] - 1, current[0][1]), current[1] + 1)
    return next_el


def get_next_7(current, previous):
    if current[0][1] > previous[0][1]:
        next_el = ((current[0][0] + 1, current[0][1]), current[1] + 1)
    else:
        next_el = ((current[0][0], current[0][1] - 1), current[1] + 1)
    return next_el


def get_starting_elements(start, matrix):
    adjacent = get_adjacent(matrix, start)
    up_start = ['|', 'F', '7']
    down_start = ['|', 'J', 'L']
    left_start = ['-', 'L', 'F']
    right_start = ['-', 'J', '7']
    starting = []
    for element in adjacent:
        x, y = element
        if x > start[0]:
            if matrix[x][y] in down_start:
                starting.append(((x, y), 1))
        elif x < start[0]:
            if matrix[x][y] in up_start:
                starting.append(((x, y), 1))
        else:
            if y > start[1]:
                if matrix[x][y] in right_start:
                    starting.append(((x, y), 1))
            else:
                if matrix[x][y] in left_start:
                    starting.append(((x, y), 1))
    return starting


def main():
    with open('day10_input.txt') as file:
        lines = file.readlines()
    data = []
    for line in lines:
        line = line.strip()
        data.append([char for char in line])
    data = np.array(data)
    start = np.where(data == 'S')
    start = np.asarray(start).T[0]
    previous1, previous2 = (tuple(start), 0), (tuple(start), 0)
    current1, current2 = get_starting_elements(start, data)
    while current1 != current2:
        current1, previous1 = get_next_element(current1, previous1, data), current1
        current2, previous2 = get_next_element(current2, previous2, data), current2
    print(current1)


if __name__ == '__main__':
    main()
