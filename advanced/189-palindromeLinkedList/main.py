from typing import Union, Optional


class SinglyLinkedListNode:
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


def palindromeLinkedList(head: SinglyLinkedListNode) -> bool:
    stack = Stack()
    push_all_node(stack, head)
    length = calc_length(head)
    current_node = head
    for _ in range(length // 2):
        stack_data = stack.pop()
        if current_node.data != stack_data:
            return False

        current_node = current_node.next

    return True


def calc_length(head: SinglyLinkedListNode) -> int:
    length = 0
    current_node = head

    while current_node is not None:
        current_node = current_node.next
        length += 1

    return length


def push_all_node(stack: Stack, head: SinglyLinkedListNode) -> None:
    current_node = head

    while current_node is not None:
        stack.push(current_node.data)
        current_node = current_node.next


print(palindromeLinkedList(SinglyLinkedListNode([1, 2, 3])))  # --> false
print(palindromeLinkedList(SinglyLinkedListNode([1, 2])))  # --> false
print(palindromeLinkedList(SinglyLinkedListNode([1, 0, 1])))  # --> true
print(palindromeLinkedList(SinglyLinkedListNode([3, 4, 4, 3, 6])))  # --> false
print(palindromeLinkedList(SinglyLinkedListNode([3, 6, 4, 4, 3, 6])))  # --> false
print(palindromeLinkedList(SinglyLinkedListNode([3, 6, 4, 4, 6, 3])))  # --> true
print(palindromeLinkedList(SinglyLinkedListNode([1, 2, 3, 2, 1])))  # --> true
