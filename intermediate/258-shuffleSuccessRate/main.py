from math import floor


def shuffleSuccessRate(arr: list[int], shuffledArr: list[int]) -> int:
    change_count = 0

    for before_index in range(len(arr)):
        if arr[before_index] != shuffledArr[before_index]:
            change_count += 1

    return floor(change_count / len(arr) * 100)


print(shuffleSuccessRate([0, 1, 2, 3, 4, 5], [1, 2, 0, 3, 4, 5]))
