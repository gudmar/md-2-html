class Fsm_states:
    reading_unknown = 'reading unknown',
    new_line = 'starting new line',
    reading_h_start_tag = 'reading heading start tag',
    reading_h_content = 'reading heading content',
    reading_h_end_tag = 'reading heading end tag',
    reading_escaped_character = 'reading escaped character',
