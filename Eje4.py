#  Pregunta 4 Parcial 2 Lenguajes de Programacion
#  Nathalia Silvera 12-10921

X = 9
Y = 2 
Z = 1

alfa = ((X + Y) % 5)+3
beta = ((Y + Z) % 5)+3

print("alfa", alfa, " ", "beta",beta)
limitSup =  alfa * beta
print("limitSup",limitSup)

#   Funcion recursiva para calcular Fa,b, donde 
#   a es alfa y b es beta 
#   recibe un argumento entero de entrada, y
#   retorna un entero

def Falfabeta(n):
    if 0 <= n < limitSup:
        return n
    
    else:
        return Falfabeta(n-6)+Falfabeta(n-12)+Falfabeta(n-18)+Falfabeta(n-24)
    
#   Funcion recursiva de Cola para calcular Fa,b, donde 
#   a es alfa y b es beta 
#   recibe un argumento entero de entrada, y
#   retorna un entero

def FalfabetaCola(n):
    if 0 <= n < limitSup:
        return n
    
    else:
        return sum([FalfabetaCola(n-beta*i) for i in range(1, alfa+1)]) 

#   Funcion iterativa para calcular Fa,b, donde 
#   a es alfa y b es beta 
#   recibe un argumento entero de entrada, y
#   retorna un entero
#   esta funcion funciona bien si no entra en la segunda condicion,
#   en la segunda condicion falla, sin embargo los valores son cercanos
def FalfabetaIterativa(n):
    if 0 <= n < limitSup:
        return n
    elif n >=limitSup+6:
        aux = 0
        aux1 = 0
        y = 0
        for i in range(1,alfa+1):
            y = y+1
            N = n-beta*i
            if(N>=limitSup):
                aux1 += N 
                if(N>=limitSup):
                    if 0<=N<limitSup:
                        return N
                    else:
                        for i in range(1,alfa+1):
                            Z = n - beta*i
                            aux += Z
                else:
                   aux += Z
            else:
               aux += Z
        return aux
    else:
        aux = 0
        for i in range(1,alfa+1):
            N = n - beta*i
            aux += N 
        return aux
      


a = Falfabeta(23)
b = Falfabeta(24)
c = Falfabeta(31)
print("Recursiva 23, 24, 31: ",a,b,c)
d = FalfabetaCola(23)
e = FalfabetaCola(24)
f = FalfabetaCola(31)
print("Recursiva de Cola 23, 24, 31: ", d,e,f )
h = FalfabetaIterativa(23)
i = FalfabetaIterativa(24)
j = FalfabetaIterativa(31)
print("Iterativa 23, 24, 31: ", h, i, j)
