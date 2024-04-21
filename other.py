def sortByMaxMin(arr: list) -> list:
    arr.sort(reverse=True)
    for i in range(0, len(arr), 2):
        arr.insert(i + 1, arr.pop())
    return arr
