from collections import Counter

# firstNonRepeating("aabbcdddeffg") --> 4
# firstNonRepeating("abcdabcdf") --> 8
# firstNonRepeating("abcddaebcdf") --> 6


def firstNonRepeating(s: str) -> int:
    counter_map = Counter(s)

    for index in range(len(s)):
        if counter_map[s[index]] == 1:
            return index
    return -1
