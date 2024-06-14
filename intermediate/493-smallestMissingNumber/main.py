def smallestMissingNumber(arr: list[int]) -> int:
    end = len(arr) - 1
    return smallest_missing_number_helper(arr, 0, end)


def smallest_missing_number_helper(arr: list[int], start: int, end: int) -> int:
    if start == end:
        return end + 1 if end == arr[end] else end

    mid = (start + end) // 2
    if mid != arr[mid]:
        return smallest_missing_number_helper(arr, start, mid - 1)

    else:
        return smallest_missing_number_helper(arr, mid + 1, end)


# print(smallestMissingNumber([0, 2, 3, 4, 6]))  # -> 1
# print(smallestMissingNumber([0, 1, 2, 3, 5]))  # -> 4
# print(smallestMissingNumber([0, 1, 2, 3, 4]))  # -> 5
