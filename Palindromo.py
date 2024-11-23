palabra = input("Ingrese una palabra para saber si es un palindromo: ")

palabrainvertida = palabra[:: -1]

if (palabra == palabrainvertida):
    print("Es palindromo")
else:
    print("No es palindromo")