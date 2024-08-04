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


def getMaxWindows(arr: list, size: int) -> list[int]:
    if size < 1 or len(arr) < size:
        return []

    result: list[int] = []
    index_dq = Deque[int]()

    def _dequeue_lower_nums(index: int) -> None:
        while (back_index := index_dq.peekBack()) is not None and arr[
            back_index
        ] <= arr[index]:
            index_dq.dequeueBack()

    def _append_max_num() -> None:
        front_index = index_dq.peekFront()
        if front_index is not None:
            result.append(arr[front_index])

    def _dequeue_out_of_window(index: int) -> None:
        window_left_index = index - size
        while (front_index := index_dq.peekFront()) is not None and (
            window_left_index
        ) >= front_index:
            index_dq.dequeueFront()

    for index in range(size):
        _dequeue_lower_nums(index)
        index_dq.enqueueBack(index)

    for index in range(size, len(arr)):
        _append_max_num()
        _dequeue_out_of_window(index)
        _dequeue_lower_nums(index)
        index_dq.enqueueBack(index)
    _append_max_num()
    return result


print(
    getMaxWindows([34, 35, 64, 34, 10, 2, 14, 5, 353, 23, 35, 63, 23], 4)
)  # -> [64, 64, 64, 34, 14, 353, 353, 353, 353, 63]
