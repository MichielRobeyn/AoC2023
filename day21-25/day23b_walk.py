import math
from copy import deepcopy


def get_next(array, start, previous):
    x, y = start
    length = len(array)
    width = len(array[0])
    next_loc = []
    for add_x in range(-1, 2, 2):
        if -1 < x + add_x < length:
            if (x + add_x, y) != previous:
                if add_x == -1 and array[x + add_x][y] in '.><^v':
                    next_loc.append((x + add_x, y))
                elif add_x == 1 and array[x + add_x][y] in '.><^v':
                    next_loc.append((x + add_x, y))

    for add_y in range(-1, 2, 2):
        if -1 < y + add_y < width:
            if (x, y + add_y) != previous:
                if add_y == -1 and array[x][y + add_y] in '.><^v':
                    next_loc.append((x, y + add_y))
                elif add_y == 1 and array[x][y + add_y] in '.><^v':
                    next_loc.append((x, y + add_y))

    return next_loc


def next_node(node, graph, visited_nodes):
    nexts = graph[node]
    nexts = [n for n in nexts if n[0] not in visited_nodes]
    return nexts


def get_longest_path(graph, start, end, length, visited_nodes=None):
    if visited_nodes is None:
        visited_nodes = set()
    visited_nodes.add(start)
    print(visited_nodes)
    if start == end:
        return length
    next_nodes = next_node(start, graph, visited_nodes)
    if next_nodes:
        return max([get_longest_path(graph, loc[0], end, length + loc[1], deepcopy(visited_nodes)) for loc in next_nodes])
    else:
        return -math.inf


def create_graph(array, start, graph):
    length = 1
    open_nodes = {(get_next(array, start, (-1, -1))[0], start)}
    closed_nodes = set()
    while open_nodes:
        start, opened = open_nodes.pop()
        previous = opened
        while start[0] != len(array) - 1:
            next_loc = get_next(array, start, previous)
            if len(next_loc) > 1:
                graph[opened].append((start, length))
                graph[start].append((opened, length))
                closed_nodes.add(opened)
                length = 1
                if start not in closed_nodes:
                    open_nodes.update([(node, start) for node in get_next(array, start, previous)])
                break
            elif len(next_loc) == 1:
                previous = start
                start = next_loc[0]
                length += 1
            else:
                break
        else:
            graph[opened].append((start, length))
            closed_nodes.add(opened)
            length = 1
            open_nodes.update([(node, start) for node in get_next(array, start, previous)])
    for key in graph:
        graph[key] = list(set(graph[key]))
    return graph


def main():
    data = []
    with open('day23_input.txt') as file:
        for line in file:
            data.append([char for char in line.strip()])

    nodes = []
    for i, row in enumerate(data):
        for j, elem in enumerate(row):
            if len(get_next(data, (i, j), (-1, -1))) > 2 and elem != '#':
                nodes.append((i, j))

    graph = dict()
    start = (0, data[0].index('.'))
    end = (len(data) - 1, data[len(data) - 1].index('.'))
    graph[start] = []
    for node in nodes:
        graph[node] = []

    graph = create_graph(data, start, graph)
    print(get_longest_path(graph, start, end, 0))


if __name__ == '__main__':
    main()
