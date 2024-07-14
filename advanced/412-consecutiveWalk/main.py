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


def consecutiveWalk(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    stack = Stack()

    stack.push(arr[0])

    for value in arr[1:]:
        if stack.peek() >= value:
            while stack.peek() is not None:
                stack.pop()

        stack.push(value)

    result = []

    while stack.peek() is not None:
        result.append(stack.pop())

    return result


consecutiveWalk([3, 4, 20, 45, 56, 6, 4, 3, 2, 3, 9])  # --> [9,3,2]
consecutiveWalk([4, 5, 4, 2, 4, 3646, 34, 64, 3, 0, -34, -54])  # --> [-54]
consecutiveWalk([4, 5, 4, 2, 4, 3646, 34, 64, 3, 0, -34, -54, 4])  # --> [4,-54]
consecutiveWalk([])  # --> []
consecutiveWalk([1])  # --> [1]
consecutiveWalk([1, 2, 3, 2, 4])  # --> [4,2]
