def shuffledPositions(arr: list[int], shuffledArr: list[int]) -> list[int]:
    shuffled_dict = {number: index for index, number in enumerate(shuffledArr)}

    return [shuffled_dict[before_num] for before_num in arr]


print(
    shuffledPositions(
        [1350, 181, 1714, 375, 1331, 943, 735], [1714, 1331, 735, 375, 1350, 181, 943]
    ),
)
