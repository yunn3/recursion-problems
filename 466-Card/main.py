class Card:

    def __init__(self, suit: str, value: str, intValue: str) -> None:

        self.suit = suit
        self.value = value
        self.intValue = intValue


def printCardArray(cards: list) -> None:
    for card in cards:
        print(card.suit + card.value + "(" + card.intValue + ")")


cards = []
cards.append(Card("♣", "A", "1"))
cards.append(Card("♦", "K", "13"))
cards.append(Card("♥", "Q", "12"))
cards.append(Card("♠", "J", "11"))

printCardArray(cards)
