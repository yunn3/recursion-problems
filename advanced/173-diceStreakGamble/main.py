from typing import Optional, TypeVar, Generic, List

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T) -> None:
        self.data = data
        self.next: Optional["Node[T]"] = None
        self.prev: Optional["Node[T]"] = None


class Deque(Generic[T]):
    def __init__(self):
        self.head = None
        self.tail = None

    def peekFront(self) -> Optional[T]:
        if self.head is None:
            return None
        return self.head.data

    def peekBack(self) -> Optional[T]:
        if self.tail is None:
            return None
        return self.tail.data

    def enqueueFront(self, data: T) -> None:
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head

        else:
            self.head.prev = Node(data)
            self.head.prev.next = self.head
            self.head = self.head.prev

    def enqueueBack(self, data: T) -> None:
        if self.tail is None:
            self.tail = Node(data)
            self.head = self.tail
        else:
            self.tail.next = Node(data)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

    def dequeueFront(self) -> Optional[T]:
        if self.head is None:
            return None

        temp = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None

        return temp.data

    def dequeueBack(self) -> Optional[T]:
        if self.tail is None:
            return None

        temp = self.tail
        self.tail = self.tail.prev

        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None

        return temp.data


class Player:
    def __init__(self, name: str, dice_rolls: List[int]) -> None:
        self.name = name
        self.dice_rolls = Deque[int]()
        for roll in dice_rolls:
            self.dice_rolls.enqueueBack(roll)

    def throw_dice(self) -> Optional[int]:
        return self.dice_rolls.dequeueFront()

    def can_throw_dice(self) -> bool:
        return self.dice_rolls.peekFront() is not None


class DiceStreakGamble:
    ROUND_PRIZE = 4

    def __init__(self, players: List[Player]) -> None:
        self.play_queue = Deque[Player]()
        self.judge_queue = Deque[Player]()
        for player in players:
            self.play_queue.enqueueBack(player)
        self.score_board = {player: {} for player in players}
        self.winner: Optional[Player] = None

    def start(self) -> None:
        while self.play_queue.peekFront() is not None:
            self.play()
            
        self.find_game_winner()

    def play(self) -> None:
        prize = 0
        prev_rolls = Deque[int]()
        player = self.play_queue.dequeueFront()
        if player is None:
            return
        while player.can_throw_dice():
            current_roll = player.throw_dice()
            prev_roll = prev_rolls.peekBack()
            if (
                prev_roll is not None
                and current_roll is not None
                and prev_roll > current_roll
            ):
                prev_rolls = Deque[int]()
                prize = 0

            if current_roll is not None:
                prev_rolls.enqueueBack(current_roll)
                prize += self.ROUND_PRIZE

        self.score_board[player]["prize"] = prize

        rolls = []
        while (prev_roll := prev_rolls.dequeueFront()) is not None:
            rolls.append(prev_roll)
        self.score_board[player]["rolls"] = rolls
        self.judge_queue.enqueueBack(player)

    def get_result(self) -> str:
        if self.winner is not None:
            rolls = ",".join(str(roll) for roll in self.score_board[self.winner]["rolls"])
            return f"Winner: {self.winner.name} won ${self.score_board[self.winner]["prize"]} by rolling [{rolls}]"
        else:
            return ""

    def find_game_winner(self) -> None:
        winner: Optional[Player] = None
        while (player := self.judge_queue.dequeueFront()) is not None:
            if winner is None:
                winner = player
            else:
                current_player_prize = self.score_board[player]["prize"]
                current_winner_prize = self.score_board[winner]["prize"]

                if current_player_prize > current_winner_prize:
                    winner = player

        self.winner = winner


def diceStreakGamble(
    player1: List[int], player2: List[int], player3: List[int], player4: List[int]
) -> str:
    p1 = Player("Player 1", player1)
    p2 = Player("Player 2", player2)
    p3 = Player("Player 3", player3)
    p4 = Player("Player 4", player4)

    game = DiceStreakGamble([p1, p2, p3, p4])
    game.start()
    
    return game.get_result()


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
