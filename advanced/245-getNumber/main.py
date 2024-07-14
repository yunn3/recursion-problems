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


def getNumber(code: str) -> str:
    result = []
    length = len(code)

    if length > 8:
        return "0"
    stack = Stack()
    stack.push(1)
    for index in range(length):
        if code[index] == "I":
            while stack.peek() is not None:
                result.append(str(stack.pop()))

        stack.push(index + 2)

    while stack.peek() is not None:
        result.append(str(stack.pop()))
    return "".join(result)


print(getNumber("D"))  # --> 21
print(getNumber("I"))  # --> 12
print(getNumber("DD"))  # --> 321
print(getNumber("IIDDD"))  # --> 126543
print(getNumber("DDIDDIID"))  # --> 321654798
print(getNumber("DIIDIDDD"))  # --> 213549876
print(getNumber("IIIDIDDD"))  # --> 123549876
print(getNumber("DIIDIDDDIID"))  # --> 0
