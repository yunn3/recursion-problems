def charInBagOfWordsCount(bagOfWords: list, keyCharacter: str) -> int:

    character_count = 0

    for word in bagOfWords:
        for character in word:
            if keyCharacter == character:
                character_count += 1

    return character_count
