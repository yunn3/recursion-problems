def primeArray(n: list) -> list:

    result = []

    for num in range(1, n + 1):
        if isPrimeNumber(num):
            result.append(num)

    return result


def isPrimeNumber(num: int) -> bool:

    if num == 2:
        return True

    elif num % 2 == 0:
        return False

    elif num < 2:
        return False

    else:
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False

        return True
