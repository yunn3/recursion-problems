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
        self._head = None

    def push(self, data) -> None:
        new_head = Node(data)
        new_head.next = self._head
        self._head = new_head

    def peek(self) -> Optional[int]:
        if self._head is not None:
            return self._head.data
        return None

    def pop(self) -> Optional[int]:
        if self._head is not None:
            temp = self._head
            self._head = self._head.next
            return temp.data
        return None


def print_sll(head: Node) -> None:
    iterator = head
    while iterator:
        print(iterator.data, end="➡")
        iterator = iterator.next

    print("END")


def reverse(arr: list) -> list:
    stack = Stack()
    reversed_arr = []
    for data in arr:
        stack.push(data)

    while stack.peek() is not None:
        reversed_arr.append(stack.pop())

    return reversed_arr
