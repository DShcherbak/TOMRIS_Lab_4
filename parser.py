import pyparsing as prs

from enum import Enum

import parse_actions as ac

class Keyword(Enum):
    IF = 0
    ELSE = 1
    WHILE = 2


keywords: dict[Keyword, str] = {Keyword.IF: 'if', Keyword.ELSE: 'else', Keyword.WHILE: 'while'}

_identifier = prs.Word(prs.alphas).set_parse_action(ac.identifier)
_integer = prs.pyparsing_common.integer.set_parse_action(ac.integer)
_var_or_num = _identifier | _integer
math_op = prs.one_of(['+', '-', '*', '/'])
_math_expr = prs.Group(_var_or_num + math_op + _var_or_num)('math_expr').set_parse_action(ac.math_expr)

_operand = _math_expr | _integer | _identifier

_assignment = prs.Group(_identifier + prs.Literal(':=') + _operand + prs.Literal(';')).set_parse_action(ac.assignment)

_bool_op = prs.one_of(['<', '<=', '>', '>=', '==', '!='])
_bool_expr = prs.Group('(' + _operand + _bool_op + _operand + ')')('bool_expr').set_parse_action(ac.condition)

_if_statement = prs.Forward()
_while_loop = prs.Forward()

_command = _if_statement | _while_loop | _assignment

_if_block = prs.Group(
    keywords[Keyword.IF] + _bool_expr +
    '{' + prs.OneOrMore(_command) + '}'
).set_results_name("if_block")

_else_block = prs.Group(
    prs.Literal(keywords[Keyword.ELSE]) +
    '{' + prs.OneOrMore(_command) + '}'
)('else_block').set_results_name('else_block')

_if_statement << prs.Group(_if_block + prs.Optional(_else_block))('if_statement').set_parse_action(ac.if_statement)

_while_loop << prs.Group(keywords[Keyword.WHILE] + _bool_expr + '{' + prs.OneOrMore(_command) + '}')('while_loop')\
    .set_parse_action(ac.while_statement)

_args_list = prs.delimited_list(_identifier)
_params = prs.Group('(' + prs.Optional(_args_list) + ')')
_program_name = prs.Group(_identifier + _params)

_program_code = prs.Group(_program_name + prs.OneOrMore(_command))('program').set_parse_action(ac.commands_list)


def parse(code: str):
    prs.ParserElement.ignoreWhitespace = True
    return _program_code.parseString(code)
