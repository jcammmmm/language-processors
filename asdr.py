import syntax as s
import globals

def begin():
  PRG()

def SH1():
  if globals.token.id == 'tk_menos' or globals.token.id == 'tk_menor_igual' or globals.token.id == 'tk_punto' or globals.token.id == 'tk_dif' or globals.token.id == 'tk_mayor' or globals.token.id == 'tk_menor' or globals.token.id == 'tk_igual' or globals.token.id == 'tk_div' or globals.token.id == 'tk_mod' or globals.token.id == 'tk_mult' or globals.token.id == 'tk_mayor_igual' or globals.token.id == 'tk_mas':
    OPE()
    EXP()
  elif globals.token.id == 'tk_par_der' or globals.token.id == 'tk_coma':
    FIN()
  else:
    raise s.SyntacticError(['+', '-', '*', '/', '%', '<', '>', '<=', '>=', '==', '!=', ',', '.', ')'])

def SE1():
  if globals.token.id == 'si':
    CND()
    SE1()
  elif globals.token.id == 'id':
    CLA()
    SE1()
  elif globals.token.id == 'booleano' or globals.token.id == 'entero' or globals.token.id == 'cadena' or globals.token.id == 'caracter' or globals.token.id == 'real':
    DCL()
    SE1()
  elif globals.token.id == 'imprimir':
    IMP()
    SE1()
  elif globals.token.id == 'leer':
    LEE()
    SE1()
  elif globals.token.id == 'para':
    FOR()
    SE1()
  elif globals.token.id == 'hacer':
    DOW()
    SE1()
  elif globals.token.id == 'mientras':
    WLE()
    SE1()
  elif globals.token.id == 'seleccionar':
    SEL()
    SE1()
  elif globals.token.id == 'romper':
    s.match('romper')
    s.match('tk_pyc')
    SE1()
  elif globals.token.id == 'fin_seleccionar' or globals.token.id == 'defecto' or globals.token.id == 'caso' or globals.token.id == 'e':
    pass
  else:
    raise s.SyntacticError(['identificador', 'leer', 'imprimir', 'booleano', 'caracter', 'entero', 'real', 'cadena', 'si', 'mientras', 'hacer', 'para', 'seleccionar', 'caso', 'romper', 'defecto', 'fin_seleccionar'])

def SRA():
  if globals.token.id == 'estructura':
    s.match('estructura')
    s.match('id')
    ATR()
  else:
    raise s.SyntacticError(['estructura'])

def DC0():
  if globals.token.id == 'tk_pyc':
    s.match('tk_pyc')
  elif globals.token.id == 'tk_coma':
    s.match('tk_coma')
    DC3()
  elif globals.token.id == 'tk_asig':
    s.match('tk_asig')
    DC8()
  else:
    raise s.SyntacticError(['=', ';', ','])

def CLA():
  if globals.token.id == 'id':
    s.match('id')
    CL2()
  else:
    raise s.SyntacticError(['identificador'])

def DC7():
  if globals.token.id == 'tk_par_izq':
    s.match('tk_par_izq')
    ARG()
    s.match('tk_par_der')
  elif globals.token.id == 'tk_menor_igual' or globals.token.id == 'tk_punto' or globals.token.id == 'tk_mult' or globals.token.id == 'tk_mayor_igual' or globals.token.id == 'tk_pyc' or globals.token.id == 'tk_dif' or globals.token.id == 'tk_mayor' or globals.token.id == 'tk_igual' or globals.token.id == 'tk_div' or globals.token.id == 'tk_mod' or globals.token.id == 'tk_menos' or globals.token.id == 'tk_menor' or globals.token.id == 'tk_mas':
    XP1()
  elif globals.token.id == 'tk_pyc':
    s.match('tk_pyc')
  else:
    raise s.SyntacticError(['+', '-', '*', '/', '%', '<', '>', '<=', '>=', '==', '!=', ';', '.', '('])

