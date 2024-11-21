import random

numero = random.randint(1, 100)
contador = 0

while True:
    eleccion = int(input("Ingrese un numero: "))
    
    if(numero == eleccion):
        print(f"Felicidades, adivinaste el numero en {contador} intentos")
        break
    elif(numero != eleccion):
        contador += 1
        if(numero < eleccion):
            print("El numero es mas chico\n")
        elif(numero > eleccion):
            print("El numero es mas alto\n")
        print("Intenta devuelta")
        print(f"Numero de intentos: {contador}\n")