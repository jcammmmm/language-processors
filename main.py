from collections import deque
import re
import enum

# \Z reads EOF
ONLY_LETTERS = "[a-zA-Z]"
ALPHANUMERIC = "[a-zA-Z0-9_]"
WHITESPACES  = r"\s|\Z"
ANYVALIDCHAR = r"\S"
TEXTSPACES   = r"\t| "


def main():
  st = StateMachine('in/99.txt')
  try:
    for i in range(53):
      var = st.next_token()
  except EOFError:
    print("EOF Reached")



class StateMachine:
  def __init__(self, filename):
    self.source = open(filename, 'r')
    self.in_buffer = deque(self.source.read(10))

  def next_token(self):
    word = []
    state = 0
    while 1:
      c = self.in_buffer.popleft()
      if c == '':
        raise EOFError("EOF REACHED")
      self.in_buffer.append(self.source.read(1))

      word.append(c)
      state, rewind, token = next_state(state, c)
      if state == 1:
        for i in range(rewind):
          x = word.pop()
          self.in_buffer.appendleft(x)
        print(word, token.name)
        return word
      elif state == 0:
        word.pop()
      elif state == -1:
        raise Exception("LEXICAL ERROR")
      


  def turn_off(self):
    self.source.close()

"""
returns a tuple compose of two integer. The first indicates the 
next state based on current input, and the second item counts
how many chars must be rewined to the main stream of chars.

A returned state of:
  -1 means Lexical Error.
  -2 means EOF
"""
def next_state(state, c):
  backw = 0
  token = Token.no_token
  if state == 0:
    if re.match(ONLY_LETTERS, c):
      state = 2
    elif re.match(r"\d", c):
      state = 3
    elif re.match("-", c):
      state = 6
    elif re.match("'", c):
      state = 7
    elif re.match("\"", c):
      state = 9
    elif re.match(WHITESPACES, c):
      state = 0
  elif state == 2:
    if re.match(ALPHANUMERIC, c):
      state = 2
    elif re.match(WHITESPACES, c):
      state = 1
      backw = 1
      token = Token.raw_word
    else:
      state = -1
  elif state == 3:
    if re.match(r"\d", c):
      state = 3
    elif re.match(r".", c):
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
    if re.match(r"'", c):
      state = 1
      token = Token.tk_caracter
    else:
      state = -1
  elif state == 9:
    if re.match("\"", c):
      state = 1
      token = Token.tk_cadena
    elif re.match(TEXTSPACES, c):
      state = 9
    elif re.match(ANYVALIDCHAR, c):
      state = 9
    elif re.match(r"\n", c):
      state = -1
    else:
      state = -1
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

if __name__ == '__main__':
  main()