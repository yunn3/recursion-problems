def intersectionOfArraysRepeats(intList1: list[int], intList2: list[int]) -> list[int]:
    hash_map = {}
    same_num_list = []

    for i in intList1:
        if i not in hash_map:
            hash_map[i] = 1

        else:
            hash_map[i] += 1

    for j in sorted(intList2):
        if j in hash_map and hash_map[j] > 0:
            same_num_list.append(j)
            hash_map[j] -= 1

    return same_num_list


print(intersectionOfArraysRepeats([3, 2, 2, 2, 1, 10, 10], [3, 2, 10, 10, 10]))
