from tokenizer.fsm_token import Token
from tokenizer.fsmTokenTypes import Token_types
import re
from tokenizer.const import end_of_data_stream
from tokenizer.tokenizer_fsm_states import Tokenizer_fsm_states

def check_if_white_space(character):
    return character.strip() == ''

def check_if_current_character_white_space(state):
    return check_if_white_space(state.character)

def save_token(state):
    token_type = identify_token(state)
    get_save_token(token_type)(state)

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

def end_line(state):
    save_character(state)
    token_type = identify_token(state)
    get_save_token(token_type)(state)

def check_if_heading_character(state):
    if state.character != end_of_data_stream and state.character != '#': return False
    is_longer_equal_6 = len(state.processed_word) > 6 and (state.character == end_of_data_stream or check_if_white_space(state.character))
    if (is_longer_equal_6): return False
    is_every_word_symbol_a_hash = all((character == '#' for character in state.processed_word))
    return is_every_word_symbol_a_hash

def get_save_heading_token():
    # heading_severity = len(state.processed_word)
    severity_to_type_map = {
        1: Token_types.h1,
        2: Token_types.h2,
        3: Token_types.h3,
        4: Token_types.h4,
        5: Token_types.h5,
        6: Token_types.h6,
    }
    return lambda state: severity_to_type_map[len(state.processed_word)]

def get_heading_token_type_if_heading(state):
    is_heading = check_if_heading_character(state)
    if is_heading:
        return get_save_heading_token()(state)

def check_if_minus_character(state): return state.character == '-'

def check_if_new_line(state): return state.character == '/n'

def check_if_digit(state): return re.search("\d", state.character)

def check_if_dot(state): return state.character == '.'

def check_if_hr(state): 
    word = state.processed_word
    splitted = list(word)
    if len(splitted) < 3: return False
    if all((char == '-' or check_if_white_space(char) for char in splitted)): return True
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

def isNotEndOfDataStream(state): 
    result = state.character != end_of_data_stream
    return result

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

def get_acceptable_token_creator(acceptableTypes):
    return lambda state: get_acceptable_token_creator(state, acceptableTypes)

def create_token(state, acceptableTypes):
    token_type = get_acceptable_token_type(state, acceptableTypes)
    return Token(token_type, value=state.processed_word)

def end_from_start_line(state):
    token = create_token(state, 'ALL')
    pass

def check_if_end_of_file(state):
    result = state.character == end_of_data_stream
    return result

def get_end_data_stream(acceptable_token_types):
    def end_data_stream(state):
        # state.processed_word = state.processed_word + state.character
        token_type = get_acceptable_token_type(state, acceptable_token_types)
        state.character = ''
        state.fsm_state = Tokenizer_fsm_states.end
        new_token = Token(token_type=token_type, value=state.processed_word)
        state.processed_word = ''
        state.output.append(new_token)
    return end_data_stream
    
