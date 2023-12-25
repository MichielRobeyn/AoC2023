import math
import sys
sys.setrecursionlimit(10000)


def get_next(array, start, previous):
    x, y = start
    length = len(array)
    width = len(array[0])
    next_loc = []
    for add_x in range(-1, 2, 2):
        if -1 < x + add_x < length:
            if (x + add_x, y) != previous:
                if add_x == -1 and array[x + add_x][y] in '.><^':
                    next_loc.append((x + add_x, y))
                elif add_x == 1 and array[x + add_x][y] in '.><v':
                    next_loc.append((x + add_x, y))

    for add_y in range(-1, 2, 2):
        if -1 < y + add_y < width:
            if (x, y + add_y) != previous:
                if add_y == -1 and array[x][y + add_y] in '.<^v':
                    next_loc.append((x, y + add_y))
                elif add_y == 1 and array[x][y + add_y] in '.>^v':
                    next_loc.append((x, y + add_y))

    return next_loc


def get_longest_path(array, start, previous, length):
    if start[0] == len(array) - 1:
        return length
    next_loc = get_next(array, start, previous)
    if next_loc:
        return max([get_longest_path(array, loc, start, length + 1) for loc in next_loc])
    else:
        return -math.inf


def main():
    data = []
    with open('day23_input.txt') as file:
        for line in file:
            data.append([char for char in line.strip()])

    start = (0, data[0].index('.'))
    print(get_longest_path(data, start, (-1, -1), 0))


if __name__ == '__main__':
    main()
