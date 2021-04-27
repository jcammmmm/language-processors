from main import match, SyntacticError
import globals

def begin():
  PRG()

def CL0():
  if globals.token.id == 'tk_par_izq':
    match('tk_par_izq')
    ARG()
    match('tk_par_der')
  else:
    raise SyntacticError(['tk_par_izq'])

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

def CL2():
  if globals.token.id == 'tk_par_izq':
    CL0()
  elif globals.token.id == 'tk_asig':
    CL1()
  else:
    raise SyntacticError(['tk_par_izq', 'tk_asig'])

def CL1():
  if globals.token.id == 'tk_asig':
    match('tk_asig')
    CL3()
  else:
    raise SyntacticError(['tk_asig'])

def LIT():
  if globals.token.id == 'tk_entero':
    match('tk_entero')
  elif globals.token.id == 'tk_real':
    match('tk_real')
  elif globals.token.id == 'tk_cadena':
    match('tk_cadena')
  else:
    raise SyntacticError(['tk_real', 'tk_cadena', 'tk_entero'])

def CLA():
  if globals.token.id == 'id':
    match('id')
    CL2()
  else:
    raise SyntacticError(['id'])

def POS():
  if globals.token.id == 'estructura' or globals.token.id == '$' or globals.token.id == 'funcion':
    INI()
  elif globals.token.id == 'eof':
    match('eof')
  else:
    raise SyntacticError(['estructura', '$', 'funcion', 'eof'])

def IMP():
  if globals.token.id == 'imprimir':
    match('imprimir')
    match('tk_par_izq')
    IM0()
  else:
    raise SyntacticError(['imprimir'])

def IM0():
  if globals.token.id == 'id':
    CLA()
    match('tk_par_der')
    match('tk_pyc')
  elif globals.token.id == 'tk_real' or globals.token.id == 'tk_cadena' or globals.token.id == 'tk_entero':
    LIT()
    match('tk_par_der')
    match('tk_pyc')
  else:
    raise SyntacticError(['tk_real', 'tk_cadena', 'id', 'tk_entero'])

def CL3():
  if globals.token.id == 'tk_real' or globals.token.id == 'tk_cadena' or globals.token.id == 'tk_entero':
    LIT()
    match('tk_pyc')
  elif globals.token.id == 'id':
    match('id')
    match('tk_pyc')
  else:
    raise SyntacticError(['id', 'tk_real', 'tk_cadena', 'tk_entero'])

def DC0():
  if globals.token.id == 'entero' or globals.token.id == 'real':
    TYP()
    match('id')
    match('tk_pyc')
    DC0()
  elif globals.token.id == 'fin_si' or globals.token.id == 'si' or globals.token.id == 'fin_estructura' or globals.token.id == 'real' or globals.token.id == 'e' or globals.token.id == 'entero' or globals.token.id == 'si_no' or globals.token.id == 'id' or globals.token.id == 'imprimir' or globals.token.id == 'retornar':
    pass
  else:
    raise SyntacticError(['fin_si', 'si', 'fin_estructura', 'real', 'e', 'entero', 'si_no', 'id', 'imprimir', 'retornar'])

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
    raise SyntacticError(['tk_par_der', 'tk_coma', 'real', 'e', 'entero'])

def XPR():
  if globals.token.id == 'tk_neg':
    match('tk_neg')
    XPR()
  elif globals.token.id == 'id':
    match('id')
    OPE()
    match('id')
  else:
    raise SyntacticError(['tk_neg', 'id'])

def BLQ():
  if globals.token.id == 'si':
    CND()
    BLQ()
  elif globals.token.id == 'id':
    CLA()
    BLQ()
  elif globals.token.id == 'entero' or globals.token.id == 'real':
    DCL()
    BLQ()
  elif globals.token.id == 'imprimir':
    IMP()
    BLQ()
  elif globals.token.id == 'fin_si':
    match('fin_si')
  elif globals.token.id == 'si_no':
    match('si_no')
    BLQ()
  else:
    raise SyntacticError(['si', 'fin_si', 'real', 'entero', 'si_no', 'id', 'imprimir'])

def BLK():
  if globals.token.id == 'retornar':
    match('retornar')
    match('id')
    match('tk_mas')
    match('id')
    match('tk_pyc')
  elif globals.token.id == 'imprimir':
    IMP()
    BLK()
  elif globals.token.id == 'entero' or globals.token.id == 'real':
    DCL()
    BLK()
  elif globals.token.id == 'si':
    CND()
    BLK()
  elif globals.token.id == 'id':
    CLA()
    BLK()
  elif globals.token.id == 'fin_principal' or globals.token.id == 'fin_funcion' or globals.token.id == 'e':
    pass
  else:
    raise SyntacticError(['fin_principal', 'fin_funcion', 'si', 'real', 'e', 'entero', 'id', 'imprimir', 'retornar'])

def OPE():
  if globals.token.id == 'tk_igual':
    match('tk_igual')
  elif globals.token.id == 'tk_menor':
    match('tk_menor')
  elif globals.token.id == 'tk_menor_igual':
    match('tk_menor_igual')
  elif globals.token.id == 'tk_mayor':
    match('tk_mayor')
  elif globals.token.id == 'tk_mayor_igual':
    match('tk_mayor_igual')
  elif globals.token.id == 'tk_mas':
    match('tk_mas')
  else:
    raise SyntacticError(['tk_menor', 'tk_menor_igual', 'tk_mayor', 'tk_mayor_igual', 'tk_mas', 'tk_igual'])

def INI():
  if globals.token.id == 'funcion':
    FUN()
  elif globals.token.id == 'estructura':
    SRA()
  elif globals.token.id == 'funcion_principal' or globals.token.id == 'e':
    pass
  else:
    raise SyntacticError(['estructura', 'funcion_principal', 'funcion', 'e'])

def DCL():
  if globals.token.id == 'entero' or globals.token.id == 'real':
    TYP()
    match('id')
    match('tk_pyc')
    DC0()
  else:
    raise SyntacticError(['entero', 'real'])

def CND():
  if globals.token.id == 'si':
    match('si')
    match('tk_par_izq')
    XPR()
    match('tk_par_der')
    match('entonces')
    BLQ()
  else:
    raise SyntacticError(['si'])

def PRG():
  if globals.token.id == 'estructura' or globals.token.id == 'funcion' or globals.token.id == 'funcion_principal':
    INI()
    match('funcion_principal')
    BLK()
    match('fin_principal')
    POS()
  else:
    raise SyntacticError(['estructura', 'funcion_principal', 'funcion'])

def SRA():
  if globals.token.id == 'estructura':
    match('estructura')
    match('id')
    DCL()
    match('fin_estructura')
  else:
    raise SyntacticError(['estructura'])

def TYP():
  if globals.token.id == 'entero':
    match('entero')
  elif globals.token.id == 'real':
    match('real')
  else:
    raise SyntacticError(['entero', 'real'])

def ARG():
  if globals.token.id == 'tk_real' or globals.token.id == 'tk_cadena' or globals.token.id == 'tk_entero':
    LIT()
    ARG()
  elif globals.token.id == 'tk_coma':
    match('tk_coma')
    LIT()
    ARG()
  elif globals.token.id == 'tk_par_der' or globals.token.id == 'e':
    pass
  else:
    raise SyntacticError(['tk_par_der', 'tk_coma', 'tk_cadena', 'e', 'tk_entero', 'tk_real'])

