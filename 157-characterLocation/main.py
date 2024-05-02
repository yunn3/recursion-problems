def characterLocation(commands: list[str]) -> list:
    cordinates = [0, 0]

    n = {"direction": 1, "magnitude": 1}
    e = {"direction": 0, "magnitude": 1}
    s = {"direction": 1, "magnitude": -1}
    w = {"direction": 0, "magnitude": -1}

    commands_list = {"N": n, "E": e, "S": s, "W": w}

    for command in commands:
        if command in commands_list:
            cordinate = commands_list[command]
            cordinates[cordinate["direction"]] = (
                cordinates[cordinate["direction"]] + cordinate["magnitude"]
            )

    return cordinates


print(characterLocation("NNANN"))
