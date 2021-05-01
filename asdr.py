from main import match, SyntacticError
import globals

def begin():
  PRG()

def POS():
  if globals.token.id == '$' or globals.token.id == 'funcion' or globals.token.id == 'estructura':
    INI()
  elif globals.token.id == 'eof':
    match('eof')
  else:
    raise SyntacticError(['estructura', 'funcion', 'EOF', '$'])

def SH1():
  if globals.token.id == 'id':
    match('id')
    SHW()
  elif globals.token.id == 'tk_entero' or globals.token.id == 'tk_caracter' or globals.token.id == 'falso' or globals.token.id == 'verdadero' or globals.token.id == 'tk_real' or globals.token.id == 'tk_cadena':
    LIT()
  else:
    raise SyntacticError(['identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def DC3():
  if globals.token.id == 'id':
    match('id')
    DC0()
  else:
    raise SyntacticError(['identificador'])

def FOR():
  if globals.token.id == 'para':
    match('para')
    match('tk_par_izq')
    DCL()
    XPR()
    match('tk_pyc')
    STP()
    match('tk_par_der')
    match('hacer')
    BLK()
    match('fin_para')
  else:
    raise SyntacticError(['para'])

def LEE():
  if globals.token.id == 'leer':
    match('leer')
    match('tk_par_izq')
    INP()
    match('tk_par_der')
    match('tk_pyc')
  else:
    raise SyntacticError(['leer'])

def SHW():
  if globals.token.id == 'id':
    match('id')
    SH0()
  elif globals.token.id == 'tk_entero' or globals.token.id == 'tk_caracter' or globals.token.id == 'falso' or globals.token.id == 'verdadero' or globals.token.id == 'tk_real' or globals.token.id == 'tk_cadena':
    LIT()
    SH0()
  elif globals.token.id == 'tk_entero' or globals.token.id == 'tk_igual' or globals.token.id == 'tk_mas' or globals.token.id == 'tk_mult' or globals.token.id == 'tk_menor_igual' or globals.token.id == 'tk_div' or globals.token.id == 'verdadero' or globals.token.id == 'tk_mayor_igual' or globals.token.id == 'tk_par_izq' or globals.token.id == 'tk_mayor' or globals.token.id == 'tk_caracter' or globals.token.id == 'tk_coma' or globals.token.id == 'tk_cadena' or globals.token.id == 'tk_mod' or globals.token.id == 'tk_par_der' or globals.token.id == 'tk_menor' or globals.token.id == 'tk_menos' or globals.token.id == 'falso' or globals.token.id == 'tk_real':
    SH0()
  elif globals.token.id == 'tk_par_izq':
    match('tk_par_izq')
    ARG()
    match('tk_par_der')
    SH0()
  else:
    raise SyntacticError(['+', '-', '*', '/', '%', '<', '>', '<=', '>=', '==', ',', '(', ')', 'identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

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

def CL4():
  if globals.token.id == 'tk_par_izq':
    match('tk_par_izq')
    ARG()
    match('tk_par_der')
  elif globals.token.id == 'tk_menor' or globals.token.id == 'tk_igual' or globals.token.id == 'tk_mas' or globals.token.id == 'tk_mayor' or globals.token.id == 'tk_mult' or globals.token.id == 'tk_menos' or globals.token.id == 'tk_div' or globals.token.id == 'tk_menor_igual' or globals.token.id == 'tk_mod' or globals.token.id == 'tk_pyc' or globals.token.id == 'tk_mayor_igual':
    XP1()
  else:
    raise SyntacticError(['+', '-', '*', '/', '%', '<', '>', '<=', '>=', '==', ';', '('])

def DOW():
  if globals.token.id == 'hacer':
    match('hacer')
    BLK()
    match('mientras')
    match('tk_par_izq')
    XPR()
    match('tk_par_der')
    match('tk_pyc')
  else:
    raise SyntacticError(['hacer'])

def AR1():
  if globals.token.id == 'tk_coma':
    match('tk_coma')
    AR2()
  elif globals.token.id == 'tk_par_der' or globals.token.id == 'e':
    pass
  else:
    raise SyntacticError([',', ')'])

def XP1():
  if globals.token.id == 'tk_menor' or globals.token.id == 'tk_igual' or globals.token.id == 'tk_mas' or globals.token.id == 'tk_mayor' or globals.token.id == 'tk_mult' or globals.token.id == 'tk_menos' or globals.token.id == 'tk_div' or globals.token.id == 'tk_menor_igual' or globals.token.id == 'tk_mod' or globals.token.id == 'tk_mayor_igual':
    OPE()
    VAL()
    XP1()
  elif globals.token.id == 'tk_par_der' or globals.token.id == 'tk_pyc' or globals.token.id == 'e':
    pass
  else:
    raise SyntacticError(['+', '-', '*', '/', '%', '<', '>', '<=', '>=', '==', ';', ')'])

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

def WLE():
  if globals.token.id == 'mientras':
    match('mientras')
    match('tk_par_izq')
    XPR()
    match('tk_par_der')
    match('hacer')
    BLK()
    match('fin_mientras')
  else:
    raise SyntacticError(['mientras'])

def ATR():
  if globals.token.id == 'real' or globals.token.id == 'caracter' or globals.token.id == 'cadena' or globals.token.id == 'entero' or globals.token.id == 'booleano':
    DCL()
    ATR()
  elif globals.token.id == 'fin_estructura' or globals.token.id == 'e':
    pass
  else:
    raise SyntacticError(['booleano', 'caracter', 'entero', 'real', 'cadena', 'fin_estructura'])

def RET():
  if globals.token.id == 'retornar':
    match('retornar')
    XPR()
    match('tk_pyc')
  else:
    raise SyntacticError(['retornar'])

def INP():
  if globals.token.id == 'id':
    match('id')
    ACC()
  else:
    raise SyntacticError(['identificador'])

def BLQ():
  if globals.token.id == 'si':
    CND()
    BLQ()
  elif globals.token.id == 'id':
    CLA()
    BLQ()
  elif globals.token.id == 'real' or globals.token.id == 'caracter' or globals.token.id == 'cadena' or globals.token.id == 'entero' or globals.token.id == 'booleano':
    DCL()
    BLQ()
  elif globals.token.id == 'imprimir':
    IMP()
    BLQ()
  elif globals.token.id == 'leer':
    LEE()
    BLQ()
  elif globals.token.id == 'para':
    FOR()
    BLQ()
  elif globals.token.id == 'hacer':
    DOW()
    BLQ()
  elif globals.token.id == 'mientras':
    WLE()
    BLQ()
  elif globals.token.id == 'seleccionar':
    SEL()
    BLQ()
  elif globals.token.id == 'fin_si':
    match('fin_si')
  elif globals.token.id == 'si_no':
    match('si_no')
    BLQ()
  else:
    raise SyntacticError(['identificador', 'leer', 'imprimir', 'booleano', 'caracter', 'entero', 'real', 'cadena', 'si', 'fin_si', 'si_no', 'mientras', 'hacer', 'para', 'seleccionar'])

def INI():
  if globals.token.id == 'funcion':
    FUN()
  elif globals.token.id == 'estructura':
    SRA()
  elif globals.token.id == 'funcion_principal' or globals.token.id == 'e':
    pass
  else:
    raise SyntacticError(['funcion_principal', 'estructura', 'funcion'])

def PRM():
  if globals.token.id == 'real' or globals.token.id == 'caracter' or globals.token.id == 'cadena' or globals.token.id == 'entero' or globals.token.id == 'booleano':
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
    raise SyntacticError([',', ')', 'booleano', 'caracter', 'entero', 'real', 'cadena'])

def ARG():
  if globals.token.id == 'tk_entero' or globals.token.id == 'tk_caracter' or globals.token.id == 'falso' or globals.token.id == 'verdadero' or globals.token.id == 'tk_real' or globals.token.id == 'tk_cadena':
    LIT()
    AR1()
  elif globals.token.id == 'id':
    match('id')
    AR1()
  else:
    raise SyntacticError(['identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

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

def SEL():
  if globals.token.id == 'seleccionar':
    match('seleccionar')
    match('tk_par_izq')
    match('id')
    match('tk_par_der')
    match('entre')
    OPC()
    match('fin_seleccionar')
  else:
    raise SyntacticError(['seleccionar'])

def AR2():
  if globals.token.id == 'tk_entero' or globals.token.id == 'tk_caracter' or globals.token.id == 'falso' or globals.token.id == 'verdadero' or globals.token.id == 'tk_real' or globals.token.id == 'tk_cadena':
    LIT()
    AR1()
  elif globals.token.id == 'id':
    match('id')
    AR1()
  else:
    raise SyntacticError(['identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def CLA():
  if globals.token.id == 'id':
    match('id')
    CL2()
  else:
    raise SyntacticError(['identificador'])

def VAL():
  if globals.token.id == 'id':
    match('id')
  elif globals.token.id == 'tk_entero' or globals.token.id == 'tk_caracter' or globals.token.id == 'falso' or globals.token.id == 'verdadero' or globals.token.id == 'tk_real' or globals.token.id == 'tk_cadena':
    LIT()
  else:
    raise SyntacticError(['identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def CL3():
  if globals.token.id == 'tk_neg':
    match('tk_neg')
    match('id')
    match('tk_pyc')
  elif globals.token.id == 'tk_entero' or globals.token.id == 'tk_caracter' or globals.token.id == 'falso' or globals.token.id == 'verdadero' or globals.token.id == 'tk_real' or globals.token.id == 'tk_cadena':
    LIT()
    match('tk_pyc')
  elif globals.token.id == 'id':
    match('id')
    CL4()
    match('tk_pyc')
  else:
    raise SyntacticError(['!', 'identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def PRG():
  if globals.token.id == 'funcion' or globals.token.id == 'funcion_principal' or globals.token.id == 'estructura':
    INI()
    match('funcion_principal')
    BLK()
    match('fin_principal')
    POS()
  else:
    raise SyntacticError(['funcion_principal', 'estructura', 'funcion'])

def IMP():
  if globals.token.id == 'imprimir':
    match('imprimir')
    match('tk_par_izq')
    SHW()
    match('tk_par_der')
    match('tk_pyc')
  else:
    raise SyntacticError(['imprimir'])

def ACC():
  if globals.token.id == 'tk_punto':
    match('tk_punto')
    match('id')
    ACC()
  elif globals.token.id == 'tk_par_der' or globals.token.id == 'e':
    pass
  else:
    raise SyntacticError(['.', ')'])

def SRA():
  if globals.token.id == 'estructura':
    match('estructura')
    match('id')
    ATR()
    match('fin_estructura')
  else:
    raise SyntacticError(['estructura'])

def BLK():
  if globals.token.id == 'retornar':
    RET()
  elif globals.token.id == 'imprimir':
    IMP()
    BLK()
  elif globals.token.id == 'real' or globals.token.id == 'caracter' or globals.token.id == 'cadena' or globals.token.id == 'entero' or globals.token.id == 'booleano':
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
  elif globals.token.id == 'para':
    FOR()
    BLK()
  elif globals.token.id == 'hacer':
    DOW()
    BLK()
  elif globals.token.id == 'mientras':
    WLE()
    BLK()
  elif globals.token.id == 'seleccionar':
    SEL()
    BLK()
  elif globals.token.id == 'fin_funcion' or globals.token.id == 'e' or globals.token.id == 'fin_seleccionar' or globals.token.id == 'fin_para' or globals.token.id == 'mientras' or globals.token.id == 'defecto' or globals.token.id == 'fin_principal' or globals.token.id == 'caso' or globals.token.id == 'fin_mientras':
    pass
  else:
    raise SyntacticError(['identificador', 'fin_principal', 'leer', 'imprimir', 'booleano', 'caracter', 'entero', 'real', 'cadena', 'si', 'mientras', 'hacer', 'fin_mientras', 'para', 'fin_para', 'seleccionar', 'caso', 'defecto', 'fin_seleccionar', 'fin_funcion', 'retornar'])

def DC2():
  if globals.token.id == 'tk_coma':
    match('tk_coma')
    DC3()
  elif globals.token.id == 'tk_pyc':
    match('tk_pyc')
  else:
    raise SyntacticError([';', ','])

def XPR():
  if globals.token.id == 'tk_neg':
    match('tk_neg')
    XPR()
  elif globals.token.id == 'tk_entero' or globals.token.id == 'id' or globals.token.id == 'tk_caracter' or globals.token.id == 'falso' or globals.token.id == 'verdadero' or globals.token.id == 'tk_real' or globals.token.id == 'tk_cadena':
    VAL()
    XP1()
  else:
    raise SyntacticError(['!', 'identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def DCL():
  if globals.token.id == 'real' or globals.token.id == 'caracter' or globals.token.id == 'cadena' or globals.token.id == 'entero' or globals.token.id == 'booleano':
    TYP()
    DC3()
  else:
    raise SyntacticError(['booleano', 'caracter', 'entero', 'real', 'cadena'])

def STP():
  if globals.token.id == 'tk_entero' or globals.token.id == 'tk_caracter' or globals.token.id == 'falso' or globals.token.id == 'verdadero' or globals.token.id == 'tk_real' or globals.token.id == 'tk_cadena':
    LIT()
  else:
    raise SyntacticError(['valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

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
  elif globals.token.id == 'tk_menos':
    match('tk_menos')
  elif globals.token.id == 'tk_mult':
    match('tk_mult')
  elif globals.token.id == 'tk_div':
    match('tk_div')
  elif globals.token.id == 'tk_mod':
    match('tk_mod')
  else:
    raise SyntacticError(['+', '-', '*', '/', '%', '<', '>', '<=', '>=', '=='])

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

def OPC():
  if globals.token.id == 'caso':
    match('caso')
    LIT()
    match('tk_dosp')
    BLK()
    OPC()
  elif globals.token.id == 'defecto':
    match('defecto')
    match('tk_dosp')
    BLK()
  elif globals.token.id == 'fin_seleccionar' or globals.token.id == 'e':
    pass
  else:
    raise SyntacticError(['caso', 'defecto', 'fin_seleccionar'])

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

def SH0():
  if globals.token.id == 'tk_menor' or globals.token.id == 'tk_igual' or globals.token.id == 'tk_mas' or globals.token.id == 'tk_mayor' or globals.token.id == 'tk_mult' or globals.token.id == 'tk_menos' or globals.token.id == 'tk_div' or globals.token.id == 'tk_menor_igual' or globals.token.id == 'tk_mod' or globals.token.id == 'tk_mayor_igual':
    OPE()
    XPR()
  elif globals.token.id == 'tk_par_izq':
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
  elif globals.token.id == 'tk_entero' or globals.token.id == 'tk_caracter' or globals.token.id == 'falso' or globals.token.id == 'verdadero' or globals.token.id == 'tk_real' or globals.token.id == 'tk_cadena':
    LIT()
  elif globals.token.id == 'tk_par_der' or globals.token.id == 'e':
    pass
  else:
    raise SyntacticError(['+', '-', '*', '/', '%', '<', '>', '<=', '>=', '==', ',', '(', ')', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

