import os

# import re
import sys

args = sys.argv


def main():
    if varidation(args):
        Executer.execute_command(args)


def varidation(args: list[str]) -> bool:
    if args[1] == "reverse" or args[1] == "copy":
        return os.path.isdir(args[2]) and os.path.isdir(args[3])

    elif args[1] == "duplicate":
        return os.path.isdir(args[2]) and args[3] > 0

    elif args[1] == "replace":
        return (
            os.path.isdir(args[1])
            and isinstance(args[2], str)
            and isinstance(args[3], str)
        )

    return False


class Executer:
    def execute_command(args: list[str]) -> None:
        COMMANDS_LIST = {
            "reverse": Commands.reverse(args),
            "copy": Commands.copy(args),
            "duplicate": Commands.duplicate(args),
            "replace": Commands.replace(args),
        }

        COMMANDS_LIST[args[1]]


class Commands:
    def reverse(args: list[str]) -> None:
        with open(args[2]) as file:
            data = file.read()
            new_string = ""
        for word in reversed(data):
            new_string += word

        with open(args[3], "w") as file:
            file.write(new_string)

    def copy(args: list[str]) -> None:
        with open(args[2]) as file:
            data = file.read()

        with open(args[3], "w") as file:
            file.write(data)

    def duplicate(args: list[str]) -> None:
        with open(args[2]) as file:
            data = file.read()
        for _ in range(args[3]):
            with open(args[2], "a") as file:
                file.write(data)

    def replace(args: list[str]) -> None:
        with open(args[2]) as file:
            data = file.read()

        with open(args[2], "w") as file:
            file.write(data.replace(args[3], args[4]))


if __name__ == "__main__":
    main()
