from tokenizer_fsm_states import Tokenizer_fsm_states

class Tokenizer_state:
    output = []
    processed_word = ''
    character = ''
    fsm_state = Tokenizer_fsm_states.start_line
