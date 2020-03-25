from Tokens import *
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos<len(self.text) else None

    def make_number(self):
        num_str = ""
        decimal_count = 0
        while (self.current_char in DIGITS+".") and (self.current_char != None):
            if self.current_char == ".": decimal_count+=1
            if decimal_count == 2: break
            num_str += self.current_char
            self.advance()
        return num_str

    def make_string(self):
        norm_str = ""
        self.advance()
        while (self.current_char != '"') and (self.current_char != None):
            norm_str += self.current_char
            self.advance()
        self.advance()
        return norm_str

    def make_keyword_or_identifier(self):
        id_str = ""
        while self.current_char in LETTERS_DIGITS:
            id_str += self.current_char
            self.advance()
        type_ = TT_KEYWORD if id_str in KEYWORDS else None
        if not type_:
            print(f"{id_str} keyword is undefined")
        return Token(type_, id_str)

    def generate_tokens(self):
        tokens = []
        while self.current_char != None:
            if self.current_char in " \t\n":
                self.advance()
            elif self.current_char == "{":
                tokens.append(Token(TT_RCURLYBRACES))
                self.advance()
            elif self.current_char == "}":
                tokens.append(Token(TT_LCURLYBRACES))
                self.advance()
            elif self.current_char == "[":
                tokens.append(Token(TT_RSQUARE))
                self.advance()
            elif self.current_char == "]":
                tokens.append(Token(TT_LSQUARE))
                self.advance()
            elif self.current_char == ":":
                tokens.append(Token(TT_COLON))
                self.advance()
            elif self.current_char == "+":
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == "-":
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current_char == "*":
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current_char == "/":
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current_char == "(":
                tokens.append(Token(TT_RPAREN))
                self.advance()
            elif self.current_char == ")":
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_char == ",":
                tokens.append(Token(TT_COMMA))
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(Token(TT_NUMBER, self.make_number()))
            elif self.current_char in LETTERS:
                tokens.append(self.make_keyword_or_identifier())
            elif self.current_char == '"':
                tokens.append(Token(TT_STRING, self.make_string()))
            else:
                return f"{self.current_char} mana hai"
        return tokens
