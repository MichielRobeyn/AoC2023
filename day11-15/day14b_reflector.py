import numpy as np


def tilt_n(array, coordinates):

    for i in range(len(array)):
        coor = coordinates[i]
        start = 0
        for (x, y) in coor:
            num = len(np.where(array[start:x, i] == 'O')[0])
            array[start:x, i] = np.concatenate((np.array(['O'] * num), np.array(['.'] * ((x - start) - num))))
            start = x + 1
        num = len(np.where(array[start:, i] == 'O')[0])
        array[start:, i] = np.concatenate((np.array(['O'] * num), np.array(['.'] * ((len(array) - start) - num))))

    return array


def cycle(array, coordinates, n):
    coordinates_n = coordinates[0]
    coordinates_w = coordinates[1]
    coordinates_s = coordinates[2]
    coordinates_e = coordinates[3]
    column_north = dict()
    column_east = dict()
    column_south = dict()
    column_west = dict()
    for i in range(len(array)):
        column_north[i] = []
        column_east[i] = []
        column_south[i] = []
        column_west[i] = []
    for coordinate in coordinates_n:
        x, y = coordinate
        column_north[y] += [(x, y)]
    for coordinate in coordinates_w:
        x, y = coordinate
        column_west[y] += [(x, y)]
    for coordinate in coordinates_s:
        x, y = coordinate
        column_south[y] += [(x, y)]
    for coordinate in coordinates_e:
        x, y = coordinate
        column_east[y] += [(x, y)]

    collection = []
    for i in range(n):
        array = tilt_n(array, column_north)
        array = np.rot90(array, -1)

        array = tilt_n(array, column_west)
        array = np.rot90(array, -1)

        array = tilt_n(array, column_south)
        array = np.rot90(array, -1)

        array = tilt_n(array, column_east)
        array = np.rot90(array, -1)
        load = calculate_load(array)
        if load not in collection:
            collection.append(load)
        else:
            print(i, collection.index(load))
            collection.append(load)
    return array


def calculate_load(array):
    load = 0
    for i in range(len(array[0])):
        load += calculate_load_column(array[:, i])
    return load


def calculate_load_column(column):
    start_load = len(column)
    load = 0
    for i in range(len(column)):
        if column[i] == 'O':
            load += start_load - i
    return load


def main():
    with open('day14_input.txt') as file:
        lines = file.readlines()

    data = []
    for line in lines:
        data.append([char for char in line.strip()])

    data = np.array(data)
    coordinates_n = np.argwhere(data == '#')
    data = np.rot90(data, -1)
    coordinates_w = np.argwhere(data == '#')
    data = np.rot90(data, -1)
    coordinates_s = np.argwhere(data == '#')
    data = np.rot90(data, -1)
    coordinates_e = np.argwhere(data == '#')
    data = np.rot90(data, -1)
    coordinates = [coordinates_n, coordinates_w, coordinates_s, coordinates_e]
    array = cycle(data, coordinates, 132)  # cycle 38, start 115, ((1000000000-115) % 38 = 17   ->   end at 115+17=132)
    print(array)

    print(calculate_load(array))


if __name__ == '__main__':
    main()
