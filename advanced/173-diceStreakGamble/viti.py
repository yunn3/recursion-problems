from typing import Optional, TypeVar, Generic, Iterator

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T) -> None:
        self.data = data
        self.next: Optional["Node[T]"] = None
        self.prev: Optional["Node[T]"] = None


class Deque(Generic[T]):
    def __init__(self) -> None:
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None

    def peek_front(self) -> Optional[T]:
        if self.head is None:
            return None
        return self.head.data

    def peek_back(self) -> Optional[T]:
        if self.tail is None:
            return None
        return self.tail.data

    def enqueue_front(self, data: T) -> None:
        new_node = Node(data)
        if self.head is not None:
            self.head.prev = new_node
            self.head.prev.next = self.head
            self.head = self.head.prev
        else:
            self.head = new_node
            self.tail = self.head

    def enqueue_back(self, data: T) -> None:
        new_node = Node(data)
        if self.tail is not None:
            self.tail.next = new_node
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
        else:
            self.head = new_node
            self.tail = self.head

    def dequeue_front(self) -> Optional[T]:
        if self.head is None:
            return None

        data = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None

        return data

    def dequeue_back(self) -> Optional[T]:
        if self.tail is None:
            return None

        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None

        return data

    def __iter__(self) -> Iterator[T]:
        iter = self.head
        while True:
            if iter is not None:
                yield iter.data
            else:
                return
            iter = iter.next


class Player:
    def __init__(self, name: str, dice_rollings: list) -> None:
        self._name = name
        self._dice_queue = Deque[int]()
        for dice in dice_rollings:
            self._dice_queue.enqueue_back(dice)

    @property
    def name(self) -> str:
        return self._name

    def throw_dice(self) -> Optional[int]:
        dice_num = self._dice_queue.dequeue_front()
        if dice_num is not None:
            return dice_num
        return None

    def can_throw_dice(self) -> bool:
        return self._dice_queue.peek_front() is not None


class DiceStreakGamble:
    _PRIZE_UNIT = 4

    def __init__(self, *players: Player) -> None:
        self._play_queue = Deque[Player]()
        for player in players:
            self._play_queue.enqueue_back(player)
        self._judge_queue = Deque[Player]()
        self._score_board = {
            player: {"prize": 0, "dice_rollings": None} for player in players
        }

        self._winner = None

    def start(self) -> None:
        while self._play_queue.peek_front() is not None:
            self._play()

        while self._judge_queue.peek_front() is not None:
            self._judge()

    def get_result_message(self) -> str:
        if self._play_queue.peek_front() is not None:
            return "The winner has yet to be determined."

        if self._winner is None:
            return "There are no winners."

        dice_rollings = self._score_board[self._winner]["dice_rollings"]
        prize = self._score_board[self._winner]["prize"]
        dice_result_string = ",".join([str(dice) for dice in dice_rollings])

        return f"Winner: {self._winner.name} won ${prize} by rolling [{dice_result_string}]"

    def _play(self) -> None:
        player = self._play_queue.dequeue_front()
        if player is None:
            raise ValueError("player is None")
        prize = 0
        dice_rolling_history = Deque[int]()
        while player.can_throw_dice():
            just_before = dice_rolling_history.peek_back()
            dice_num = player.throw_dice()

            if dice_num is not None:
                if self._is_bust(dice_num, just_before):
                    dice_rolling_history = Deque[int]()
                    prize = 0
                prize += self._PRIZE_UNIT
                dice_rolling_history.enqueue_back(dice_num)
            else:
                continue

        self._judge_queue.enqueue_back(player)
        self._score_board[player] = {
            "prize": prize,
            "dice_rollings": dice_rolling_history,
        }

    def _judge(self) -> None:
        player = self._judge_queue.dequeue_front()
        if player is None:
            raise ValueError("player is None")

        if self._is_winning(player):
            self._winner = player

    def _is_bust(self, dice: int, just_before: Optional[int]) -> bool:
        return just_before is not None and dice < just_before

    def _is_winning(self, player: Player) -> bool:
        is_winning = False
        if self._winner is None:
            is_winning = True
        else:
            prize = self._score_board[player]["prize"]
            winners_prize = self._score_board[self._winner]["prize"]
            is_winning = prize > winners_prize

        return is_winning


def diceStreakGamble(player1: list, player2: list, player3: list, player4: list) -> str:
    p1 = Player("Player 1", player1)
    p2 = Player("Player 2", player2)
    p3 = Player("Player 3", player3)
    p4 = Player("Player 4", player4)
    game = DiceStreakGamble(p1, p2, p3, p4)
    game.start()
    return game.get_result_message()


print(
    diceStreakGamble([1, 2, 3], [3, 4, 2], [4, 2, 4], [6, 16, 4])
)  # ---> Winner: Player 1 won $12 by rolling [1,2,3]
print(
    diceStreakGamble([1, 2, 3, -1, 4, 5], [3, 4, 2], [4, 2, 4], [6, 16, 4])
)  # --> Winner: Player 1 won $12 by rolling [-1,4,5]
print(
    diceStreakGamble([4, 3, 2, 1], [4, 3, 2, 1], [4, 3, 2, 1], [4, 3, 2, 1])
)  # --> Winner: Player 1 won $4 by rolling [1]
print(
    diceStreakGamble([1, 2, 3], [3, 4, 2], [4, 2, 4], [6, 16, 26])
)  # --> Winner: Player 1 won $12 by rolling [1,2,3]
print(
    diceStreakGamble([1, 2, 1], [3, 4, 2], [4, 2, 4], [6, 16, 26])
)  # --> Winner: Player 4 won $12 by rolling [6,16,26]
print(
    diceStreakGamble(
        [5, 19, 19, 20], [23, 23, 32, 5], [20, 23, 30, 23], [12, 20, 24, 29]
    )
)  # --> Winner: Player 1 won $16 by rolling [5,19,19,20]
print(
    diceStreakGamble(
        [10, 9, 9, 9, 1, 4], [10, 9, 9, 9, 1, 4], [0, 1, 3, 6, 2, 8], [1, 2, 2, 1, 0, 1]
    )
)  # --> Winner: Player 1 won $8 by rolling [1,4]
print(
    diceStreakGamble(
        [2, 45, 56, 6, 4, 10, 34, 20, 3, 4],
        [20, 45, 56, 6, 4, 3, 5, 3, 2, 20],
        [3, 4, 20, 20, 21, 30, 33, 35, 35, 36],
        [3, 4, 20, 45, 56, 6, 4, 3, 5, 9],
    )
)  # --> Winner: Player 3 won $40 by rolling [3,4,20,20,21,30,33,35,35,36]
