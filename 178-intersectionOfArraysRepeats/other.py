from collections import defaultdict


def intersectionOfArraysRepeats(int_list_1: list, int_list_2: list) -> list:
    item_count_map = defaultdict(int)
    for item in int_list_1:
        item_count_map[item] += 1

    def _is_there_left(_item: int) -> bool:
        result = item_count_map[_item] > 0
        if result:
            item_count_map[_item] -= 1
        return result

    return sorted(item for item in int_list_2 if _is_there_left(item))
