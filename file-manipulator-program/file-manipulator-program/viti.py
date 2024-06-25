import os
import re
from collections.abc import Callable
import sys


def main():
    commands = Commands()
    Executer(commands).execute_command(sys.argv[1:])


class Validator:
    POS_INT_REGEX = re.compile(r"^\d+$")

    @staticmethod
    def is_exists_file(arg: str) -> bool:
        return os.path.isfile(arg)

    @staticmethod
    def is_dir(arg: str) -> bool:
        return os.path.isdir(arg)

    @staticmethod
    def is_pos_int(arg: str) -> bool:
        return bool(Validator.POS_INT_REGEX.match(arg))


class Commands:
    def __init__(self) -> None:
        self.commands_dict = {
            "copy": self.copy,
            "reverse": self.reverse,
            "duplicate": self.duplicate,
            "replace": self.replace,
        }

    def get(self, command_str: str) -> Callable[[list[str]], None] | None:
        return self.commands_dict.get(command_str)

    def reverse(self, args: list[str]) -> None:
        if not self.is_valid_reverse_args(args):
            return

        with open(args[0]) as file:
            data = file.read()
            new_string = ""
        for word in reversed(data):
            new_string += word

        with open(args[1], "w") as file:
            file.write(new_string)

    def is_valid_reverse_args(self, args: list[str]) -> bool:
        return (
            len(args) == 2
            and Validator.is_exists_file(args[0])
            and not Validator.is_dir(args[1])
        )

    def copy(self, args: list[str]) -> None:
        if not self.is_valid_copy_args(args):
            return
        with open(args[0]) as file:
            data = file.read()

        with open(args[1], "w") as file:
            file.write(data)

    def is_valid_copy_args(self, args: list[str]) -> bool:
        return (
            len(args) == 2
            and Validator.is_exists_file(args[0])
            and not Validator.is_dir(args[1])
        )

    def duplicate(self, args: list[str]) -> None:
        if not self.is_valid_duplicate_args(args):
            return

        with open(args[0]) as file:
            data = file.read()
        for _ in range(int(args[1])):
            with open(args[0], "a") as file:
                file.write(data)

    def is_valid_duplicate_args(self, args: list[str]) -> bool:
        return (
            len(args) == 2
            and Validator.is_exists_file(args[0])
            and Validator.is_pos_int(args[1])
        )

    def replace(self, args: list[str]) -> None:
        if not self.is_valid_replace_args(args):
            return
        with open(args[0]) as file:
            data = file.read()

        with open(args[0], "w") as file:
            file.write(data.replace(args[1], args[2]))

    def is_valid_replace_args(self, args: list[str]) -> bool:
        return len(args) == 1 and Validator.is_exists_file(args[0])


class Executer:
    def __init__(self, commands: Commands) -> None:
        # commands: dict{str: function}
        self.commands = commands

    def execute_command(self, args: list[str]) -> None:
        # コマンドの取得
        command = self.commands.get(args[0])
        # コマンドの存在確認
        if not command:
            return

        # コマンドの実行
        command(args[1:])


if __name__ == "__main__":
    main()
