class SinglyLinkedListNode:

    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


class SinglyLinkedList:

    def __init__(self, head: SinglyLinkedListNode) -> None:
        self.head = head

    def at(self, index: int) -> SinglyLinkedListNode:
        current_node = self.head

        for i in range(index):
            current_node = current_node.next
            if current_node is None:
                return None
        return current_node


def getIndexValue(head: SinglyLinkedListNode, index: int) -> int:
    linked_list = SinglyLinkedList(head)
    node = linked_list.at(index - 1)
    if node is None:
        raise IndexError()
    return node.data


def singlyLinkedList(arr: list) -> SinglyLinkedListNode:
    head = SinglyLinkedListNode(arr[0])
    prev = head
    for data in arr[1:]:
        prev.next = SinglyLinkedListNode(data)
        prev = prev.next

    return head


print(getIndexValue(singlyLinkedList([3, 2, 1, 5, 6, 4]), 7))  # -> 3
# print(getIndexValue(singlyLinkedList([7, 8, 2, 3, 1, 7, 8, 11, 4, 3, 2]), 5))  # -> 1
# print(
#     getIndexValue(
#         singlyLinkedList([34, 35, 64, 34, 10, 2, 14, 5, 353, 23, 35, 63, 23]),
#         7,  # -> 14
#     )
# )
