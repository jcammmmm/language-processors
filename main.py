import os
from syntax import launch_syntactic_analizer

def main():
    if os.getenv('STAGE') == 'DEVELOPMENT':
        """
        run the analizer in batch from file
        """
        src = [
            ('in/a02.psi', 'El analisis sintactico ha finalizado exitosamente.'),
            ('in/a03.psi', 'El analisis sintactico ha finalizado exitosamente.'),
            ('in/a04.psi', 'El analisis sintactico ha finalizado exitosamente.'),
            ('in/a05.psi', 'El analisis sintactico ha finalizado exitosamente.'),
            ('in/a08.psi', 'El analisis sintactico ha finalizado exitosamente.'),
            ('in/a11.psi', '<3,17> Error sintactico: se encontro: "0"; se esperaba: "identificador".'),
            ('in/a12.psi', '<5,11> Error sintactico: se encontro: ","; se esperaba: ".", ")".'),
            ('in/a13.psi', '<8,8> Error sintactico: se encontro: "res"; se esperaba: "entonces".'),
            ('in/a16.psi', '<9,1> Error sintactico: se encontro: "fin_principal"; se esperaba: "identificador", "leer", "imprimir", "booleano", "caracter", "entero", "real", "cadena", "si", "mientras", "hacer", "para", "seleccionar", "romper".'),
            ('in/a17.psi', '<2,5> Error sintactico: se encontro: "hacer"; se esperaba: "identificador", "booleano", "caracter", "entero", "real", "cadena", "fin_estructura".'),
            ('in/a18.psi', '<3,1> Error sintactico: se encontro: "fin_funcion"; se esperaba: "identificador", "leer", "imprimir", "booleano", "caracter", "entero", "real", "cadena", "si", "mientras", "hacer", "para", "seleccionar", "romper", "retornar".'),
            ('in/a19.psi', 'El analisis sintactico ha finalizado exitosamente.'),
            ('in/a20.psi', 'Error sintactico: falta funcion_principal'),
            ('in/a21.psi', '<3,12> Error sintactico: se encontro: ";"; se esperaba: "-", "!", "(", "identificador", "valor_entero", "valor_real", "valor_caracter", "valor_cadena", "falso", "verdadero".'),
            # src_loc = 'in/a22.psi' # <8,10> Error sintactico: se encontro: ";"; se esperaba: "=", ".", "(", "identificador".
            # src_loc = 'in/a23.psi' # <9,14> Error sintactico: se encontro: ")"; se esperaba: "-", "!", "(", "identificador", "valor_entero", "valor_real", "valor_caracter", "valor_cadena", "falso", "verdadero".
        ]
        for f in src:
            print("SRC : {}".format(f[0]))
            print("OUR : {}".format(launch_syntactic_analizer(f[0])))
            print("EXP : {}".format(f[1]))
    else:
        """
        only run the analizer once from console
        """
        print(launch_syntactic_analizer(), end='')

if __name__ == "__main__":
    main()