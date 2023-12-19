def run_through(instructions, nodes, end, steps):
    for instruction in instructions:
        if end != 'ZZZ':
            end = nodes[end][instruction]
            steps += 1
        else:
            return steps
    return run_through(instructions, nodes, end, steps)


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
    print(run_through(instructions, nodes, 'AAA', 0))


if __name__ == '__main__':
    main()
