from typing import List


def largestRectangle(h: List[int]) -> int:
    length = len(h)
    max_area = 0

    for i in range(length):
        min_height = h[i]
        for j in range(i, length):
            min_height = min(min_height, h[j])
            current_area = min_height * (j - i + 1)
            max_area = max(max_area, current_area)

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
