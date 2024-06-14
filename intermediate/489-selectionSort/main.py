def selectionSort(arr: list[int]) -> list[int]:

    length = len(arr)
    for i in range(length):
        min_index = i

        for j in range(i + 1, length):
            if arr[j] < arr[min_index]:
                min_index = j

        tmp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = tmp

    return arr


print(selectionSort([11, 45, 32, 75, 88, 15, 15]))
