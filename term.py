from enum import Enum

class TermOperator(Enum):
    Plus = 1
    Minus = 2
    Multiply = 3
    Divide = 4

class Term:
    def __init__(self, operator, lhs, rhs):
        self.operator = operator
        self.lhs = lhs
        self.rhs = rhs


class ValueType(Enum):
    Value = 1
    Var = 2
    Term = 3
