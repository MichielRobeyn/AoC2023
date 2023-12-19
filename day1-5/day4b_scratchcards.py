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
        card_id = int(card_id.strip().split()[1])
        matches = number_of_matches(card_numbers)
        cards[card_id] = matches, 1
    for key in cards:
        for i in range(cards[key][0]):
            cards[key+(i+1)] = cards[key+(i+1)][0], cards[key+(i+1)][1] + cards[key][1]
    total = 0
    for element in cards.values():
        total += element[1]
    print(total)


if __name__ == '__main__':
    main()
