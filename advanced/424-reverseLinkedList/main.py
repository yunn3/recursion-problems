from typing import Union


class SinglyLinkedListNode:

    def __init__(self, data: Union[int, None]) -> None:
        self.data = data
        self.next = None

    def insert(self, new_node: "SinglyLinkedListNode") -> None:
        temp_node = self.next
        self.next = new_node
        new_node.next = temp_node


class SinglyLinkedList:

    def __init__(self, head: SinglyLinkedListNode) -> None:
        self.head = head


def singlyLinkedList(arr: list) -> SinglyLinkedListNode:
    head = SinglyLinkedListNode(arr[0])
    current_node = head

    for data in arr[1:]:
        current_node.next = SinglyLinkedListNode(data)
        current_node = current_node.next

    return head


def reverseLinkedList(head: SinglyLinkedListNode) -> SinglyLinkedListNode:
    current_node = head
    prev_node = None

    while current_node is not None:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node

    return prev_node
