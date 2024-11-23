nota1 = int(input("Ingrese la primer nota del estudiante: "))
nota2 = int(input("Ingrese la segunda nota del estudiante: "))
nota3 = int(input("Ingrese la tercer nota del estudiante: "))

promedio = 0

def promediarNota():
    promedio = (nota1 + nota2 + nota3) /3
    print(f"El promedio de {nota1}, {nota2}, {nota3} es: {promedio: .2f}")
    if (promedio <= 7):
        print("Desaprobado")
    else:
        print("Aprobado")
    
promediarNota()