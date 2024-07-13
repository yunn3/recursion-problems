from typing import Optional


class SinglyLinkedListNode:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next: Optional["SinglyLinkedListNode"] = None


def insertNodeInSorted(
    head: Optional[SinglyLinkedListNode], data: int
) -> Optional[SinglyLinkedListNode]:
    dummy = SinglyLinkedListNode(0)
    dummy.next = head
    iterator = dummy
    while iterator.next and iterator.next.data < data:
        iterator = iterator.next

    new_node = SinglyLinkedListNode(data)
    new_node.next, iterator.next = iterator.next, new_node

    return dummy.next
