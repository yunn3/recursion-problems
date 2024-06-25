class SinglyLinkedListNode:

    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


class SinglyLinkedList:

    def __init__(self, head: SinglyLinkedListNode) -> None:
        self.head = head
        self.tail = head

    def add(self, node: SinglyLinkedListNode) -> None:
        self.tail.next = node
        self.tail = self.tail.next


def getLinkedList(arr: list) -> SinglyLinkedList:
    numList = SinglyLinkedList(SinglyLinkedListNode(arr[0]))

    for i in range(1, len(arr)):
        numList.add(SinglyLinkedListNode(arr[i]))

    return numList.head


# print(getLinkedList([3, 2, 1, 5, 6, 4]))
