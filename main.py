import enum
import re
from collections import deque

# \Z reads EOF
EOF          = ''
ONLY_LETTERS = "[a-zA-Z]"
ALPHANUMERIC = "[a-zA-Z0-9_]"  
WHITESPACES  = r"\s|\Z"       # [ \t\n\r\f\v]
ANYVALIDCHAR = r"\S"          # [^ \t\n\r\f\v].
TEXTSPACES   = r"\t| "

TK_DELTA_ID       = 1000
TK_ID_TYPES_BEGIN = 1000
TK_ID_OPS_BEGIN   = TK_ID_TYPES_BEGIN + TK_DELTA_ID
TK_ID_CMMT_BEGIN  = TK_ID_TYPES_BEGIN + 2*TK_DELTA_ID


def main():
  st = StateMachine('in/03.txt')
  try:
    for _ in range(53):
      var = st.next_token()
      print(var)
  except LexicalError:
    print("Lexical error.")
  except EOFReachedError:
    print("EOF reached.")

class StateMachine:
  def __init__(self, filename):
    self.source = open(filename, 'r')
    self.in_buffer = deque(self.source.read(10))
    self.line = 1
    self.col = 0

  def next_token(self):
    word = []
    state = 0
    while 1:
      c = self.in_buffer.popleft()
      self.in_buffer.append(self.source.read(1))

      self.col += 1
      word.append(c)
      
      state, rewind, token = next_state(state, c)
      line = self.line
      column = self.col 
      if c == '\n':
        self.col = 0
        self.line += 1
          
      if state == 1:
        for _ in range(rewind):
          x = word.pop()
          if x != '\n':
            self.col -= 1
            self.in_buffer.appendleft(x)
        return build_token(token, ''.join(word), line, column - len(word) - rewind + 1)
      elif state == 0:
        word.pop()
      elif state == -1:
        raise LexicalError()
      elif state == -2:
        raise EOFReachedError()
      elif state == -3:
        word = []
        state = 0

  def turn_off(self):
    self.source.close()

def build_token(token_type, lexeme, line, column):
  token_id = token_type.value
  token = ""
  if token_type == Token.raw_word:
    if lexeme in RESERVED_WORDS:
      # reserved words
      token = "{}".format(lexeme)
    else:
      # identifiers
      token = "id,{}".format(lexeme)
  elif TK_ID_TYPES_BEGIN <= token_id and token_id <= TK_DELTA_ID + 100:
    # types
    token = "{},{}".format(token_type.name, lexeme)
  elif TK_ID_OPS_BEGIN <= token_id and token_id <= TK_ID_OPS_BEGIN + 100:
    # operators and symbols
    token = "{}".format(token_type.name)
  
  token = "<{},{},{}>".format(token, line, column)
  return token 

    

"""
returns a tuple composed of three integer. The first indicates the 
next state based on current input, the second counts how many chars 
must be rewined to the main stream of chars, and the last gives the
name of the actual recognized token.

A returned state of:
   1 means accept state, a valid token was recognized
   0 means pure blank char (outside comment), initial state
  -1 means Lexical Error.
  -2 means EOF
  -3 means comment block or line and should be ignored
"""
def next_state(state, c):
  backw = 0
  token = Token.no_token
  if state == 0:
    if re.match(ONLY_LETTERS, c):
      state = 2
    elif re.match(r"\d", c):
      state = 3
    elif c == '-':
      state = 6
    elif c == '\'':
      state = 7
    elif c == '"':
      state = 9
    elif re.match(WHITESPACES, c) and c != EOF:
      state = 0
    elif re.match("ñ|Ñ", c):
      # this chars are not permmited
      state = -1
    elif c == '<':
      state = 10
    elif c == '>':
      state = 11
    elif c == '=':
      state = 12
    elif c == '!':
      state = 13
    elif c == '|':
      state = 14
    elif c == '&':
      state = 15
    # + * % : ; , . ( )
    elif c == '+':
      state = 16
    elif c == '*':
      state = 17
    elif c == '%':
      state = 18
    elif c == ':':
      state = 19
    elif c == ';':
      state = 20
    elif c == ',':
      state = 21
    elif c == '.':
      state = 22
    elif c == '(':
      state = 23
    elif c == ')':
      state = 24
    elif c == '/':
      state = 25
    elif EOF == c:
      state = -2
    else:
      # not valid char, e.g., '#', '$'
      state = -1
  elif state == 2:
    if re.match(ALPHANUMERIC, c):
      state = 2
    else:
      state = 1
      backw = 1
      token = Token.raw_word
  elif state == 3:
    if re.match(r"\d", c):
      state = 3
    elif c == '.':
      state = 4
    else:
      state = 1
      backw = 1
      token = Token.tk_entero
  elif state == 4:
    if re.match(r"\d", c):
      state = 5
    else:
      state = 1
      backw = 2
      token = Token.tk_entero
  elif state == 5:
    if re.match(r"\d", c):
      state = 5
    else:
      state = 1
      backw = 1
      token = Token.tk_real
  elif state == 6:
    if re.match(r"\d", c):
      state = 3
    else:
      state = 1
      backw = 1
      token = Token.tk_menos
  elif state == 7:
    if re.match(ANYVALIDCHAR, c):
      state = 8
    else:
      state = -1
  elif state == 8:
    if c == '\'':
      state = 1
      token = Token.tk_caracter
    elif EOF == c:
      # by specification, ' cannot stay never alone
      state = -1
    else:
      # char literal must have only one char
      state = -1
  elif state == 9:
    if c == '"':
      state = 1
      token = Token.tk_cadena
    elif EOF == c:
      # by specification, " cannot stay never alone
      state = -1
    elif re.match(TEXTSPACES, c):
      state = 9
    elif re.match(ANYVALIDCHAR, c):
      state = 9
    elif c == '\n':
      state = -1
    else:
      state = -1
  elif state == 10:
    if c == '=':
      state = 1
      token = Token.tk_menor_igual
    else:
      state = 1
      token = Token.tk_menor
      backw = 1
  elif state == 11:
    if c == '=':
      state = 1
      token = Token.tk_mayor_igual
    else:
      state = 1
      token = Token.tk_mayor
      backw = 1
  elif state == 12:
    if c == '=':
      state = 1
      token = Token.tk_igual
    else:
      state = 1
      token = Token.tk_asig
      backw = 1
  elif state == 13:
    if c == '=':
      state = 1
      token = Token.tk_dif
    else:
      state = 1
      token = Token.tk_neg
      backw = 1
  elif state == 14:
    if c == '|':
      state = 1
      token = Token.tk_o
    else:
      # lexical error '|' cannot appear alone
      state = -1
  elif state == 15:
    if c == '&':
      state = 1
      token = Token.tk_y
    else:
      # lexical error '&' cannot appear alone
      state = -1
  # + * % : ; , . ( )  
  elif state == 16:
    state = 1
    token = Token.tk_mas
    backw = 1
  elif state == 17:
    state = 1
    token = Token.tk_mult
    backw = 1
  elif state == 18:
    state = 1
    token = Token.tk_mod
    backw = 1
  elif state == 19:
    state = 1
    token = Token.tk_dosp
    backw = 1
  elif state == 20:
    state = 1
    token = Token.tk_pyc
    backw = 1
  elif state == 21:
    state = 1
    token = Token.tk_coma
    backw = 1
  elif state == 22:
    state = 1
    token = Token.tk_punto
    backw = 1
  elif state == 23:
    state = 1
    token = Token.tk_par_izq
    backw = 1
  elif state == 24:
    state = 1
    token = Token.tk_par_der
    backw = 1
  elif state == 25:
    if c == '*':
      state = 26
    elif c == '/':
      state = 28
    else:
      state = 1
      token = Token.tk_div
      backw = 1
  elif state == 26:
    if c == '*':
      state = 27
    elif EOF == c:
      # lexical error, comments should be closed
      state = -1 
    else:
      state = 26
  elif state == 27:
    if c == '/':
      state = -3
    else:
      state = 26
  elif state == 28:
    if c == '\n' or c == '':
      state = -3
    else:
      state = 28
  else:
    raise NotImplementedError("The state #{state} is not defined.")

  return (state, backw, token)

