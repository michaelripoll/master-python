"""
Ejercicio 4. Pedir dos numeros al usuario y hacer todas las
operaciones basicas de una calculadora y mostrarlo por pantalla.
"""

numero1 = int(input("Ingrese primer numero: "))
numero2 = int(input("Ingrese segundo numero: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(f"Suma: {suma},\nResta: {resta},\nMultiplicación:{multiplicacion},\nDivisión: {division}")