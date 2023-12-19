import numpy as np
# 7 = five of a kind, 6 = four of a kind, 5 = full house, 4 = three of a kind, 3 = two pair, 2 = one pair, 1 = high card
# 13 = A, 12 = K, 11 = Q, 10 = J, 9 = T, 8 = 9, 7 = 8, 6 = 7, 5 = 6, 4 = 5, 3 = 4, 2 = 3, 1 = 2


def label(array_hand):
    hand = dict()
    cards = np.arange(13, 0, -1)
    for card in cards:
        hand[card] = 0
    for number_card in array_hand:
        hand[number_card] += 1
    if max(hand.values()) == 5:
        return 7
    elif max(hand.values()) == 4:
        return 6
    elif max(hand.values()) == 3:
        if 2 in hand.values():
            return 5
        else:
            return 4
    elif max(hand.values()) == 2:
        if list(hand.values()).count(2) == 2:
            return 3
        else:
            return 2
    else:
        return 1


def convert_cards(string_cards):
    cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    cards_converted = np.arange(13, 0, -1)

    hand = np.array([cards_converted[cards.index(card)] for card in string_cards])
    return hand


def get_hand_value(hand):
    hand_cards, hand_value = hand
    value = 10000000000*hand_value
    multiplier = 100000000
    for card in hand_cards:
        value += card*multiplier
        multiplier = multiplier/100
    return value


def main():
    with open('day7_input.txt') as file:
        lines = file.readlines()
    hands = []
    bids = []
    for line in lines:
        string_hand, bid = line.strip().split()
        hand = convert_cards(string_hand)
        value = label(hand)
        hands.append(get_hand_value((hand, value)))
        bids.append(int(bid))

    hands = np.array(hands)
    indices = hands.argsort()
    bids = np.array(bids)
    bids_sorted = bids[indices]
    bids_multiplier = np.arange(1, len(bids_sorted) + 1)
    reward_per_bid = bids_multiplier*bids_sorted
    print(reward_per_bid.sum())


if __name__ == '__main__':
    main()
