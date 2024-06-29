from typing import Optional


class SinglyLinkedListNode:
    def __init__(self, data: int) -> None:
        self.data = data
        self._next = None

    @property
    def next(self) -> Optional["SinglyLinkedListNode"]:
        return self._next

    @next.setter
    def next(self, node: Optional["SinglyLinkedListNode"]) -> None:
        self._next = node


def middleNode(head: SinglyLinkedListNode) -> SinglyLinkedListNode:
    index = 0
    middle = head
    iterator = head
    while iterator.next is not None and middle.next is not None:
        iterator = iterator.next
        if index % 2 == 0:
            middle = middle.next
        index += 1
    return middle
