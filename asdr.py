from main import match, SyntacticError
import globals

def begin():
  PRG()

def CL2():
  if globals.token.id == 'id':
    match('id')
    match('tk_pyc')
  elif globals.token.id == 'tk_punto':
    match('tk_punto')
    match('id')
    CL5()
    match('tk_asig')
    LIT()
    match('tk_pyc')
  elif globals.token.id == 'tk_par_izq':
    match('tk_par_izq')
    ARG()
    match('tk_par_der')
  elif globals.token.id == 'tk_asig':
    match('tk_asig')
    CL3()
  else:
    raise SyntacticError(['=', '.', '(', 'identificador'])

def CL3():
  if globals.token.id == 'tk_neg':
    match('tk_neg')
    match('id')
    match('tk_pyc')
  elif globals.token.id == 'tk_caracter' or globals.token.id == 'tk_entero' or globals.token.id == 'falso' or globals.token.id == 'tk_real' or globals.token.id == 'tk_cadena' or globals.token.id == 'verdadero':
    LIT()
    match('tk_pyc')
  elif globals.token.id == 'id':
    match('id')
    CL4()
    match('tk_pyc')
  else:
    raise SyntacticError(['!', 'identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def FO1():
  if globals.token.id == 'si':
    CND()
    FO1()
  elif globals.token.id == 'id':
    CLA()
    FO1()
  elif globals.token.id == 'caracter' or globals.token.id == 'entero' or globals.token.id == 'real' or globals.token.id == 'booleano' or globals.token.id == 'cadena':
    DCL()
    FO1()
  elif globals.token.id == 'imprimir':
    IMP()
    FO1()
  elif globals.token.id == 'leer':
    LEE()
    FO1()
  elif globals.token.id == 'para':
    FOR()
    FO1()
  elif globals.token.id == 'hacer':
    DOW()
    FO1()
  elif globals.token.id == 'mientras':
    WLE()
    FO1()
  elif globals.token.id == 'seleccionar':
    SEL()
    FO1()
  elif globals.token.id == 'romper':
    match('romper')
    FO1()
  elif globals.token.id == 'fin_para':
    match('fin_para')
  else:
    raise SyntacticError(['identificador', 'leer', 'imprimir', 'booleano', 'caracter', 'entero', 'real', 'cadena', 'si', 'mientras', 'hacer', 'para', 'fin_para', 'seleccionar', 'romper'])

def ARG():
  if globals.token.id == 'tk_caracter' or globals.token.id == 'tk_entero' or globals.token.id == 'falso' or globals.token.id == 'tk_real' or globals.token.id == 'tk_cadena' or globals.token.id == 'verdadero':
    LIT()
    AR1()
  elif globals.token.id == 'id':
    match('id')
    AR1()
  else:
    raise SyntacticError(['identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def PRM():
  if globals.token.id == 'caracter' or globals.token.id == 'entero' or globals.token.id == 'real' or globals.token.id == 'booleano' or globals.token.id == 'cadena':
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
    raise SyntacticError([',', ')', 'booleano', 'caracter', 'entero', 'real', 'cadena'])

def SHW():
  if globals.token.id == 'id':
    match('id')
    SH0()
  elif globals.token.id == 'tk_caracter' or globals.token.id == 'tk_entero' or globals.token.id == 'falso' or globals.token.id == 'tk_real' or globals.token.id == 'tk_cadena' or globals.token.id == 'verdadero':
    LIT()
    SH0()
  elif globals.token.id == 'tk_mayor_igual' or globals.token.id == 'tk_menor' or globals.token.id == 'tk_par_der' or globals.token.id == 'falso' or globals.token.id == 'tk_mas' or globals.token.id == 'tk_par_izq' or globals.token.id == 'verdadero' or globals.token.id == 'tk_div' or globals.token.id == 'tk_igual' or globals.token.id == 'tk_entero' or globals.token.id == 'tk_mult' or globals.token.id == 'tk_real' or globals.token.id == 'tk_menos' or globals.token.id == 'tk_mod' or globals.token.id == 'tk_menor_igual' or globals.token.id == 'tk_caracter' or globals.token.id == 'tk_coma' or globals.token.id == 'tk_mayor' or globals.token.id == 'tk_cadena':
    SH0()
  elif globals.token.id == 'tk_par_izq':
    match('tk_par_izq')
    ARG()
    match('tk_par_der')
    SH0()
  else:
    raise SyntacticError(['+', '-', '*', '/', '%', '<', '>', '<=', '>=', '==', ',', '(', ')', 'identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def POS():
  if globals.token.id == 'funcion':
    FUN()
    POS()
  elif globals.token.id == 'estructura':
    SRA()
    POS()
  elif globals.token.id == 'eof':
    match('eof')
  else:
    raise SyntacticError(['estructura', 'funcion', 'EOF'])

def INP():
  if globals.token.id == 'id':
    match('id')
    ACC()
  else:
    raise SyntacticError(['identificador'])

def AT1():
  if globals.token.id == 'tk_coma':
    match('tk_coma')
    match('id')
    AT1()
  elif globals.token.id == 'tk_pyc' or globals.token.id == 'e':
    pass
  else:
    raise SyntacticError([';', ','])

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

def XP1():
  if globals.token.id == 'tk_mayor_igual' or globals.token.id == 'tk_menor_igual' or globals.token.id == 'tk_menor' or globals.token.id == 'tk_igual' or globals.token.id == 'tk_mult' or globals.token.id == 'tk_mas' or globals.token.id == 'tk_menos' or globals.token.id == 'tk_mayor' or globals.token.id == 'tk_div' or globals.token.id == 'tk_mod':
    OPE()
    VAL()
    XP1()
  elif globals.token.id == 'tk_pyc' or globals.token.id == 'e' or globals.token.id == 'tk_par_der':
    pass
  else:
    raise SyntacticError(['+', '-', '*', '/', '%', '<', '>', '<=', '>=', '==', ';', ')'])

def DCL():
  if globals.token.id == 'caracter' or globals.token.id == 'entero' or globals.token.id == 'real' or globals.token.id == 'booleano' or globals.token.id == 'cadena':
    TYP()
    DC3()
  else:
    raise SyntacticError(['booleano', 'caracter', 'entero', 'real', 'cadena'])

def SRA():
  if globals.token.id == 'estructura':
    match('estructura')
    match('id')
    ATR()
  else:
    raise SyntacticError(['estructura'])

def IMP():
  if globals.token.id == 'imprimir':
    match('imprimir')
    match('tk_par_izq')
    SHW()
    match('tk_par_der')
    match('tk_pyc')
  else:
    raise SyntacticError(['imprimir'])

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

def CLA():
  if globals.token.id == 'id':
    match('id')
    CL2()
  else:
    raise SyntacticError(['identificador'])

def AR1():
  if globals.token.id == 'tk_coma':
    match('tk_coma')
    AR2()
  elif globals.token.id == 'e' or globals.token.id == 'tk_par_der':
    pass
  else:
    raise SyntacticError([',', ')'])

def BLK():
  if globals.token.id == 'imprimir':
    IMP()
    BLK()
  elif globals.token.id == 'caracter' or globals.token.id == 'entero' or globals.token.id == 'real' or globals.token.id == 'booleano' or globals.token.id == 'cadena':
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
  elif globals.token.id == 'defecto' or globals.token.id == 'caso' or globals.token.id == 'fin_principal' or globals.token.id == 'e' or globals.token.id == 'fin_seleccionar':
    pass
  else:
    raise SyntacticError(['identificador', 'fin_principal', 'leer', 'imprimir', 'booleano', 'caracter', 'entero', 'real', 'cadena', 'si', 'mientras', 'hacer', 'para', 'seleccionar', 'caso', 'defecto', 'fin_seleccionar'])

def RET():
  if globals.token.id == 'retornar':
    match('retornar')
    XPR()
    match('tk_pyc')
  else:
    raise SyntacticError(['retornar'])

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

def WLE():
  if globals.token.id == 'mientras':
    match('mientras')
    match('tk_par_izq')
    XPR()
    match('tk_par_der')
    match('hacer')
    WL1()
  else:
    raise SyntacticError(['mientras'])

def SH0():
  if globals.token.id == 'tk_mayor_igual' or globals.token.id == 'tk_menor_igual' or globals.token.id == 'tk_menor' or globals.token.id == 'tk_igual' or globals.token.id == 'tk_mult' or globals.token.id == 'tk_mas' or globals.token.id == 'tk_menos' or globals.token.id == 'tk_mayor' or globals.token.id == 'tk_div' or globals.token.id == 'tk_mod':
    OPE()
    XPR()
  elif globals.token.id == 'tk_par_izq':
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
  elif globals.token.id == 'tk_caracter' or globals.token.id == 'tk_entero' or globals.token.id == 'falso' or globals.token.id == 'tk_real' or globals.token.id == 'tk_cadena' or globals.token.id == 'verdadero':
    LIT()
  elif globals.token.id == 'e' or globals.token.id == 'tk_par_der':
    pass
  else:
    raise SyntacticError(['+', '-', '*', '/', '%', '<', '>', '<=', '>=', '==', ',', '(', ')', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def VAL():
  if globals.token.id == 'id':
    match('id')
  elif globals.token.id == 'tk_caracter' or globals.token.id == 'tk_entero' or globals.token.id == 'falso' or globals.token.id == 'tk_real' or globals.token.id == 'tk_cadena' or globals.token.id == 'verdadero':
    LIT()
  else:
    raise SyntacticError(['identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def DO1():
  if globals.token.id == 'si':
    CND()
    DO1()
  elif globals.token.id == 'id':
    CLA()
    DO1()
  elif globals.token.id == 'caracter' or globals.token.id == 'entero' or globals.token.id == 'real' or globals.token.id == 'booleano' or globals.token.id == 'cadena':
    DCL()
    DO1()
  elif globals.token.id == 'imprimir':
    IMP()
    DO1()
  elif globals.token.id == 'leer':
    LEE()
    DO1()
  elif globals.token.id == 'para':
    FOR()
    DO1()
  elif globals.token.id == 'hacer':
    DOW()
    DO1()
  elif globals.token.id == 'mientras':
    WLE()
    DO1()
  elif globals.token.id == 'seleccionar':
    SEL()
    DO1()
  elif globals.token.id == 'romper':
    match('romper')
    DO1()
  elif globals.token.id == 'mientras':
    match('mientras')
  else:
    raise SyntacticError(['identificador', 'leer', 'imprimir', 'booleano', 'caracter', 'entero', 'real', 'cadena', 'si', 'mientras', 'hacer', 'para', 'seleccionar', 'romper'])

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
    FO1()
  else:
    raise SyntacticError(['para'])

def CL5():
  if globals.token.id == 'tk_punto':
    match('tk_punto')
    match('id')
    CL5()
  elif globals.token.id == 'e' or globals.token.id == 'tk_asig':
    pass
  else:
    raise SyntacticError(['=', '.'])

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
  elif globals.token.id == 'tk_caracter' or globals.token.id == 'tk_entero' or globals.token.id == 'verdadero' or globals.token.id == 'falso' or globals.token.id == 'tk_real' or globals.token.id == 'tk_cadena' or globals.token.id == 'id':
    VAL()
    XP1()
  else:
    raise SyntacticError(['!', 'identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def SH1():
  if globals.token.id == 'id':
    match('id')
    SHW()
  elif globals.token.id == 'tk_caracter' or globals.token.id == 'tk_entero' or globals.token.id == 'falso' or globals.token.id == 'tk_real' or globals.token.id == 'tk_cadena' or globals.token.id == 'verdadero':
    LIT()
  else:
    raise SyntacticError(['identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

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

def DOW():
  if globals.token.id == 'hacer':
    match('hacer')
    DO1()
    match('tk_par_izq')
    XPR()
    match('tk_par_der')
    match('tk_pyc')
  else:
    raise SyntacticError(['hacer'])

def LGC():
  if globals.token.id == 'imprimir':
    IMP()
    LGC()
  elif globals.token.id == 'caracter' or globals.token.id == 'entero' or globals.token.id == 'real' or globals.token.id == 'booleano' or globals.token.id == 'cadena':
    DCL()
    LGC()
  elif globals.token.id == 'si':
    CND()
    LGC()
  elif globals.token.id == 'id':
    CLA()
    LGC()
  elif globals.token.id == 'leer':
    LEE()
    LGC()
  elif globals.token.id == 'para':
    FOR()
    LGC()
  elif globals.token.id == 'hacer':
    DOW()
    LGC()
  elif globals.token.id == 'mientras':
    WLE()
    LGC()
  elif globals.token.id == 'seleccionar':
    SEL()
    LGC()
  elif globals.token.id == 'retornar' or globals.token.id == 'e':
    pass
  elif globals.token.id == 'romper':
    match('romper')
    LGC()
  else:
    raise SyntacticError(['identificador', 'leer', 'imprimir', 'booleano', 'caracter', 'entero', 'real', 'cadena', 'si', 'mientras', 'hacer', 'para', 'seleccionar', 'romper', 'retornar'])

def TPO():
  if globals.token.id == 'id':
    match('id')
  elif globals.token.id == 'caracter' or globals.token.id == 'entero' or globals.token.id == 'real' or globals.token.id == 'booleano' or globals.token.id == 'cadena':
    TYP()
  else:
    raise SyntacticError(['identificador', 'booleano', 'caracter', 'entero', 'real', 'cadena'])

def STP():
  if globals.token.id == 'tk_caracter' or globals.token.id == 'tk_entero' or globals.token.id == 'falso' or globals.token.id == 'tk_real' or globals.token.id == 'tk_cadena' or globals.token.id == 'verdadero':
    LIT()
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
    LGC()
    RET()
    match('fin_funcion')
  else:
    raise SyntacticError(['funcion'])

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
  elif globals.token.id == 'e' or globals.token.id == 'fin_seleccionar':
    pass
  else:
    raise SyntacticError(['caso', 'defecto', 'fin_seleccionar'])

def WL1():
  if globals.token.id == 'si':
    CND()
    WL1()
  elif globals.token.id == 'id':
    CLA()
    WL1()
  elif globals.token.id == 'caracter' or globals.token.id == 'entero' or globals.token.id == 'real' or globals.token.id == 'booleano' or globals.token.id == 'cadena':
    DCL()
    WL1()
  elif globals.token.id == 'imprimir':
    IMP()
    WL1()
  elif globals.token.id == 'leer':
    LEE()
    WL1()
  elif globals.token.id == 'para':
    FOR()
    WL1()
  elif globals.token.id == 'hacer':
    DOW()
    WL1()
  elif globals.token.id == 'mientras':
    WLE()
    WL1()
  elif globals.token.id == 'seleccionar':
    SEL()
    WL1()
  elif globals.token.id == 'romper':
    match('romper')
    WL1()
  elif globals.token.id == 'fin_mientras':
    match('fin_mientras')
  else:
    raise SyntacticError(['identificador', 'leer', 'imprimir', 'booleano', 'caracter', 'entero', 'real', 'cadena', 'si', 'mientras', 'hacer', 'fin_mientras', 'para', 'seleccionar', 'romper'])

def DC3():
  if globals.token.id == 'id':
    match('id')
    DC0()
  else:
    raise SyntacticError(['identificador'])

def BLQ():
  if globals.token.id == 'si':
    CND()
    BLQ()
  elif globals.token.id == 'id':
    CLA()
    BLQ()
  elif globals.token.id == 'caracter' or globals.token.id == 'entero' or globals.token.id == 'real' or globals.token.id == 'booleano' or globals.token.id == 'cadena':
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

def ATR():
  if globals.token.id == 'caracter' or globals.token.id == 'entero' or globals.token.id == 'real' or globals.token.id == 'booleano' or globals.token.id == 'cadena' or globals.token.id == 'id':
    TPO()
    match('id')
    AT1()
    match('tk_pyc')
    ATR()
  elif globals.token.id == 'fin_estructura':
    match('fin_estructura')
  else:
    raise SyntacticError(['identificador', 'booleano', 'caracter', 'entero', 'real', 'cadena', 'fin_estructura'])

def CL4():
  if globals.token.id == 'tk_par_izq':
    match('tk_par_izq')
    ARG()
    match('tk_par_der')
  elif globals.token.id == 'tk_mayor_igual' or globals.token.id == 'tk_menor_igual' or globals.token.id == 'tk_menor' or globals.token.id == 'tk_igual' or globals.token.id == 'tk_pyc' or globals.token.id == 'tk_mult' or globals.token.id == 'tk_mas' or globals.token.id == 'tk_menos' or globals.token.id == 'tk_mayor' or globals.token.id == 'tk_div' or globals.token.id == 'tk_mod':
    XP1()
  else:
    raise SyntacticError(['+', '-', '*', '/', '%', '<', '>', '<=', '>=', '==', ';', '('])

def INI():
  if globals.token.id == 'funcion':
    FUN()
    INI()
  elif globals.token.id == 'estructura':
    SRA()
    INI()
  elif globals.token.id == 'funcion_principal' or globals.token.id == 'e':
    pass
  else:
    raise SyntacticError(['funcion_principal', 'estructura', 'funcion'])

def ACC():
  if globals.token.id == 'tk_punto':
    match('tk_punto')
    match('id')
    ACC()
  elif globals.token.id == 'e' or globals.token.id == 'tk_par_der':
    pass
  else:
    raise SyntacticError(['.', ')'])

def LEE():
  if globals.token.id == 'leer':
    match('leer')
    match('tk_par_izq')
    INP()
    match('tk_par_der')
    match('tk_pyc')
  else:
    raise SyntacticError(['leer'])

def PRG():
  if globals.token.id == 'funcion_principal' or globals.token.id == 'estructura' or globals.token.id == 'funcion':
    INI()
    match('funcion_principal')
    BLK()
    match('fin_principal')
    POS()
  else:
    raise SyntacticError(['funcion_principal', 'estructura', 'funcion'])

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

def AR2():
  if globals.token.id == 'tk_caracter' or globals.token.id == 'tk_entero' or globals.token.id == 'falso' or globals.token.id == 'tk_real' or globals.token.id == 'tk_cadena' or globals.token.id == 'verdadero':
    LIT()
    AR1()
  elif globals.token.id == 'id':
    match('id')
    AR1()
  else:
    raise SyntacticError(['identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

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

