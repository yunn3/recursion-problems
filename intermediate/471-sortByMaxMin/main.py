def sortByMaxMin(arr: list) -> list:

    middle_index = len(arr) // 2
    sorted_arr = sorted(arr)
    first_half = sorted_arr[:middle_index]
    second_half = sorted_arr[middle_index:]

    insert_position = 0

    for num in reversed(second_half):
        first_half.insert(insert_position, num)
        insert_position += 2

    return first_half
