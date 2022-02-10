"""
Ejercicio 6. Mostrar todas las tablas de multplicar del 1 al 10.
Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10.
"""

for cabecera in range(1, 11):

    print(f"\n#### Tabla de multiplicar del número {cabecera} ####")

    for numero_tabla in range(1, 11):

        if cabecera == 45:
            print("No se pueden mostrar numeros prohibidos !!")
            break  
        print(f"{cabecera} x {numero_tabla} = {cabecera*numero_tabla}")
else:
    print("Ejecución finalizada.")