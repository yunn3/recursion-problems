from typing import Optional


class SinglyLinkedListNode:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next: Optional["SinglyLinkedListNode"] = None


def deleteTail(head: Optional[SinglyLinkedListNode]) -> Optional[SinglyLinkedListNode]:
    dummy = SinglyLinkedListNode(0)
    dummy.next = head
    current = dummy
    while current and current.next and current.next.next:
        current = current.next

    current.next = None
    return dummy.next
