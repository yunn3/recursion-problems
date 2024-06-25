import os
import re
import sys

args = sys.argv


def main():
    if varidation(args):
        Commands.execute()


def varidation(args: list[str]) -> bool:
    if args[1] == "reverse" or args[1] == "copy":
        return os.path.exists(args[2]) and os.path.exists(args[3])

    elif args[1] == "duplicate":
        return os.path.exists(args[2]) and args[3] > 0

    elif args[1] == "replace":
        return (
            os.path.exists(args[1])
            and isinstance(args[2], str)
            and isinstance(args[3], str)
        )

    return False


class Commands:
    def execute(args: list[str]) -> str:
        return args[1]

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
