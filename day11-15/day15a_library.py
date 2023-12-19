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
    total = 0
    for string in string_list:
        total += hash_to_number(string)
    print(total)


if __name__ == '__main__':
    main()
