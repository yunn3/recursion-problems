from collections import defaultdict


def findPairs(numbers: list[int]) -> list[int]:
    num_count_map = defaultdict(int)

    for num in numbers:
        num_count_map[num] += 1

    return sorted([key for key in set(numbers) if num_count_map[key] == 2])
