def missingItems(listA: list[int], listB: list[int]) -> list[int]:
    little_bro_map = {v: v for v in listB}

    # for item in listA:
    #     if item not in little_bro_map:
    #         missing_list.append(item)

    # return missing_list

    return [item for item in listA if item not in little_bro_map]
