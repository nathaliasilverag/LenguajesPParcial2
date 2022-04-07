""" Ejercicio 2 Parcial 2
    Nathalia Silvera 12-10921"""

from sys import exit
from operaciones import *

def main():
    print("""Manejador de expresiones aritmeticas en pre y post orden \n""")
    print("""Si desea salir del manejador solo escriba SALIR \n""")
    while True:
        my_input=input(">> ")
        my_input=my_input.upper()
        elems=my_input.split(" ")
        commando=elems[0]
        #Termina con la ejecucion del programa
        if commando=="SALIR":
            exit(0)
        #Evalua la expresion en el orden introducido por el usuario (Pre o Post)
        elif commando=="EVAL" and len(elems)>1:
            order=elems[1]
            if order=="PRE"or order=="POST" and len(elems)>2:
                expr=elems[2:]
                try:
                    my_expr=convert_expr(order,expr)
                    try:
                        print(eval(my_expr))
                    except:
                        print("Error")
                        print("Intenta con: "+my_expr)
                except:
                    print("Expresion Erronea")
                    print("Ingrese correctamente el orden de los elementos")
                    print("recuerda usar "+str(order))
            else:
                printDeAyuda("order")
        #Crea la salida en consola para mostrar al usuario la expresion parentizada 
        elif commando=="MOSTRAR" and len(elems)>1:
            order=elems[1]
            if order=="PRE"or order=="POST" and len(elems)>2:
                expr=elems[2:]
                my_expr=convert_expr(order,expr)
                print(my_expr)
            else:
                printDeAyuda("order")
        else:
            printDeAyuda()

""" Funcion auxiliar para convertir la lista en una 
    expresion aritmetica"""
def convert_expr(order,expr):
    if order=="PRE":
        return PreOrden(expr)
    elif order=="POST":
        return PostOrden(expr)
    else:
        return None

""" Funcion que imprime una guia al usuario de como 
    ingresar los argumentos en consola"""

def printDeAyuda(option=None):
    response="""Prueba con el siguiente formato:
    EVAL <order> <expr>
    MOSTRAR <order> <expr>
    SALIR    
    <order> debe ser: PRE or POST
    <expr> tiene que ser de esta forma:
    + * + 3 4 5 7
    8 3 - 8 4 4 + * +
    El orden de los operandos y numeros depende de la expresion a aplicar.
    \n"""

    if option=="order":
        response=response[:24]+response[87:]

    elif option=="expr":
        response=response[:24]+response[118:]

    print(response)

if __name__ == "__main__":
    main()