def hasSameStructure(inputChar, words):
    word_hash_map = {}
    char_hash_map = {}
    word_list = words.split()
    length_word_list = len(word_list)

    if length_word_list != len(inputChar):
        return False

    for index in range(length_word_list):
        word = word_list[index]
        char = inputChar[index]

        if word not in word_hash_map and char not in char_hash_map:
            word_hash_map[word] = char
            char_hash_map[char] = word

        elif word_hash_map.get(word) != char:
            return False

    return True


print(hasSameStructure("tut", "hot mild mild"))
