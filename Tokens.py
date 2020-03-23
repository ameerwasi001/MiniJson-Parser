from string import ascii_letters

TT_RCURLYBRACES = "RCURLYBRACES"
TT_LCURLYBRACES = "LCURLYBRACES"
TT_RSQUARE = "RSQUARE"
TT_LSQUARE = "LSQUARE"
TT_COLON = "COLON"
TT_NUMBER = "NUMBER"
TT_STRING = "STRING"
TT_COMMA = "COMMA"
TT_KEYWORD = "KEYWORD"
TT_IDENTIFIER = "IDENTIFIER"

DIGITS = "0123456789"
LETTERS = ascii_letters
LETTERS_DIGITS = DIGITS+LETTERS

KEYWORDS = [
'null',
'false',
'true'
]

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def matches(self, type_, value):
        return self.type == type_ and self.value == value

    def __repr__(self):
        if self.value: return f"[{self.type}: {self.value}]"
        return self.type
