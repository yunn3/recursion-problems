def canMakeTargetVal(arr: list[int], target: int) -> bool:
    list_length = len(arr)

    for add_index in range(list_length):
        for target_index in range(add_index + 1, list_length):
            if arr[add_index] + arr[target_index] == target:
                return True

    return False
