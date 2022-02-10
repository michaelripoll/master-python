"""
Ejercicio 2:
Escribir un programa que añada valores a una lista
mientras que su longitud sea menos a 120 y luego mostrar la lista.
Plus: Usar while y for.
"""

print("\n********** For **********")
coleccionFor = []
coleccionWhile = []

for item in range(1, 121):
    valor = int(input("Ingresar valores: "))

    if len(coleccionFor) <= 11:
        coleccionFor.append(valor)
        print(coleccionFor)

print("\n********** While **********")
contador = 1
while contador <= 120:
    valor = int(input("Ingresar valores: "))

    if len(coleccionWhile) <= 120:
        coleccionWhile.append(valor)
        print(coleccionWhile)
        contador +=1
    