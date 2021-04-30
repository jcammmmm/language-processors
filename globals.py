from lexer import Lexer
import os

"""
src_loc (source location) if None, it means that 
source code will be readed from stdin. This makes
that lexer without file location will be instanced.
"""
src_loc = None
if os.getenv('STAGE') == 'DEVELOPMENT':
    src_loc = 'in/a04.psi'

global token, lexer
token = ''
lexer = (Lexer(src_loc) if src_loc else Lexer()) 