def OPC():
  if globals.token.id == 'caso':
    s.match('caso')
    LIT()
    s.match('tk_dosp')
    SE1()
    OPC()
  elif globals.token.id == 'defecto':
    s.match('defecto')
    s.match('tk_dosp')
    SE1()
  elif globals.token.id == 'e' or globals.token.id == 'fin_seleccionar':
    pass
  else:
    raise s.SyntacticError(['caso', 'defecto', 'fin_seleccionar'])

def AR1():
  if globals.token.id == 'tk_coma':
    s.match('tk_coma')
    AR2()
  elif globals.token.id == 'tk_par_der' or globals.token.id == 'e':
    pass
  else:
    raise s.SyntacticError([',', ')'])

def RET():
  if globals.token.id == 'retornar':
    s.match('retornar')
    XPR()
    s.match('tk_pyc')
  else:
    raise s.SyntacticError(['retornar'])

def VAL():
  if globals.token.id == 'id':
    s.match('id')
  elif globals.token.id == 'tk_caracter' or globals.token.id == 'tk_entero' or globals.token.id == 'falso' or globals.token.id == 'tk_cadena' or globals.token.id == 'verdadero' or globals.token.id == 'tk_real':
    LIT()
  else:
    raise s.SyntacticError(['identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def BLQ():
  if globals.token.id == 'si':
    CND()
    BLQ()
  elif globals.token.id == 'id':
    CLA()
    BLQ()
  elif globals.token.id == 'booleano' or globals.token.id == 'entero' or globals.token.id == 'cadena' or globals.token.id == 'caracter' or globals.token.id == 'real':
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

def CL4():
  if globals.token.id == 'tk_par_izq':
    s.match('tk_par_izq')
    ARG()
    s.match('tk_par_der')
  elif globals.token.id == 'tk_menor_igual' or globals.token.id == 'tk_punto' or globals.token.id == 'tk_mult' or globals.token.id == 'tk_mayor_igual' or globals.token.id == 'tk_pyc' or globals.token.id == 'tk_dif' or globals.token.id == 'tk_mayor' or globals.token.id == 'tk_igual' or globals.token.id == 'tk_div' or globals.token.id == 'tk_mod' or globals.token.id == 'tk_menos' or globals.token.id == 'tk_menor' or globals.token.id == 'tk_mas':
    XP1()
  else:
    raise s.SyntacticError(['+', '-', '*', '/', '%', '<', '>', '<=', '>=', '==', '!=', ';', '.', '('])

def XPR():
  if globals.token.id == 'tk_neg':
    s.match('tk_neg')
    XPR()
  elif globals.token.id == 'tk_caracter' or globals.token.id == 'tk_entero' or globals.token.id == 'falso' or globals.token.id == 'tk_cadena' or globals.token.id == 'verdadero' or globals.token.id == 'tk_real' or globals.token.id == 'id':
    VAL()
    XP1()
  else:
    raise s.SyntacticError(['!', 'identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def FO1():
  if globals.token.id == 'si':
    CND()
    FO1()
  elif globals.token.id == 'id':
    CLA()
    FO1()
  elif globals.token.id == 'booleano' or globals.token.id == 'entero' or globals.token.id == 'cadena' or globals.token.id == 'caracter' or globals.token.id == 'real':
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

def LEE():
  if globals.token.id == 'leer':
    s.match('leer')
    s.match('tk_par_izq')
    INP()
    s.match('tk_par_der')
    s.match('tk_pyc')
  else:
    raise s.SyntacticError(['leer'])

def INP():
  if globals.token.id == 'id':
    s.match('id')
    ACC()
  else:
    raise s.SyntacticError(['identificador'])

def PRG():
  if globals.token.id == 'funcion' or globals.token.id == 'estructura' or globals.token.id == 'funcion_principal':
    INI()
    s.match('funcion_principal')
    BLK()
    s.match('fin_principal')
    POS()
  else:
    raise s.SyntacticError(['funcion_principal', 'estructura', 'funcion'])

def FIN():
  if globals.token.id == 'tk_coma':
    s.match('tk_coma')
    SHW()
  elif globals.token.id == 'tk_par_der':
    s.match('tk_par_der')
  else:
    raise s.SyntacticError([',', ')'])

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

def OPE():
  if globals.token.id == 'tk_punto':
    s.match('tk_punto')
  elif globals.token.id == 'tk_igual':
    s.match('tk_igual')
  elif globals.token.id == 'tk_dif':
    s.match('tk_dif')
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
    raise s.SyntacticError(['+', '-', '*', '/', '%', '<', '>', '<=', '>=', '==', '!=', '.'])

def CL2():
  if globals.token.id == 'id':
    s.match('id')
    s.match('tk_pyc')
  elif globals.token.id == 'tk_punto':
    s.match('tk_punto')
    s.match('id')
    CL5()
    s.match('tk_asig')
    VAL()
    XP1()
    s.match('tk_pyc')
  elif globals.token.id == 'tk_par_izq':
    s.match('tk_par_izq')
    ARG()
    s.match('tk_par_der')
    s.match('tk_pyc')
  elif globals.token.id == 'tk_asig':
    s.match('tk_asig')
    CL3()
  else:
    raise s.SyntacticError(['=', '.', '(', 'identificador'])

def AT1():
  if globals.token.id == 'tk_coma':
    s.match('tk_coma')
    s.match('id')
    AT1()
  elif globals.token.id == 'tk_pyc' or globals.token.id == 'e':
    pass
  else:
    raise s.SyntacticError([';', ','])

def EX1():
  if globals.token.id == 'tk_menos' or globals.token.id == 'tk_menor_igual' or globals.token.id == 'tk_punto' or globals.token.id == 'tk_dif' or globals.token.id == 'tk_mayor' or globals.token.id == 'tk_menor' or globals.token.id == 'tk_igual' or globals.token.id == 'tk_div' or globals.token.id == 'tk_mod' or globals.token.id == 'tk_mult' or globals.token.id == 'tk_mayor_igual' or globals.token.id == 'tk_mas':
    OPE()
    VAL()
    EX1()
  elif globals.token.id == 'tk_par_der' or globals.token.id == 'tk_coma':
    FIN()
  else:
    raise s.SyntacticError(['+', '-', '*', '/', '%', '<', '>', '<=', '>=', '==', '!=', ',', '.', ')'])

def DCL():
  if globals.token.id == 'booleano' or globals.token.id == 'entero' or globals.token.id == 'cadena' or globals.token.id == 'caracter' or globals.token.id == 'real':
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
  elif globals.token.id == 'booleano' or globals.token.id == 'entero' or globals.token.id == 'cadena' or globals.token.id == 'caracter' or globals.token.id == 'real':
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

def CL3():
  if globals.token.id == 'tk_neg':
    s.match('tk_neg')
    s.match('id')
    s.match('tk_pyc')
  elif globals.token.id == 'tk_caracter' or globals.token.id == 'tk_entero' or globals.token.id == 'falso' or globals.token.id == 'tk_cadena' or globals.token.id == 'verdadero' or globals.token.id == 'tk_real':
    LIT()
    s.match('tk_pyc')
  elif globals.token.id == 'id':
    s.match('id')
    CL4()
    s.match('tk_pyc')
  else:
    raise s.SyntacticError(['!', 'identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def BEG():
  if globals.token.id == 'booleano' or globals.token.id == 'entero' or globals.token.id == 'cadena' or globals.token.id == 'caracter' or globals.token.id == 'real':
    TYP()
    s.match('id')
    s.match('tk_asig')
    BE1()
  elif globals.token.id == 'id':
    s.match('id')
    s.match('tk_asig')
    BE1()
  else:
    raise s.SyntacticError(['identificador', 'booleano', 'caracter', 'entero', 'real', 'cadena'])

def ATR():
  if globals.token.id == 'id':
    s.match('id')
    AT2()
  elif globals.token.id == 'booleano' or globals.token.id == 'entero' or globals.token.id == 'cadena' or globals.token.id == 'caracter' or globals.token.id == 'real':
    TYP()
    AT2()
  elif globals.token.id == 'fin_estructura':
    s.match('fin_estructura')
  else:
    raise s.SyntacticError(['identificador', 'booleano', 'caracter', 'entero', 'real', 'cadena', 'fin_estructura'])

def AT2():
  if globals.token.id == 'id':
    s.match('id')
    AT1()
    s.match('tk_pyc')
    ATR()
  else:
    raise s.SyntacticError(['identificador'])

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

def PRM():
  if globals.token.id == 'booleano' or globals.token.id == 'entero' or globals.token.id == 'cadena' or globals.token.id == 'caracter' or globals.token.id == 'id' or globals.token.id == 'real':
    TIP()
    s.match('id')
    PRM()
  elif globals.token.id == 'tk_coma':
    s.match('tk_coma')
    TIP()
    s.match('id')
    PRM()
  elif globals.token.id == 'tk_par_der' or globals.token.id == 'e':
    pass
  else:
    raise s.SyntacticError([',', ')', 'identificador', 'booleano', 'caracter', 'entero', 'real', 'cadena'])

def TIP():
  if globals.token.id == 'id':
    s.match('id')
  elif globals.token.id == 'booleano' or globals.token.id == 'entero' or globals.token.id == 'cadena' or globals.token.id == 'caracter' or globals.token.id == 'real':
    TYP()
  else:
    raise s.SyntacticError(['identificador', 'booleano', 'caracter', 'entero', 'real', 'cadena'])

def EXP():
  if globals.token.id == 'tk_caracter' or globals.token.id == 'tk_entero' or globals.token.id == 'falso' or globals.token.id == 'tk_cadena' or globals.token.id == 'verdadero' or globals.token.id == 'tk_real' or globals.token.id == 'id':
    VAL()
    EX1()
  else:
    raise s.SyntacticError(['identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def ARG():
  if globals.token.id == 'tk_caracter' or globals.token.id == 'tk_entero' or globals.token.id == 'falso' or globals.token.id == 'tk_cadena' or globals.token.id == 'verdadero' or globals.token.id == 'tk_real':
    LIT()
    AR1()
  elif globals.token.id == 'id':
    s.match('id')
    AR1()
  elif globals.token.id == 'tk_par_der':
    pass
  else:
    raise s.SyntacticError([')', 'identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def DO1():
  if globals.token.id == 'mientras':
    s.match('mientras')
    s.match('tk_par_izq')
    XPR()
    s.match('tk_par_der')
    DO2()
  elif globals.token.id == 'si':
    CND()
    DO1()
  elif globals.token.id == 'id':
    CLA()
    DO1()
  elif globals.token.id == 'booleano' or globals.token.id == 'entero' or globals.token.id == 'cadena' or globals.token.id == 'caracter' or globals.token.id == 'real':
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
  else:
    raise s.SyntacticError(['identificador', 'leer', 'imprimir', 'booleano', 'caracter', 'entero', 'real', 'cadena', 'si', 'mientras', 'hacer', 'para', 'seleccionar', 'romper'])

def SH0():
  if globals.token.id == 'tk_menos' or globals.token.id == 'tk_menor_igual' or globals.token.id == 'tk_punto' or globals.token.id == 'tk_dif' or globals.token.id == 'tk_mayor' or globals.token.id == 'tk_menor' or globals.token.id == 'tk_igual' or globals.token.id == 'tk_div' or globals.token.id == 'tk_mod' or globals.token.id == 'tk_mult' or globals.token.id == 'tk_mayor_igual' or globals.token.id == 'tk_mas':
    OPE()
    EXP()
  elif globals.token.id == 'tk_par_der' or globals.token.id == 'tk_coma':
    FIN()
  elif globals.token.id == 'tk_par_izq':
    s.match('tk_par_izq')
    ARG()
    s.match('tk_par_der')
    FIN()
  else:
    raise s.SyntacticError(['+', '-', '*', '/', '%', '<', '>', '<=', '>=', '==', '!=', ',', '.', '(', ')'])

def DO3():
  if globals.token.id == 'booleano' or globals.token.id == 'romper' or globals.token.id == 'cadena' or globals.token.id == 'si' or globals.token.id == 'caracter' or globals.token.id == 'real' or globals.token.id == 'mientras' or globals.token.id == 'entero':
    DO1()
  elif globals.token.id == 'fin_mientras':
    s.match('fin_mientras')
    DO1()
  else:
    raise s.SyntacticError(['booleano', 'caracter', 'entero', 'real', 'cadena', 'si', 'mientras', 'fin_mientras', 'romper'])

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

def FOR():
  if globals.token.id == 'para':
    s.match('para')
    s.match('tk_par_izq')
    BEG()
    s.match('tk_pyc')
    XPR()
    s.match('tk_pyc')
    STP()
    s.match('tk_par_der')
    s.match('hacer')
    FO1()
  else:
    raise s.SyntacticError(['para'])

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

def BE1():
  if globals.token.id == 'tk_caracter' or globals.token.id == 'tk_entero' or globals.token.id == 'falso' or globals.token.id == 'tk_cadena' or globals.token.id == 'verdadero' or globals.token.id == 'tk_real':
    LIT()
  elif globals.token.id == 'id':
    s.match('id')
  else:
    raise s.SyntacticError(['identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def SHW():
  if globals.token.id == 'id':
    s.match('id')
    SH0()
  elif globals.token.id == 'tk_menos':
    s.match('tk_menos')
    VAL()
    FIN()
  elif globals.token.id == 'tk_neg':
    s.match('tk_neg')
    VAL()
    FIN()
  elif globals.token.id == 'tk_par_izq':
    s.match('tk_par_izq')
    VAL()
    OPE()
    VAL()
    s.match('tk_par_der')
    OPE()
    VAL()
    XP1()
    FIN()
  elif globals.token.id == 'tk_caracter' or globals.token.id == 'tk_entero' or globals.token.id == 'falso' or globals.token.id == 'tk_cadena' or globals.token.id == 'verdadero' or globals.token.id == 'tk_real':
    LIT()
    SH1()
  else:
    raise s.SyntacticError(['-', '!', '(', 'identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def FUN():
  if globals.token.id == 'funcion':
    s.match('funcion')
    TIP()
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

def DO2():
  if globals.token.id == 'tk_pyc':
    s.match('tk_pyc')
  elif globals.token.id == 'hacer':
    s.match('hacer')
    DO3()
  else:
    raise s.SyntacticError([';', 'hacer'])

def XP1():
  if globals.token.id == 'tk_menos' or globals.token.id == 'tk_menor_igual' or globals.token.id == 'tk_punto' or globals.token.id == 'tk_dif' or globals.token.id == 'tk_mayor' or globals.token.id == 'tk_menor' or globals.token.id == 'tk_igual' or globals.token.id == 'tk_div' or globals.token.id == 'tk_mod' or globals.token.id == 'tk_mult' or globals.token.id == 'tk_mayor_igual' or globals.token.id == 'tk_mas':
    OPE()
    VAL()
    XP1()
  elif globals.token.id == 'tk_pyc' or globals.token.id == 'tk_par_der' or globals.token.id == 'tk_coma' or globals.token.id == 'e':
    pass
  else:
    raise s.SyntacticError(['+', '-', '*', '/', '%', '<', '>', '<=', '>=', '==', '!=', ';', ',', '.', ')'])

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

def DC2():
  if globals.token.id == 'tk_coma':
    s.match('tk_coma')
    DC3()
  elif globals.token.id == 'tk_pyc':
    s.match('tk_pyc')
  else:
    raise s.SyntacticError([';', ','])

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

def AR2():
  if globals.token.id == 'tk_caracter' or globals.token.id == 'tk_entero' or globals.token.id == 'falso' or globals.token.id == 'tk_cadena' or globals.token.id == 'verdadero' or globals.token.id == 'tk_real':
    LIT()
    AR1()
  elif globals.token.id == 'id':
    s.match('id')
    AR1()
  else:
    raise s.SyntacticError(['identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

def ACC():
  if globals.token.id == 'tk_punto':
    s.match('tk_punto')
    s.match('id')
    ACC()
  elif globals.token.id == 'tk_par_der' or globals.token.id == 'e':
    pass
  else:
    raise s.SyntacticError(['.', ')'])

def DC3():
  if globals.token.id == 'id':
    s.match('id')
    DC0()
  else:
    raise s.SyntacticError(['identificador'])

def DC8():
  if globals.token.id == 'tk_caracter' or globals.token.id == 'tk_entero' or globals.token.id == 'falso' or globals.token.id == 'tk_cadena' or globals.token.id == 'verdadero' or globals.token.id == 'tk_real':
    LIT()
    DC2()
  elif globals.token.id == 'tk_menos':
    s.match('tk_menos')
    s.match('id')
    s.match('tk_pyc')
  elif globals.token.id == 'tk_neg':
    s.match('tk_neg')
    s.match('id')
    s.match('tk_pyc')
  elif globals.token.id == 'tk_par_izq':
    s.match('tk_par_izq')
    ARG()
    s.match('tk_par_der')
    s.match('tk_pyc')
  elif globals.token.id == 'tk_caracter' or globals.token.id == 'tk_entero' or globals.token.id == 'falso' or globals.token.id == 'tk_cadena' or globals.token.id == 'verdadero' or globals.token.id == 'tk_real':
    LIT()
    s.match('tk_pyc')
  elif globals.token.id == 'id':
    s.match('id')
    DC7()
    s.match('tk_pyc')
  else:
    raise s.SyntacticError(['-', '!', '(', 'identificador', 'valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

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

def LGC():
  if globals.token.id == 'imprimir':
    IMP()
    LGC()
  elif globals.token.id == 'booleano' or globals.token.id == 'entero' or globals.token.id == 'cadena' or globals.token.id == 'caracter' or globals.token.id == 'real':
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
    s.match('romper')
    LGC()
  else:
    raise s.SyntacticError(['identificador', 'leer', 'imprimir', 'booleano', 'caracter', 'entero', 'real', 'cadena', 'si', 'mientras', 'hacer', 'para', 'seleccionar', 'romper', 'retornar'])

def DOW():
  if globals.token.id == 'hacer':
    s.match('hacer')
    DO1()
  else:
    raise s.SyntacticError(['hacer'])

def IMP():
  if globals.token.id == 'imprimir':
    s.match('imprimir')
    s.match('tk_par_izq')
    SHW()
    s.match('tk_pyc')
  else:
    raise s.SyntacticError(['imprimir'])

def CL5():
  if globals.token.id == 'tk_punto':
    s.match('tk_punto')
    s.match('id')
    CL5()
  elif globals.token.id == 'tk_asig' or globals.token.id == 'e':
    pass
  else:
    raise s.SyntacticError(['=', '.'])

def BLK():
  if globals.token.id == 'imprimir':
    IMP()
    BLK()
  elif globals.token.id == 'booleano' or globals.token.id == 'entero' or globals.token.id == 'cadena' or globals.token.id == 'caracter' or globals.token.id == 'real':
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
  elif globals.token.id == 'fin_principal' or globals.token.id == 'e':
    pass
  else:
    raise s.SyntacticError(['identificador', 'fin_principal', 'leer', 'imprimir', 'booleano', 'caracter', 'entero', 'real', 'cadena', 'si', 'mientras', 'hacer', 'para', 'seleccionar'])

def STP():
  if globals.token.id == 'tk_caracter' or globals.token.id == 'tk_entero' or globals.token.id == 'falso' or globals.token.id == 'tk_cadena' or globals.token.id == 'verdadero' or globals.token.id == 'tk_real':
    LIT()
  else:
    raise s.SyntacticError(['valor_entero', 'valor_real', 'valor_caracter', 'valor_cadena', 'falso', 'verdadero'])

