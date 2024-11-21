#Lista de compras:
#Pedí al usuario que ingrese productos para una lista de compras y mostrá la lista completa al final.
#Permití que elimine algún elemento.

lista = ["manzana", "pan", "atun", "sopa"]

lista.append(input("Agrega un elemento a la lista del supermercado: \n"))

print(f"\nlista del supermercado actual:")
for i in lista:
    print(i)

while True:
    eliminar = input("¿Desea eliminar un alimento de la lista? (SI/NO)").lower()
    if(eliminar != "si" and eliminar != "no"):
        print("Ingresa solo 'si' o 'no'")
    else:
        if (eliminar == "si"):
            print(f"Productos a eliminar: {lista}")
            producto = input("Elimina un producto: ")
            if producto in lista:
                lista.remove(producto)
                print(f"Producto eliminado correctamente\nLista actualizada: {lista}")
                break
            else:
                print("El producto no esta en la lista.")
        elif(eliminar == "no"):
            print("Adios entonces")
            break
