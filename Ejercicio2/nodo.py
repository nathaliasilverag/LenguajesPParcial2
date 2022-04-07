""" Ejercicio 2 Parcial 2
    Nathalia Silvera 12-10921"""

class Node:
    """ Estructura que representa un arbol binario """
    def __init__(self, string,left=None,right=None):
        self.left = left
        self.right = right
        self.string = string

    def __str__(self):
        return "("+str(self.left)+str(self.string)+str(self.right)+")"