import pyparsing as prs

from enum import Enum


class Keyword(Enum):
    IF = 0
    ELSE = 1
    WHILE = 2


keywords: dict[Keyword, str] = {Keyword.IF: 'if', Keyword.ELSE: 'else', Keyword.WHILE: 'while'}

_identifier = prs.Word(prs.alphas).set_parse_action()
_integer = prs.pyparsing_common.integer
_var_or_num = _identifier | _integer
math_op = prs.one_of(['+', '-', '*', '/'])
_math_expr = prs.Group(_var_or_num + math_op + _var_or_num)('math_expr')

_operand = _math_expr | _integer | _identifier

_assignment = prs.Group(_identifier + prs.Literal(':=') + _operand + prs.Literal(';'))("assignment")

_bool_op = prs.one_of(['<', '<=', '>', '>=', '==', '!='])
_bool_expr = prs.Group('(' + _operand + _bool_op + _operand + ')')('bool_expr')

_if_statement = prs.Forward()
_while_loop = prs.Forward()

_command = prs.Group(_if_statement | _while_loop | _assignment)('command')

_if_block = prs.Group(keywords[Keyword.IF] + _bool_expr + '{' + prs.OneOrMore(_command) + '}')('if_block')
_else_block = prs.Group(keywords[Keyword.ELSE] + '{' + prs.OneOrMore(_command) + '}')('else_block')
_if_statement << prs.Group(_if_block + prs.Optional(_else_block))("")('if_statement')

_while_loop << prs.Group(keywords[Keyword.WHILE] + _bool_expr + '{' + prs.OneOrMore(_command) + '}')('while_loop')

_args_list = prs.delimited_list(_identifier)
_params = prs.Group('(' + prs.Optional(_args_list) + ')')
_program_name = prs.Group(_identifier + _params)

_program_code = prs.Group(_program_name + prs.OneOrMore(_command))('program')


def parse(code: str):
    prs.ParserElement.ignoreWhitespace = True
    return _program_code.parseString(code)


def get_commands(s: str):
    result = parse(s)
    for g in result:
        print(g)


