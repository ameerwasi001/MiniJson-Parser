token_to_op = {
    "MUL" : "*",
    "PLUS": "+",
    "MINUS": "-",
    "DIV": "/"
}

class ModelNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        out = f"{self.key}: {self.value}"
        return "{"+out+"}"

class StringNode:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"'{self.value}'"

class NumberNode:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.value}"

class ArrayNode:
    def __init__(self, elements):
        self.elements = elements

    def __repr__(self):
        array = ", ".join([str(x) for x in self.elements])
        return f"[{array}]"

class BinOpNode:
    def __init__(self, left_node, op_tok, right_node):
        self.left_node = left_node
        self.op_tok = op_tok
        self.right_node = right_node

    def __repr__(self):
        conv_operated = f"({self.left_node} {token_to_op[str(self.op_tok)]} {self.right_node})"
        conv_operated = eval(conv_operated)
        return f"{conv_operated}"

class nullObject:
    def __init__(self):
        self.state = None

    def __repr__(self):
        return "null"

class booleanObject:
    def __init__(self, state):
        self.state = state

    def __repr__(self):
        return "true" if self.state else "false"
