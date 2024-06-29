from math import ceil


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

    def preappend(self, node: SinglyLinkedListNode) -> None:
        node.next = self.head
        self.head = node

    def append(self, node: SinglyLinkedListNode) -> None:
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = node


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


def insertHeadTail(head: SinglyLinkedListNode, data: int) -> SinglyLinkedListNode:
    singly_linked_list = SinglyLinkedList(head)
    singly_linked_list.preappend(SinglyLinkedListNode(data))
    singly_linked_list.append(SinglyLinkedListNode(data))

    return singly_linked_list.head


def middleNode(head: SinglyLinkedListNode) -> SinglyLinkedListNode:
    length = 0
    current_node = head

    while current_node.next is not None:
        current_node = current_node.next
        length += 1

    current_node = head
    for _ in range(ceil(length / 2)):
        current_node = current_node.next

    return current_node
