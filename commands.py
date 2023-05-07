from enum import Enum


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


    def concat(self, command):
        assert(self.type == CommandType.Do and command.type == CommandType.Do)
        self.assignments.concat(command.assignments)
        self.simplifyCommands()


    def simplifyCommands(self):
        pass 

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
