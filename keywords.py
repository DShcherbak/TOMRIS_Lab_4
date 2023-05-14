from enum import Enum


class Keyword(Enum):
    IF = 0
    ELSE = 1
    WHILE = 2


keywords: dict[Keyword, str] = {Keyword.IF: 'if', Keyword.ELSE: 'else', Keyword.WHILE: 'while'}
