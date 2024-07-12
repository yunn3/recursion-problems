class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def insertNodeInSorted(head: SinglyLinkedListNode, data: int) -> SinglyLinkedListNode:
    current_node = head

    while current_node.next > data:
        current_node = current_node.next

    if current_node.next is None:
        new_node = SinglyLinkedListNode(data)
        current_node.next = new_node

    else:
        new_node = SinglyLinkedListNode(data)
        new_node.next = current_node.next
        current_node.next = new_node

    return head
