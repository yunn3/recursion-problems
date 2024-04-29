def isMountain(height: list[int]) -> bool:
    top_index = 0
    bottom_index = 0
    is_ascending = True
    height_length = len(height)

    if height_length <= 2:
        return False

    for index in range(1, height_length):

        if is_ascending and height[index] < height[index - 1]:
            top_index = index - 1
            is_ascending = False
            if index == height_length - 1:
                bottom_index = index

        elif is_ascending and height[index] == height[index - 1]:
            top_index = index - 1
            bottom_index = top_index
            break

        elif is_ascending and index == height_length - 1:
            top_index = index
            break

        elif not is_ascending and height[index] >= height[index - 1]:
            bottom_index = index - 1
            break

        elif not is_ascending and index == height_length - 1:
            bottom_index = index
            break

    return (
        top_index < height_length - 1
        and bottom_index == height_length - 1
        and top_index != 0
    )


print(isMountain([1, 2, 3, 2]))
