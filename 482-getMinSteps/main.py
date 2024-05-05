def getMinSteps(n):
    cache = [n + 1] * (n + 1)
    cache[1] = 0

    for num in range(2, n + 1):
        cache[num] = 1 + cache[num - 1]
        if num % 2 == 0:
            cache[num] = min(cache[num], 1 + cache[num // 2])

        if num % 3 == 0:
            cache[num] = min(cache[num], 1 + cache[num // 3])

    return cache[n]
