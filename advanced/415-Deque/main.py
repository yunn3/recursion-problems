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

    def peekBack(self) -> Optional[T]:
        if self.tail is None:
            return None
        return self.tail.data

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

    def dequeueBack(self) -> Optional[T]:
        if self.tail is None:
            return None

        temp = self.tail
        self.tail = self.tail.prev

        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None

        return temp.data


q = Deque[int]()

q.enqueueBack(4)
q.enqueueBack(50)
print(q.peekFront())  # --> 4
print(q.peekBack())  # --> 50
q.enqueueFront(36)
q.enqueueFront(96)
print(q.peekFront())  # --> 96
print(q.peekBack())  # --> 50
print(q.dequeueBack())  # --> 50
print(q.dequeueBack())  # --> 4
print(q.peekFront())  # --> 96
print(q.peekBack())  # --> 36
q.enqueueFront(20)
print(q.dequeueBack())  # --> 36
