def check_if_white_space(character):
    return character.strip() == ''

def check_if_blank_not_new_line(character):
    return character in ['\n', '\r', '\t']
