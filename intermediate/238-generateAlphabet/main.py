def generateAlphabet(firstAlphabet: str, secondAlphabet: str) -> list:

    result = []
    lower_alphabets = [ord(firstAlphabet.lower()), ord(secondAlphabet.lower())]
    max_alphabet = max(lower_alphabets)
    min_alphabet = min(lower_alphabets)

    for ascii_num in range(min_alphabet, max_alphabet + 1):
        result.append(chr(ascii_num))

    return result


print(generateAlphabet("Z", "a"))
