import numpy as np


def merge(dict_1, dict_2):
    dict_3 = {**dict_1, **dict_2}
    for key, value in dict_3.items():
        if key in dict_1 and key in dict_2:
            dict_3[key] = [value, dict_1[key]]
    return dict_3


def get_next(array, start, direction):
    x, y = start
    if array[x][y] == '.':
        if direction == 0:
            return (x, y + 1), direction
        elif direction == 1:
            return (x + 1, y), direction
        elif direction == 2:
            return (x, y - 1), direction
        else:
            return (x - 1, y), direction
    elif array[x][y] == '-':
        if direction == 0:
            return (x, y + 1), direction
        else:
            return (x, y - 1), direction
    elif array[x][y] == '|':
        if direction == 1:
            return (x + 1, y), direction
        else:
            return (x - 1, y), direction
    elif array[x][y] == '/':
        if direction == 0:
            return (x - 1, y), 3
        elif direction == 1:
            return (x, y - 1), 2
        elif direction == 2:
            return (x + 1, y), 1
        else:
            return (x, y + 1), 0
    else:
        if direction == 0:
            return (x + 1, y), 1
        elif direction == 1:
            return (x, y + 1), 0
        elif direction == 2:
            return (x - 1, y), 3
        else:
            return (x, y - 1), 2


def get_energized(array, coll=None, direction=None, start=None):
    if coll is None:
        coll = dict()
    if direction is None:
        direction = 0
    if start is None:
        start = (0, 0)

    if not (start[0] in range(len(array)) and start[1] in range(len(array[0]))):
        return coll
    running = True
    coll[start] = [direction]
    if (direction == 0 or direction == 2) and array[start[0]][start[1]] == '|':
        return merge(get_energized(array, coll, 1, (start[0] + 1, start[1])),
                     get_energized(array, coll, 3, (start[0] - 1, start[1])))
    elif (direction == 1 or direction == 3) and array[start[0]][start[1]] == '-':
        return merge(get_energized(array, coll, 0, (start[0], start[1] + 1)),
                     get_energized(array, coll, 2, (start[0], start[1] - 1)))

    next_coord, direction = get_next(array, start, direction)
    if not (next_coord[0] in range(len(array)) and next_coord[1] in range(len(array[0]))):
        running = False
    while running:
        if next_coord in coll.keys():
            if direction in coll[next_coord]:
                return coll
            else:
                coll[next_coord].append(direction)
        else:
            coll[next_coord] = [direction]

        if (direction == 0 or direction == 2) and array[next_coord[0]][next_coord[1]] == '|':
            return merge(get_energized(array, coll, 1, (next_coord[0] + 1, next_coord[1])), get_energized(array, coll, 3, (next_coord[0] - 1, next_coord[1])))
        elif (direction == 1 or direction == 3) and array[next_coord[0]][next_coord[1]] == '-':
            return merge(get_energized(array, coll, 0, (next_coord[0], next_coord[1] + 1)), get_energized(array, coll, 2, (next_coord[0], next_coord[1] - 1)))
        else:
            next_coord, direction = get_next(array, next_coord, direction)
        if not (next_coord[0] in range(len(array)) and next_coord[1] in range(len(array[0]))):
            running = False
    return coll


def main():
    with open('day16_input.txt') as file:
        lines = file.readlines()

    data = []
    for line in lines:
        data.append([char for char in line.strip()])

    data = np.array(data)
    coll = get_energized(data)
    print(len(coll.keys()))


if __name__ == '__main__':
    main()
