"""
Ejercicio 2. Escribir un script que nos muestre por pantalla
todos los numeros pares del 1 al 120
"""
mostrar_numero = 0

for mostrar_numero in range(1, 121):
    if mostrar_numero % 2 == 0:
        print(mostrar_numero)
else:
    print("Ejecución finalizada.")
    
