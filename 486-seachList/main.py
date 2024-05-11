def seachList(numList: list[int], value: int) -> int:
    search_dict = {number: index for index, number in enumerate(numList)}
    output = search_dict.get(value)
    if output is None:
        return -1

    return output


print(seachList([3, 10, 23, 3, 4, 50, 2, 3, 4, 18, 6, 1, -2], 23))
