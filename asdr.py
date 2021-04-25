from main import match
import globals

def begin():
  PRG()

def PRG():
  if globals.token == 'funcion_principal':
    match('funcion_principal')
    XPR()
    match('finprincipal')
  else:
    raise SyntaxError('funcion_principal')

def XPR():
  if globals.token == 'imprimir':
    match('imprimir')
    match('tk_par_izq')
    match('tk_entero')
    match('tk_mas')
    match('tk_entero')
    match('tk_par_der')
    match('tk_pyc')
  else:
    raise SyntaxError('imprimir')

