def longestPalindromeLength(string):
    length = 0
    hash_map = {}

    for char in string:
        if hash_map.get(char) is None:
            hash_map[char] = 1

        else:
            length += 2
            del hash_map[char]

    return length + 1 if hash_map else length
