from fsm_token import Token
from fsmTokenTypes import Token_types
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
    heading_severity = len(state.processed_word)
    severity_to_type_map = {
        1: Token_types.h1,
        2: Token_types.h2,
        3: Token_types.h3,
        4: Token_types.h4,
        5: Token_types.h5,
        6: Token_types.h6,
    }
    token_type = severity_to_type_map[heading_severity]
    return get_save_token(token_type)

def check_if_minus_character(state): state.character == '-'

def check_if_digit(state): re.search("\d", state.character)

def check_if_dot(state): state.character == '.'

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
