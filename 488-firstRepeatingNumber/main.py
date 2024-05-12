def firstRepeatingNumber(nums: list[int]) -> int:
    min_index = -1
    hash_map = {}

    for index in range(len(nums)):
        if hash_map.get(nums[index]) is None:
            hash_map[nums[index]] = index

        elif min_index == -1:
            min_index = hash_map[nums[index]]

        else:
            min_index = min(hash_map[nums[index]], min_index)

    return nums[min_index] if min_index != -1 else min_index


print(firstRepeatingNumber([2, 12, 5, 10, 9, 8]))
print(firstRepeatingNumber([1, 5, 3, 4, 3, 1, 6, 6]))
print(firstRepeatingNumber([11, 45, 32, 75, 88, 15, 15]))
