def sumOfOddElement(arr: list) -> int:

    total = 0

    for num in arr:
        if isOddNumber(num):
            total += num

    return total


def isOddNumber(num: int) -> bool:
    return num % 2 != 0
