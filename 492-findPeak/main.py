def findPeak(arr: list[int]) -> int:
    return find_peak_helper(arr, 0, len(arr) - 1)


def find_peak_helper(arr, start, end):
    mid = (start + end) // 2

    if (
        mid == 0
        or arr[mid] >= arr[mid - 1]
        and mid == len(arr) - 1
        or arr[mid] >= arr[mid + 1]
    ):
        return arr[mid]

    elif mid > 0 and arr[mid] < arr[mid - 1]:
        return find_peak_helper(arr, start, mid - 1)

    else:
        return find_peak_helper(arr, mid + 1, end)


print(findPeak([2, 4, 5, 12, 12, 7, 8, 14]))
