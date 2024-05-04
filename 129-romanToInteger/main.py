def romanToInteger(romanNumber: str) -> int:
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    total = 0
    length = len(romanNumber)

    for index in range(length - 1):

        if roman_dict[romanNumber[index]] >= roman_dict[romanNumber[index + 1]]:
            total += roman_dict[romanNumber[index]]
        else:
            total -= roman_dict[romanNumber[index]]

    return total + roman_dict[romanNumber[-1]]


print(romanToInteger("XCVIII"))
