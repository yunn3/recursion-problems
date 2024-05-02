def characterLocation(commands: list[str]) -> list:
    cordinates = [0, 0]

    commands_list = {
        "N": {"direction": 1, "magnitude": 1},
        "E": {"direction": 0, "magnitude": 1},
        "S": {"direction": 1, "magnitude": -1},
        "W": {"direction": 0, "magnitude": -1},
    }

    for command in commands:
        if command in commands_list:
            cordinates[commands_list[command]["direction"]] = (
                cordinates[commands_list[command]["direction"]]
                + commands_list[command]["magnitude"]
            )

    return cordinates


print(characterLocation("NNANN"))
