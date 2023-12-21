def get_end_positions(data):
    start = [(index, row.index('S')) for index, row in enumerate(data) if 'S' in row]
    data[start[0][0]][start[0][1]] = '.'
    new_starts = start
    for i in range(64):
        new_starting = []
        for coord in new_starts:
            new_starting.extend(get_next(data, coord))
        new_starts = set(new_starting)
    return len(new_starts)


def get_next(data, start_pos):
    next_pos = []
    x, y = start_pos
    steps = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    for step in steps:
        step_x, step_y = step
        if step_x in range(len(data)) and step_y in range(len(data[0])) and data[step_x][step_y] == '.':
            next_pos.append(step)
    return next_pos


def main():
    with open('day21_input.txt') as file:
        data = []
        for line in file:
            data.append([char for char in line.strip()])

    print(get_end_positions(data))


if __name__ == '__main__':
    main()
