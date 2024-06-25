class SinglyLinkedListNode:

    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None

    def insert(self, new_node: "SinglyLinkedListNode") -> None:
        temp_node = self.next
        self.next = new_node
        new_node.next = temp_node


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


def doubleEvenNumber(head: SinglyLinkedListNode) -> SinglyLinkedListNode:
    index = 0
    iterator = head

    while iterator is not None:
        current_node = iterator
        iterator = iterator.next

        if index % 2 == 0:
            new_node = SinglyLinkedListNode(current_node.data * 2)
            current_node.insert(new_node)

        index += 1

    return head


print(doubleEvenNumber(singlyLinkedList([3, 2, 1, 5, 6, 4])))
print(doubleEvenNumber(singlyLinkedList([3])))
print(doubleEvenNumber(singlyLinkedList([3, 1])))
print(doubleEvenNumber(singlyLinkedList([3, 1, 5])))
