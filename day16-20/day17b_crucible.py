import numpy as np
from collections import defaultdict
from heapq import heappop, heappush


def get_neighbours(current):
    (x, y), line = current
    if 3 < line[1] < 10:
        if line[0] == 0:
            return [((x, y + 1), (1, 1)), ((x, y - 1), (3, 1)), ((x + 1, y), (0, line[1] + 1))]
        elif line[0] == 1:
            return [((x + 1, y), (0, 1)), ((x - 1, y), (2, 1)), ((x, y + 1), (1, line[1] + 1))]
        elif line[0] == 2:
            return [((x, y + 1), (1, 1)), ((x, y - 1), (3, 1)), ((x - 1, y), (2, line[1] + 1))]
        else:
            return [((x + 1, y), (0, 1)), ((x - 1, y), (2, 1)), ((x, y - 1), (3, line[1] + 1))]
    elif line[1] <= 3:
        if line[0] == 0:
            return [((x + 1, y), (0, line[1] + 1))]
        elif line[0] == 1:
            return [((x, y + 1), (1, line[1] + 1))]
        elif line[0] == 2:
            return [((x - 1, y), (2, line[1] + 1))]
        else:
            return [((x, y - 1), (3, line[1] + 1))]
    else:
        if line[0] == 0:
            return [((x, y + 1), (1, 1)), ((x, y - 1), (3, 1))]
        elif line[0] == 1:
            return [((x + 1, y), (0, 1)), ((x - 1, y), (2, 1))]
        elif line[0] == 2:
            return [((x, y + 1), (1, 1)), ((x, y - 1), (3, 1))]
        else:
            return [((x + 1, y), (0, 1)), ((x - 1, y), (2, 1))]


def a_star(start, goal, array):
    num_rows, num_columns = len(array), len(array[0])
    open_nodes = [(0, (start, (0, 0))), (0, (start, (1, 0)))]

    g_score = defaultdict(lambda: np.inf)

    while open_nodes:
        current = heappop(open_nodes)

        if current[1][0] == goal:
            if 3 < current[1][1][1] < 11:
                return current[0]
            else:
                continue

        for neighbour in get_neighbours(current[1]):
            x, y = neighbour[0]
            if x in range(num_rows) and y in range(num_columns):
                tentative_g = current[0] + array[neighbour[0]]
                if tentative_g < g_score[neighbour]:
                    g_score[neighbour] = tentative_g
                    heappush(open_nodes, (g_score[neighbour], neighbour))
    return -1


def main():
    with open('day17_input.txt') as file:
        lines = file.readlines()

    data = []
    for line in lines:
        data.append([int(char) for char in line.strip()])
    data = np.array(data)

    print(a_star((0, 0), (len(data) - 1, len(data[0]) - 1), data))


if __name__ == '__main__':
    main()
