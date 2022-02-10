"""
Ejercicio 1.
Hacer un programa que tenga una lista de 8 numeros
enteros y haga lo siguiente:
- Recorrer la lista y mostrarla.
- Hacer funcion que recorra listas de numeros y devuelva un string.
- Ordenarla y mostrarla.
- Mostrar su longitud.
- Buscar algun elemento(que el usuario pida por teclado).
"""

numeros = [2, 1, 5, 4, 6, 3, 8, 7]
buscar = int(input("Ingresa numero a encontrar: "))


print("\n********** listado de contactos sin ordenar **********")

for numero in numeros:
    print(f"El numero encontrado es: {numero}")

print("\n********** listado de contactos ordenados **********")

numeros.sort()
for numero in numeros:
    print(f"El numero encontrado es: {numero}")

print(f"La longitud de la lista es: " + str(len(numeros)))
print(buscar in numeros)

print("\n********** listado de contactos función **********")
def recorrer(lista):
    resultante = ""
    for elemento in lista:
        resultante += "Elemento: " + str(elemento)
        resultante += "\n"
    return resultante

print(recorrer(numeros))