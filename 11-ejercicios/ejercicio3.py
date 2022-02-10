"""
Ejercicio 3:
Programa que compruebe si una variable esta vacia
y si esta vacia, rellenar la con texto en minusculas y mostrarlo
en mayusculas.
"""

texto = " "

if len(texto.strip()) <= 0:
    texto = "rellenada"
else:
    print(f"Variable con contenido {texto}")
print(texto.upper())