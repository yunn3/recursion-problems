from math import ceil


def primesUpToNCount(n: int) -> int:
    if n <= 2:
        return 0

    composite_number_count = 2
    cache = [True for _ in range(n)]
    cache[0] = cache[1] = False

    for number in range(2, ceil(n**0.5)):
        if cache[number]:
            for index in range(number * 2, n, number):
                if cache[index]:
                    cache[index] = False
                    composite_number_count += 1

    return n - composite_number_count


primesUpToNCount(13)
