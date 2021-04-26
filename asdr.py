from main import match
import globals

def begin():
  PRG()

def DEF():
  if globals.token.id == 'funcion':
    FUN()
  elif globals.token.id == 'estructura':
    SRA()
  elif globals.token.id == 'funcion_principal':
    pass
  else:
    raise SyntaxError('funcion, estructura, funcion_principal')

def TYP():
  if globals.token.id == 'entero':
    match('entero')
  elif globals.token.id == 'real':
    match('real')
  else:
    raise SyntaxError('entero, real')

def CLL():
  if globals.token.id == 'id':
    match('id')
    match('tk_par_izq')
    ARG()
    match('tk_par_der')
  else:
    raise SyntaxError('id')

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

def SRA():
  if globals.token.id == 'estructura':
    match('estructura')
    match('id')
    DCL()
    match('fin_estructura')
  else:
    raise SyntaxError('estructura')

def PRM():
  if globals.token.id == 'entero' or globals.token.id == 'real':
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
    raise SyntaxError('entero, real, tk_coma, tk_par_der, e')

def LIT():
  if globals.token.id == 'tk_entero':
    match('tk_entero')
  elif globals.token.id == 'tk_real':
    match('tk_real')
  else:
    raise SyntaxError('tk_entero, tk_real')

def DCL():
  if globals.token.id == 'entero' or globals.token.id == 'real':
    TYP()
    match('id')
    match('tk_pyc')
    DCL()
  elif globals.token.id == 'fin_estructura' or globals.token.id == 'e':
    pass
  else:
    raise SyntaxError('entero, real, fin_estructura, e')

def PRG():
  if globals.token.id == 'estructura' or globals.token.id == 'funcion_principal' or globals.token.id == 'funcion':
    DEF()
    match('funcion_principal')
    BLK()
    match('fin_principal')
    DEF()
  else:
    raise SyntaxError('estructura, funcion_principal, funcion')

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

