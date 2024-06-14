from collections import defaultdict


def findPairs(numbers: list[int]) -> list[int]:
    num_count_map = defaultdict(int)

    for num in numbers:
        num_count_map[num] += 1

    return sorted(num for num, count in num_count_map.items() if count == 2)
