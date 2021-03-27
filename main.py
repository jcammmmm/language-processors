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

def main():
  st = StateMachine('in/99.txt')
  try:
    for _ in range(53):
      var = st.next_token()
      print(var)
  except NameError:
    print("Lexical error.")
  except EOFError:
    print("EOF reached.")



class StateMachine:
  def __init__(self, filename):
    self.source = open(filename, 'r')
    self.in_buffer = deque(self.source.read(10))

  def next_token(self):
    word = []
    state = 0
    prev_state = state
    while 1:
      c = self.in_buffer.popleft()
      self.in_buffer.append(self.source.read(1))

      word.append(c)
      state, rewind, token = next_state(state, c)
      if state == 1:
        for _ in range(rewind):
          x = word.pop()
          self.in_buffer.appendleft(x)
        return word, token.name
      elif state == 0:
        word.pop()
      elif state == -1:
        raise NameError("LEXICAL ERROR")
      elif state == -2:
        raise EOFError("EOF reached.")
      elif state == -3:
        # block of comment, ignore...
        return
    
    prev_state = state
      
  def turn_off(self):
    self.source.close()

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
      token = Token.entero
  elif state == 4:
    if re.match(r"\d", c):
      state = 5
    else:
      state = 1
      backw = 2
      token = Token.entero
  elif state == 5:
    if re.match(r"\d", c):
      state = 5
    else:
      state = 1
      backw = 1
      token = Token.real
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
    if c == '\n':
      state = -3
    else:
      state = 28
  else:
    raise NotImplementedError("The state #{state} is not defined.")

  return (state, backw, token)

class Token(enum.Enum):
  raw_word = 0
  no_token = 1
  funcion_principal = 1
  fin_principal = 2
  entero = 3
  real = 4
  cadena = 5
  caracter = 6
  id = 4
  tk_entero = 7
  tk_real = 8
  tk_cadena = 9
  tk_caracter = 11
  tk_mas = 111
  tk_menos = 1111
  tk_mult = 12
  tk_div = 122
  tk_mod = 1222
  tk_asig = 13
  tk_menor = 133
  tk_mayor = 1333
  tk_menor_igual = 14
  tk_mayor_igual = 144
  tk_igual = 1444
  tk_y = 14444
  tk_o = 15
  tk_dif = 155
  tk_neg = 1555
  tk_dosp = 15555
  tk_pyc = 155555
  tk_coma = 16
  tk_punto = 166
  tk_par_izq = 1666
  tk_par_der = 166666
  comment_block = 17
  comment_line = 177

RESERVED_WORDS = [
  "leer",
  "escribir"
]

if __name__ == '__main__':
  main()

