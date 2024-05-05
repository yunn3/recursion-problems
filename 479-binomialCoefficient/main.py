def binomialCoefficient(n, k):
    cache = [[0] * (k + 1) for _ in range(n + 1)]
    cache[0][0] = 1

    for row in range(1, n + 1):  # 行の探索のため
        for column in range(k + 1):  # 列の探索のため
            if column == 0:
                cache[row][column] = 1

            elif row == column:
                cache[row][column] = 1
                break

            else:
                cache[row][column] = cache[row - 1][column - 1] + cache[row - 1][column]

    return cache[n][k]
