class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def insertNodeInSorted(head: SinglyLinkedListNode, data: int) -> SinglyLinkedListNode:
    new_node = SinglyLinkedListNode(data)

    if head.data >= data:
        new_node.next = head
        return new_node

    current_node = head
    while current_node.next is not None:
        if current_node.next.data > data:
            new_node.next = current_node.next
            current_node.next = new_node
            return head

        current_node = current_node.next

    current_node.next = new_node

    return head
