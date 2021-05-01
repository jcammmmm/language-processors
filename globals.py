from lexer import Lexer
import os

token = ''

def init(src_loc):
    """
    src_loc (source location) if None, it means that 
    source code will be readed from stdin. This makes
    that lexer without file location will be instanced.
    """        
    global lexer
    lexer = Lexer(src_loc) 