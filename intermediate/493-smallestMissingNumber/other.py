def smallestMissingNumber(arr: list) -> int:
    def _helper(
        start: int,
        end: int,
    ) -> int:
        if start == end:
            # If the index and the element are not equal, the missing number is the index
            # If the index and the element are equal, the missing number is the next index
            return start if arr[start] != start else start + 1
        mid = (start + end) // 2
        # If the index and the element are equal, the missing number is in the left subarray
        # If they are not equal, the missing number is in the right subarray
        return _helper(start, mid) if arr[mid] != mid else _helper(mid + 1, end)

    return _helper(0, len(arr) - 1)
