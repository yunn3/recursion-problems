from typing import Optional, TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T) -> None:
        self.data = data
        self.next: Optional["Node[T]"] = None
        self.prev: Optional["Node[T]"] = None


class Deque(Generic[T]):
    def __init__(self):
        self.head = None
        self.tail = None

    def peekFront(self) -> Optional[T]:
        if self.head is None:
            return None
        return self.head.data

    def enqueueFront(self, data: T) -> None:
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head

        else:
            self.head.prev = Node(data)
            self.head.prev.next = self.head
            self.head = self.head.prev

    def enqueueBack(self, data: T) -> None:
        if self.tail is None:
            self.tail = Node(data)
            self.head = self.tail
        else:
            self.tail.next = Node(data)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

    def dequeueFront(self) -> Optional[T]:
        if self.head is None:
            return None

        temp = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None

        return temp.data


def getMax(arr: list) -> int:
    q = Deque[int]()

    for num in arr:
        front = q.peekFront()
        if front is not None and front <= num:
            q.enqueueFront(num)

        else:
            q.enqueueBack(num)
    max_value = q.peekFront()

    if max_value is None:
        return 0
    return max_value


print(getMax([3, 2, 1, 5, 6, 4]))  # --> 6
print(getMax([7, 8, 2, 3, 1, 7, 8, 11, 4, 3, 2]))  # --> 11
print(getMax([34, 35, 64, 34, 10, 2, 14, 5, 353, 23, 35, 63, 23]))  # --> 353
print(getMax([1]))  # --> 1
