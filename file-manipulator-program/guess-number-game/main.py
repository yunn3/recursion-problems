from random import randint


class Number:
    def __init__(self) -> None:
        self.min_number = input("Enter min number")
        self.max_number = input("Enter max number")

    def is_collect_input(self) -> bool:
        return self.min_number <= self.max_number

    def generate_ans(self) -> int | str:
        if self.is_collect_input():
            return randint(self.min_number, self.max_number)
        return "Invaild input."

class Game:
    def __init__(self, min_number, max_number) -> None:
        self.ans = Number.generate_ans()
        self.min_number = Number()
        self.max_number = Number()

    def guess_number(self) -> str:
        quantity = (self.max_number - self.min_number + 1) // 2

        while quantity > 0:
            user_ans = input(
                f"Enter number you guess. You can try {quantity} times remaining",
            )

            quantity - 1

            if user_ans > self.ans:
                print("Incorrect. The number is greater than the number")

            elif user_ans < self.ans:
                print("Incorrect. The number is less than the number")

            return "Congrat! you finaly found the number"

        return "Unfortunatly, you didn't find the number..."

user_input = 