from typing import Optional, TypeVar, Generic

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
        if self.head is not None:
            return self.head.data
        return None

    def pop(self) -> Optional[T]:
        if self.head is not None:
            temp = self.head
            self.head = self.head.next
            return temp.data
        return None


class ExpressionParser:
    _PLUS_SYMBOL = "+"
    _MINUS_SYMBOL = "-"
    _MULTIPLE_SYMBOL = "*"
    _DIVIDE_SYMBOL = "/"
    _LEFT_BRACKET = "("
    _RIGHT_BRACKET = ")"
    _SYMBOLS = set(
        [
            _PLUS_SYMBOL,
            _MINUS_SYMBOL,
            _MULTIPLE_SYMBOL,
            _DIVIDE_SYMBOL,
            _LEFT_BRACKET,
            _RIGHT_BRACKET,
        ]
    )
    _OPERATORS = set([_PLUS_SYMBOL, _MINUS_SYMBOL, _MULTIPLE_SYMBOL, _DIVIDE_SYMBOL])
    _OPERATOR_PRIORITIES = {
        _PLUS_SYMBOL: 1,
        _MINUS_SYMBOL: 1,
        _MULTIPLE_SYMBOL: 10,
        _DIVIDE_SYMBOL: 10,
    }

    def __init__(self) -> None:
        self._operand_stack = Stack[int]()
        self._operator_stack = Stack[str]()

    def process(self, expression: str) -> int:
        ref = len(expression)

        for index in reversed(range(len(expression))):
            if self._is_operator(expression, index):
                operator = expression[index]
                while (
                    (peeked_operator := self._operator_stack.peek()) is not None
                    and peeked_operator != self._RIGHT_BRACKET
                    and self._OPERATOR_PRIORITIES[peeked_operator]
                    > self._OPERATOR_PRIORITIES[operator]
                ):
                    self._operate()
                self._operator_stack.push(expression[index])

            elif self._is_sign(expression, index):
                sign = expression[index]
                if sign == self._MINUS_SYMBOL:
                    self._operand_stack.push(-1)
                    self._operator_stack.push(self._MULTIPLE_SYMBOL)

            elif self._is_left_bracket(expression, index):
                while self._operator_stack.peek() != self._RIGHT_BRACKET:
                    self._operate()
                self._operator_stack.pop()

            elif self._is_right_bracket(expression, index):
                right_bracket = expression[index]
                self._operator_stack.push(right_bracket)

            elif self._can_trim_num(expression, index):
                num = int(expression[index:ref])
                self._operand_stack.push(num)

            if self._is_symbol(expression, index):
                ref = index

        while self._operator_stack.peek() is not None:
            self._operate()

        result = self._operand_stack.pop()
        if result is None:
            raise ValueError("result is None.")
        return result

    def _operate(self) -> None:
        left_operand = self._operand_stack.pop()
        right_operand = self._operand_stack.pop()
        operator = self._operator_stack.pop()
        if left_operand is None:
            raise ValueError("left_operand: None")
        if right_operand is None:
            raise ValueError("right_operand: None")
        if operator is None:
            raise ValueError("left_operand: None")

        self._operand_stack.push(self._calculate(left_operand, right_operand, operator))

    def _calculate(self, left_operand: int, right_operand: int, operator: str) -> int:
        if operator == "+":
            return left_operand + right_operand
        elif operator == "-":
            return left_operand - right_operand
        elif operator == "*":
            return left_operand * right_operand
        if right_operand == 0:
            raise ValueError("right must not be zero")
        return int(left_operand / right_operand)

    def _is_operator(self, expression: str, index: int) -> bool:
        return (
            index != 0
            and expression[index] in self._OPERATORS
            and expression[index - 1] not in self._OPERATORS
        )

    def _is_sign(self, expression: str, index: int) -> bool:
        return (
            index < len(expression) - 1
            and expression[index + 1].isdecimal()
            and (
                expression[index] == self._PLUS_SYMBOL
                or expression[index] == self._MINUS_SYMBOL
            )
            and (index == 0 or expression[index - 1] in self._OPERATORS)
        )

    def _is_left_bracket(self, expression: str, index: int) -> bool:
        return expression[index] == self._LEFT_BRACKET

    def _is_right_bracket(self, expression: str, index: int) -> bool:
        return expression[index] == self._RIGHT_BRACKET

    def _can_trim_num(self, expression: str, index: int) -> bool:
        return expression[index].isdecimal() and (
            index == 0 or not expression[index - 1].isdecimal()
        )

    def _is_symbol(self, expression: str, index: int) -> bool:
        return expression[index] in self._SYMBOLS


def expressionParenthesisParser(expression: str) -> int:
    expression_parser = ExpressionParser()
    return expression_parser.process(expression)


# テストケース
result1 = expressionParenthesisParser("2+4*6")
result2 = expressionParenthesisParser("2*3+4")
result3 = expressionParenthesisParser("3-3+3")
result4 = expressionParenthesisParser("2+2+2")
result5 = expressionParenthesisParser("1-1-1")
result6 = expressionParenthesisParser("3*3/3*3*3")
result7 = expressionParenthesisParser("42")
result8 = expressionParenthesisParser("7*3622*636*2910*183+343/2926/1026")
result9 = expressionParenthesisParser("(2*3)+(1+2)")
result10 = expressionParenthesisParser("4/(486-484)")
result11 = expressionParenthesisParser("(1+(2+3+4)-3)+(9+5)")
result12 = expressionParenthesisParser("(100+300)*5+(20-10)/10")
result13 = expressionParenthesisParser("(100+200)/3*100+1000/10")


print(result1)  # --> 26
print(result2)  # --> 10
print(result3)  # --> 3
print(result4)  # --> 6
print(result5)  # --> -1
print(result6)  # --> 27
print(result7)  # --> 42
print(result8)  # --> 8587122934320
print(result9)  # --> 9
print(result10)  # --> 2
print(result11)  # --> 21
print(result12)  # --> 2001
print(result13)  # --> 10100
