"""
Ejercicio 7. Hacer un programa que muestre todos los numeros impares
entre dos numeros que decida el usuario.
"""

numero1 = int(input("Ingrese valor inicial: "))
numero2 = int(input("Ingrese valor final: "))
mostrar_numero = 0

if numero1 < numero2:
    for mostrar_numero in range(numero1, (numero2 + 1)):
        if mostrar_numero % 2 != 0:
            print(mostrar_numero)
    else:
        print("Ejecución finalizada.")
else:
    print("El valor inicial ingresado no puede ser mayor que el valor final !")