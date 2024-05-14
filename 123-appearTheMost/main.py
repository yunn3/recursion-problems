def appearTheMost(levels: list[int]) -> int:
    hashmap = {}

    for level in levels:
        if level in hashmap:
            hashmap[level] += 1

        else:
            hashmap[level] = 1

    max_count = max(hashmap.values())
    return sorted(level for level, count in hashmap.items() if count == max_count)


print(appearTheMost([1, 22, 48, 500, 3000, 10000, 30, 30, 30]))
