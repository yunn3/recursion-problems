class SinglyLinkedListNode:

    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


class SinglyLinkedList:

    def __init__(self, head: SinglyLinkedListNode) -> None:
        self.head = head


def insertAtPosition(
    head: SinglyLinkedListNode, position: int, data: int
) -> SinglyLinkedListNode:
    current_node = head

    for _ in range(position):
        if current_node is None:
            return head
        current_node = current_node.next

    new_node = SinglyLinkedListNode(data)
    new_node.next = current_node.next
    current_node.next = new_node

    return head
