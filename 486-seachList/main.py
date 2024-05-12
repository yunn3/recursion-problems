def seachList(numList: list[int], value: int) -> int:
    """
    numList = [3,10,23...3,4]
    num_dict = {
        3: 0,
        10:1,
        23:3,
        ...
    }
    """

    search_dict = {}
    for index, num in enumerate(numList):
        search_dict.setdefault(num, index)

    return search_dict[value] if search_dict.get(value) is not None else -1


print(seachList([3, 10, 23, 3, 4, 50, 2, 3, 4, 18, 6, 1, -2], 3))
