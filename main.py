def fibonacciNumberStack(n, arrayOutput):
    # 多次元配列の中に入れるための outputStack という配列
    outputStack = []

    # ベースケース
    if n == 0:
        outputStack.append(0)
        arrayOutput.append(outputStack)
        return 0

    # ベースケース
    elif n == 1:
        outputStack.append(1)
        arrayOutput.append(outputStack)
        return 1

    answer1 = fibonacciNumberStack(n - 1, outputStack)
    answer2 = fibonacciNumberStack(n - 2, outputStack)

    outputStack.append(answer1 + answer2)
    arrayOutput.append(outputStack)

    return answer1 + answer2


# 多次元配列を受け取り、平坦化された 1 次元配列を返します
def flatten(multiarray):
    arr1d = []
    for value in multiarray:
        if isinstance(value, list):
            arr1d += flatten(value)
        else:
            arr1d.append(value)
    return arr1d


callStack = []
print(fibonacciNumberStack(5, callStack))
print(callStack)

# 多次元配列を平坦化して 1 次元配列にします
print(flatten(callStack))


def ex(a) -> list[str]:
    return
