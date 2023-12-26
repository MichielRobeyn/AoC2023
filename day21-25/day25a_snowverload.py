import networkx as nx


def graph(data):
    edges = []
    for key in data:
        edges.extend([(key, value) for value in data[key]])
    circuit = nx.Graph()
    circuit.add_edges_from(edges)
    print(nx.minimum_edge_cut(circuit))
    circuit.remove_edges_from(nx.minimum_edge_cut(circuit))
    return [len(c) for c in nx.connected_components(circuit)]


def main():
    data = dict()
    with open('day25_input.txt') as file:
        for line in file:
            origin, destination = line.strip().split(':')
            destination = destination.split()
            data[origin] = destination

    lengths = graph(data)
    if len(lengths) == 2:
        print(lengths[0] * lengths[1])


if __name__ == '__main__':
    main()
