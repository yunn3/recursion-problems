from typing import Optional


class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self._next = None

    @property
    def next(self) -> Optional["SinglyLinkedListNode"]:
        return self._next

    @next.setter
    def next(self, item: Optional["SinglyLinkedListNode"]):
        self._next = item


class SinglyLinkedList:
    def __init__(self) -> None:
        self._head = None
        self._tail = None

    @property
    def head(self) -> Optional[SinglyLinkedListNode]:
        return self._head

    def add(self, node: SinglyLinkedListNode) -> None:
        if self._head is None and self._tail is None:
            self._head = node
            self._tail = node
        else:
            self._tail.next = node

        if isinstance(self._tail, SinglyLinkedListNode):
            while self._tail.next is not None:
                self._tail = self._tail.next


def getLinkedList(arr: list) -> Optional[SinglyLinkedListNode]:
    linked_list = SinglyLinkedList()
    for data in arr:
        linked_list.add(SinglyLinkedListNode(data))
    return linked_list.head
