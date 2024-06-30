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


def mergeTwoSortedLinkedLists(
    head1: Optional[SinglyLinkedListNode],
    head2: Optional[SinglyLinkedListNode],
) -> Optional[SinglyLinkedListNode]:
    merged_head = SinglyLinkedListNode(0)
    current = merged_head
    while head1 and head2:
        if head1.data < head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next

        current = current.next
    current.next = head1 if not head2 else head2

    return merged_head.next
