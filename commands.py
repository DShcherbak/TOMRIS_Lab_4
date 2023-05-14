from enum import Enum
import os

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
            return Term(value=applyOperator(lhs.value, rhs.value, term.operator))
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

    def __repr__(self):
        type_str = ''
        match self.type:
            case CommandType.Do:
                type_str = 'assignment'
            case CommandType.If:
                type_str = 'if'
            case CommandType.While:
                type_str = 'while'
            case _:
                type_str = 'NotKnown'

        def cmds_str(cmds):
            separated_commands = ''
            match cmds:
                case list():
                    separated_commands = \
                        f'{os.linesep.join(["    " + str(cmd) for cmd in cmds])}'
                case dict():
                    key = list(cmds.keys())[0]
                    separated_commands = \
                        f'\n    {str(key) + " := " + str(cmds[key])}\n'
                case _:
                    pass
            return f'[\n{separated_commands}\n]'

        return f'Command<{type_str}>' \
               f'{"(" + str(self.condition) + ")" if self.type in (CommandType.If, CommandType.While) is not None else ""}' \
               f'{cmds_str(self.assignments if self.type == CommandType.Do else self.commands)}' \
               f'{os.linesep + "else" + cmds_str(self.elseCommands) if self.type == CommandType.If and hasattr(self, "elseCommands") else ""}'

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

    def __repr__(self):
        operator_str = ''
        match self.operator:
            case ConditionType.EQ:
                operator_str = '=='
            case ConditionType.LT:
                operator_str = 'LT'
            case ConditionType.GT:
                operator_str = 'GT'
            case ConditionType.LQ:
                operator_str = 'LE'
            case ConditionType.GQ:
                operator_str = 'GE'
            case ConditionType.NQ:
                operator_str = '!='
            case _:
                operator_str = 'NotFound'
        return f'Condition({self.lhs} {operator_str} {self.rhs})'

    
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

def compatible(oper1, oper2):
    return oper1 == oper2 \
            or (oper1 == ConditionType.EQ and (oper2 == ConditionType.LQ or oper2 == ConditionType.GQ)) \
            or (oper2 == ConditionType.EQ and (oper1 == ConditionType.LQ or oper1 == ConditionType.GQ)) \

    


def flip(condition):
    rev = reverse(condition)
    rev.lhs, rev.rhs = rev.rhs, rev.lhs
    return rev 


def One():
    return Condition(ConditionType.TRUE, None, None)
