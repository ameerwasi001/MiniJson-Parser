from Nodes import *
from Tokens import *

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
        if self.current_tok.type == TT_NUMBER:
            value = self.current_tok.value
            self.advance()
            return NumberNode(value)
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
            return "Why did you not start with a curly brace"
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
