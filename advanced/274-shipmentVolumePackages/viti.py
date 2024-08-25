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

    def peek_front(self) -> Optional[T]:
        if self.head is None:
            return None
        return self.head.data

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


def shipmentVolumePackages(packages: list[int]) -> int:
    if len(packages) <= 1:
        return 0

    sorted_packages = sorted(packages)
    package_queue = Queue[int]()

    for package in sorted_packages:
        package_queue.enqueue(package)

    result = 0
    while (first_package := package_queue.dequeue()) is not None and (
        second_package := package_queue.dequeue()
    ) is not None:
        # 新しい荷物を作成
        new_package = first_package + second_package
        # 結果に加える
        result += new_package
        sort_enqueue(package_queue, new_package)

    return result


def sort_enqueue(queue: Queue[int], value: int) -> None:
    # 末尾に新しい荷物を追加できるなら追加して次のループへ
    back = queue.peek_back()
    if back is None or back <= value:
        queue.enqueue(value)
        return

    # 末尾以外の場所に荷物を追加する
    # 追加できる場所を探す
    while (front := queue.peek_front()) is not None and front <= value:
        queue.dequeue()
        queue.enqueue(front)

    # 新しい荷物を追加
    queue.enqueue(value)

    # 最も小さい荷物を先頭に昇順とする
    while (
        (front := queue.peek_front()) is not None
        and (back := queue.peek_back()) is not None
        and front >= back
    ):
        queue.dequeue()
        queue.enqueue(front)


print(shipmentVolumePackages([6, 5, 6]))  # --> 28
print(shipmentVolumePackages([5, 3, 10, 9, 4]))  # --> 69
print(shipmentVolumePackages([15]))  # --> 0
print(shipmentVolumePackages([1, 2, 3, 4, 5, 6, 10]))  # --> 80
print(shipmentVolumePackages([5, 4, 3, 2, 1]))  # --> 33
print(shipmentVolumePackages([45, 65, 20, 3, 4, 5, 66, 19, 23, 3, 1]))  # --> 700
