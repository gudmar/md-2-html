from fsmTokenTypes import Token_types

class Token:
    type = Token_types.undefined
    value = None
    def __init__(self, **kwargs):
        self.type
        token_type, value = kwargs
        if token_type: self.type = token_type
        if value: self.value = value
