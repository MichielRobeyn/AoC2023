import numpy as np


def get_previous_element(array):
    difference = np.diff(array)
    if not difference.any():
        next_element = array[0]
    else:
        next_element = array[0] - get_previous_element(difference)
    return next_element


def main():
    with open('day9_input.txt') as file:
        lines = file.readlines()

    dimension_row = len(lines[0].strip().split())
    content = np.empty((0, dimension_row), int)

    for line in lines:
        arr = np.array([[int(x) for x in line.strip().split()]])
        content = np.append(content, arr, axis=0)

    print(np.sum(np.apply_along_axis(get_previous_element, 1, content)))


if __name__ == '__main__':
    main()
