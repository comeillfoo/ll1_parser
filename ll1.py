#!/usr/bin/env python3
import argparse, sys
from lexer import lex
from tokens import *

M = {
    Program: { Id: [ StatementList() ], For: [ StatementList() ] },
    StatementList: { Id: [ Statement(), StatementList_() ], For: [ Statement(), StatementList_() ] },
    Statement: { Id: [ Assignment() ], For: [ ForStatement() ] },
    StatementList_: { Id: [ StatementList() ], For: [ StatementList() ], End: [], Eof: [ ] },
    Assignment: { Id: [ Id(), Assign(), Expression(), Semicolon() ] },
    ForStatement: { For: [ For(), Assignment(), ForDirection(), Expression(), Do(), ForBody() ] },
    Expression: { Not: [ Term(), Expression_() ], OpenBracket: [ Term(), Expression_() ], Id: [ Term(), Expression_() ], Int: [ Term(), Expression_() ] },
    Term: { Not: [ Not(), Factor(), Term_() ], OpenBracket: [ Factor(), Term_() ], Id: [ Factor(), Term_() ], Int: [ Factor(), Term_() ] },
    Term_: {
        Plus: [],
        Minus: [],
        Multiply: [ Multiply(), Factor(), Term_() ],
        Divide: [ Divide(), Factor(), Term_(), ],
        Greater: [],
        Less: [],
        Equal: [],
        CloseBracket: [],
        Semicolon: [],
        Do: [] },
    Expression_: {
        Plus: [ Plus(), Term(), Expression_() ],
        Minus: [ Minus(), Term(), Expression_() ],
        Greater: [ Greater(), Term(), Expression_() ],
        Less: [ Less(), Term(), Expression_() ],
        Equal: [ Equal(), Term(), Expression_() ],
        CloseBracket: [],
        Semicolon: [],
        Do: [] },
    Factor: {
        OpenBracket: [ OpenBracket(), Expression(), CloseBracket() ],
        Id: [ Id() ],
        Int: [ Int() ]
    },
    ForDirection: {
        To: [ To() ],
        DownTo: [ DownTo() ]
    },
    ForBody: {
        Id: [ Statement() ],
        For: [ Statement() ],
        Begin: [ Begin(), StatementList(), End() ]
    }
}

def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser('ll1')
    p.add_argument('filename')
    return p


def state(store, input, x, insym) -> str:
    r = f'STORE: {" ".join(map(lambda x: x.__str__(), store))}\n'
    r += f'INPUT: {" ".join(map(lambda x: x.__str__(), input))}\n'
    r += f'X: {x}, InSym: {insym}'
    return r


def main():
    args = parser().parse_args()
    tokens = None
    with open(args.filename, 'r') as f:
        tokens = f.read()

    # parse
    tokens = lex(tokens)
    STORE = [ Program(), Eof() ]
    X, InSym = STORE[0], tokens.pop(0)
    while type(X) != Eof:
        X = STORE[0]
        if X.is_terminal or type(X) == Eof:
            if type(X) == type(InSym):
                if type(X) == Eof:
                    break
                STORE.pop(0)
                InSym = tokens.pop(0)
            else:
                raise Exception(f'{args.filename} parsing FAILED:\nexpected {X}, found {InSym}\n{state(STORE, tokens, X, InSym)}')
        else: # X is non-terminal
            try:
                rule = M[type(X)][type(InSym)]
                STORE.pop(0) # remove X from magazine
                for token in rule[::-1]:
                    STORE.insert(0, token)
                print(f'applied: {X} -> {" ".join(map(lambda x: x.__str__(), rule))}')
            except KeyError as e:
                raise Exception(f'{args.filename} parsing FAILED:\nnot found rule in M\n{state(STORE, tokens, X, InSym)}')

    print(f'{args.filename} parsing SUCCEED\n{state(STORE, tokens, X, InSym)}')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e, file=sys.stderr)
        exit(1)