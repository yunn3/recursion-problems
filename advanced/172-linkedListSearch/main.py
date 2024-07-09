class SinglyLinkedListNode:

    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


class SinglyLinkedList:

    def __init__(self, head: SinglyLinkedListNode) -> None:
        self.head = head


def linkedListSearch(head: SinglyLinkedListNode, data: int) -> int:
    current_node = head
    index = 0

    while current_node is not None:
        if current_node.data == data:
            return index

        current_node = current_node.next
        index += 1

    return -1
