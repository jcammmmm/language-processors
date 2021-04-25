from generator import gen_asdr
from lexer import Lexer
import globals
import asdr

def main():
    gen_asdr("grammar/incr.gmr")
    globals.init() #"in/01.psi")
    globals.token = get_tk(globals.lexer.next_token())
    asdr.begin()
    if (globals.token != ''):
        raise SyntaxError("NOT EOF")
    else:
        print("El analisis sintactico ha finalizado exitosamente.")

def match(expected_token):
    if globals.token == expected_token:
        globals.token = get_tk(globals.lexer.next_token())
    else:
        raise SyntaxError(expected_token)

def get_tk(lexer_token):
    """
    it is supposed that the lexer_token has the following form:
    <token_name,num,num>
    """
    return lexer_token.split(',')[0][1:]

if __name__ == "__main__":
    main() 