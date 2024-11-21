#Conversión de temperatura:
#Escribí un programa que convierta una temperatura de grados Celsius a Fahrenheit o viceversa.

def CelsiusaFahrenheit():
    celsius = int(input("Ingrese la temperatura en Celsius: "))
    fahrenheit = (celsius * (9/5) + 32)
    print(f"{celsius}° celsius serian {fahrenheit}° fahrenheit")
    
def CelsiusaKelvin():
    celsius = int(input("Ingrese la temperatura en Celsius: "))
    kelvin = celsius + 273.15
    print(f"{celsius}° celsius serian {kelvin}° kelvin")

def FahremheitaCelsius():
    fahrenheit = int(input("Ingrese la temperatura en fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}° fahrenheit serian {celsius}° Celsius")
    
def FahrenheitaKelvin():
    fahrenheit = int(input("Ingrese la temperatura en fahrenheit: "))
    kelvin = (fahrenheit - 32) * 9/5 + 273.15
    print(f"{fahrenheit}° fahrenheit serian {kelvin}° Kelvin")
    
def KelvinaCelsius():
    kelvin = int(input("Ingrese la temperatura en Kelvin: "))
    celsius = kelvin - 273.15
    print(f"{kelvin}° kelvin serian {celsius}° Celsius")
    
def KelvinaFahrenheit():
    kelvin = int(input("Ingrese la temperatura en Kelvin: "))
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    print(f"{kelvin}° kelvin serian {fahrenheit}° Fahrenheit")
    
eleccion = int(input("Ingrese la opcion que desee convertir:\n1_Celsius a Fahrenheit\n2_Celsius a Kelvin\n3_Fahremheit a Celsius\n4_Fahrenheit a Kelvin\n5_Kelvin a Celsius\n6_Kelvin a Fahrenheit\n7_Salir\n"))

while eleccion != 7:
    try:
        if(eleccion == 1):
            CelsiusaFahrenheit()
            break
        elif(eleccion == 2):
            CelsiusaKelvin()
            break
        elif (eleccion == 3):
            FahremheitaCelsius()
            break
        elif(eleccion == 4):
            FahrenheitaKelvin()
            break
        elif(eleccion == 5):
            KelvinaCelsius()
            break
        elif(eleccion == 6):
            KelvinaFahrenheit()
            break           
        elif(eleccion == 7):
            print("Adios")
        else:
            print("Se produjo un error. Ingrese una opcion devuelta")
    except ValueError:
        print("Hubo un error, ingrese una opcion habilitada.")
