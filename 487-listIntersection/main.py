from collections import defaultdict


def listIntersection(targetList: list[int], searchList: list[int]) -> list[int]:
    target_dict = defaultdict(bool)
    intersections = []
    """
    targetList = [3,4,5,10,2,20,4,5]
    target_dict = {3:True, 4:True, 5:True, 10:True...}
    """
    for target_number in targetList:
        target_dict[target_number] = True

    for search_number in sorted(set(searchList)):
        if target_dict[search_number]:
            intersections.append(search_number)

    return intersections


print(listIntersection([3, 4, 5, 10, 2, 20, 4, 5], [4, 20, 22, 2, 2, 2, 10, 1, 4]))
