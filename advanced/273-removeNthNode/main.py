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


def removeNthNode(head: SinglyLinkedListNode, n: int) -> SinglyLinkedListNode:
    if n <= 0:
        return head

    dummy_head = SinglyLinkedListNode(0)
    dummy_head.next = head
    current_node = dummy_head
    prev_removehead_node = dummy_head
    index = 0

    while current_node.next is not None:
        index += 1
        # 常に移動
        current_node = current_node.next
        if index > n:
            prev_removehead_node = prev_removehead_node.next

    if n <= index:
        prev_removehead_node.next = prev_removehead_node.next.next

    return dummy_head.next
