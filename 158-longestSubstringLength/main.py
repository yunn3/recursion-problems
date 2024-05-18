def longestSubstringLength(password: str) -> int:
    char_index_map = {}
    max_length = 0
    start = 0

    for end, char in enumerate(password):
        if char in char_index_map:
            start = max(start, char_index_map[char] + 1)
        char_index_map[char] = end
        length = end - start + 1
        max_length = max(max_length, length)

    return max_length


print(longestSubstringLength("inciduntilloetassumendaet"))
