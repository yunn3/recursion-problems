def addEveryOtherElement(intArr: list) -> int:

    total = 0

    for index in range(0, len(intArr), 2):
        total += intArr[index]
    return total
