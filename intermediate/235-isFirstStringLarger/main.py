def isFirstStringLarger(s1: str, s2: str) -> bool:

    first_ascii_sum = calcSumOfAscii(s1.lower())
    second_ascii_sum = calcSumOfAscii(s2.lower())

    return first_ascii_sum > second_ascii_sum


def calcSumOfAscii(string: str) -> int:

    total = 0

    for character in string:
        total += ord(character)

    return total
