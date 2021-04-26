from main import match
import globals

def begin():
  PRG()

def CLL():
  if globals.token.id == 'id':
    match('id')
    match('tk_par_izq')
    ARG()
    match('tk_par_der')
  else:
    raise SyntaxError('id')

def PRM():
  if globals.token.id == 'real' or globals.token.id == 'entero':
    TYP()
    match('id')
    PRM()
  elif globals.token.id == 'tk_coma':
    match('tk_coma')
    TYP()
    match('id')
    PRM()
  elif globals.token.id == 'tk_par_der' or globals.token.id == 'e':
    pass
  else:
    raise SyntaxError('real, entero, tk_coma, tk_par_der, e')

def TYP():
  if globals.token.id == 'entero':
    match('entero')
  elif globals.token.id == 'real':
    match('real')
  else:
    raise SyntaxError('entero, real')

def PRG():
  if globals.token.id == 'funcion':
    FUN()
    match('funcion_principal')
    BLK()
    match('fin_principal')
    SRA()
  else:
    raise SyntaxError('funcion')

def FUN():
  if globals.token.id == 'funcion':
    match('funcion')
    TYP()
    match('id')
    match('tk_par_izq')
    PRM()
    match('tk_par_der')
    match('hacer')
    BLK()
    match('fin_funcion')
  else:
    raise SyntaxError('funcion')

def BLK():
  if globals.token.id == 'imprimir':
    match('imprimir')
    match('tk_par_izq')
    CLL()
    match('tk_par_der')
    match('tk_pyc')
  elif globals.token.id == 'retornar':
    match('retornar')
    match('id')
    match('tk_mas')
    match('id')
    match('tk_pyc')
  else:
    raise SyntaxError('imprimir, retornar')

def ARG():
  if globals.token.id == 'tk_real' or globals.token.id == 'tk_entero':
    LIT()
    ARG()
  elif globals.token.id == 'tk_coma':
    match('tk_coma')
    LIT()
    ARG()
  elif globals.token.id == 'tk_par_der' or globals.token.id == 'e':
    pass
  else:
    raise SyntaxError('tk_real, tk_entero, tk_coma, tk_par_der, e')

def DCL():
  if globals.token.id == 'real' or globals.token.id == 'entero':
    TYP()
    match('id')
    match('tk_pyc')
    DCL()
  elif globals.token.id == 'e' or globals.token.id == 'fin_estructura':
    pass
  else:
    raise SyntaxError('real, entero, e, fin_estructura')

def LIT():
  if globals.token.id == 'tk_entero':
    match('tk_entero')
  elif globals.token.id == 'tk_real':
    match('tk_real')
  else:
    raise SyntaxError('tk_entero, tk_real')

def SRA():
  if globals.token.id == 'estructura':
    match('estructura')
    match('id')
    DCL()
    match('fin_estructura')
  else:
    raise SyntaxError('estructura')

