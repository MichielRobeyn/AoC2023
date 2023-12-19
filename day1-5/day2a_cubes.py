# cubes = [number(red), number(green), number(blue)]
def possible_games(gameslist, cubes):
    total = 0
    for key in gameslist:
        if gameslist[key][0] <= cubes[0] and gameslist[key][1] <= cubes[1] and gameslist[key][2] <= cubes[2]:
            total += int(key)
    return total


def extract_information(text):
    red, green, blue = 0, 0, 0
    info = text.split(',')
    for item in info:
        if 'red' in item:
            red = int(''.join(filter(lambda i: i.isdigit(), item)))
        if 'green' in item:
            green = int(''.join(filter(lambda i: i.isdigit(), item)))
        if 'blue' in item:
            blue = int(''.join(filter(lambda i: i.isdigit(), item)))
    return red, green, blue


def main():
    cubes = [12, 13, 14]
    with open('day2_input.txt') as file:
        lines = file.readlines()
    gameslist = dict()
    for line in lines:
        (game, information) = line.strip().split(':')
        game_id = game.split(' ')[1]
        information_list = information.split(';')
        red, green, blue = 0, 0, 0
        for item in information_list:
            item_red, item_green, item_blue = extract_information(item)
            red = max(red, item_red)
            green = max(green, item_green)
            blue = max(blue, item_blue)
        gameslist[game_id] = (red, green, blue)
    print(possible_games(gameslist, cubes))


if __name__ == '__main__':
    main()
