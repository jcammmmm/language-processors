from generator import gen_asdr
from lexer import Lexer
import globals
import asdr

def main():
    globals.init() # "in/a02.psi")
    globals.token = globals.lexer.next_token()
    try:
        asdr.begin()
        if (globals.token != ''):
            raise SyntaxError("NOT EOF")
        else:
            print("El analisis sintactico ha finalizado exitosamente.")
    except SyntaxError as se:
        print("ERROR: {}".format(se.msg))

def match(expected_token):
    if globals.token.id == expected_token:
        globals.token = globals.lexer.next_token()
    else:
        raise SyntaxError(expected_token)

    
if __name__ == "__main__":
    main()