from utils import *
from tokenizer.tokenizer_utils import *
from tokenizer.tokenizer_fsm_states import Tokenizer_fsm_states
from tokenizer.fsmTokenTypes import Token_types
from functools import reduce

tokenizer_from_start_line_transitions = [
    {
        'start_state': Tokenizer_fsm_states.start_line,
        'next_state' : Tokenizer_fsm_states.reading_indentions,
        'trigger_function': check_if_current_character_white_space,
        'action': save_character,
    },
    {
        'start_state': Tokenizer_fsm_states.start_line,
        'next_state' : Tokenizer_fsm_states.reading_heading,
        'trigger_function': check_if_heading_character,
        'action': save_character,
    },
    {
        'start_state': Tokenizer_fsm_states.start_line,
        'next_state' : Tokenizer_fsm_states.reading_ul_item,
        'trigger_function': check_if_minus_character,
        'action': save_character,
    },
    {
        'start_state': Tokenizer_fsm_states.start_line,
        'next_state' : Tokenizer_fsm_states.reading_word,
        'trigger_function': check_if_indention_to_word_trigger,
        'action': save_character,
    },
    {
        'start_state': Tokenizer_fsm_states.start_line,
        'next_state' : Tokenizer_fsm_states.end,
        'trigger_function': check_if_end_of_file,
        'action': end_from_start_line
    },

]

tokenizer_from_reading_indention_transitions = [
    {
        'start_state': Tokenizer_fsm_states.reading_indentions,
        'next_state' : Tokenizer_fsm_states.reading_indentions,
        'trigger_function': check_if_current_character_white_space,
        'action': get_save_token(Token_types.indention),
    },
    {
        'start_state': Tokenizer_fsm_states.reading_indentions,
        'next_state' : Tokenizer_fsm_states.reading_heading,
        'trigger_function': check_if_heading_character,
        'action': get_save_token(Token_types.indention),
    },
    {
        'start_state': Tokenizer_fsm_states.reading_indentions,
        'next_state' : Tokenizer_fsm_states.reading_ul_item,
        'trigger_function': check_if_minus_character,
        'action': get_save_token(Token_types.indention),
    },
    {
        'start_state': Tokenizer_fsm_states.reading_indentions,
        'next_state' : Tokenizer_fsm_states.reading_word,
        'trigger_function': check_if_indention_to_word_trigger,
        'action': get_save_token(Token_types.indention),
    },
    {
        'start_state': Tokenizer_fsm_states.reading_indentions,
        'next_state' : Tokenizer_fsm_states.end,
        'trigger_function': check_if_end_of_file,
        'action': get_end_data_stream([Token_types.indention]),
        # 'action': get_save_token(Token_types.indention),
    },
]

tokenizer_from_reading_heading_transitions = [
    {
        'start_state' : Tokenizer_fsm_states.reading_heading,
        'next_state': Tokenizer_fsm_states.reading_heading,
        'trigger_function': check_if_heading_character,
        'action': save_character,
    },
    {
        'start_state' : Tokenizer_fsm_states.reading_heading,
        'next_state': Tokenizer_fsm_states.reading_spaces,
        'trigger_function': check_if_current_character_white_space,
        'action': get_save_heading_token(),
        # 'action': get_save_heading_token(Token_types.indention),
    },
    {
        'start_state' : Tokenizer_fsm_states.reading_heading,
        'next_state': Tokenizer_fsm_states.reading_word,
        'trigger_function': isTrue,
        'action': save_character,
    },
    {
        'start_state' : Tokenizer_fsm_states.reading_heading,
        'next_state': Tokenizer_fsm_states.end,
        'trigger_function': check_if_end_of_file,
        'action': get_end_data_stream([
            Token_types.h1,
            Token_types.h2,
            Token_types.h3,
            Token_types.h4,
            Token_types.h5,
            Token_types.h6,
            Token_types.new_line,
            Token_types.word,
        ]),
    },
]

tokenizer_from_reading_ul_item_transitions = [
    {
        'start_state' : Tokenizer_fsm_states.reading_ul_item,
        'next_state': Tokenizer_fsm_states.reading_spaces,
        'trigger_function': check_if_current_character_white_space,
        'action': get_save_token(Token_types.ul_item),
    },
    {
        'start_state' : Tokenizer_fsm_states.reading_ul_item,
        'next_state': Tokenizer_fsm_states.reading_hr,
        'trigger_function': check_if_minus_character,
        'action': save_character,
    },
    {
        'start_state' : Tokenizer_fsm_states.reading_ul_item,
        'next_state': Tokenizer_fsm_states.reading_word,
        'trigger_function': isTrue,
        'action': save_character,
    },
    {
        'start_state' : Tokenizer_fsm_states.reading_ul_item,
        'next_state': Tokenizer_fsm_states.end,
        'trigger_function': check_if_end_of_file,
        'action': get_end_data_stream([
            Token_types.ul_item,
            Token_types.word,
        ]),
    },
]

tokenizer_from_reading_word_transitions = [
    {
        'start_state' : Tokenizer_fsm_states.reading_word,
        'next_state': Tokenizer_fsm_states.reading_spaces,
        'trigger_function': check_if_current_character_white_space,
        'action': get_save_token(Token_types.word),
    },
    {
        'start_state' : Tokenizer_fsm_states.reading_word,
        'next_state': Tokenizer_fsm_states.end,
        'trigger_function': check_if_end_of_file,
        'action': get_end_data_stream([
            Token_types.word,
        ]),
    },
    {
        'start_state' : Tokenizer_fsm_states.reading_word,
        'next_state': Tokenizer_fsm_states.reading_word,
        'trigger_function': isTrue,
        'action': save_character,
    },
]

tokenizer_transition_lists = [
    tokenizer_from_start_line_transitions,
    tokenizer_from_reading_indention_transitions,
    tokenizer_from_reading_heading_transitions,
    tokenizer_from_reading_ul_item_transitions,
    tokenizer_from_reading_word_transitions
]

def flatten(acc, arr):
    acc.extend(arr)
    return acc

tokenizer_transitions = reduce(flatten, tokenizer_transition_lists, [])


