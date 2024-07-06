class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, arr: list) -> None:
        if len(arr) <= 0:
            self.head = Node(None)
            self.tail = self.head
            return

        self.head = Node(arr[0])
        current_node = self.head

        for data in arr[1:]:
            current_node.next = Node(data)

            current_node.next.prev = current_node
            current_node = current_node.next

        self.tail = current_node


numList = DoublyLinkedList([1, 2, 3, 4, 5, 6, 7])
print(numList.head.data)
print(numList.head.next.data)
print(numList.head.next.prev.data)
print(numList.tail.data)
print(numList.tail.prev.data)
print(numList.tail.prev.prev.data)
