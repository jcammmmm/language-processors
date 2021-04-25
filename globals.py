from lexer import Lexer

def init(src_loc):
    global token
    token = ''
    global lexer
    lexer = Lexer(src_loc)