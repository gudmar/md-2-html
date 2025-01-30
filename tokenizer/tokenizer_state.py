from tokenizer.tokenizer_fsm_states import Tokenizer_fsm_states

class Tokenizer_state:
    def __init__(self):
        self.output = []
        self.processed_word = ''
        self.character = ''
        self.fsm_state = Tokenizer_fsm_states.start_line
    def __str__(self):
        return 'Tokenizer state: <output=[{}], procesed_word=[{}], character=[{}], fsm_state=[{}]>'.format(self.output, self.processed_word, self.character, self.fsm_state)

    def __repr__(self):
        return 'Tokenizer state: <output=\[{}], procesed_word=\[{}], character=\[{}], fsm_state=\[{}]>'.format(self.output, self.processed_word, self.character, self.fsm_state)

