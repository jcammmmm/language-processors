from main import match, SyntacticError
import globals

def begin():
  PRG()

def BLQ():
  if globals.token.id == 'si':
    CND()
    BLQ()
  elif globals.token.id == 'id':
    CLA()
    BLQ()
  elif globals.token.id == 'booleano' or globals.token.id == 'cadena' or globals.token.id == 'caracter' or globals.token.id == 'real' or globals.token.id == 'entero':
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
    raise SyntacticError(['identificador', 'leer', 'imprimir', 'booleano', 'caracter', 'entero', 'real', 'cadena', 'si', 'fin_si', 'si_no'])

def SH0():
  if globals.token.id == 'tk_par_izq':
    match('tk_par_izq')
    ARG()
    match('tk_par_der')
  elif globals.token.id == 'tk_par_der' or globals.token.id == 'e':
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
  elif globals.token.id == 'tk_real' or globals.token.id == 'tk_cadena' or globals.token.id == 'falso' or globals.token.id == 'tk_entero' or globals.token.id == 'verdadero' or globals.token.id == 'tk_caracter':
    LIT()
  elif globals.token.id == 'tk_par_der' or globals.token.id == 'e':
    pass
  else:
    raise SyntacticError([',', '(', ')', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero', 'e'])

def DCL():
  if globals.token.id == 'booleano' or globals.token.id == 'cadena' or globals.token.id == 'caracter' or globals.token.id == 'real' or globals.token.id == 'entero':
    TYP()
    DC3()
  else:
    raise SyntacticError(['booleano', 'caracter', 'entero', 'real', 'cadena'])

def SHW():
  if globals.token.id == 'id':
    match('id')
    SH0()
  elif globals.token.id == 'tk_real' or globals.token.id == 'tk_cadena' or globals.token.id == 'falso' or globals.token.id == 'tk_entero' or globals.token.id == 'verdadero' or globals.token.id == 'tk_caracter':
    LIT()
    SH0()
  elif globals.token.id == 'tk_real' or globals.token.id == 'tk_coma' or globals.token.id == 'tk_cadena' or globals.token.id == 'falso' or globals.token.id == 'tk_entero' or globals.token.id == 'tk_par_der' or globals.token.id == 'tk_par_izq' or globals.token.id == 'verdadero' or globals.token.id == 'tk_caracter':
    SH0()
  elif globals.token.id == 'tk_par_izq':
    match('tk_par_izq')
    ARG()
    match('tk_par_der')
    SH0()
  else:
    raise SyntacticError([',', '(', ')', 'identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def TYP():
  if globals.token.id == 'booleano':
    match('booleano')
  elif globals.token.id == 'caracter':
    match('caracter')
  elif globals.token.id == 'entero':
    match('entero')
  elif globals.token.id == 'real':
    match('real')
  elif globals.token.id == 'cadena':
    match('cadena')
  else:
    raise SyntacticError(['booleano', 'caracter', 'entero', 'real', 'cadena'])

def XPR():
  if globals.token.id == 'tk_neg':
    match('tk_neg')
    XPR()
  elif globals.token.id == 'id':
    match('id')
    XP1()
  else:
    raise SyntacticError(['!', 'identificador'])

def AR2():
  if globals.token.id == 'tk_real' or globals.token.id == 'tk_cadena' or globals.token.id == 'falso' or globals.token.id == 'tk_entero' or globals.token.id == 'verdadero' or globals.token.id == 'tk_caracter':
    LIT()
    AR1()
  elif globals.token.id == 'id':
    match('id')
    AR1()
  else:
    raise SyntacticError(['identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def DC3():
  if globals.token.id == 'id':
    match('id')
    DC0()
  else:
    raise SyntacticError(['identificador'])

def SH1():
  if globals.token.id == 'id':
    match('id')
    SHW()
  elif globals.token.id == 'tk_real' or globals.token.id == 'tk_cadena' or globals.token.id == 'falso' or globals.token.id == 'tk_entero' or globals.token.id == 'verdadero' or globals.token.id == 'tk_caracter':
    LIT()
  else:
    raise SyntacticError(['identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def AR1():
  if globals.token.id == 'tk_coma':
    match('tk_coma')
    AR2()
  elif globals.token.id == 'tk_par_der' or globals.token.id == 'e':
    pass
  else:
    raise SyntacticError([',', ')', 'e'])

def XP1():
  if globals.token.id == 'tk_mayor' or globals.token.id == 'tk_menor_igual' or globals.token.id == 'tk_igual' or globals.token.id == 'tk_mayor_igual' or globals.token.id == 'tk_mas' or globals.token.id == 'tk_menor':
    OPE()
    match('id')
  elif globals.token.id == 'tk_par_der' or globals.token.id == 'tk_pyc' or globals.token.id == 'e':
    pass
  else:
    raise SyntacticError(['+', '<', '>', '<=', '>=', '==', ';', ')', 'e'])

def DC2():
  if globals.token.id == 'tk_coma':
    match('tk_coma')
    DC3()
  elif globals.token.id == 'tk_pyc':
    match('tk_pyc')
  else:
    raise SyntacticError([';', ','])

def SRA():
  if globals.token.id == 'estructura':
    match('estructura')
    match('id')
    ATR()
    match('fin_estructura')
  else:
    raise SyntacticError(['estructura'])

def DC0():
  if globals.token.id == 'tk_pyc':
    match('tk_pyc')
  elif globals.token.id == 'tk_coma':
    match('tk_coma')
    DC3()
  elif globals.token.id == 'tk_asig':
    match('tk_asig')
    LIT()
    DC2()
  else:
    raise SyntacticError(['=', ';', ','])

def BLK():
  if globals.token.id == 'retornar':
    RET()
  elif globals.token.id == 'imprimir':
    IMP()
    BLK()
  elif globals.token.id == 'booleano' or globals.token.id == 'cadena' or globals.token.id == 'caracter' or globals.token.id == 'real' or globals.token.id == 'entero':
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
  elif globals.token.id == 'fin_principal' or globals.token.id == 'fin_funcion' or globals.token.id == 'e':
    pass
  else:
    raise SyntacticError(['identificador', 'fin_principal', 'leer', 'imprimir', 'booleano', 'caracter', 'entero', 'real', 'cadena', 'si', 'fin_funcion', 'retornar', 'e'])

def ATR():
  if globals.token.id == 'booleano' or globals.token.id == 'cadena' or globals.token.id == 'caracter' or globals.token.id == 'real' or globals.token.id == 'entero':
    DCL()
    ATR()
  elif globals.token.id == 'fin_estructura' or globals.token.id == 'e':
    pass
  else:
    raise SyntacticError(['booleano', 'caracter', 'entero', 'real', 'cadena', 'fin_estructura', 'e'])

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
    raise SyntacticError(['+', '<', '>', '<=', '>=', '=='])

def IMP():
  if globals.token.id == 'imprimir':
    match('imprimir')
    match('tk_par_izq')
    SHW()
    match('tk_par_der')
    match('tk_pyc')
  else:
    raise SyntacticError(['imprimir'])

def PRM():
  if globals.token.id == 'booleano' or globals.token.id == 'cadena' or globals.token.id == 'caracter' or globals.token.id == 'real' or globals.token.id == 'entero':
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
    raise SyntacticError([',', ')', 'booleano', 'caracter', 'entero', 'real', 'cadena', 'e'])

def CL3():
  if globals.token.id == 'tk_real' or globals.token.id == 'tk_cadena' or globals.token.id == 'falso' or globals.token.id == 'tk_entero' or globals.token.id == 'verdadero' or globals.token.id == 'tk_caracter':
    LIT()
    match('tk_pyc')
  elif globals.token.id == 'id':
    match('id')
    CL4()
  else:
    raise SyntacticError(['identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

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
  if globals.token.id == 'funcion' or globals.token.id == 'estructura' or globals.token.id == 'funcion_principal':
    INI()
    match('funcion_principal')
    BLK()
    match('fin_principal')
    POS()
  else:
    raise SyntacticError(['funcion_principal', 'estructura', 'funcion'])

def CL2():
  if globals.token.id == 'tk_par_izq':
    match('tk_par_izq')
    ARG()
    match('tk_par_der')
  elif globals.token.id == 'tk_asig':
    match('tk_asig')
    CL3()
  else:
    raise SyntacticError(['=', '('])

def POS():
  if globals.token.id == 'funcion' or globals.token.id == 'estructura' or globals.token.id == '$':
    INI()
  elif globals.token.id == 'eof':
    match('eof')
  else:
    raise SyntacticError(['estructura', 'funcion', 'EOF', '$'])

def ARG():
  if globals.token.id == 'tk_real' or globals.token.id == 'tk_cadena' or globals.token.id == 'falso' or globals.token.id == 'tk_entero' or globals.token.id == 'verdadero' or globals.token.id == 'tk_caracter':
    LIT()
    AR1()
  elif globals.token.id == 'id':
    match('id')
    AR1()
  else:
    raise SyntacticError(['identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def RET():
  if globals.token.id == 'retornar':
    match('retornar')
    XPR()
    match('tk_pyc')
  else:
    raise SyntacticError(['retornar'])

def LIT():
  if globals.token.id == 'verdadero':
    match('verdadero')
  elif globals.token.id == 'falso':
    match('falso')
  elif globals.token.id == 'tk_caracter':
    match('tk_caracter')
  elif globals.token.id == 'tk_entero':
    match('tk_entero')
  elif globals.token.id == 'tk_real':
    match('tk_real')
  elif globals.token.id == 'tk_cadena':
    match('tk_cadena')
  else:
    raise SyntacticError(['valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

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

def CL4():
  if globals.token.id == 'tk_pyc':
    match('tk_pyc')
  elif globals.token.id == 'tk_par_izq':
    match('tk_par_izq')
    ARG()
    match('tk_par_der')
    match('tk_pyc')
  else:
    raise SyntacticError([';', '('])

def LEE():
  if globals.token.id == 'leer':
    match('leer')
    match('tk_par_izq')
    match('id')
    match('tk_par_der')
    match('tk_pyc')
  else:
    raise SyntacticError(['leer'])

def CLA():
  if globals.token.id == 'id':
    match('id')
    CL2()
  else:
    raise SyntacticError(['identificador'])

def INI():
  if globals.token.id == 'funcion':
    FUN()
  elif globals.token.id == 'estructura':
    SRA()
  elif globals.token.id == 'funcion_principal' or globals.token.id == 'e':
    pass
  else:
    raise SyntacticError(['funcion_principal', 'estructura', 'funcion', 'e'])

