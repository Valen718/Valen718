print("Bienvenido al conversor, elije una opcion")

def funcion1():
    print("Vamos a calcular la superficie.")
    
    base = int(input("Ingrese la base del triangulo: "))
    altura = int(input("Ingrese la altura del triangulo: "))
    
    superficie = (base * altura) / 2
    print(f"La superficie es: {superficie}")

def funcion2():
    print("Vamos a convertir kilos a libras.")
    
    kilos = int(input("Ingresa el kilo: "))
    
    libras = kilos * 2.20462
    
    print(f"El peso en libras seria de {libras} libras")

def funcion3():
    print("Kilometros a Millas.")
    
    kilometros = int(input("Introduce los kilometros que quieras pasar a millas: "))
    
    Milla = kilometros * 0.621371
    
    print(f"Los kilometros seleccionados en millas serian de {Milla} millas.")

def elegirConversor():
    try:
        numero = int(input("Elegi una opcion\n1_Calcular superficie de un triangulo\n2_Pasaje kilos a libras\n3_Pasaje de Kilometros a Millas\n"))
        if numero == 1:
            funcion1()
        elif numero == 2:
            funcion2()
        elif numero == 3:
            funcion3()
        else:
            print("Debe ingresar la opcion habilitada.")
    except ValueError:
        print("Hubo un error.\nIngresa un numero valido")

elegirConversor()