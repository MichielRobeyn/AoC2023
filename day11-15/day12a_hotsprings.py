import numpy as np


def get_num_solutions(springs, number, indices, target):
    valid = 0
    if number > 1:
        for i in range(len(indices) - (number-1)):
            springs[indices[i]] = '#'
            if temp_check(springs, target, indices[i]):
                valid += get_num_solutions(springs, number-1, indices[i+1:], target)
            springs[indices[i]] = '?'
    else:
        for i in range(len(indices)):
            springs[indices[i]] = '#'
            valid += check_sequential(springs, target)
            springs[indices[i]] = '?'
    return valid


def temp_check(lst, target, max_index):
    num = 0
    i = 0
    for j, el in enumerate(lst):
        if j < max_index:
            if el == '#':
                num += 1
                if num > target[i]:
                    return False
            else:
                if num != 0:
                    if num == target[i]:
                        num = 0
                        i += 1
                    else:
                        return False
    return True


def check_sequential(lst, target):
    num = 0
    i = 0
    for el in lst:
        if el == '#':
            num += 1
        else:
            if num != 0:
                if num == target[i]:
                    num = 0
                    i += 1
                else:
                    return 0
    if num != 0:
        if num != target[i]:
            return 0
    return 1


def main():
    with open('day12_input.txt') as file:
        lines = file.readlines()

    data = []
    for line in lines:
        spring = line.strip().split()[0]
        spring = np.array([char for char in spring])
        seq = line.strip().split()[1]
        seq = [int(element) for element in seq.split(',')]
        data.append((spring, seq, sum(seq) - np.count_nonzero(spring == '#'), np.array([x for x in range(len(spring)) if spring[x] == '?'])))

    total = 0
    for dat in data:
        if dat[2] == 0 or dat[2] == len(dat[3]):
            total += 1
        else:
            total += get_num_solutions(dat[0], dat[2], dat[3], dat[1])
    print(total)


if __name__ == '__main__':
    main()
