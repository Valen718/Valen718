nota1 = int(input("Ingrese la primer nota del estudiante: "))
nota2 = int(input("Ingrese la segunda nota del estudiante: "))
nota3 = int(input("Ingrese la tercer nota del estudiante: "))

promedio = (nota1 + nota2 + nota3) /3
print(f"El promedio de {nota1}, {nota2}, {nota3} es: {promedio: .2f}")
if (promedio <= 7):
    print("Desaprobado")
else:
    print("Aprobado")
    
with open("mi_archivo.txt", "w") as archivo:
    archivo.write(f"El promedio es: {promedio}, jiji")

with open("mi_archivo.txt", "r") as archivo:
    salida = archivo.read()
    print("El archivo guardado:\n")
    print(salida)

###################################### LEER ARCHIVOS Y MOSTRARLO EN LINEA #################################


with open("mi_archivo.txt", "r") as archivo:
    for Linea in archivo:
        print(Linea.strip())