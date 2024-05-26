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
        self.card_num_count_map = defaultdict(int)

    def add(self, card: Card) -> None:
        self.cards.append(card)
        self.card_num_count_map[card.num] += 1


class HandHelper:
    @staticmethod
    def convert_from_card_str_arr(card_str_arr: list) -> Hand:
        hand = Hand()
        for card_str in card_str_arr:
            card = Card(card_str)
            hand.add(card)

        return hand


class PairOfCards:
    CARD_LEVEL_ARR = [1, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    def __init__(self, player1_hand: Hand, player2_hand: Hand) -> None:
        self.player1_hand = player1_hand
        self.player2_hand = player2_hand

    def get_winner(self) -> str:
        match_winner = "draw"
        max_pair_num = 0
        player1_count_map = self.player1_hand.card_num_count_map
        player2_count_map = self.player2_hand.card_num_count_map

        for card_num in self.CARD_LEVEL_ARR:
            if (
                player1_count_map[card_num] > player2_count_map[card_num]
                and player1_count_map[card_num] > max_pair_num
            ):
                match_winner = "player1"
                max_pair_num = player1_count_map[card_num]

            elif (
                player1_count_map[card_num] < player2_count_map[card_num]
                and player2_count_map[card_num] > max_pair_num
            ):
                match_winner = "player2"
                max_pair_num = player2_count_map[card_num]

        return match_winner


def winnerPairOfCards(player1: list[str], player2: list[str]) -> str:
    player1_hand = HandHelper.convert_from_card_str_arr(player1)
    player2_hand = HandHelper.convert_from_card_str_arr(player2)
    pair_of_cards = PairOfCards(player1_hand, player2_hand)

    return pair_of_cards.get_winner()


print(winnerPairOfCards(["♣4", "♥7", "♥7", "♠Q", "♣J"], ["♥7", "♥7", "♣K", "♠Q", "♦2"]))
