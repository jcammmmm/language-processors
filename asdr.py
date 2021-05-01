import syntax as s
import globals

def begin():
  PRG()

def PRM():
  if globals.token.id == 'caracter' or globals.token.id == 'real' or globals.token.id == 'booleano' or globals.token.id == 'entero' or globals.token.id == 'cadena':
    TYP()
    s.match('id')
    PRM()
  elif globals.token.id == 'tk_coma':
    s.match('tk_coma')
    TYP()
    s.match('id')
    PRM()
  elif globals.token.id == 'e' or globals.token.id == 'tk_par_der':
    pass
  else:
    raise s.SyntacticError([',', ')', 'booleano', 'caracter', 'entero', 'real', 'cadena'])

def VAL():
  if globals.token.id == 'id':
    s.match('id')
  elif globals.token.id == 'falso' or globals.token.id == 'tk_caracter' or globals.token.id == 'tk_real' or globals.token.id == 'tk_entero' or globals.token.id == 'verdadero' or globals.token.id == 'tk_cadena':
    LIT()
  else:
    raise s.SyntacticError(['identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def SRA():
  if globals.token.id == 'estructura':
    s.match('estructura')
    s.match('id')
    ATR()
  else:
    raise s.SyntacticError(['estructura'])

def INI():
  if globals.token.id == 'funcion':
    FUN()
    INI()
  elif globals.token.id == 'estructura':
    SRA()
    INI()
  elif globals.token.id == 'e' or globals.token.id == 'funcion_principal':
    pass
  else:
    raise s.SyntacticError(['funcion_principal', 'estructura', 'funcion'])

def SH0():
  if globals.token.id == 'tk_mayor' or globals.token.id == 'tk_div' or globals.token.id == 'tk_menor' or globals.token.id == 'tk_mult' or globals.token.id == 'tk_mod' or globals.token.id == 'tk_menor_igual' or globals.token.id == 'tk_mayor_igual' or globals.token.id == 'tk_igual' or globals.token.id == 'tk_mas' or globals.token.id == 'tk_menos':
    OPE()
    XPR()
  elif globals.token.id == 'tk_par_izq':
    s.match('tk_par_izq')
    ARG()
    s.match('tk_par_der')
  elif globals.token.id == 'e' or globals.token.id == 'tk_par_der':
    pass
  elif globals.token.id == 'tk_coma':
    s.match('tk_coma')
    s.match('id')
    SH0()
  elif globals.token.id == 'tk_par_izq':
    s.match('tk_par_izq')
    ARG()
    s.match('tk_par_der')
    SH0()
  elif globals.token.id == 'falso' or globals.token.id == 'tk_caracter' or globals.token.id == 'tk_real' or globals.token.id == 'tk_entero' or globals.token.id == 'verdadero' or globals.token.id == 'tk_cadena':
    LIT()
  elif globals.token.id == 'e' or globals.token.id == 'tk_par_der':
    pass
  else:
    raise s.SyntacticError(['+', '-', '*', '/', '%', '<', '>', '<=', '>=', '==', ',', '(', ')', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def SH1():
  if globals.token.id == 'id':
    s.match('id')
    SHW()
  elif globals.token.id == 'falso' or globals.token.id == 'tk_caracter' or globals.token.id == 'tk_real' or globals.token.id == 'tk_entero' or globals.token.id == 'verdadero' or globals.token.id == 'tk_cadena':
    LIT()
  else:
    raise s.SyntacticError(['identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def INP():
  if globals.token.id == 'id':
    s.match('id')
    ACC()
  else:
    raise s.SyntacticError(['identificador'])

def CL4():
  if globals.token.id == 'tk_par_izq':
    s.match('tk_par_izq')
    ARG()
    s.match('tk_par_der')
  elif globals.token.id == 'tk_mayor' or globals.token.id == 'tk_menor' or globals.token.id == 'tk_div' or globals.token.id == 'tk_mult' or globals.token.id == 'tk_mod' or globals.token.id == 'tk_pyc' or globals.token.id == 'tk_menor_igual' or globals.token.id == 'tk_mayor_igual' or globals.token.id == 'tk_igual' or globals.token.id == 'tk_mas' or globals.token.id == 'tk_menos':
    XP1()
  else:
    raise s.SyntacticError(['+', '-', '*', '/', '%', '<', '>', '<=', '>=', '==', ';', '('])

def PRG():
  if globals.token.id == 'funcion' or globals.token.id == 'estructura' or globals.token.id == 'funcion_principal':
    INI()
    s.match('funcion_principal')
    BLK()
    s.match('fin_principal')
    POS()
  else:
    raise s.SyntacticError(['funcion_principal', 'estructura', 'funcion'])

def TYP():
  if globals.token.id == 'booleano':
    s.match('booleano')
  elif globals.token.id == 'caracter':
    s.match('caracter')
  elif globals.token.id == 'entero':
    s.match('entero')
  elif globals.token.id == 'real':
    s.match('real')
  elif globals.token.id == 'cadena':
    s.match('cadena')
  else:
    raise s.SyntacticError(['booleano', 'caracter', 'entero', 'real', 'cadena'])

def WLE():
  if globals.token.id == 'mientras':
    s.match('mientras')
    s.match('tk_par_izq')
    XPR()
    s.match('tk_par_der')
    s.match('hacer')
    WL1()
  else:
    raise s.SyntacticError(['mientras'])

def XP1():
  if globals.token.id == 'tk_mayor' or globals.token.id == 'tk_div' or globals.token.id == 'tk_menor' or globals.token.id == 'tk_mult' or globals.token.id == 'tk_mod' or globals.token.id == 'tk_menor_igual' or globals.token.id == 'tk_mayor_igual' or globals.token.id == 'tk_igual' or globals.token.id == 'tk_mas' or globals.token.id == 'tk_menos':
    OPE()
    VAL()
    XP1()
  elif globals.token.id == 'e' or globals.token.id == 'tk_par_der' or globals.token.id == 'tk_pyc':
    pass
  else:
    raise s.SyntacticError(['+', '-', '*', '/', '%', '<', '>', '<=', '>=', '==', ';', ')'])

def BLK():
  if globals.token.id == 'imprimir':
    IMP()
    BLK()
  elif globals.token.id == 'caracter' or globals.token.id == 'real' or globals.token.id == 'booleano' or globals.token.id == 'entero' or globals.token.id == 'cadena':
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
  elif globals.token.id == 'e' or globals.token.id == 'fin_seleccionar' or globals.token.id == 'caso' or globals.token.id == 'defecto' or globals.token.id == 'fin_principal':
    pass
  else:
    raise s.SyntacticError(['identificador', 'fin_principal', 'leer', 'imprimir', 'booleano', 'caracter', 'entero', 'real', 'cadena', 'si', 'mientras', 'hacer', 'para', 'seleccionar', 'caso', 'defecto', 'fin_seleccionar'])

def BLQ():
  if globals.token.id == 'si':
    CND()
    BLQ()
  elif globals.token.id == 'id':
    CLA()
    BLQ()
  elif globals.token.id == 'caracter' or globals.token.id == 'real' or globals.token.id == 'booleano' or globals.token.id == 'entero' or globals.token.id == 'cadena':
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
    s.match('fin_si')
  elif globals.token.id == 'si_no':
    s.match('si_no')
    BLQ()
  else:
    raise s.SyntacticError(['identificador', 'leer', 'imprimir', 'booleano', 'caracter', 'entero', 'real', 'cadena', 'si', 'fin_si', 'si_no', 'mientras', 'hacer', 'para', 'seleccionar'])

def LEE():
  if globals.token.id == 'leer':
    s.match('leer')
    s.match('tk_par_izq')
    INP()
    s.match('tk_par_der')
    s.match('tk_pyc')
  else:
    raise s.SyntacticError(['leer'])

def ACC():
  if globals.token.id == 'tk_punto':
    s.match('tk_punto')
    s.match('id')
    ACC()
  elif globals.token.id == 'e' or globals.token.id == 'tk_par_der':
    pass
  else:
    raise s.SyntacticError(['.', ')'])

def LIT():
  if globals.token.id == 'verdadero':
    s.match('verdadero')
  elif globals.token.id == 'falso':
    s.match('falso')
  elif globals.token.id == 'tk_caracter':
    s.match('tk_caracter')
  elif globals.token.id == 'tk_entero':
    s.match('tk_entero')
  elif globals.token.id == 'tk_real':
    s.match('tk_real')
  elif globals.token.id == 'tk_cadena':
    s.match('tk_cadena')
  else:
    raise s.SyntacticError(['valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def TPO():
  if globals.token.id == 'id':
    s.match('id')
  elif globals.token.id == 'caracter' or globals.token.id == 'real' or globals.token.id == 'booleano' or globals.token.id == 'entero' or globals.token.id == 'cadena':
    TYP()
  else:
    raise s.SyntacticError(['identificador', 'booleano', 'caracter', 'entero', 'real', 'cadena'])

def CL5():
  if globals.token.id == 'tk_punto':
    s.match('tk_punto')
    s.match('id')
    CL5()
  elif globals.token.id == 'e' or globals.token.id == 'tk_asig':
    pass
  else:
    raise s.SyntacticError(['=', '.'])

def AR2():
  if globals.token.id == 'falso' or globals.token.id == 'tk_caracter' or globals.token.id == 'tk_real' or globals.token.id == 'tk_entero' or globals.token.id == 'verdadero' or globals.token.id == 'tk_cadena':
    LIT()
    AR1()
  elif globals.token.id == 'id':
    s.match('id')
    AR1()
  else:
    raise s.SyntacticError(['identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def DC3():
  if globals.token.id == 'id':
    s.match('id')
    DC0()
  else:
    raise s.SyntacticError(['identificador'])

def DC0():
  if globals.token.id == 'tk_pyc':
    s.match('tk_pyc')
  elif globals.token.id == 'tk_coma':
    s.match('tk_coma')
    DC3()
  elif globals.token.id == 'tk_asig':
    s.match('tk_asig')
    LIT()
    DC2()
  else:
    raise s.SyntacticError(['=', ';', ','])

def DOW():
  if globals.token.id == 'hacer':
    s.match('hacer')
    DO1()
    s.match('tk_par_izq')
    XPR()
    s.match('tk_par_der')
    s.match('tk_pyc')
  else:
    raise s.SyntacticError(['hacer'])

def XPR():
  if globals.token.id == 'tk_neg':
    s.match('tk_neg')
    XPR()
  elif globals.token.id == 'falso' or globals.token.id == 'tk_caracter' or globals.token.id == 'tk_real' or globals.token.id == 'tk_entero' or globals.token.id == 'id' or globals.token.id == 'verdadero' or globals.token.id == 'tk_cadena':
    VAL()
    XP1()
  else:
    raise s.SyntacticError(['!', 'identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def IMP():
  if globals.token.id == 'imprimir':
    s.match('imprimir')
    s.match('tk_par_izq')
    SHW()
    s.match('tk_par_der')
    s.match('tk_pyc')
  else:
    raise s.SyntacticError(['imprimir'])

def OPE():
  if globals.token.id == 'tk_igual':
    s.match('tk_igual')
  elif globals.token.id == 'tk_menor':
    s.match('tk_menor')
  elif globals.token.id == 'tk_menor_igual':
    s.match('tk_menor_igual')
  elif globals.token.id == 'tk_mayor':
    s.match('tk_mayor')
  elif globals.token.id == 'tk_mayor_igual':
    s.match('tk_mayor_igual')
  elif globals.token.id == 'tk_mas':
    s.match('tk_mas')
  elif globals.token.id == 'tk_menos':
    s.match('tk_menos')
  elif globals.token.id == 'tk_mult':
    s.match('tk_mult')
  elif globals.token.id == 'tk_div':
    s.match('tk_div')
  elif globals.token.id == 'tk_mod':
    s.match('tk_mod')
  else:
    raise s.SyntacticError(['+', '-', '*', '/', '%', '<', '>', '<=', '>=', '=='])

def FOR():
  if globals.token.id == 'para':
    s.match('para')
    s.match('tk_par_izq')
    DCL()
    XPR()
    s.match('tk_pyc')
    STP()
    s.match('tk_par_der')
    s.match('hacer')
    FO1()
  else:
    raise s.SyntacticError(['para'])

def OPC():
  if globals.token.id == 'caso':
    s.match('caso')
    LIT()
    s.match('tk_dosp')
    BLK()
    OPC()
  elif globals.token.id == 'defecto':
    s.match('defecto')
    s.match('tk_dosp')
    BLK()
  elif globals.token.id == 'e' or globals.token.id == 'fin_seleccionar':
    pass
  else:
    raise s.SyntacticError(['caso', 'defecto', 'fin_seleccionar'])

def STP():
  if globals.token.id == 'falso' or globals.token.id == 'tk_caracter' or globals.token.id == 'tk_real' or globals.token.id == 'tk_entero' or globals.token.id == 'verdadero' or globals.token.id == 'tk_cadena':
    LIT()
  else:
    raise s.SyntacticError(['valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def CL3():
  if globals.token.id == 'tk_neg':
    s.match('tk_neg')
    s.match('id')
    s.match('tk_pyc')
  elif globals.token.id == 'falso' or globals.token.id == 'tk_caracter' or globals.token.id == 'tk_real' or globals.token.id == 'tk_entero' or globals.token.id == 'verdadero' or globals.token.id == 'tk_cadena':
    LIT()
    s.match('tk_pyc')
  elif globals.token.id == 'id':
    s.match('id')
    CL4()
    s.match('tk_pyc')
  else:
    raise s.SyntacticError(['!', 'identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def LGC():
  if globals.token.id == 'imprimir':
    IMP()
    LGC()
  elif globals.token.id == 'caracter' or globals.token.id == 'real' or globals.token.id == 'booleano' or globals.token.id == 'entero' or globals.token.id == 'cadena':
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
  elif globals.token.id == 'e' or globals.token.id == 'retornar':
    pass
  elif globals.token.id == 'romper':
    s.match('romper')
    LGC()
  else:
    raise s.SyntacticError(['identificador', 'leer', 'imprimir', 'booleano', 'caracter', 'entero', 'real', 'cadena', 'si', 'mientras', 'hacer', 'para', 'seleccionar', 'romper', 'retornar'])

def FO1():
  if globals.token.id == 'si':
    CND()
    FO1()
  elif globals.token.id == 'id':
    CLA()
    FO1()
  elif globals.token.id == 'caracter' or globals.token.id == 'real' or globals.token.id == 'booleano' or globals.token.id == 'entero' or globals.token.id == 'cadena':
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
    s.match('romper')
    FO1()
  elif globals.token.id == 'fin_para':
    s.match('fin_para')
  else:
    raise s.SyntacticError(['identificador', 'leer', 'imprimir', 'booleano', 'caracter', 'entero', 'real', 'cadena', 'si', 'mientras', 'hacer', 'para', 'fin_para', 'seleccionar', 'romper'])

def CLA():
  if globals.token.id == 'id':
    s.match('id')
    CL2()
  else:
    raise s.SyntacticError(['identificador'])

def AT1():
  if globals.token.id == 'tk_coma':
    s.match('tk_coma')
    s.match('id')
    AT1()
  elif globals.token.id == 'e' or globals.token.id == 'tk_pyc':
    pass
  else:
    raise s.SyntacticError([';', ','])

def FUN():
  if globals.token.id == 'funcion':
    s.match('funcion')
    TYP()
    s.match('id')
    s.match('tk_par_izq')
    PRM()
    s.match('tk_par_der')
    s.match('hacer')
    LGC()
    RET()
    s.match('fin_funcion')
  else:
    raise s.SyntacticError(['funcion'])

def ATR():
  if globals.token.id == 'caracter' or globals.token.id == 'real' or globals.token.id == 'booleano' or globals.token.id == 'id' or globals.token.id == 'entero' or globals.token.id == 'cadena':
    TPO()
    s.match('id')
    AT1()
    s.match('tk_pyc')
    ATR()
  elif globals.token.id == 'fin_estructura':
    s.match('fin_estructura')
  else:
    raise s.SyntacticError(['identificador', 'booleano', 'caracter', 'entero', 'real', 'cadena', 'fin_estructura'])

def RET():
  if globals.token.id == 'retornar':
    s.match('retornar')
    XPR()
    s.match('tk_pyc')
  else:
    raise s.SyntacticError(['retornar'])

def SEL():
  if globals.token.id == 'seleccionar':
    s.match('seleccionar')
    s.match('tk_par_izq')
    s.match('id')
    s.match('tk_par_der')
    s.match('entre')
    OPC()
    s.match('fin_seleccionar')
  else:
    raise s.SyntacticError(['seleccionar'])

def POS():
  if globals.token.id == 'funcion':
    FUN()
    POS()
  elif globals.token.id == 'estructura':
    SRA()
    POS()
  elif globals.token.id == 'eof':
    s.match('eof')
  else:
    raise s.SyntacticError(['estructura', 'funcion', 'EOF'])

def CND():
  if globals.token.id == 'si':
    s.match('si')
    s.match('tk_par_izq')
    XPR()
    s.match('tk_par_der')
    s.match('entonces')
    BLQ()
  else:
    raise s.SyntacticError(['si'])

def DCL():
  if globals.token.id == 'caracter' or globals.token.id == 'real' or globals.token.id == 'booleano' or globals.token.id == 'entero' or globals.token.id == 'cadena':
    TYP()
    DC3()
  else:
    raise s.SyntacticError(['booleano', 'caracter', 'entero', 'real', 'cadena'])

def WL1():
  if globals.token.id == 'si':
    CND()
    WL1()
  elif globals.token.id == 'id':
    CLA()
    WL1()
  elif globals.token.id == 'caracter' or globals.token.id == 'real' or globals.token.id == 'booleano' or globals.token.id == 'entero' or globals.token.id == 'cadena':
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
    s.match('romper')
    WL1()
  elif globals.token.id == 'fin_mientras':
    s.match('fin_mientras')
  else:
    raise s.SyntacticError(['identificador', 'leer', 'imprimir', 'booleano', 'caracter', 'entero', 'real', 'cadena', 'si', 'mientras', 'hacer', 'fin_mientras', 'para', 'seleccionar', 'romper'])

def DO1():
  if globals.token.id == 'si':
    CND()
    DO1()
  elif globals.token.id == 'id':
    CLA()
    DO1()
  elif globals.token.id == 'caracter' or globals.token.id == 'real' or globals.token.id == 'booleano' or globals.token.id == 'entero' or globals.token.id == 'cadena':
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
    s.match('romper')
    DO1()
  elif globals.token.id == 'mientras':
    s.match('mientras')
  else:
    raise s.SyntacticError(['identificador', 'leer', 'imprimir', 'booleano', 'caracter', 'entero', 'real', 'cadena', 'si', 'mientras', 'hacer', 'para', 'seleccionar', 'romper'])

def AR1():
  if globals.token.id == 'tk_coma':
    s.match('tk_coma')
    AR2()
  elif globals.token.id == 'e' or globals.token.id == 'tk_par_der':
    pass
  else:
    raise s.SyntacticError([',', ')'])

def CL2():
  if globals.token.id == 'id':
    s.match('id')
    s.match('tk_pyc')
  elif globals.token.id == 'tk_punto':
    s.match('tk_punto')
    s.match('id')
    CL5()
    s.match('tk_asig')
    LIT()
    s.match('tk_pyc')
  elif globals.token.id == 'tk_par_izq':
    s.match('tk_par_izq')
    ARG()
    s.match('tk_par_der')
  elif globals.token.id == 'tk_asig':
    s.match('tk_asig')
    CL3()
  else:
    raise s.SyntacticError(['=', '.', '(', 'identificador'])

def SHW():
  if globals.token.id == 'id':
    s.match('id')
    SH0()
  elif globals.token.id == 'falso' or globals.token.id == 'tk_caracter' or globals.token.id == 'tk_real' or globals.token.id == 'tk_entero' or globals.token.id == 'verdadero' or globals.token.id == 'tk_cadena':
    LIT()
    SH0()
  elif globals.token.id == 'tk_mult' or globals.token.id == 'tk_par_der' or globals.token.id == 'verdadero' or globals.token.id == 'tk_menos' or globals.token.id == 'falso' or globals.token.id == 'tk_menor' or globals.token.id == 'tk_mas' or globals.token.id == 'tk_mayor' or globals.token.id == 'tk_mod' or globals.token.id == 'tk_menor_igual' or globals.token.id == 'tk_entero' or globals.token.id == 'tk_coma' or globals.token.id == 'tk_div' or globals.token.id == 'tk_par_izq' or globals.token.id == 'tk_caracter' or globals.token.id == 'tk_real' or globals.token.id == 'tk_mayor_igual' or globals.token.id == 'tk_igual' or globals.token.id == 'tk_cadena':
    SH0()
  elif globals.token.id == 'tk_par_izq':
    s.match('tk_par_izq')
    ARG()
    s.match('tk_par_der')
    SH0()
  else:
    raise s.SyntacticError(['+', '-', '*', '/', '%', '<', '>', '<=', '>=', '==', ',', '(', ')', 'identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def ARG():
  if globals.token.id == 'falso' or globals.token.id == 'tk_caracter' or globals.token.id == 'tk_real' or globals.token.id == 'tk_entero' or globals.token.id == 'verdadero' or globals.token.id == 'tk_cadena':
    LIT()
    AR1()
  elif globals.token.id == 'id':
    s.match('id')
    AR1()
  else:
    raise s.SyntacticError(['identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def DC2():
  if globals.token.id == 'tk_coma':
    s.match('tk_coma')
    DC3()
  elif globals.token.id == 'tk_pyc':
    s.match('tk_pyc')
  else:
    raise s.SyntacticError([';', ','])

