from lexer import Lexer
import os

"""
src_loc (source location) if None, it means that 
source code will be readed from stdin. This makes
that lexer without file location will be instanced.
"""
src_loc = None
if os.getenv('STAGE') == 'DEVELOPMENT':
    # src_loc = 'in/a02.psi' # El analisis sintactico ha finalizado exitosamente.
    # src_loc = 'in/a03.psi' # El analisis sintactico ha finalizado exitosamente.
    # src_loc = 'in/a04.psi' # El analisis sintactico ha finalizado exitosamente.
    # src_loc = 'in/a05.psi' # El analisis sintactico ha finalizado exitosamente.
    # src_loc = 'in/a08.psi' # El analisis sintactico ha finalizado exitosamente.
    # src_loc = 'in/a11.psi' # <3,17> Error sintactico: se encontro: "0"; se esperaba: "identificador".
    # src_loc = 'in/a12.psi' # <5,11> Error sintactico: se encontro: ","; se esperaba: ".", ")".
    # src_loc = 'in/a13.psi' # <8,8> Error sintactico: se encontro: "res"; se esperaba: "entonces".
    src_loc = 'in/a16.psi' # <6,5> Error sintactico: se encontro: "fin_mientras"; se esperaba: "identificador", "...
    # src_loc = 'in/a17.psi' # 
    # src_loc = 'in/a18.psi' # 
    # src_loc = 'in/a19.psi' # 
    # src_loc = 'in/a20.psi' # 
    # src_loc = 'in/a21.psi' # 
    # src_loc = 'in/a22.psi' # 
    # src_loc = 'in/a23.psi' # 

global token, lexer
token = ''
lexer = (Lexer(src_loc) if src_loc else Lexer()) 