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
