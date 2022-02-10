"""
Ejercicio 9. Hacer un programa que pida numeros al usuario 
indefinidamente hasta meter el numero 111
"""

contador = 1

while contador < 100:
    numero = int(input("Ingrese un número: "))
    if numero == 111:
        print("Fin de la ejecución.")
        break
    print(contador)
    contador += 1

else:
    print("Fin de la ejecución.")