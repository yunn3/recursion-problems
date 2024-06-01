def doubledArray(arr: list[int]) -> list[int]:
    return doubled_array_helper(arr, 0, len(arr) - 1)


def doubled_array_helper(arr: list[int], start: int, end: int) -> list[int]:
    if start == end:
        arr[start] *= 2

    else:
        mid = (start + end) // 2

        doubled_array_helper(arr, start, mid)
        doubled_array_helper(arr, mid + 1, end)

    return arr


doubledArray([1, 1, 2, 2, 3, 3])
