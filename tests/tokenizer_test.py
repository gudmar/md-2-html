# python -m tests.tokenizer_tests.py   runs from child directory, from a module dir
print(__package__)
from fsm_token import Token
from fsmTokenTypes import Token_types
from tests.test_runner import run_tests
from get_tokens import get_tokens

tokenizer_test_cases = [
    {
        'description':'Should recognize indention',
        'input': ' ',
        'expected': [Token(value=' ', token_type=Token_types.indention)]
    },
    {
        'description': 'Should recognize a word token',
        'input': 'word',
        'expected': [Token(value='word', token_type=Token_types.word)]
    },
    {
        'description': 'Should recognize a h1 token',
        'input': '#',
        'expected': [Token(value='#', token_type = Token_types.h1)]
    },
    {
        'description': 'Should recognize a h2 token',
        'input': '##',
        'expected': [Token(value='##', token_type = Token_types.h2)]
    },
    {
        'description': 'Should recognize a h6 token',
        'input': '######',
        'expected': [Token(value='######', token_type = Token_types.h6)]
    },
    {
        'description': 'Should recognize a word token, when there are more # then 6',
        'input': '#######',
        'expected': [Token(value='#######', token_type = Token_types.word)]
    },
    {
        'description': 'Should recognize a hr token, when there are 3 minuses in the row',
        'input': '---',
        'expected': [Token(value='---', token_type = Token_types.rule)]
    },
    {
        'description': 'Should recognize a hr token, when there are 6 minuses in the row',
        'input': '------',
        'expected': [Token(value='------', token_type = Token_types.rule)]
    },
    {
        'description': 'Should recognize a word token, when there are 2 minuses in the row',
        'input': '--',
        'expected': [Token(value='--', token_type = Token_types.word)]
    },
    {
        'description': 'Should recognize an unordered list item when there is a single minus starting line',
        'input': '-',
        'expected': [Token(value='-', token_type = Token_types.ul_item)]
    },
    {
        'description': 'Should recognize an indention and unordered list item when there is a single minus starting line',
        'input': '  -',
        'expected': [Token(value='  ', token_type = Token_types.indention), Token(value=' -', token_type = Token_types.ul_item)]
    },
    {
        'description': 'Should recognize a word, space and word token when there is word, space and minus',
        'input': 'asdf  -',
        'expected': [Token(value='  ', token_type = Token_types.word),Token(value='  ', token_type = Token_types.white_space), Token(value='-', token_type = Token_types.word)]
    },
]

run_tests(tokenizer_test_cases, get_tokens)
