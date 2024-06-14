def addEveryOtherElement(intArr: list) -> int:
    total = 0
    for value in intArr[::2]:
        total += value
    return total
