from typing import Union, Optional


class Node:
    def __init__(self, data: Union[int, list]) -> None:
        self.data = 0
        self.next = None
        if type(data) is int:
            self.data = data
        elif type(data) is list:
            return self._init_from_list(data)

    def _init_from_list(self, data: list) -> None:
        self.data = data[0] if data else 0
        iterator = self
        for value in data[1:]:
            iterator.next = Node(value)
            iterator = iterator.next


class Stack:
    def __init__(self) -> None:
        self.head = None

    def push(self, data) -> None:
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head

    def peek(self) -> Optional[int]:
        if self.head is not None:
            return self.head.data
        return None

    def pop(self) -> Optional[int]:
        if self.head is not None:
            temp = self.head
            self.head = self.head.next
            return temp.data
        return None


def print_sll(head: Node) -> None:
    iterator = head
    while iterator:
        print(iterator.data, end="➡")
        iterator = iterator.next

    print("END")


def dailyStockPrice(stocks: list) -> list:
    if not stocks:
        return []
    stocks_length = len(stocks)
    result = [0 for _ in range(stocks_length)]
    stack = Stack()
    stack.push(0)

    for i in range(1, stocks_length):
        while stack.peek() is not None:
            days = stack.peek()
            if stocks[days] < stocks[i]:
                stack.pop()
                result[days] = i - days

            else:
                break

        stack.push(i)

    return result


dailyStockPrice([58, 59, 71])  # --> [1,1,0]
dailyStockPrice([58, 59, 37, 83])  # --> [1,2,1,0]
dailyStockPrice([63, 63, 64])  # --> [2,1,0]
dailyStockPrice([85, 83, 67, 83, 81, 38, 88, 85])  # --> [6,5,1,3,2,1,0,0]
dailyStockPrice([38, 37, 38, 35, 34, 37, 39, 40, 33, 33])  # --> [6,1,4,2,1,1,1,0,0,0]
