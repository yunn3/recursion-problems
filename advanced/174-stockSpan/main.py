from typing import Optional, TypeVar, Generic, List

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

    def peek_front(self) -> Optional[T]:
        if self.head is None:
            return None
        return self.head.data

    def peek_back(self) -> Optional[T]:
        if self.tail is None:
            return None
        return self.tail.data

    def enqueue_front(self, data: T) -> None:
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head

        else:
            self.head.prev = Node(data)
            self.head.prev.next = self.head
            self.head = self.head.prev

    def enqueue_back(self, data: T) -> None:
        if self.tail is None:
            self.tail = Node(data)
            self.head = self.tail
        else:
            self.tail.next = Node(data)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

    def dequeue_front(self) -> Optional[T]:
        if self.head is None:
            return None

        temp = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None

        return temp.data

    def dequeue_back(self) -> Optional[T]:
        if self.tail is None:
            return None

        temp = self.tail
        self.tail = self.tail.prev

        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None

        return temp.data


def stockSpan(stocks: List[int]) -> List[int]:
    result = []
    span_indices = Deque()

    for index in range(len(stocks)):
        # span_indices の back にある要素が現在の株価よりも小さければ取り除く
        prev_index = span_indices.peek_back()

        while prev_index is not None and stocks[prev_index] <= stocks[index]:
            span_indices.dequeue_back()
            prev_index = span_indices.peek_back()

        # span_indices が空なら、現在のインデックスまでがスパンになる
        if prev_index is None:
            span = index + 1
        else:
            span = index - prev_index

        result.append(span)
        span_indices.enqueue_back(index)

    return result


print(stockSpan([30, 50, 60, 20, 30, 64, 80]))  # --> [1,2,3,1,2,6,7]
print(stockSpan([24, 5, 67, 60, 24, 64, 23, 536, 345]))  # --> [1,1,3,1,1,3,1,8,1]
print(stockSpan([200, 85, 40, 60, 40, 65, 90]))  # --> [1,1,1,2,1,4,6]
print(stockSpan([30, 45, 20, 100, 235, 300, 4500, 40, 100]))  # --> [1,2,1,4,5,6,7,1,2]
print(
    stockSpan([34, 640, 100, 234, 56, 34, 25, 200, 1020, 160])
)  # --> [1,2,1,2,1,1,1,4,9,1]
