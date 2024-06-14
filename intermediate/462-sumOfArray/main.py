def sumOfArray(arr: list[int]) -> int:
    return sum_of_array_helper(arr, 0, len(arr) - 1)


def sum_of_array_helper(arr: list[int], start: int, end: int) -> int:

    if start == end:
        return arr[start]

    mid = (start + end) // 2
    left_arr = sum_of_array_helper(arr, start, mid)
    right_arr = sum_of_array_helper(arr, mid + 1, end)

    return left_arr + right_arr


print(sumOfArray([2, 4, 6, 8, 10, 12]))
