from collections import defaultdict


class Card:
    PICTURE_CARDS_TABLE = {"A": 1, "J": 11, "Q": 12, "K": 13}

    def __init__(self, card_str: str) -> None:
        self.suit = card_str[0]
        self.sign = card_str[1:]
        self.num = self.convert_sign_2_num(self.sign)

    @staticmethod
    def convert_sign_2_num(sign: str) -> int:
        if sign in Card.PICTURE_CARDS_TABLE:
            return Card.PICTURE_CARDS_TABLE[sign]

        else:
            return int(sign)


class Hand:
    def __init__(self) -> None:
        self.cards = []

    def add(self, card: Card) -> None:
        self.cards.append(card)


card1 = Card("♦A")
card2 = Card("♥Q")
hand = Hand()
hand.add(card1)
hand.add(card2)
for card in hand.cards:
    print(card.suit, card.sign, card.num)


def winnerPairOfCards(player1: list[str], player2: list[str]) -> str:
    player1_hand_arr = generate_int_hand(player1)
    player2_hand_arr = generate_int_hand(player2)

    card_level_arr = [1, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    player1_countmap = generate_countmap(player1_hand_arr)
    player2_countmap = generate_countmap(player2_hand_arr)

    match_winner = "draw"
    max_pair_num = 0

    for card_num in card_level_arr:
        if (
            player1_countmap[card_num] > player2_countmap[card_num]
            and player1_countmap[card_num] > max_pair_num
        ):
            match_winner = "player1"
            max_pair_num = player1_countmap[card_num]

        elif (
            player1_countmap[card_num] < player2_countmap[card_num]
            and player2_countmap[card_num] > max_pair_num
        ):
            match_winner = "player2"
            max_pair_num = player2_countmap[card_num]

    return match_winner


def generate_int_hand(cards: list[str]) -> list[int]:

    picture_card = {"A": 1, "J": 11, "Q": 12, "K": 13}
    hand_arr = []
    for card_num in cards:

        if card_num[1:] in picture_card:
            hand_arr.append(picture_card[card_num[1:]])
        else:
            hand_arr.append(int(card_num[1:]))

    return hand_arr


def generate_countmap(hand_arr: list[int]) -> dict[int]:
    countmap = defaultdict(int)

    for card in hand_arr:
        countmap[card] += 1

    return countmap


# print(winnerPairOfCards(["♣4", "♥7", "♥7", "♠Q", "♣J"], ["♥7", "♥7", "♣K", "♠Q", "♦2"]))
