# Below needs fixing. If run from not tests may cause problems,
# perhaps conditional statement, or a test framework
from tokenizer.fsmTokenTypes import Token_types

class Token:
    type = Token_types.undefined
    value = None
    def __init__(self, **kwargs):
        token_type, value = kwargs['token_type'], kwargs['value']
        print('type: {} value: {}'.format(token_type, value))
        if token_type: self.type = token_type
        if value: self.value = value

    def __eq__(self, obj):
        print(self.type == obj.type and self.value == obj.value)
        print('{} {}'.format(self.type, obj.type))
        print('{} {}'.format(self.__getattribute__('type'), obj.__getattribute__('type')))
        print('{} {}'.format(self.value, obj.value))
        return self.type == obj.type and self.value == obj.value

    def __str__(self):
        return 'Token: <type: [{}], value: [{}]>'.format(self.type, self.value)

    def __repr__(self):
        return 'Token: <type: \[{}], value: \[{}]>'.format(self.type, self.value)


