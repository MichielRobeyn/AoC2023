import math


def recordbreaking(time, max_distance):
    a = -1
    b = time
    c = -max_distance
    d = b**2 - 4 * a * c
    result = (-b + math.sqrt(d)) / (2 * a)
    return time - 2 * (math.floor(result)) - 1


def main():
    with open('day6_input.txt') as file:
        lines = file.readlines()
    time = int(''.join(lines[0].strip().split(':')[1].strip().split()))
    max_distance = int(''.join(lines[1].strip().split(':')[1].strip().split()))
    possible_buttonpresses = recordbreaking(time, max_distance)
    print(possible_buttonpresses)


if __name__ == '__main__':
    main()
