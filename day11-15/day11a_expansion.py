import numpy as np
from scipy.spatial.distance import cityblock
from itertools import combinations


def main():
    with open('day11_input.txt') as file:
        lines = file.readlines()
    data = []
    for line in lines:
        data.append([char for char in line.strip()])
    data = np.array(data)

    empty_rows = np.all(np.isin(data, '.'), axis=1)
    empty_rows = [i for i, x in enumerate(empty_rows) if x]
    data = np.insert(data, empty_rows, '.', axis=0)
    empty_columns = np.all(np.isin(data, '.'), axis=0)
    empty_columns = [i for i, x in enumerate(empty_columns) if x]
    data = np.insert(data, empty_columns, '.', axis=1)

    locations = np.argwhere(data == '#')
    total = 0
    for combination in combinations(locations, 2):
        total += cityblock(combination[0], combination[1])
    print(total)


if __name__ == '__main__':
    main()
