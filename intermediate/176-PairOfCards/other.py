from collections import defaultdict


class Card:
    SIGN_PATTERNS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    SUIT_PATTERNS = ("♥", "♠", "♦", "♣")

    def __init__(
        self,
        suit: str,
        sign: str,
    ) -> None:
        if suit not in self.SUIT_PATTERNS:
            raise ValueError
        if sign not in self.SIGN_PATTERNS:
            raise ValueError

        self._suit = suit
        self._sign = sign

    @property
    def sign(self) -> str:
        return self._sign


class PlayerCards:
    MAX_CARDS = 20  # 手札は最大20枚まで

    def __init__(self) -> None:
        self._cards = []
        self._sign_count_map = defaultdict(int)  # サイン毎の枚数のハッシュマップ

    def get_count(self, sign: str):
        return self._sign_count_map[sign]

    def add(self, card: Card) -> None:
        if len(self._cards) > self.MAX_CARDS:
            return
        self._cards.append(card)
        self._sign_count_map[card.sign] += 1

    def __len__(self) -> int:
        return len(self._cards)


class Player:
    def __init__(self, name: str) -> None:
        self._name = name
        self._hand = PlayerCards()

    @property
    def name(self) -> str:
        return self._name

    @property
    def hand(self) -> PlayerCards:
        return self._hand

    def set_player_cards_from_card_str_array(self, card_str_array: list) -> None:
        for card_str in card_str_array:
            card = Card(suit=card_str[0], sign=card_str[1:])
            self.hand.add(card)


class PairOfCards:
    # カードの序列（強さ）
    CARD_SIGN_HIERARCHY = (
        "A",
        "K",
        "Q",
        "J",
        "10",
        "9",
        "8",
        "7",
        "6",
        "5",
        "4",
        "3",
        "2",
    )

    def __init__(self, player1: Player, player2: Player) -> None:
        # 手札の枚数が異なる場合はゲームを続行できない
        if len(player1.hand) != len(player2.hand):
            raise ValueError

        self._players = [player1, player2]

    def get_result(self) -> str:
        index = self.get_winner_index()
        if index < 0:
            return "draw"
        return self._players[index].name

    def get_winner_index(self) -> int:
        winner_index = -1
        max_count = 0  # すべてのプレイヤーにおける最大の枚数
        # カードのランク順に枚数を判定する
        for sign in self.CARD_SIGN_HIERARCHY:
            p1_count = self._players[0].hand.get_count(sign)
            p2_count = self._players[1].hand.get_count(sign)
            # 同じ枚数である時は何もしない
            # 枚数が勝っており、最大枚数も超えていれば勝者と最大枚数を更新する
            if p1_count > p2_count and p1_count > max_count:
                winner_index = 0
                max_count = p1_count
            elif p2_count > p1_count and p2_count > max_count:
                winner_index = 1
                max_count = p2_count

        return winner_index


def winnerPairOfCards(player1: list, player2: list) -> str:
    p1 = Player("player1")
    p2 = Player("player2")
    p1.set_player_cards_from_card_str_array(player1)
    p2.set_player_cards_from_card_str_array(player2)

    pair_of_cards_game = PairOfCards(p1, p2)

    return pair_of_cards_game.get_result()


print(
    winnerPairOfCards(["♣4", "♥7", "♥7", "♠Q", "♣J"], ["♥10", "♥6", "♣K", "♠Q", "♦2"])
)
