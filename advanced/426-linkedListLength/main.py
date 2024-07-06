class SinglyLinkedListNode:

    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


class SinglyLinkedList:

    def __init__(self, head: SinglyLinkedListNode) -> None:
        self.head = head


def linkedListLength(head: SinglyLinkedListNode) -> int:
    current_node = head
    node_length = 0

    while current_node is not None:
        node_length += 1
        current_node = current_node.next

    return node_length
