def winnerBlackjack(playerCards: list, houseCards: list) -> bool:

    burst = 22
    player_point = calcSumofCardsNum(playerCards)
    house_point = calcSumofCardsNum(houseCards)

    if player_point > 21:
        return False
    elif house_point < burst and house_point >= player_point:
        return False
    return True


def calcSumofCardsNum(cards: list) -> int:

    total = 0
    except_mark = [card[1:] for card in cards]

    card_value = {
        "A": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
    }

    for card in except_mark:
        total += card_value[card]

    return total


# 25,33
winnerBlackjack(["♥7", "♦10", "♦8"], ["♥Q", "♥7", "♦2", "♣Q"])
