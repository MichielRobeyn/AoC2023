import numpy as np


def hash_to_number(string):
    value = 0
    for char in string:
        value += ord(char)
        value = 17 * value
        value = value % 256
    return value


def main():
    with open('day15_input.txt') as file:
        string = file.read()
    string_list = string.strip().split(',')

    boxes = dict()
    for i in range(256):
        boxes[i] = []

    for string in string_list:
        if '-' in string:
            label, focal = string.split('-')
            box = hash_to_number(label)
            boxes[box] = [item for item in boxes[box] if item[0] != label]
        else:
            label, focal = string.split('=')
            box = hash_to_number(label)
            if boxes[box]:
                if label in [el[0] for el in boxes[box]]:
                    index = [el[0] for el in boxes[box]].index(label)
                    boxes[box][index] = [label, int(focal)]
                else:
                    boxes[box].append([label, int(focal)])
            else:
                boxes[box].append([label, int(focal)])
    total = 0
    for key in boxes:
        if boxes[key]:
            for i, value in enumerate(boxes[key]):
                total += (key+1) * (i+1) * value[1]
    print(total)


if __name__ == '__main__':
    main()
