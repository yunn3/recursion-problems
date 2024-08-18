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


def isParenthesesValid(parentheses: str) -> bool:
    BRACKET_PAIRS = {")": "(", "}": "{", "]": "["}
    bracket_queue = Deque()

    for bracket in parentheses:
        if bracket in BRACKET_PAIRS:
            if BRACKET_PAIRS[bracket] == bracket_queue.peek_back():
                bracket_queue.dequeue_back()
            else:
                return False
        elif bracket in BRACKET_PAIRS.values():
            bracket_queue.enqueue_back(bracket)
        else:
            return False

    if bracket_queue.peek_front() is None:
        return True
    return False


print(isParenthesesValid("{}"))  # --> true
print(isParenthesesValid("[{}]"))  # --> true
print(isParenthesesValid("[{(]"))  # --> false
print(isParenthesesValid("(){}[]"))  # --> true
print(isParenthesesValid("((()(())))"))  # --> true
print(isParenthesesValid("[{(}])"))  # --> false
print(isParenthesesValid("]][}{({()){}("))  # --> false
print(isParenthesesValid("{(([])[])[]}[]"))  # --> true
print(isParenthesesValid("{(([])[])[]]}"))  # --> false
print(isParenthesesValid("{{[[(())]]}}"))  # --> true
