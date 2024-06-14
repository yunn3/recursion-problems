from collections import Counter


def firstRepeatingNumber(nums: list[int]) -> int:
    counter_dict = Counter(nums)
    max_value = max(counter_dict.items(), key=lambda x: x[1])
    if max_value[1] < 2:
        return -1
    return max_value[0]


print(firstRepeatingNumber([2, 12, 5, 10, 9, 8]))
print(firstRepeatingNumber([1, 5, 3, 4, 3, 1, 6]))
print(firstRepeatingNumber([11, 45, 32, 75, 88, 15, 15]))
