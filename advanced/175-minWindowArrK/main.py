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


def minWindowArrK(intArr: List[int], k: int) -> List[int]:
    if k < 1 or len(intArr) < k:
        return []

    result: List[int] = []
    index_dq = Deque[int]()

    def _dequeue_lower_nums(index: int) -> None:
        while (back_index := index_dq.peek_back()) is not None and intArr[
            back_index
        ] <= intArr[index]:
            index_dq.dequeue_back()

    def _append_max_num() -> None:
        front_index = index_dq.peek_front()
        if front_index is not None:
            result.append(intArr[front_index])

    def _dequeue_out_of_window(index: int) -> None:
        window_left_index = index - k
        while (front_index := index_dq.peek_front()) is not None and (
            window_left_index
        ) >= front_index:
            index_dq.dequeue_front()

    for index in range(k):
        _dequeue_lower_nums(index)
        index_dq.enqueue_back(index)

    for index in range(k, len(intArr)):
        _append_max_num()
        _dequeue_out_of_window(index)
        _dequeue_lower_nums(index)
        index_dq.enqueue_back(index)
    _append_max_num()
    return result
