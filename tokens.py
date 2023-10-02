
class Token:
    is_terminal = True
    def __init__(self, attr = None):
        self.attr = attr

    def __str__(self) -> str:
        return f'{type(self).__name__.upper()}' + ('' if self.attr is None else f'({self.attr})')


class Plus(Token):
    is_terminal = True

class Minus(Token):
    is_terminal = True

class Multiply(Token):
    is_terminal = True

class Divide(Token):
    is_terminal = True

class Greater(Token):
    is_terminal = True

class Less(Token):
    is_terminal = True

class Equal(Token):
    is_terminal = True

class Assign(Token):
    is_terminal = True

class Not(Token):
    is_terminal = True

class OpenBracket(Token):
    is_terminal = True

class CloseBracket(Token):
    is_terminal = True

class Semicolon(Token):
    is_terminal = True

class Id(Token):
    is_terminal = True

class Int(Token):
    is_terminal = True

class For(Token):
    is_terminal = True

class To(Token):
    is_terminal = True

class DownTo(Token):
    is_terminal = True

class Do(Token):
    is_terminal = True

class Begin(Token):
    is_terminal = True

class End(Token):
    is_terminal = True

class Eof(Token):
    is_terminal = True

class Program(Token):
    is_terminal = False

class StatementList(Token):
    is_terminal = False

class Statement(Token):
    is_terminal = False

class StatementList_(Token):
    is_terminal = False

class Assignment(Token):
    is_terminal = False

class ForStatement(Token):
    is_terminal = False

class Expression(Token):
    is_terminal = False

class Term(Token):
    is_terminal = False

class Term_(Token):
    is_terminal = False

class Expression_(Token):
    is_terminal = False

class Factor(Token):
    is_terminal = False

class ForDirection(Token):
    is_terminal = False

class ForBody(Token):
    is_terminal = False
