import numpy as np


def get_coords(lines):
    coords = [(0, 0)]
    last_coord = (0, 0)
    for line in lines:
        x, y = last_coord
        direction, number, colour = line
        if direction == 'U':
            last_coord = (x - int(number), y)
            coords.append(last_coord)
        elif direction == 'D':
            last_coord = (x + int(number), y)
            coords.append(last_coord)
        elif direction == 'R':
            last_coord = (x, y + int(number))
            coords.append(last_coord)
        else:
            last_coord = (x, y - int(number))
            coords.append(last_coord)
    return coords


def get_perimeter(coords):
    start = coords[0]
    length = 0
    for coord in coords[1:]:
        length += abs(start[0] - coord[0]) + abs(start[1] - coord[1])
        start = coord
    return length


def shoelace(x_y):
    x_y = np.array(x_y)
    x_y = x_y.reshape(-1, 2)

    x = x_y[:, 0]
    y = x_y[:, 1]

    s1 = np.sum(x*np.roll(y, -1))
    s2 = np.sum(y*np.roll(x, -1))

    area = .5*np.absolute(s1 - s2)

    return area


def main():
    with open('day18_input.txt') as file:
        lines = file.readlines()

    data = []
    for line in lines:
        data.append(line.strip().split())

    coords = get_coords(data)
    perimeter = get_perimeter(coords)
    area = shoelace(coords)
    interior_points = area + 1 - (perimeter/2)
    print(interior_points+perimeter)


if __name__ == '__main__':
    main()
