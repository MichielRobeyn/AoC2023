import numpy as np
from scipy.spatial.distance import cityblock
from itertools import combinations
import bisect


def count_elements_between(sorted_list, low, high):
    left = bisect.bisect_left(sorted_list, low)
    right = bisect.bisect_right(sorted_list, high)
    return right - left


def get_distance(data, expansion_factor):
    empty_rows = np.all(np.isin(data, '.'), axis=1)
    empty_rows = [i for i, x in enumerate(empty_rows) if x]
    empty_columns = np.all(np.isin(data, '.'), axis=0)
    empty_columns = [i for i, x in enumerate(empty_columns) if x]
    locations = np.argwhere(data == '#')
    total = 0
    extra = 0
    for combination in combinations(locations, 2):
        total += cityblock(combination[0], combination[1])
        min_row = min(combination[0][0], combination[1][0])
        max_row = max(combination[0][0], combination[1][0])
        min_column = min(combination[0][1], combination[1][1])
        max_column = max(combination[0][1], combination[1][1])
        extra += count_elements_between(empty_rows, min_row, max_row) * (expansion_factor - 1)
        extra += count_elements_between(empty_columns, min_column, max_column) * (expansion_factor - 1)
    return total + extra


def main():
    with open('day11_input.txt') as file:
        lines = file.readlines()
    data = []
    for line in lines:
        data.append([char for char in line.strip()])
    data = np.array(data)

    print(get_distance(data, 1000000))


if __name__ == '__main__':
    main()
