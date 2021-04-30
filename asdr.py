from main import match, SyntacticError
import globals

def begin():
  PRG()

def CL3():
  if globals.token.id == 'tk_entero' or globals.token.id == 'tk_cadena' or globals.token.id == 'tk_real':
    LIT()
    match('tk_pyc')
  elif globals.token.id == 'id':
    match('id')
    CL4()
  else:
    raise SyntacticError(['id', 'tk_entero', 'tk_cadena', 'tk_real'])

def CLA():
  if globals.token.id == 'id':
    match('id')
    CL2()
  else:
    raise SyntacticError(['id'])

def XPR():
  if globals.token.id == 'tk_neg':
    match('tk_neg')
    XPR()
  elif globals.token.id == 'id':
    match('id')
    XP1()
  else:
    raise SyntacticError(['id', 'tk_neg'])

def DC0():
  if globals.token.id == 'tk_coma':
    match('tk_coma')
    DC1()
  elif globals.token.id == 'tk_pyc':
    match('tk_pyc')
  else:
    raise SyntacticError(['tk_pyc', 'tk_coma'])

def ATR():
  if globals.token.id == 'real' or globals.token.id == 'entero':
    DCL()
    ATR()
  elif globals.token.id == 'e' or globals.token.id == 'fin_estructura':
    pass
  else:
    raise SyntacticError(['real', 'entero', 'e', 'fin_estructura'])

def IMP():
  if globals.token.id == 'imprimir':
    match('imprimir')
    match('tk_par_izq')
    SHW()
    match('tk_par_der')
    match('tk_pyc')
  else:
    raise SyntacticError(['imprimir'])

def INI():
  if globals.token.id == 'funcion':
    FUN()
  elif globals.token.id == 'estructura':
    SRA()
  elif globals.token.id == 'funcion_principal' or globals.token.id == 'e':
    pass
  else:
    raise SyntacticError(['funcion_principal', 'e', 'estructura', 'funcion'])

def CL4():
  if globals.token.id == 'tk_pyc':
    match('tk_pyc')
  elif globals.token.id == 'tk_par_izq':
    match('tk_par_izq')
    ARG()
    match('tk_par_der')
    match('tk_pyc')
  else:
    raise SyntacticError(['tk_pyc', 'tk_par_izq'])

def LIT():
  if globals.token.id == 'tk_entero':
    match('tk_entero')
  elif globals.token.id == 'tk_real':
    match('tk_real')
  elif globals.token.id == 'tk_cadena':
    match('tk_cadena')
  else:
    raise SyntacticError(['tk_entero', 'tk_cadena', 'tk_real'])

def BLQ():
  if globals.token.id == 'si':
    CND()
    BLQ()
  elif globals.token.id == 'id':
    CLA()
    BLQ()
  elif globals.token.id == 'real' or globals.token.id == 'entero':
    DCL()
    BLQ()
  elif globals.token.id == 'imprimir':
    IMP()
    BLQ()
  elif globals.token.id == 'leer':
    LEE()
    BLQ()
  elif globals.token.id == 'fin_si':
    match('fin_si')
  elif globals.token.id == 'si_no':
    match('si_no')
    BLQ()
  else:
    raise SyntacticError(['id', 'imprimir', 'fin_si', 'real', 'entero', 'si', 'leer', 'si_no'])

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
  elif globals.token.id == 'e' or globals.token.id == 'tk_par_der':
    pass
  else:
    raise SyntacticError(['e', 'real', 'entero', 'tk_par_der', 'tk_coma'])

def AR1():
  if globals.token.id == 'tk_coma':
    match('tk_coma')
    AR2()
  elif globals.token.id == 'e' or globals.token.id == 'tk_par_der':
    pass
  else:
    raise SyntacticError(['e', 'tk_coma', 'tk_par_der'])

def DC1():
  if globals.token.id == 'id':
    match('id')
    DC2()
  else:
    raise SyntacticError(['id'])

def BLK():
  if globals.token.id == 'retornar':
    RET()
  elif globals.token.id == 'imprimir':
    IMP()
    BLK()
  elif globals.token.id == 'real' or globals.token.id == 'entero':
    DCL()
    BLK()
  elif globals.token.id == 'si':
    CND()
    BLK()
  elif globals.token.id == 'id':
    CLA()
    BLK()
  elif globals.token.id == 'leer':
    LEE()
    BLK()
  elif globals.token.id == 'e' or globals.token.id == 'fin_principal' or globals.token.id == 'fin_funcion':
    pass
  else:
    raise SyntacticError(['id', 'imprimir', 'e', 'fin_funcion', 'real', 'entero', 'fin_principal', 'si', 'leer', 'retornar'])

def XP1():
  if globals.token.id == 'tk_menor_igual' or globals.token.id == 'tk_mayor_igual' or globals.token.id == 'tk_igual' or globals.token.id == 'tk_mayor' or globals.token.id == 'tk_mas' or globals.token.id == 'tk_menor':
    OPE()
    match('id')
  elif globals.token.id == 'e' or globals.token.id == 'tk_pyc' or globals.token.id == 'tk_par_der':
    pass
  else:
    raise SyntacticError(['tk_menor_igual', 'tk_pyc', 'tk_mayor_igual', 'tk_igual', 'e', 'tk_mayor', 'tk_mas', 'tk_par_der', 'tk_menor'])

