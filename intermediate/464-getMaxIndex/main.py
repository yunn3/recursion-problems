def getMaxIndex(arr: list) -> int:

    max_index = 0

    for index in range(len(arr)):
        if arr[index] >= arr[max_index]:
            max_index = index
    return max_index
