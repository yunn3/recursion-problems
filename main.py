def test(hoge) -> None:
    x = 0
    y = 0

    x += hoge
    y -= hoge
    print("==", "!=", "<=", ">=")

    return x + y


print(test(1))
