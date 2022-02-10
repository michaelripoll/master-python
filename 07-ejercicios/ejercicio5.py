"""
Ejercicio 5. Hacer un programa que muestre todos los numeros entre
dos numeros qe diga el usuario.
"""

contador = 0
numero1 = int(input("Ingrese primer numero: "))
numero2 = int(input("Ingrese segundo numero: "))

for contador in range(numero1, (numero2 + 1)):
    if contador >= numero1 and contador <= numero2:
        print(contador)
else:
    print("Ejecución finalizada.") 