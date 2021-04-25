from generator import gen_asdr
from lexer import Lexer
import globals
import asdr

def main():
    globals.init()
    # gen_asdr("grammar/incr.gmr")
    lex = Lexer("in/01.psi")
    while 1:
        globals.token = get_tk(lex.next_token())
        asdr.begin()

def match(token):
    pass

def get_tk(token):
    """
    it is supposed that the token has the following form:
    <token_name,num,num>
    """
    return token.split(',')[0][1:]

if __name__ == "__main__":
    main() 