from enum import Enum
from term import Term, applyOperator


def _calcTermValue(term: Term, assignments: dict) -> Term:
    if term is None:
        return None
    if term.isLeaf():
        if term.value is not None:
            return Term(value=term.value)
        elif term.name in assignments:
            return assignments[term.name]
        else:
            return term
    else:
        lhs = _calcTermValue(term.lhs)
        rhs = _calcTermValue(term.rhs)
        if lhs is None:
            return rhs
        if rhs is None:
            return lhs
        if lhs.hasValue() and rhs.hasValue():
            return Term(value=applyOperator(lhs.value, rhs.value, term.value))
        else:
            return Term(operator=term.operator, lhs=lhs, rhs=rhs)


class CommandType(Enum):
    Empty = 0
    Do = 1
    If = 2
    While = 3


class Command:
    def __init__(self, type, args, condition = None, elseCommands = None):
        self.type = type
        if type == CommandType.Do:
            self.assignments = args
        elif type == CommandType.If:
            self.condition = condition
            self.commands = args
            if elseCommands is not None:
                self.elseCommands = elseCommands
        else:
            self.condition = condition
            self.commands = args


    def _getNewAssignment(self, newAssignment):
        name = newAssignment[0]
        term = newAssignment[1]
        self.assignments[name] = _calcTermValue(term=term, assignments=self.assignments)
        pass


    def concat(self, command):
        assert(self.type == CommandType.Do and command.type == CommandType.Do)
        for assignment in command.assignments:
            self._getNewAssignment(newAssignment = assignment)


def Eps():
    return Command(CommandType.Empty, [])


class ConditionType(Enum):
    TRUE = 0
    EQ = 1
    GT = 2
    LT = 3
    GQ = 4
    LQ = 5
    NQ = 6


class Condition:
    def __init__(self, operator, lhs, rhs):
        self.operator = operator
        self.lhs = lhs
        self.rhs = rhs

    
def reverse(condition):
    revCondition = Condition(condition.operator, condition.lhs, condition.rhs)
    if condition.operator == ConditionType.EQ:
        revCondition.operator = ConditionType.NQ
    elif condition.operator == ConditionType.GT:
        revCondition.operator = ConditionType.LQ
    elif condition.operator == ConditionType.LT:
        revCondition.operator = ConditionType.GQ
    elif condition.operator == ConditionType.GQ:
        revCondition.operator = ConditionType.LT
    elif condition.operator == ConditionType.LQ:
        revCondition.operator = ConditionType.GT
    elif condition.operator == ConditionType.NQ:
        revCondition.operator = ConditionType.EQ
    return revCondition


def flip(condition):
    rev = reverse(condition)
    rev.lhs, rev.rhs = rev.rhs, rev.lhs
    return rev 


def One():
    return Condition(ConditionType.TRUE, None, None)
