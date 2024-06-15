import random
from enum import Enum


def main() -> None:
    guess_the_num = GuessTheNumberGame()
    guess_the_num.start()


class GamePhase(Enum):
    SETUP = 0
    GUESSING = 1
    GUESSED = 2
    FAILURE = 3
    EXIT = 4


class GuessTheNumberGame:
    def __init__(self) -> None:
        self._n = 0
        self._m = 0
        self._max_try_count = 0
        self._try_count = 0
        self._game_phase = GamePhase.SETUP

    def reset(self) -> None:
        self._game_phase = GamePhase.SETUP
        self.start()

    def start(self) -> None:
        while True:
            match self._game_phase:
                case GamePhase.SETUP:
                    self._setup()
                case GamePhase.GUESSING:
                    self._try_guessing()
                case GamePhase.GUESSED:
                    self._guessed()
                case GamePhase.FAILURE:
                    self._failure()
                case _:
                    return
            self._print_partition(20)

    def _print_partition(self, n: int) -> None:
        print("-" * n)

    def _guessed(self) -> None:
        print("Conguratulations!!")
        print("You guessed.")
        self._game_phase = GamePhase.EXIT

    def _failure(self) -> None:
        print("You failed to guess.")
        print(f'The answer is "{self._random_num}".')
        self._game_phase = GamePhase.EXIT

    def _try_guessing(self) -> None:
        self._try_count += 1
        number = int(input("Guess number: "))
        if number < self._random_num:
            print(f'"{number}" is less than random number.')
        elif number > self._random_num:
            print(f'"{number}" is greater than random number.')
        else:
            self._game_phase = GamePhase.GUESSED
            return

        if self._try_count == self._max_try_count:
            self._game_phase = GamePhase.FAILURE

    def _setup(self) -> None:
        self._setup_min_max_num()
        self._setup_max_try_count()
        self._setup_rand_num()
        self._game_phase = GamePhase.GUESSING

    def _init_try_count(self) -> None:
        self._try_count = 0

    def _setup_max_try_count(self) -> None:
        num_count = self._m - self._n + 1
        self._max_try_count = num_count // 2 + num_count % 2

    def _setup_min_max_num(self) -> None:
        while True:
            n = int(input("Min number: "))
            m = int(input("Max number: "))
            if n <= m:
                self._n = n
                self._m = m
                return
            else:
                print("The min number must be less than or equal to the max number.")

    def _setup_rand_num(self) -> None:
        self._random_num = random.randint(self._n, self._m)


if __name__ == "__main__":
    main()
