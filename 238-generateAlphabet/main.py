def generateAlphabet(firstAlphabet: str, secondAlphabet: str) -> list:

    result = []
    lower_alphabets = sorted([ord(firstAlphabet.lower()), ord(secondAlphabet.lower())])
    for ascii_num in range((lower_alphabets[0]), (lower_alphabets[1]) + 1):
        result.append(chr(ascii_num))

    return result
