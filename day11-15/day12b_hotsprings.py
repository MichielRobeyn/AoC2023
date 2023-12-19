from functools import cache


@cache
def get_num_solutions(springs, target):
    current_target = target[0]
    future_targets = target[1:]

    current_target_after_index = current_target - 1
    future_target_len = sum(future_targets) + len(future_targets)

    valid = 0
    for i in range(len(springs) - future_target_len - current_target_after_index):
        if all(char in '?#' for char in springs[i: i + current_target]):
            if len(future_targets) == 0:
                if all(char in '?.' for char in springs[i + current_target:]):
                    valid += 1
            elif springs[i + current_target] in '?.':
                valid += get_num_solutions(springs[i + current_target + 1:], future_targets)

        if springs[i] not in '.?':
            break
    return valid


def main():
    with open('day12_input.txt') as file:
        lines = file.readlines()

    data = []
    for line in lines:
        springs = line.strip().split()[0]
        sequential_damaged = line.strip().split()[1]
        spring = '?'.join((springs,)*5)
        seq = ','.join((sequential_damaged,)*5)
        seq = [int(element) for element in seq.split(',')]
        data.append((spring, tuple(seq)))

    total = 0
    for i, dat in enumerate(data):
        total += get_num_solutions(dat[0], dat[1])
    print(total)


if __name__ == '__main__':
    main()
