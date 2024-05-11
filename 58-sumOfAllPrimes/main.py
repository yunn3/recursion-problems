import math


def sumOfAllPrimes(n):
    total = 0
    cache = [True] * (n + 1)
    cache[0] = cache[1] = False

    for number in range(2, math.ceil(math.sqrt(n))):
        if not cache[number]:
            continue

        for multiple_number in range(number * 2, n + 1, number):
            cache[multiple_number] = False

    for index in range(len(cache)):
        if cache[index]:
            total += index

    return total


print(sumOfAllPrimes(16))
