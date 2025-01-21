from fsmStates import Fsm_states

class Parser_state:
    empty_token = None
    unknown_tag = None
    def __init__(self):
        self.character = '',
        self.token = Parser_state.empty_token,
        self.tag = Parser_state.unknown_tag,
        self.word = '', 
        self.output = '',
        self.current_output = '',
        self.fsm_state = Fsm_states.new_line,
        # self.is_headline_locked = False, # word before \# makes it impossible to render line as a headline

    def end_expression(self): # like whole line, as bold may be included in italic and italic in bold
        # ends: whole line, whole list, whole table
        self.current_output = self.current_output + self.word
        self.output = self.output + self.current_output

    # def lock_headline(self):
    #     self.is_headline_locked = True

    def move_to_next_line(self):
        self.character = ''
        self.token = Parser_state.empty_token,
        self.tag = Parser_state.unknown_tag,
        self.word = ''
        self.current_output = ''
        self.fsm_state = Fsm_states.new_line,
        # self.is_headline_locked = False,

    def end_word(self):
        # meet tag divider, run this. Space does not gave to be the divider
        self.current_output = self.current_output + self.word
        self.word = ''

    def set_fsm_state(self, new_state):
        self.fsm_state = new_state

    def append_word(self):
        self.word = self.word + self.character
        self.character = ''
