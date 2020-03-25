from Nodes import *
from Tokens import *
import sys

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = -1
        self.advance()

    def advance(self):
        self.pos += 1
        self.current_tok = self.tokens[self.pos] if self.pos<len(self.tokens) else None

    def parse(self):
        res = self.models()
        return res

    def checkIfNumberOrString(self):
        value = None
        if self.current_tok.type in (TT_NUMBER, TT_PLUS, TT_MINUS, TT_MUL, TT_DIV, TT_LPAREN, TT_RPAREN):
            value = self.expr()
        elif self.current_tok.type == TT_STRING:
            value = self.current_tok.value
            self.advance()
            return StringNode(value)
        return value

    def atom(self):
        value = self.checkIfNumberOrString()
        if self.current_tok.matches(TT_KEYWORD, "null"):
            value = nullObject()
            self.advance()
        if self.current_tok.matches(TT_KEYWORD, "false"):
            value = booleanObject(0)
            self.advance()
        if self.current_tok.matches(TT_KEYWORD, "true"):
            value = booleanObject(1)
            self.advance()
        if self.current_tok.type == TT_RSQUARE:
            value = self.array()
        value = value if value else self.models()
        return value

    def bin_op(self, func, ops):
        left = func()
        while self.current_tok.type in ops:
            op_tok = self.current_tok
            self.advance()
            right = func()
            left = BinOpNode(left, op_tok, right)
        return left

    def expr(self):
        return self.bin_op(self.term, (TT_PLUS, TT_MINUS))

    def term(self):
        return self.bin_op(self.factor, (TT_MUL, TT_DIV))

    def factor(self):
        if self.current_tok.type == TT_NUMBER:
            number = self.current_tok.value
            self.advance()
            return NumberNode(number)
        elif self.current_tok.type == TT_RPAREN:
            self.advance()
            expr =  self.expr()
            if self.current_tok.type != TT_LPAREN:
                return "Expected ')'"
            self.advance()
            return expr
        else:
            print("Expected '(' or NUMBER")
            sys.exit()

    def array(self):
        array = []
        if self.current_tok.type != TT_RSQUARE:
            return "Expected '['"
        self.advance()
        if self.current_tok.type != TT_LSQUARE:
            array.append(self.atom())
            while self.current_tok.type == TT_COMMA:
                self.advance()
                array.append(self.atom())
        if self.current_tok.type != TT_LSQUARE:
            return "Expected ']'"
        self.advance()
        return ArrayNode(array)

    def models(self):
        models = []
        if self.current_tok.type != TT_RCURLYBRACES:
            return f"Why did you not start with a curly brace, instaed you ended with {self.current_tok}"
        self.advance()
        models.append(self.model())
        while self.current_tok.type == TT_COMMA:
            self.advance()
            models.append(self.model())
        if self.current_tok.type != TT_LCURLYBRACES:
            return "Why did you not end with a curly brace"
        self.advance()
        return ArrayNode(models)

    def model(self):
        key = self.checkIfNumberOrString()
        if not key: return "This needs to be either a number or a string"
        if self.current_tok.type != TT_COLON:
            return "This needs to be a colon"
        self.advance()
        value = self.atom()
        return ModelNode(key, value)
