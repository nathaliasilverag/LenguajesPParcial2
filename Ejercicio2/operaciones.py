""" Ejercicio 2 Parcial 2
    Nathalia Silvera 12-10921"""


from nodo import Node
operadores=["*","/","+","-"]

"""Funcion para convertir una lista de elementos 
    en una expresion aritmentica en PreOrden"""
def PreOrden(list):
    #Si solo tengo un operador no puedo hacer nada, lo devuelvo 
    #como string
    if not list[0] in operadores and len(list)==1:
        return str(list[0]) 
    #caso en que la lista solo contenga 3 elementos 
    elif len(list)==3:
        return str(Node(list[0],list[1],list[2]))
    #caso en que la lista tenga mas de 3 elementos, debe verificar 
    #la lista de operadores muestras simbol sea true verifica los 
    #operadores y luego busca los enteros.
    else:
        for i in range(1,len(list)-2):
            if list[i] in operadores:
                
                simbol=False
                for j in range(i,len(list)+1):
                    if list[j] in operadores:
                        simbol=True
                        break

                if i+3<len(list) and not list[i+3] in operadores and not (i-2>0 and not list[i-2] in operadores) and not simbol:
                    pass
                else:
                    if not list[i+1] in operadores and not list[i+2] in operadores:
                        temp=list[i]
                        list[i]=str(Node(temp,list[i+1],list[i+2]))
                        del list[i+1]
                        del list[i+1]
                        break
        return PreOrden(list)


"""Funcion para convertir una lista de elementos 
    en una expresion aritmentica en PostOrden"""

def PostOrden(list):
    #Si solo tengo un operador no puedo hacer nada, lo devuelvo 
    #como string
    if not list[0] in operadores and len(list)==1:
        return str(list[0])
    #caso en que la lista solo contenga 3 elementos 
    elif len(list)==3:
        return str(Node(list[2],list[0],list[1]))
    #caso en que la lista tenga mas de 3 elementos, debe verificar 
    #la lista de operadores muestras simbol sea true verifica los 
    #operadores y luego busca los enteros.
    else:
        for i in range(0,len(list)-2):
            if list[i+2] in operadores:

                simbol=False
                for j in range(0,i+2):
                    if list[j] in operadores:
                        simbol=True
                        break
                if i-1>0 and not list[i-1] in operadores and not(i>0 and not list[i] in operadores) and not simbol:
                    pass
                else:
                    if not list[i] in operadores and not list[i+1] in operadores:
                        temp=list[i]
                        list[i]=str(Node(list[i+2],temp,list[i+1]))
                        del list[i+1]
                        del list[i+1]
                        break
        return PostOrden(list)