class Token(enum.Enum):
  raw_word          = 0
  reserved_word     = 1
  identifier        = 2
  no_token          = 3
  tk_entero         = TK_ID_TYPES_BEGIN
  tk_real           = TK_ID_TYPES_BEGIN + 1
  tk_cadena         = TK_ID_TYPES_BEGIN + 2
  tk_caracter       = TK_ID_TYPES_BEGIN + 3
  tk_mas            = TK_ID_OPS_BEGIN
  tk_menos          = TK_ID_OPS_BEGIN + 1
  tk_mult           = TK_ID_OPS_BEGIN + 2
  tk_div            = TK_ID_OPS_BEGIN + 3
  tk_mod            = TK_ID_OPS_BEGIN + 4 
  tk_asig           = TK_ID_OPS_BEGIN + 5
  tk_menor          = TK_ID_OPS_BEGIN + 6
  tk_mayor          = TK_ID_OPS_BEGIN + 7
  tk_menor_igual    = TK_ID_OPS_BEGIN + 8
  tk_mayor_igual    = TK_ID_OPS_BEGIN + 9
  tk_igual          = TK_ID_OPS_BEGIN + 10
  tk_y              = TK_ID_OPS_BEGIN + 11
  tk_o              = TK_ID_OPS_BEGIN + 12
  tk_dif            = TK_ID_OPS_BEGIN + 13
  tk_neg            = TK_ID_OPS_BEGIN + 14
  tk_dosp           = TK_ID_OPS_BEGIN + 15
  tk_pyc            = TK_ID_OPS_BEGIN + 16
  tk_coma           = TK_ID_OPS_BEGIN + 17
  tk_punto          = TK_ID_OPS_BEGIN + 18
  tk_par_izq        = TK_ID_OPS_BEGIN + 19
  tk_par_der        = TK_ID_OPS_BEGIN + 20
  comment_block     = TK_ID_CMMT_BEGIN
  comment_line      = TK_ID_CMMT_BEGIN + 1

RESERVED_WORDS = {
  # inout
  "leer",
  "escribir",
  "imprimir",
  # main,
  "funcion_principal",
  "fin_principal",
  # types
  "booleano",
  "caracter",
  "entero",
  "real",
  "cadena",
  "falso",
  "verdadero",
  # if-else
  "si",
  "entonces",
  "si_no",
  "fin_si",
  # while
  "mientras",
  "hacer",
  "fin_mientras",
  # for
  "para",
  "hacer",
  "fin_para",
  # do while
  "hacer",
  "mientras",
  # switch
  "seleccionar",
  "entre",
  "caso",
  "romper",
  "defecto",
  "fin_seleccionar",
  # struct
  "estructura",
  "fin_estructura",
  # funciones
  "funcion",
  "hacer",
  "retornar",
  "fin_funcion"
}

class LexicalError(Exception):
  """ Thrown when a Lexical error occurs"""
  pass

class EOFReachedError(Exception):
  """ Thrown when the file has been completely parsed"""
  pass

if __name__ == '__main__':
  main()

