def rotateByTimes(ids: list[int], n: int) -> list[int]:
    new_rooms = []
    list_length = len(ids)

    for current_index in range(list_length):
        new_rooms.append(
            ids[(list_length - n % list_length + current_index) % list_length],
        )
    return new_rooms


print(rotateByTimes(([4, 23, 104, 435, 5002, 3], 26)))
