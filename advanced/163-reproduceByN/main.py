from typing import Union


class SinglyLinkedListNode:
    def __init__(self, data: Union[int, list]) -> None:
        self.data = 0
        self.next = None
        if type(data) is int:
            self.data = data
        elif type(data) is list:
            return self._init_from_list(data)

    def _init_from_list(self, data: list) -> None:
        self.data = data[0] if data else 0
        iterator = self
        for value in data[1:]:
            iterator.next = SinglyLinkedListNode(value)
            iterator = iterator.next


def print_sll(head: SinglyLinkedListNode) -> None:
    iterator = head
    while iterator:
        print(iterator.data, end="➡")
        iterator = iterator.next

    print("END")


def reproduceByN(head: SinglyLinkedListNode, n: int) -> SinglyLinkedListNode:
    if n <= 1:
        return head

    current_node = head

    for _ in range(n - 1):
        copied_head = SinglyLinkedListNode(current_node.data)
        copied_current_node = copied_head

        while current_node.next is not None:
            current_node = current_node.next
            new_node = SinglyLinkedListNode(current_node.data)
            copied_current_node.next = new_node
            copied_current_node = copied_current_node.next

        current_node.next = copied_head
        current_node = copied_head

    return head


print_sll(reproduceByN(SinglyLinkedListNode([3, 2, 1]), 3))
