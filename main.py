from generator import gen_asdr
from lexer import Lexer
import globals
import asdr

def main():
    gen_asdr("grammar/incr.gmr")
    globals.init("in/01.psi")
    globals.token = globals.lexer.next_token()
    asdr.begin()
    if (globals.token != ''):
        raise SyntaxError("NOT EOF")
    else:
        print("El analisis sintactico ha finalizado exitosamente.")

def match(expected_token):
    if globals.token.id == expected_token:
        globals.token = globals.lexer.next_token()
    else:
        raise SyntaxError(expected_token)

if __name__ == "__main__":
    main()