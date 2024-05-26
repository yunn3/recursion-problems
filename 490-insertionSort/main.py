def insertionSort(arr: list[int]) -> list[int]:
    length = len(arr)

    for i in range(length):
        for j in reversed(range(i)):
            if arr[j + 1] < arr[j]:
                tmp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = tmp
            else:
                break

    return arr


print(insertionSort([11, 45, 32, 75, 88, 15, 15]))
