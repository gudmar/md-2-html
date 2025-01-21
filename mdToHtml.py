from Parser_state import *
from fsmTransitions import process_next_character

def md_to_html(text):
    parser_state = Parser_state()
    for character in text:
        parser_state.character = character
        process_next_character(parser_state)
