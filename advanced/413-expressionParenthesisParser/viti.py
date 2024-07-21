from os import RTLD_DEEPBIND
from typing import Callable, Optional, TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T) -> None:
        self.data = data
        self.next: Optional["Node[T]"] = None


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


def expressionParenthesisParser(expression: str) -> int:
    return ExpressionParser().process(expression)


class ExpressionParser:
    _PLUS_SYMBOL = "+"
    _MINUS_SYMBOL = "-"
    _MULTIPLE_SYMBOL = "*"
    _DIVIDE_SYMBOL = "/"
    _LEFT_BRACKET_SYMBOL = "("
    _RIGHT_BRACKET_SYMBOL = ")"
    _SIGNS = set([_PLUS_SYMBOL, _MINUS_SYMBOL])
    _BRACKETS = set([_LEFT_BRACKET_SYMBOL, _RIGHT_BRACKET_SYMBOL])
    _OPERATORS = set([_PLUS_SYMBOL, _MINUS_SYMBOL, _MULTIPLE_SYMBOL, _DIVIDE_SYMBOL])
    _SYMBOLS = set().union(_SIGNS, _OPERATORS, _BRACKETS)
    _SYMBOL_PRIORITIES = {
        _PLUS_SYMBOL: 1,
        _MINUS_SYMBOL: 1,
        _MULTIPLE_SYMBOL: 100,
        _DIVIDE_SYMBOL: 100,
        _LEFT_BRACKET_SYMBOL: 200,
        _RIGHT_BRACKET_SYMBOL: 0,
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
        ref = len(expression)
        i = ref - 1

        while 0 <= i:
            # 演算子であるとき
            if self._is_operator(expression, i):
                operator = expression[i]
                continue_condition: Callable[[Stack[str]], bool] = lambda opr_stk: (
                    (opr := opr_stk.peek()) is not None
                    and self._SYMBOL_PRIORITIES[opr] > self._SYMBOL_PRIORITIES[operator]
                )
                self._operate(continue_condition)
                self._operator_stack.push(operator)
            # 符号であるとき
            elif self._is_sign(expression, i):
                sign = expression[i]
                if sign == self._MINUS_SYMBOL:
                    self._operand_stack.push(-1)
                    self._operator_stack.push(self._MULTIPLE_SYMBOL)

            elif self._is_right_bracket(expression, i):
                r_bracket = expression[i]
                self._operator_stack.push(r_bracket)
            elif self._is_left_bracket(expression, i):
                continue_condition: Callable[[Stack[str]], bool] = lambda opr_stk: (
                    (opr := opr_stk.peek()) is not None
                    and opr != self._RIGHT_BRACKET_SYMBOL
                )
                self._operate(continue_condition)
                self._operator_stack.pop()
            elif self._can_trim_number(expression, i):
                num = int(expression[i:ref])
                self._operand_stack.push(num)
            ref = i if self._is_symbol(expression, i) else ref
            i -= 1

        continue_condition: Callable[[Stack[str]], bool] = (
            lambda opr_stk: opr_stk.peek() is not None
        )
        self._operate(continue_condition)
        result = self._operand_stack.pop()
        if result is None:
            raise ValueError("result is not found")
        return result

    def _operate(self, continue_condition: Callable[[Stack[str]], bool]) -> None:
        while continue_condition(self._operator_stack):
            operator = self._operator_stack.pop()
            left = self._operand_stack.pop()
            right = self._operand_stack.pop()
            if operator is None or left is None or right is None:
                raise ValueError("None in operator or operand")
            operate_method = self._operate_methods.get(operator)
            if operate_method is None:
                raise ValueError(f"operate method is not found: symbol: {operator}")
            self._operand_stack.push(operate_method(left, right))

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
    def _is_symbol(cls, expression: str, position: int) -> bool:
        return expression[position] in cls._SYMBOLS

    @classmethod
    def _is_operator(cls, expression: str, position: int) -> bool:
        return (
            position != 0
            and expression[position] in cls._OPERATORS
            and expression[position - 1] not in cls._OPERATORS
        )

    @classmethod
    def _is_sign(cls, expression: str, position: int) -> bool:
        return (
            position < len(expression) - 1
            and expression[position] in cls._SIGNS
            and expression[position + 1].isdecimal()
            and (position == 0 or expression[position - 1] in cls._OPERATORS)
        )

    @classmethod
    def _can_trim_number(cls, expression: str, position: int) -> bool:
        return expression[position].isdecimal() and (
            position == 0 or expression[position - 1] in cls._SYMBOLS
        )

    @classmethod
    def _is_left_bracket(cls, expression: str, position: int) -> bool:
        return expression[position] == cls._LEFT_BRACKET_SYMBOL

    @classmethod
    def _is_right_bracket(cls, expression: str, position: int) -> bool:
        return expression[position] == cls._RIGHT_BRACKET_SYMBOL


print(expressionParenthesisParser("(10+-10*5)+(2-9*3)"))
