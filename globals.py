from lexer import Lexer

def init(src_loc=None):
    global token, lexer
    token = ''
    lexer = (Lexer(src_loc) if src_loc else Lexer())   