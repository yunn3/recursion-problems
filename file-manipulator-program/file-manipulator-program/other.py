import os
import re

# import sys

args = ["other.py", "copy", "memo.txt", "copy.txt"]


def main():
    if validation(args):
        Executer.execute_command(args[1:])


def validation(args: list[str]) -> bool:
    if args[0] == "reverse" or args[0] == "copy":
        return os.path.exists(args[1]) and not os.path.isdir(args[2])

    elif args[0] == "duplicate":
        return os.path.exists(args[1]) and int(args[2]) > 0

    elif args[0] == "replace":
        return (
            os.path.exists(args[0])
            and isinstance(args[1], str)
            and isinstance(args[2], str)
        )

    return False


class Validator:
    POS_INT_REGEX = re.compile(r"^\d+$")

    @staticmethod
    def is_exists_file(arg: str) -> bool:
        os.path.isfile(args)

    @staticmethod
    def is_dir(arg: str) -> bool:
        return os.path.isdir(arg)

    @staticmethod
    def is_pos_int(arg: str) -> bool:
        return bool(Validator.POS_INT_REGEX.match(arg))


class Commands:
    @staticmethod
    def reverse(args: list[str]) -> None:
        if not Commands.is_valid_reverse_args(args):
            return

        with open(args[0]) as file:
            data = file.read()
            new_string = ""
        for word in reversed(data):
            new_string += word

        with open(args[1], "w") as file:
            file.write(new_string)

    @staticmethod
    def is_valid_reverse_args(args: list[str]) -> bool:
        return (
            len(args) == 2
            and Validator.is_exists(args[0])
            and Validator.is_exists_file(args[0])
            and not Validator.is_dir(args[1])
        )

    @staticmethod
    def copy(args: list[str]) -> None:
        with open(args[0]) as file:
            data = file.read()

        with open(args[1], "w") as file:
            file.write(data)

    @staticmethod
    def is_valid_copy_args(args: list[str]) -> bool:
        return (
            len(args) == 2
            and Validator.is_exists(args[0])
            and Validator.is_exists_file(args[0])
            and not Validator.is_dir(args[1])
        )

    @staticmethod
    def duplicate(args: list[str]) -> None:
        if Commands.is_valid_copy_args(args):
            return

        with open(args[0]) as file:
            data = file.read()
        for _ in range(int(args[1])):
            with open(args[0], "a") as file:
                file.write(data)

    @staticmethod
    def is_valid_duplicate_args(arg: list[str]) -> bool:
        return (
            len(args) == 2
            and Validator.is_exists_file(args[0])
            and Validator.is_pos_int(args[1])
        )

    @staticmethod
    def replace(args: list[str]) -> None:
        if Commands.is_valid_replace_arg(args):
            return

        with open(args[0]) as file:
            data = file.read()

        with open(args[0], "w") as file:
            file.write(data.replace(args[2], args[3]))

    @staticmethod
    def is_valid_replace_arg(args: list[str]) -> bool:
        return len(args) == 1 and Validator.is_exists_file(args[0])


class Executer:
    def __init__(self) -> None:

        self.commands = Commands

    def execute_command(self, args: list[str]) -> None:
        if args[1] not in self.commands:
            return

        self.commands[args[0]](args[2:])


if __name__ == "__main__":
    main()
