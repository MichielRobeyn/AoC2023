import numpy as np
from copy import deepcopy


def get_next(dict_ranges, rules):
    lst = []
    leftover_dict = deepcopy(dict_ranges)
    for rule in rules[:-1]:
        base, end = rule.split(':')
        if base[1] == '<':
            dict_temp = deepcopy(leftover_dict)
            dict_temp[base[0]] = (dict_temp[base[0]][0], max(int(base[2:]) - 1, dict_temp[base[0]][0]))
            leftover_dict[base[0]] = (min(dict_ranges[base[0]][1], int(base[2:]) - 1), dict_ranges[base[0]][1])
            lst.append((dict_temp, end))
        elif rule[1] == '>':
            dict_temp = deepcopy(leftover_dict)
            dict_temp[base[0]] = (min(dict_temp[base[0]][1], int(base[2:])), dict_temp[base[0]][1])
            leftover_dict[base[0]] = (dict_ranges[base[0]][0], max(int(base[2:]), dict_ranges[base[0]][0]))
            lst.append((dict_temp, end))

    lst.append((leftover_dict, rules[-1]))
    return lst


def get_accepted(workflow, flow='in', dict_ranges=None):
    if dict_ranges is None:
        dict_ranges = {'x': (0, 4000), 'm': (0, 4000), 'a': (0, 4000), 's': (0, 4000)}
    total = 0
    if flow == 'A':
        return np.prod([dict_ranges[key][1] - dict_ranges[key][0] for key in dict_ranges.keys()], dtype='int64')
    elif flow == 'R':
        return 0
    else:
        list_ranges = get_next(dict_ranges, workflow[flow])
        for pos_range, flow2 in list_ranges:
            total += get_accepted(workflow, flow2, pos_range)
    return total


def main():
    with open('input.txt') as file:
        data = file.read()

    rules, parts = data.strip().split('\n\n')
    workflow = dict()
    for rule in rules.split():
        key, values = rule.split('{')
        values = values[:-1].split(',')
        workflow[key] = values

    print(get_accepted(workflow))


if __name__ == '__main__':
    main()
