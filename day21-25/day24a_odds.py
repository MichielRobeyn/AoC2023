import numpy as np


def calc_valid_intersections(data, lower, upper):
    total = 0
    for i, (hail1_loc, hail1_v) in enumerate(data):
        for j, (hail2_loc, hail2_v) in enumerate(data[i + 1:]):
            a = np.array([[-hail1_v[0], hail2_v[0]], [-hail1_v[1], hail2_v[1]]])
            b = np.array([hail1_loc[0] - hail2_loc[0], hail1_loc[1] - hail2_loc[1]])
            if a[0][0]/a[0][1] != a[1][0]/a[1][1]:
                x = np.linalg.solve(a, b)
                if x[0] >= 0 and x[1] >= 0:
                    x_coord = x[1] * hail2_v[0] + hail2_loc[0]
                    y_coord = x[1] * hail2_v[1] + hail2_loc[1]
                    if lower <= x_coord <= upper and lower <= y_coord <= upper:
                        total += 1
    return total


def main():
    data = []
    with open('day24_input.txt') as file:
        for line in file:
            position, velocity = line.strip().split('@')
            position = tuple([int(char) for char in position.split(',')])
            velocity = tuple([int(char) for char in velocity.split(',')])
            data.append((position, velocity))

    print(calc_valid_intersections(data, 200000000000000, 400000000000000))


if __name__ == '__main__':
    main()
