import numpy as np


def palindrome(array):
    total = 0
    for i in range(len(array) - 1):
        left, right = i, i + 1
        while left > -1 and right < len(array):
            if (array[left, :] == array[right, :]).all():
                left -= 1
                right += 1
            else:
                break
        else:
            total += 100*(i+1)

    for i in range(len(array[0]) - 1):
        left, right = i, i + 1
        while left > -1 and right < len(array[0]):
            if (array[:, left] == array[:, right]).all():
                left -= 1
                right += 1
            else:
                break
        else:
            total += i+1
    return total


def main():
    with open('day13_input.txt') as file:
        blocks = file.read().split('\n\n')
        data = []
        for i, block in enumerate(blocks):
            lines = block.splitlines()
            data.append([])
            for line in lines:
                data[i].append([char for char in line.strip()])
    total = 0
    for dat in data:
        total += palindrome(np.array(dat))
    print(total)


if __name__ == '__main__':
    main()
