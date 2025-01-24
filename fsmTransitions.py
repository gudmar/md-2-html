from md_parser_fsm_states import Fsm_states
from utils import *

def end_previous_state(parser_state):
    parser_state.output = parser_state.output + parser_state['current_output']

def process_new_line(parser_state):
    character = parser_state.character
    if character == '#':
        # Not ending anything as this is new line
        parser_state.set_fsm_state(Fsm_states.reading_h_start_tag)
        parser_state.append_word()
        return True
    if check_if_blank_not_new_line(character):
        parser_state.append_word()
        return True
    if 
    parser_state.set_fsm_state(Fsm_states.reading_unknown)

def process_unknown(parser_state):
    parser_state.append_word();
    return True

def process_h_start_tag(parser_state):
    character = parser_state.character
    if character == '#':
        parser_state.set_fsm_state(Fsm_states.reading_h_start_tag)
        parser_state.appendWord();
        return True
    

parser_state_to_action_map = {
    Fsm_states.reading_unknown: process_unknown
}

def process_next_character(parser_state):
    token, tag, word, output, current_output, fsm_state = parser_state

