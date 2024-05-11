def shuffledPositions(arr: list[int], shuffledArr: list[int]) -> list[int]:
    after_dict = {number: index for index, number in enumerate(shuffledArr)}
    after_arr = []

    for before_num in arr:
        after_arr.append(after_dict[before_num])

    return after_arr


print(
    shuffledPositions(
        [1350, 181, 1714, 375, 1331, 943, 735], [1714, 1331, 735, 375, 1350, 181, 943]
    ),
)
