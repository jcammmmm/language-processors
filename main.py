import globals
import asdr

def main():
    globals.init("in/a20.psi")
    globals.token = globals.lexer.next_token()
    try:
        asdr.begin()
        if (globals.token.id == 'EOF'):
            print("El analisis sintactico ha finalizado exitosamente.", end='')
        else:
            raise SyntacticError(["NOT EOF"])
    except SyntaxError as se:
        print(se.err_mssg())

def match(expected_token):
    if globals.token.id == expected_token:
        globals.token = globals.lexer.next_token()
    else:
        raise SyntacticError([expected_token])

class SyntacticError(SyntaxError):
    def __init__(self, expected_tokens):
        """
        A list of expected tokens
        """
        self.expected = expected_tokens

    def err_mssg(self):
        if self.expected[0] == 'funcion_principal':
            mssg = "Error sintactico: falta funcion_principal"
        else:
            line = globals.token.line
            col  = globals.token.column
            curr = globals.token.id
            expc = ', '.join(['"{}"'.format(tk) for tk in self.expected])
            mssg = '<{},{}> Error sintactico: se encontro: "{}"; se esperaba: {}'.format(line, col, curr, expc)
        return mssg

if __name__ == "__main__":
    main()