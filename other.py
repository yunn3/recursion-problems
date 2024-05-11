from math import ceil


def primesUpToNCount(n: int) -> int:
    if n <= 2:
        return 0

    half_num = ceil(n**0, 5)
    cache = [True for _ in range(half_num)]
    cache[0] = cache[1] = False

    for number in range(3, half_num):
        if cache[number]:
            decrease_num = number
            while decrease_num >= 2:
                if number % decrease_num == 0:
                    for num in range(number, half_num, number):
                        cache[num] = False
