#Aca voy a practicar la recursividad.

def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
        
def imprimir_sucesion(n):
    for i in range(n + 1):
        print(Fibonacci(i), end="\n")
        
imprimir_sucesion(10)