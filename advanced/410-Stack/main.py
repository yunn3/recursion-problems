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


s1 = Stack()
s1.push(2)
print(s1.peek())  # --> 2
s1.push(4)
s1.push(3)
s1.push(1)
print(s1.pop())  # --> 1
print(s1.peek())  # --> 3
s2 = Stack()
s2.pop()
s2.push(9)
s2.push(8)
print(s2.peek())  # --> 8
