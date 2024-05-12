def appearTheMost(levels: list[int]) -> int:
    hashmap = {}

    for level in levels:
        if level in hashmap:
            hashmap[level] += 1

        else:
            hashmap[level] = 1

    max_value = max(hashmap.values())
    return sorted(key for key, value in hashmap.items() if value == max_value)


print(appearTheMost([1, 22, 48, 500, 3000, 10000, 30, 30, 30]))
