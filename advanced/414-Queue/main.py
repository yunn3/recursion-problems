from typing import Optional, TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T) -> None:
        self.data = data
        self.next: Optional["Node[T]"] = None


class Queue(Generic[T]):
    def __init__(self) -> None:
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None

    def peekFront(self) -> Optional[T]:
        return self.peek_front()

    def peek_front(self) -> Optional[T]:
        if self.head is None:
            return None
        return self.head.data

    def peekBack(self) -> Optional[T]:
        return self.peek_back()

    def peek_back(self) -> Optional[T]:
        if self.tail is None:
            return self.peek_front()
        return self.tail.data

    def enqueue(self, data: T) -> None:
        if self.tail is None:
            self.head = Node(data)
            self.tail = self.head

        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    def dequeue(self) -> Optional[T]:
        if self.head is None:
            return None

        temp = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return temp.data


q = Queue[int]()

q.enqueue(4)
print(q.peekFront())  # --> 4
print(q.peekBack())  # --> 4
q.enqueue(50)
print(q.peekFront())  # --> 4
print(q.peekBack())  # --> 50
q.enqueue(64)
print(q.peekFront())  # --> 4
print(q.peekBack())  # --> 64
print(q.dequeue())  # --> 4
