def text_to_digits(text):
    digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    digits_map = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    index = digits.index(text)
    return digits_map[index]


def extract_digits(line):
    digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    first_digit = 0
    last_digit = 0
    for i in range(len(line)):
        if line[i].isdigit():
            if first_digit == 0:
                first_digit = line[i]
                last_digit = line[i]
                i += 1
            else:
                last_digit = line[i]
                i += 1
        elif line[i:i + 3] in digits:
            if first_digit == 0:
                first_digit = text_to_digits(line[i:i + 3])
                last_digit = text_to_digits(line[i:i + 3])
                i += 1
            else:
                last_digit = text_to_digits(line[i:i + 3])
                i += 1
        elif line[i:i + 4] in digits:
            if first_digit == 0:
                first_digit = text_to_digits(line[i:i + 4])
                last_digit = text_to_digits(line[i:i + 4])
                i += 1
            else:
                last_digit = text_to_digits(line[i:i + 4])
                i += 1
        elif line[i:i + 5] in digits:
            if first_digit == 0:
                first_digit = text_to_digits(line[i:i + 5])
                last_digit = text_to_digits(line[i:i + 5])
                i += 1
            else:
                last_digit = text_to_digits(line[i:i + 5])
                i += 1
        else:
            i += 1
    number = first_digit + last_digit
    return number


def main():
    with open('day1_input.txt') as file:
        content = file.readlines()
    total = 0
    for line in content:
        number = extract_digits(line)
        total += int(number)
    print(total)


if __name__ == '__main__':
    main()
