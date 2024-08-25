from collections import deque


def calc_area(
    stack: deque[int], h: list[int], current_index: int, max_area: int
) -> int:
    while stack and h[current_index] < h[stack[-1]]:
        top_index = stack.pop()
        height = h[top_index]
        width = current_index - stack[-1] - 1
        max_area = max(max_area, height * width)

    return max_area


def largestRectangle(h: list[int]) -> int:
    height_list = [0] + h + [0]
    stack = deque[int]()
    length = len(height_list)
    max_area = 0

    for current_index in range(length):
        max_area = calc_area(stack, height_list, current_index, max_area)
        stack.append(current_index)

    return max_area


print(largestRectangle([3, 2, 3]))  # --> 6
print(largestRectangle([1, 2, 5, 2, 3, 4]))  # --> 10
print(largestRectangle([1, 2, 3, 4, 5]))  # --> 9
print(largestRectangle([3, 4, 5, 8, 10, 2, 1, 3, 9]))  # --> 16
print(largestRectangle([1, 2, 1, 3, 5, 2, 3, 4]))  # --> 10
print(largestRectangle([11, 11, 10, 10, 10]))  # --> 50
print(
    largestRectangle([8979, 4570, 6436, 5083, 7780, 3269, 5400, 7579, 2324, 2116])
)  # --> 26152
