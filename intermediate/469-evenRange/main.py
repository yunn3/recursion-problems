def evenRange(a, b):

    result = []

    for num in range(a, b + 1):
        if num % 2 == 0:
            result.append(num)

    return result
