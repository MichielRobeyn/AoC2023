from itertools import product
# possible problems: multiple same numbers next to a symbol, number adjacent to 2 symbols


def locate_gear_symbols(matrix):
    symbols = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '*':
                symbols.append((i, j))
    return symbols


def adjacent(coordinates):
    ranges = [(x - 1, x, x + 1) for x in coordinates]
    result = list(product(*ranges))
    result.pop(len(result) // 2)
    return result


def extract_numbers(location, matrix):
    adjacent_coordinates = adjacent(location)
    numbers = []
    for coordinate in adjacent_coordinates:
        i = coordinate[0]
        j = coordinate[1]
        number = ''
        digits = True
        while j < len(matrix[i]) and digits:
            if matrix[i][j].isdigit():
                number += matrix[i][j]
                j += 1
            else:
                digits = False
        j = coordinate[1] - 1
        digits = True
        while j >= 0 and digits and number != '':
            if matrix[i][j].isdigit():
                number = matrix[i][j] + number
                j -= 1
            else:
                digits = False
        numbers.append(number)
    return numbers


def get_gear_ratio(numbers):
    numbers = set(numbers)
    numbers.discard('')
    result = 0
    if len(numbers) == 2:
        result = 1
        for number in numbers:
            result *= int(number)
    return result


def main():
    with open('day3_input.txt') as file:
        lines = file.readlines()

    matrix = []
    for i, line in enumerate(lines):
        matrix.append([])
        for j in range(len(line.strip())):
            matrix[i].append(line[j])
    symbols = locate_gear_symbols(matrix)
    total = 0
    for symbol in symbols:
        numbers = extract_numbers(symbol, matrix)
        total += get_gear_ratio(numbers)
    print(total)


if __name__ == '__main__':
    main()
