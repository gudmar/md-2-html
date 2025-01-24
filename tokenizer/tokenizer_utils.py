from tokenizer.fsm_token import Token
from tokenizer.fsmTokenTypes import Token_types
import re

def check_if_white_space(character):
    return character.strip() == ''

def check_if_current_character_white_space(state):
    return check_if_white_space(state.character)

def get_save_token(token_type):
    def save_token(state):
        token = Token(token_type=token_type, value=state.processed_word)
        state.output.append(token)
        state.processed_word = ''
        state.character = ''
    return save_token

def save_character(state):
    state.processed_word = state.processed_word + state.character
    state.character = ''

def check_if_heading_character(state):
    if state.character != '#': return False
    is_shorter_then_6 = len(state.processed_word) < 6
    if (is_shorter_then_6): return False
    is_every_word_symbol_a_hash = all((character == '#' for character in state.processed_word))
    return is_every_word_symbol_a_hash

def get_save_heading_token(state):
    # heading_severity = len(state.processed_word)
    severity_to_type_map = {
        1: Token_types.h1,
        2: Token_types.h2,
        3: Token_types.h3,
        4: Token_types.h4,
        5: Token_types.h5,
        6: Token_types.h6,
    }
    # token_type = severity_to_type_map[heading_severity]
    return lambda state: severity_to_type_map[len(state.processed_word)]
    # return get_save_token(token_type)

def get_heading_token_type_if_heading(state):
    is_heading = check_if_heading_character(state)
    if is_heading:
        return get_save_heading_token()

def check_if_minus_character(state): state.character == '-'

def check_if_digit(state): re.search("\d", state.character)

def check_if_dot(state): state.character == '.'

def check_if_hr(state): 
    word = state.processed_word
    splitted = ''.split(word)
    if len(splitted) < 3: return False
    if all((char == '-' for char in splitted)): return True
    return False

def check_if_indention_to_word_trigger(state):
    not_indention_to_word_triggers = [
        check_if_current_character_white_space,
        check_if_heading_character,
        check_if_digit,
    ]
    for check_if_not_trigger in not_indention_to_word_triggers:
        is_not_trigger = check_if_not_trigger(state)
        if (is_not_trigger): return False
    return True

def isTrue(state): True

def identify_token(state):
    heading_token_type = get_heading_token_type_if_heading(state)
    if heading_token_type != None: return heading_token_type
    if check_if_hr(state): return Token_types.rule
    processed_word = state.processed_word
    token_type_map = {
        '*': Token_types.italic,
        '**': Token_types.bold,
        '`': Token_types.code,
        "'''": Token_types.pre,
        ' ': Token_types.indention,
        '   ': Token_types.indention,
        '\r': Token_types.indention,
        '\n': Token_types.indention,
        '\r\n': Token_types.indention,
        '-': Token_types.ul_item,
    }
    return Token_types.word

def get_acceptable_token_type(state, acceptableTypes):
    suggested_type = identify_token(state)
    if (acceptableTypes == 'ALL'): return suggested_type
    if (suggested_type in acceptableTypes): return suggested_type
    return Token_types.word

def create_token(state, acceptableTypes):
    token_type = get_acceptable_token_type(state, acceptableTypes)
    return Token(token_type, value=state.processed_word)

def endFromStartLine(state):
    save_character(state)

