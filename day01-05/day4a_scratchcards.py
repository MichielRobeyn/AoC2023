def points(matches):
    if matches > 0:
        return 2**(matches-1)
    else:
        return 0


def number_of_matches(numbers):
    winning_line, number_line = numbers.strip().split('|')
    winning_numbers = winning_line.strip().split()
    numbers = number_line.strip().split()
    matches = 0
    for number in numbers:
        if number in winning_numbers:
            matches += 1
    return matches


def main():
    with open('day4_input.txt') as file:
        lines = file.readlines()
    cards = dict()
    for line in lines:
        card_id, card_numbers = line.strip().split(':')
        matches = number_of_matches(card_numbers)
        cards[card_id] = points(matches)
    print(sum(cards.values()))


if __name__ == '__main__':
    main()
