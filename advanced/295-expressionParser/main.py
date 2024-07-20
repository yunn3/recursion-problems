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


def expressionParser(expression: str) -> int:
    OPERATORS = {
        "+": {"priority": 1},
        "-": {"priority": 1},
        "*": {"priority": 2},
        "/": {"priority": 2},
    }
    operand_stack = Stack[int]()
    operator_stack = Stack[str]()
    length = len(expression)
    ref = length

    for index in reversed(range(length)):
        if index == 0:
            operand = int(expression[index:ref])
            operand_stack.push(operand)
            while operator_stack.peek() is not None:
                operate(operand_stack, operator_stack)

        elif expression[index] in OPERATORS and expression[index - 1] not in OPERATORS:
            operator = expression[index]
            operand = int(expression[index + 1 : ref])
            ref = index
            operand_stack.push(operand)

            while (peeked_operator := operator_stack.peek()) is not None and OPERATORS[
                peeked_operator
            ]["priority"] > OPERATORS[operator]["priority"]:
                operate(operand_stack, operator_stack)

            operator_stack.push(operator)
    result = operand_stack.pop()
    if result is None:
        raise ValueError("result: None")
    return result


def operate(operand_stack: Stack[int], operator_stack: Stack[str]) -> None:
    left_operand = operand_stack.pop()
    right_operand = operand_stack.pop()
    operator = operator_stack.pop()
    if left_operand is None:
        raise ValueError("left_operand: None")
    if right_operand is None:
        raise ValueError("right_operand: None")
    if operator is None:
        raise ValueError("left_operand: None")

    operand_stack.push(calculate(left_operand, right_operand, operator))


def calculate(left_operand: int, right_operand: int, operator: str) -> int:
    if operator == "+":
        return left_operand + right_operand
    elif operator == "-":
        return left_operand - right_operand
    elif operator == "*":
        return left_operand * right_operand
    return left_operand // right_operand


print(expressionParser("2+4*6"))  # --> 26
print(expressionParser("2*3+4"))  # --> 10
print(expressionParser("3-3+3"))  # --> 3
print(expressionParser("2+2+2"))  # --> 6
print(expressionParser("1-1-1"))  # --> -1
print(expressionParser("3*3/3*3*3"))  # --> 27
print(expressionParser("14/3*2"))  # --> 8
print(expressionParser("12/3*4"))  # --> 16
print(expressionParser("1+2+3+4+5+6+7+8+9+10"))  # --> 55
print(expressionParser("1+2*5/3+6/4*2"))  # --> 6
print(expressionParser("42"))  # --> 42
print(expressionParser("7*3622*636*2910*183+343/2926/1026"))  # --> 8587122934320
