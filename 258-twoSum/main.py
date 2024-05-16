from collections import defaultdict


def twoSum(intArr: list[int], sumInt: int) -> list:
    hash_map = defaultdict(int)
    length_intArr = len(intArr)
    for augend_index in range(length_intArr - 1):

        # hash_mapにaugend_indexの要素がなければ計算、
        # 重複計算を回避するためrangeの第一引数はaugend_index + 1
        if intArr[augend_index] not in hash_map:
            for addend_index in range(augend_index + 1, length_intArr):
                if intArr[augend_index] + intArr[addend_index] == sumInt:
                    return [augend_index, addend_index]

            hash_map[intArr[augend_index]] = augend_index

    return []


twoSum(
    [
        214,
        666,
        347,
        904,
        817,
        209,
        365,
        563,
        479,
        231,
        58,
        162,
        324,
        40,
        632,
        267,
        949,
        126,
        863,
        749,
        773,
        705,
        217,
        903,
    ],
    1766,
)
