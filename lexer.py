#!/usr/bin/env python3
from tokens import *
import re

CHARS = {
    '+': Plus(),
    '-': Minus(),
    '*': Multiply(),
    '/': Divide(),
    '>': Greater(),
    '<': Less(),
    '=': Assign(),
    '!': Not(),
    '(': OpenBracket(),
    ')': CloseBracket(),
    ';': Semicolon()
}

KEYWORDS = {
    'for': For(),
    'to': To(),
    'downto': DownTo(),
    'do': Do(),
    'begin': Begin(),
    'end': End(),
    '==': Equal(),
    ':=': PascalAssign()
}

INT = re.compile(r'([0-9]+).*')
ID = re.compile(r'([a-zA-Z_][0-9a-zA-Z_]*).*')
KEYWORD = re.compile(r'(for|to|downto|do|begin|end|==|:=).*')

def lex(text: str) -> list[Token]:
    text = text.strip()
    if not text:
        return [ Eof() ]

    integer = INT.match(text)
    id = ID.match(text)
    keyword = KEYWORD.match(text)
    if keyword:
        kw = keyword.groups()[0]
        r = [ KEYWORDS[kw] ]
        r.extend(lex(text[len(kw):]))
        return r
    elif id:
        ident = id.groups()[0]
        r = [ Id(ident) ]
        r.extend(lex(text[len(ident):]))
        return r
    elif integer:
        raw_value = integer.groups()[0]
        r = [ Int(int(raw_value))]
        r.extend(lex(text[len(raw_value):]))
        return r
    elif text[0] in CHARS:
        r = [ CHARS[text[0]] ]
        r.extend(lex(text[1:]))
        return r

    raise Exception(f'unknown symbol "{text}"')
