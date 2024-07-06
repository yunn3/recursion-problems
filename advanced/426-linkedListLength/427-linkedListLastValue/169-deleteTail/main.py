class SinglyLinkedListNode:

    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


class SinglyLinkedList:

    def __init__(self, head: SinglyLinkedListNode) -> None:
        self.head = head


def deleteTail(head: SinglyLinkedListNode) -> SinglyLinkedListNode:
    dummy_head = SinglyLinkedListNode(None)
    current_node = dummy_head
    current_node.next = head

    while current_node.next.next is not None:
        current_node = current_node.next

    current_node.next = None

    return dummy_head.next
