class SinglyLinkedListNode:

    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


class SinglyLinkedList:

    def __init__(self, head: SinglyLinkedListNode) -> None:
        self.head = head


def findMinNum(head: SinglyLinkedListNode) -> int:
    current_node = head
    min_num = current_node.data
    index = 0
    min_index = 0

    while current_node.next is not None:
        current_node = current_node.next
        index += 1

        if current_node.data <= min_num:
            min_num = current_node.data
            min_index = index

    return min_index
