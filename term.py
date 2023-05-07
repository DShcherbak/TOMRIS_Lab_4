from enum import Enum

class TermOperator(Enum):
    Plus = 1
    Minus = 2
    Multiply = 3
    Divide = 4


def applyOperator(lhs, rhs, operator: TermOperator):
    if operator == TermOperator.Plus:
        return lhs + rhs
    elif operator == TermOperator.Minus:
        return lhs - rhs
    elif operator == TermOperator.Multiply:
        return lhs * rhs
    return lhs / rhs


class Term:
    def __init__(self, operator = None, lhs = None, rhs = None, value = None, name = None):
        self.operator = operator
        self.lhs = lhs
        self.rhs = rhs
        self.value = value
        self.name = name

    def isLeaf(self):
        return self.lhs is None and self.rhs is None
    
    def hasValue(self):
        return self.value is not None