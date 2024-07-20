from typing import Optional, TypeVar, Generic
import re

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T) -> None:
        self.data = data
        self.next: Optional["Node[T]"] = None


def make_singly_linked_list(arr: list) -> Optional[Node]:
    if not arr:
        return None
    head = Node(arr[0])
    iterator = head
    for value in arr[1:]:
        iterator.next = Node(value)
        iterator = iterator.next
    return head


def print_sll(head: Node) -> None:
    iterator = head
    while iterator:
        print(iterator.data, end="➡")
        iterator = iterator.next

    print("END")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self.head: Optional[Node[T]] = None

    def push(self, data: T) -> None:
        new_head = Node[T](data)
        new_head.next = self.head
        self.head = new_head

    def peek(self) -> Optional[T]:
        if self.head:
            return self.head.data
        return None

    def pop(self) -> Optional[T]:
        if self.head:
            temp = self.head
            self.head = self.head.next
            return temp.data
        return None


def expressionParser(expression: str) -> int:
    return ExpressionParser().process(expression)


class ExpressionParser:
    _EXPRESSION_REGEX = re.compile(r"^-*[0-9]+([\+-\/\*]+-*[0-9]+)*$")
    _PLUS_SYMBOL = "+"
    _MINUS_SYMBOL = "-"
    _MULTIPLE_SYMBOL = "*"
    _DIVIDE_SYMBOL = "/"
    _OPERATORS = set([_PLUS_SYMBOL, _MINUS_SYMBOL, _MULTIPLE_SYMBOL, _DIVIDE_SYMBOL])
    _PRIORITY_LOW = 1
    _PRIORITY_HIGH = 10
    _OPERATOR_PRIORITIES = {
        _PLUS_SYMBOL: _PRIORITY_LOW,
        _MINUS_SYMBOL: _PRIORITY_LOW,
        _MULTIPLE_SYMBOL: _PRIORITY_HIGH,
        _DIVIDE_SYMBOL: _PRIORITY_HIGH,
    }

    def __init__(self) -> None:
        self._operate_methods = {
            self._PLUS_SYMBOL: self._operate_addition,
            self._MINUS_SYMBOL: self._operate_subtraction,
            self._MULTIPLE_SYMBOL: self._operate_multiplication,
            self._DIVIDE_SYMBOL: self._operate_division,
        }
        self._operand_stack = Stack[int]()
        self._operator_stack = Stack[str]()

    def process(self, expression: str) -> int:
        if not self.can_process(expression):
            return 0
        ref = len(expression)
        index = ref - 1

        while 0 < index:
            before_symbol = expression[index - 1]
            symbol = expression[index]
            if (
                symbol in self._OPERATORS
                and (
                    symbol != self._MINUS_SYMBOL
                    or before_symbol not in self._OPERATORS
                )
            ):  # fmt: skip
                operand = int(expression[index + 1 : ref])
                self._operand_stack.push(operand)
                left_operator = symbol
                while right_operator := self._operator_stack.peek():
                    if (
                        self._OPERATOR_PRIORITIES[left_operator]
                        >= self._OPERATOR_PRIORITIES[right_operator]
                    ):
                        break
                    self._operand_stack.push(self._operate())

                self._operator_stack.push(left_operator)
                ref = index
            index -= 1

        self._operand_stack.push(int(expression[index:ref]))
        while self._operator_stack.peek() is not None:
            self._operand_stack.push(self._operate())

        result = self._operand_stack.pop()
        return result if result is not None else 0

    def _operate(self) -> int:
        operator = self._operator_stack.pop()
        left = self._operand_stack.pop()
        right = self._operand_stack.pop()
        print(operator, left, right)
        if operator is None or left is None or right is None:
            return 0

        operate_method = self._operate_methods.get(operator)
        if operate_method is None:
            return 0

        return operate_method(left, right)

    def _operate_addition(self, left: int, right: int) -> int:
        return left + right

    def _operate_subtraction(self, left: int, right: int) -> int:
        return left - right

    def _operate_multiplication(self, left: int, right: int) -> int:
        return left * right

    def _operate_division(self, left: int, right: int) -> int:
        if right == 0:
            raise ValueError("right must not be zero")
        return left // right

    @classmethod
    def can_process(cls, expression: str) -> bool:
        match = cls._EXPRESSION_REGEX.match(expression)
        return match is not None


print(expressionParser("-10+3*2"))
