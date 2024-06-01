def findPeak(arr: list) -> int:
    return find_peak_helper(arr, 0, len(arr) - 1)


def find_peak_helper(arr, start, end):
    if start == end:
        return arr[start]

    mid = (start + end) // 2

    # 左側へ再帰する余地があり、左のほうが大きい場合
    if mid > 0 and arr[mid] < arr[mid - 1]:
        # 左側へ再帰する
        return find_peak_helper(arr, start, mid - 1)

    # 右側へ再帰する余地があり、右のほうが大きい場合
    elif mid < len(arr) - 1 and arr[mid] < arr[mid + 1]:
        # 右側へ再帰する
        return find_peak_helper(arr, mid + 1, end)
    # (mid == 0 or arr[mid] >= arr[mid - 1])
    # and
    # (mid == len(arr) - 1 or arr[mid] >= arr[mid + 1])
    else:
        return arr[mid]


print(findPeak([2, 4, 5, 12, 12, 7, 8, 14]))
