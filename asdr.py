from main import match, SyntacticError
import globals

def begin():
  PRG()

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
    raise SyntacticError(['retornar', 'imprimir'])

def ARG():
  if globals.token.id == 'tk_real' or globals.token.id == 'tk_entero':
    LIT()
    ARG()
  elif globals.token.id == 'tk_coma':
    match('tk_coma')
    LIT()
    ARG()
  elif globals.token.id == 'e' or globals.token.id == 'tk_par_der':
    pass
  else:
    raise SyntacticError(['tk_coma', 'tk_real', 'tk_par_der', 'e', 'tk_entero'])

def TYP():
  if globals.token.id == 'entero':
    match('entero')
  elif globals.token.id == 'real':
    match('real')
  else:
    raise SyntacticError(['entero', 'real'])

def DEF():
  if globals.token.id == 'funcion':
    FUN()
  elif globals.token.id == 'estructura':
    SRA()
  elif globals.token.id == 'funcion_principal':
    pass
  else:
    raise SyntacticError(['funcion_principal', 'funcion', 'estructura'])

def DCL():
  if globals.token.id == 'entero' or globals.token.id == 'real':
    TYP()
    match('id')
    match('tk_pyc')
    DCL()
  elif globals.token.id == 'fin_estructura' or globals.token.id == 'e':
    pass
  else:
    raise SyntacticError(['entero', 'real', 'fin_estructura', 'e'])

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
    raise SyntacticError(['funcion'])

def CLL():
  if globals.token.id == 'id':
    match('id')
    match('tk_par_izq')
    ARG()
    match('tk_par_der')
  else:
    raise SyntacticError(['id'])

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
  elif globals.token.id == 'e' or globals.token.id == 'tk_par_der':
    pass
  else:
    raise SyntacticError(['tk_coma', 'real', 'tk_par_der', 'entero', 'e'])

def LIT():
  if globals.token.id == 'tk_entero':
    match('tk_entero')
  elif globals.token.id == 'tk_real':
    match('tk_real')
  else:
    raise SyntacticError(['tk_real', 'tk_entero'])

def PRG():
  if globals.token.id == 'funcion_principal' or globals.token.id == 'funcion' or globals.token.id == 'estructura':
    DEF()
    match('funcion_principal')
    BLK()
    match('fin_principal')
    DEF()
  else:
    raise SyntacticError(['funcion_principal', 'funcion', 'estructura'])

def SRA():
  if globals.token.id == 'estructura':
    match('estructura')
    match('id')
    DCL()
    match('fin_estructura')
  else:
    raise SyntacticError(['estructura'])

