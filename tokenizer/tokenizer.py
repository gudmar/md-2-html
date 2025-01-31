from tokenizer.tokenizer_state import Tokenizer_state
from tokenizer.tokenizer_transitions import tokenizer_transitions
from tokenizer.const import end_of_data_stream

def get_next_state_recipe(fsm_state, transitions):
    for recipe in transitions:        
        if fsm_state.fsm_state == recipe['start_state'] and recipe['trigger_function'](fsm_state):
            print('{},{} => {}'.format(fsm_state, recipe['start_state'], recipe['next_state']))
            return recipe
    return None

def process_tokenizer_state(fsm_state):
    next_state_recipe = get_next_state_recipe(fsm_state, tokenizer_transitions)
    if next_state_recipe == None:
        raise TypeError('No transition from state "{}" when character "{}" met allowed'.format(fsm_state.fsm_state, fsm_state.character))
    fsm_state.fsm_state = next_state_recipe['next_state']
    next_state_recipe['action'](fsm_state)

def get_tokens(text):
    fsm_state = Tokenizer_state()
    print(fsm_state)
    for character in text:
        fsm_state.character = character
        process_tokenizer_state(fsm_state)
    fsm_state.character = end_of_data_stream
    process_tokenizer_state(fsm_state) # this is for the end of the file
    return fsm_state.output
