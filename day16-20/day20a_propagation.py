def main():
    data = dict()
    with open('input.txt') as file:
        for line in file:
            key, values = line.strip().split(' -> ')
            data[key] = values
    print(data)


if __name__ == '__main__':
    main()
