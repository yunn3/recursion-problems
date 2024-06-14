def twoSum(intArr: list[int], sumInt: int) -> list:

    length_intArr = len(intArr)
    hash_map = {v: length_intArr - 1 - i for i, v in enumerate(reversed(intArr))}

    for index, value in enumerate(intArr):
        diff = sumInt - value

        if diff in hash_map and hash_map[diff] != index:
            return (
                [index, hash_map[diff]]
                if hash_map[diff] > index
                else [hash_map[diff], index]
            )

    return []


print(
    twoSum(
        [
            1,
            2,
            3,
            3,
        ],
        6,
    ),
)
