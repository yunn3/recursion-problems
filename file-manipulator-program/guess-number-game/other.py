import math
import sys
from random import randint


def main() -> None:
    param = GameParameter()
    game = Game(param)
    game.guess_number()


class GameParameter:
    def __init__(self) -> None:
        self.min_number = int(input("Enter min number: "))
        self.max_number = int(input("Enter max number: "))

        if not self.is_collect_input():
            sys.exit()

        self.ans = self.generate_ans()
        self.max_timport sys
from random import randint
import math


def main() -> None:
    param = GameParameter()
    game = Game(param)
    game.guess_number()


class GameParameter:
    def __init__(self) -> None:
        self.min_number = int(input("Enter min number: "))
        self.max_number = int(input("Enter max number: "))

        if not self.is_collect_input():
            sys.exit()

        self.ans = self.generate_ans()
        self.max_try_count = self.generate_max_try_count()

    def is_collect_input(self) -> bool:
        return self.min_number <= self.max_number

    def generate_ans(self) -> int:
        return randint(self.min_number, self.max_number)

    def generate_max_try_count(self) -> int:
        return math.ceil((self.max_number - self.min_number + 1) / 2)


class Game:
    def __init__(self, param: GameParameter) -> None:
        self.param = param

    def guess_number(self) -> None:
        quantity = self.param.max_try_count
        while quantity > 0:
            user_ans = int(
                input(
                    f"Enter number you guess. You can try {quantity} times remaining: ",
                ),
            )
            quantity -= 1

            if user_ans > self.param.ans:
                print("Incorrect. This number is greater than the target.")

            elif user_ans < self.param.ans:
                print("Incorrect. This number is less than the target.")
            else:
                print("Congrat! you finaly found the number")
                return

        print("Unfortunatly, you didn't find the number...")


if __name__ == "__main__":
    main()ry_count = self.generate_max_try_count()

    def is_collect_input(self) -> bool:
        return self.min_number <= self.max_number

    def generate_ans(self) -> int:
        return randint(self.min_number, self.max_number)

    def generate_max_try_count(self) -> int:
        return math.ceil((self.max_number - self.min_number + 1) / 2)


class Game:
    def __init__(self, param: GameParameter) -> None:
        self.param = param

    def guess_number(self) -> None:
        quantity = self.param.max_try_count
        while quantity > 0:
            user_ans = int(
                input(
                    f"Enter number you guess. You can try {quantity} times remaining: ",
                ),
            )
            quantity -= 1

            if user_ans > self.param.ans:
                print("Incorrect. This number is greater than the target.")

            elif user_ans < self.param.ans:
                print("Incorrect. This number is less than the target.")
            else:
                print("Congrat! you finaly found the number")
                return

        print("Unfortunatly, you didn't find the number...")


if __name__ == "__main__":
    main()
