def main():
    with open('day1_input.txt') as file:
        content = file.readlines()
    total = 0
    for line in content:
        digits = ''.join(filter(lambda i: i.isdigit(), line))
        value = digits[0] + digits[-1]
        total += int(value)
    print(total)


if __name__ == '__main__':
    main()
