import numpy as np


def calculate_load(array):
    load = 0
    for i in range(len(array[0])):
        load += calculate_load_column(array[:, i])
    return load


def calculate_load_column(column):
    round_stones = 0
    i = 0
    start_load = len(column)
    load = 0
    while i < len(column):
        if column[i] == 'O':
            round_stones += 1
        elif column[i] == '#':
            load += round_stones*start_load - (((round_stones-1)*round_stones)/2)
            round_stones = 0
            start_load = len(column) - (i + 1)
        i += 1
    load += round_stones * start_load - (((round_stones - 1) * round_stones) / 2)
    return load


def main():
    with open('day14_input.txt') as file:
        lines = file.readlines()

    data = []
    for line in lines:
        data.append([char for char in line.strip()])

    data = np.array(data)
    print(calculate_load(data))


if __name__ == '__main__':
    main()
