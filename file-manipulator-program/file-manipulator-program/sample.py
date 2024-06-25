import re
import sys
import os


def main() -> None:
    FileManipulateCommands().execute()


class Validator:
    FILE_PATH_CHAR_BL = " !?@#$%^&*()\\<>{},\"';:"
    PATTERNS = {
        "pos_int": re.compile(r"^\d+$"),
    }

    @staticmethod
    def file_path(arg: str) -> str:
        char_set = set(char for char in arg)
        for bl_char in Validator.FILE_PATH_CHAR_BL:
            if bl_char in char_set:
                return ""
        return arg

    @staticmethod
    def pos_int(arg: str) -> int:
        if Validator.PATTERNS["pos_int"].match(arg):
            return int(arg)
        return 0


class CopyCommand:
    def __init__(self) -> None:
        pass

    def run(self, *args) -> None:
        kwargs = self._make_copy_args(*args)

        if not kwargs:
            print("Arguments are missing.")
            return

        self._copy_file(**kwargs)

    def _copy_file(self, **kwargs) -> None:
        with (
            open(kwargs["input_path"]) as input,
            open(kwargs["output_path"], "w") as output,
        ):
            for iline in input:
                output.write(iline)

    def _make_copy_args(self, *args) -> dict:
        if len(args) < 2:
            return {}
        return {
            "input_path": self._validate_input_path(args[0]),
            "output_path": self._validate_input_path(args[1]),
        }

    def _validate_input_path(self, arg: str) -> str:
        return Validator.file_path(arg)

    def _validate_output_path(self, arg: str) -> str:
        return Validator.file_path(arg)


class ReverseCommand:
    def __init__(self) -> None:
        pass

    def run(self, *args) -> None:
        kwargs = self._make_reverse_args(*args)

        if not kwargs:
            print("Arguments are missing.")
            return

        self._reverse_file_contents(**kwargs)

    def _reverse_file_contents(self, **kwargs) -> None:
        with (
            open(kwargs["input_path"]) as input,
            open(kwargs["output_path"], "w") as output,
        ):
            reversed_lines = []
            for iline in input:
                reversed_lines.append(iline[::-1])
            output.writelines(reversed_lines[::-1])

    def _make_reverse_args(self, *args) -> dict:
        if len(args) < 2:
            return {}
        return {
            "input_path": self._validate_input_path(args[0]),
            "output_path": self._validate_input_path(args[1]),
        }

    def _validate_input_path(self, arg: str) -> str:
        return Validator.file_path(arg)

    def _validate_output_path(self, arg: str) -> str:
        return Validator.file_path(arg)


class DuplicateContentsCommand:
    def __init__(self) -> None:
        pass

    def run(self, *args) -> None:
        kwargs = self._make_kwargs(*args)

        if not kwargs:
            print("Arguments are missing.")
            return

        self._duplicate_contnts(**kwargs)

    def _duplicate_contnts(self, **kwargs) -> None:
        input_path = kwargs["input_path"]
        output_path = self._gen_tmp_file_name(kwargs["input_path"])
        with (
            open(input_path, "r") as input,
            open(output_path, "w") as output,
        ):
            for _ in range(kwargs["times"]):
                for iline in input:
                    output.write(iline)
                input.seek(0)

        os.remove(kwargs["input_path"])
        os.rename(output_path, input_path)

    def _gen_tmp_file_name(self, inputpath: str) -> str:
        return f"{inputpath}.tmp"

    def _make_kwargs(self, *args) -> dict:
        if len(args) < 2:
            return {}
        return {
            "input_path": self._validate_input_path(args[0]),
            "times": self._validate_times(args[1]),
        }

    def _validate_input_path(self, arg: str) -> str:
        return Validator.file_path(arg)

    def _validate_times(self, arg: str) -> int:
        return Validator.pos_int(arg)


class ReplaceStringCommand:
    def __init__(self) -> None:
        pass

    def run(self, *args) -> None:
        kwargs = self._make_kwargs(*args)

        if not kwargs:
            print("Arguments are missing.")
            return

        self._replace_string(**kwargs)

    def _replace_string(self, **kwargs) -> None:
        input_path = kwargs["input_path"]
        output_path = self._gen_tmp_file_name(kwargs["input_path"])
        with (
            open(input_path, "r") as input,
            open(output_path, "w") as output,
        ):
            input_text = input.read()
            output.write(
                input_text.replace(
                    kwargs["old_str"],
                    kwargs["new_str"],
                ),
            )

        os.remove(kwargs["input_path"])
        os.rename(output_path, input_path)

    def _gen_tmp_file_name(self, inputpath: str) -> str:
        return f"{inputpath}.replace.tmp"

    def _make_kwargs(self, *args) -> dict:
        if len(args) < 3:
            return {}
        return {
            "input_path": self._validate_input_path(args[0]),
            "old_str": self._validate_old_str(args[1]),
            "new_str": self._validate_new_str(args[2]),
        }

    def _validate_input_path(self, arg: str) -> str:
        return Validator.file_path(arg)

    def _validate_new_str(self, arg: str) -> str:
        return arg

    def _validate_old_str(self, arg: str) -> str:
        return arg


class FileManipulateCommands:
    def __init__(self) -> None:
        self._commands = {
            "copy": CopyCommand().run,
            "reverse": ReverseCommand().run,
            "duplicate-contents": DuplicateContentsCommand().run,
            "replace-string": ReplaceStringCommand().run,
        }

    def execute(self) -> None:
        if len(sys.argv) < 1:
            return

        command_str = sys.argv[1]
        if command_str not in self._commands:
            print(f'"{command_str}" command does not exist.')
            return

        self._commands[command_str](*sys.argv[2:])


if __name__ == "__main__":
    main()
