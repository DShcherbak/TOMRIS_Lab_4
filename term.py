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

    def __repr__(self):
        operator_str = ''
        match self.operator:
            case TermOperator.Plus:
                operator_str = '+'
            case TermOperator.Minus:
                operator_str = '-'
            case TermOperator.Multiply:
                operator_str = '*'
            case TermOperator.Divide:
                operator_str = "/"
            case _:
                operator_str = 'NotFound'
        name = str(self.name) if self.name is not None else ""
        value = str(self.value) if self.value is not None else ""
        op = f'({self.lhs} {operator_str} {self.rhs})' if self.operator is not None else ""
        return f'Term<' \
               f'{("name = " + str(name)) if name else ""}' \
               f'{("value = " + str(value)) if value else ""}' \
               f'>{op if op else ""}'

    def isLeaf(self):
        return self.lhs is None and self.rhs is None
    
    def hasValue(self):
        return self.value is not None
