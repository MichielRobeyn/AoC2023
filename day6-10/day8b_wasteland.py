import numpy as np


def loop(instructions, nodes, end, list_nodes, steps):

    for i, instruction in enumerate(instructions):
        end = nodes[end][instruction]
        element = (i, end)
        if element in list_nodes:
            return list_nodes.index(element), steps - list_nodes.index(element), \
                [i-list_nodes.index(element) for i in range(len(list_nodes)) if list_nodes[i][1][2] == 'Z']
        else:
            list_nodes.append(element)
            steps += 1
    return loop(instructions, nodes, end, list_nodes, steps)


def calculate_steps(values):
    starting_seq, loop_len, index_z, num_of_loops = values
    return starting_seq + num_of_loops * loop_len + index_z + 1


def calculate_smallest_multiple(list_results):
    results = np.apply_along_axis(calculate_steps, 1, list_results)
    return np.lcm.reduce(results)  # endpoints are located at exactly starting seq + (loop length - starting seq) -> lcm


def main():
    with open('day8_input.txt') as file:
        lines = file.readlines()
    list_nodelines = lines[2:]
    instructions = lines[0].strip()
    instructions = [0 if char == 'L' else 1 for char in instructions]
    nodes = dict()
    for node in list_nodelines:
        node_split = node.strip().split()
        nodes[node_split[0]] = (node_split[2][1:-1], node_split[3][:-1])

    start = [key for key in nodes if key[2] == 'A']
    loops = []
    for startitem in start:
        starting_seq, loop_len, index_z = loop(instructions, nodes, startitem, [], 0)
        loops.append([starting_seq, loop_len, index_z[0], 0])  # only 1 seq ends with z for every loop
    loops = np.array(loops, dtype='int64')
    print(calculate_smallest_multiple(loops))


if __name__ == '__main__':
    main()
