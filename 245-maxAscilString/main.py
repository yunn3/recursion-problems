def maxAscilString(stringList: list[str]) -> int:
    ascii_totals = []
    total = 0
    for string in stringList:
        for character in string:
            total += ord(character)
        ascii_totals.append(total)
        total = 0
    return ascii_totals.index(max(ascii_totals))
