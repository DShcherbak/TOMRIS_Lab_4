import commands
import term


def identifier(s) -> term.Term:
    return term.Term(name=s[0])


def integer(*args) -> term.Term:
    token = args[2]
    return term.Term(value=int(token[0]))


def bracketed_expr(*args) -> term.Term:
    tokens = args[2][0]
    return tokens[1]


def _term_operator(s) -> term.TermOperator:
    if s == '+':
        return term.TermOperator.Plus
    elif s == '-':
        return term.TermOperator.Minus
    elif s == '*':
        return term.TermOperator.Multiply
    elif s == '/':
        return term.TermOperator.Divide
    else:
        raise ValueError('Cannot convert operator from string')


def math_expr(*args) -> term.Term:
    tokens = args[2][0]
    first_operand = tokens[0]
    res = None
    # taking two consequent elements from the list on every iteration
    for op, operand in zip(tokens[1::2], tokens[2::2]):
        if res is None:
            res = term.Term(lhs=first_operand,
                            operator=_term_operator(op),
                            rhs=operand)
        else:
            res = term.Term(lhs=res,
                            operator=_term_operator(op),
                            rhs=operand)

    return res if res is not None else first_operand


def assignment(*args) -> commands.Command:
    tokens = args[2][0]
    assignment_dic = {tokens[0].name: tokens[2]}
    return commands.Command(type=commands.CommandType.Do, args=assignment_dic)


def _bool_operator(s) -> commands.ConditionType:
    if s == '==':
        return commands.ConditionType.EQ
    elif s == '>':
        return commands.ConditionType.GT
    elif s == '<':
        return commands.ConditionType.LT
    elif s == '>=':
        return commands.ConditionType.GQ
    elif s == '<=':
        return commands.ConditionType.LQ
    elif s == '!=':
        return commands.ConditionType.NQ
    else:
        raise ValueError("Cannot parse boolean operator")


def condition(*args) -> commands.Condition:
    tokens = args[2][0]
    return commands.Condition(lhs=tokens[1],
                              operator=_bool_operator(tokens[2]),
                              rhs=tokens[3])


def if_statement(*args) -> commands.Command:
    tokens = args[2][0]
    if_block = tokens[0]
    else_block = None
    if len(tokens) == 2:    # both if and else blocks
        else_block = tokens[1]
    return commands.Command(
        type=commands.CommandType.If,
        condition=if_block[1],  # list of commands
        args=if_block[3: -1],
        elseCommands=else_block[2: -1] if else_block is not None else None  # list of commands
    )


def while_statement(*args) -> commands.Command:
    tokens = args[2][0]
    return commands.Command(
        type=commands.CommandType.While,
        condition=tokens[1],
        args=tokens[3: -1]  # list of commands
    )


def commands_list(*args) -> list[commands.Command]:
    tokens = args[2][0]
    return tokens[1:]