def LEE():
  if globals.token.id == 'leer':
    match('leer')
    match('tk_par_izq')
    match('id')
    match('tk_par_der')
    match('tk_pyc')
  else:
    raise SyntacticError(['leer'])

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

def SH1():
  if globals.token.id == 'id':
    match('id')
    SHW()
  elif globals.token.id == 'tk_entero' or globals.token.id == 'tk_cadena' or globals.token.id == 'tk_real':
    LIT()
  else:
    raise SyntacticError(['id', 'tk_entero', 'tk_cadena', 'tk_real'])

def SH0():
  if globals.token.id == 'tk_par_izq':
    match('tk_par_izq')
    ARG()
    match('tk_par_der')
  elif globals.token.id == 'e' or globals.token.id == 'tk_par_der':
    pass
  elif globals.token.id == 'tk_coma':
    match('tk_coma')
    match('id')
    SH0()
  elif globals.token.id == 'tk_par_izq':
    match('tk_par_izq')
    ARG()
    match('tk_par_der')
    SH0()
  elif globals.token.id == 'tk_entero' or globals.token.id == 'tk_cadena' or globals.token.id == 'tk_real':
    LIT()
  elif globals.token.id == 'e' or globals.token.id == 'tk_par_der':
    pass
  else:
    raise SyntacticError(['tk_par_izq', 'tk_real', 'e', 'tk_entero', 'tk_par_der', 'tk_cadena', 'tk_coma'])

def PRG():
  if globals.token.id == 'funcion_principal' or globals.token.id == 'funcion' or globals.token.id == 'estructura':
    INI()
    match('funcion_principal')
    BLK()
    match('fin_principal')
    POS()
  else:
    raise SyntacticError(['funcion_principal', 'estructura', 'funcion'])

def SHW():
  if globals.token.id == 'id':
    match('id')
    SH0()
  elif globals.token.id == 'tk_entero' or globals.token.id == 'tk_cadena' or globals.token.id == 'tk_real':
    LIT()
    SH0()
  elif globals.token.id == 'tk_par_izq' or globals.token.id == 'tk_real' or globals.token.id == 'tk_entero' or globals.token.id == 'tk_par_der' or globals.token.id == 'tk_cadena' or globals.token.id == 'tk_coma':
    SH0()
  elif globals.token.id == 'tk_par_izq':
    match('tk_par_izq')
    ARG()
    match('tk_par_der')
    SH0()
  else:
    raise SyntacticError(['id', 'tk_par_izq', 'tk_real', 'tk_entero', 'tk_par_der', 'tk_cadena', 'tk_coma'])

def DC2():
  if globals.token.id == 'tk_coma':
    match('tk_coma')
    match('id')
    DC2()
  elif globals.token.id == 'tk_pyc':
    match('tk_pyc')
  else:
    raise SyntacticError(['tk_pyc', 'tk_coma'])

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
    raise SyntacticError(['tk_menor_igual', 'tk_igual', 'tk_mayor_igual', 'tk_mayor', 'tk_mas', 'tk_menor'])

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

def ARG():
  if globals.token.id == 'tk_entero' or globals.token.id == 'tk_cadena' or globals.token.id == 'tk_real':
    LIT()
    AR1()
  elif globals.token.id == 'id':
    match('id')
    AR1()
  else:
    raise SyntacticError(['id', 'tk_entero', 'tk_cadena', 'tk_real'])

def DCL():
  if globals.token.id == 'real' or globals.token.id == 'entero':
    TYP()
    match('id')
    DC0()
  else:
    raise SyntacticError(['real', 'entero'])

def RET():
  if globals.token.id == 'retornar':
    match('retornar')
    XPR()
    match('tk_pyc')
  else:
    raise SyntacticError(['retornar'])

def POS():
  if globals.token.id == '$' or globals.token.id == 'funcion' or globals.token.id == 'estructura':
    INI()
  elif globals.token.id == 'eof':
    match('eof')
  else:
    raise SyntacticError(['estructura', 'eof', '$', 'funcion'])

def TYP():
  if globals.token.id == 'entero':
    match('entero')
  elif globals.token.id == 'real':
    match('real')
  else:
    raise SyntacticError(['real', 'entero'])

def SRA():
  if globals.token.id == 'estructura':
    match('estructura')
    match('id')
    ATR()
    match('fin_estructura')
  else:
    raise SyntacticError(['estructura'])

def AR2():
  if globals.token.id == 'tk_entero' or globals.token.id == 'tk_cadena' or globals.token.id == 'tk_real':
    LIT()
    AR1()
  elif globals.token.id == 'id':
    match('id')
    AR1()
  else:
    raise SyntacticError(['id', 'tk_entero', 'tk_cadena', 'tk_real'])

def CL2():
  if globals.token.id == 'tk_par_izq':
    match('tk_par_izq')
    ARG()
    match('tk_par_der')
  elif globals.token.id == 'tk_asig':
    match('tk_asig')
    CL3()
  else:
    raise SyntacticError(['tk_par_izq', 'tk_asig'])

