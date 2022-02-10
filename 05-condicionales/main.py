"""

# Condicional IF

SI se_cumple_esta_condicion:
    Ejecutar grupo de instrucciones
SI NO:
    Se ejecutan otro grupo de instrucciones

if condicion:
    instrucciones
else:
    otras instrucciones


# Operadores de comparación
== igual
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

# Operadores logicos
and Y
or O
! Negación
not No

"""

# Ejemplo 1
print("########## EJEMPLO 1 ##########")

color = "Verde"
#color = input("Adivina cual es mi color favorito: ")

if color == "rojo":
    print("El color es Rojo")
else:
    print("Color incorrecto !!")

# Ejemplo 2
print("\n########## EJEMPLO 2 ##########")

year = 2020
#year = int(input("En que año estamos?"))

if(year >= 2021):
    print("Estamos de 2021 en adelante !!")
else:
    print("Es un año anterior a 2021")

# Ejemplo 3
print("\n########## EJEMPLO 3 ##########")

nombre = "Michael Ripoll"
ciudad = "Barcelona"
continente = "Europa"
edad = 28
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad !!")
    if continente != "Europa":
        print("El usuaro no es Europeo")
    else:
        print(f"Es europeo y de ciudad {ciudad}")
else:
    print(f"{nombre} no es mayor de edad !!")

# Ejemplo 4
print("\n########## EJEMPLO 4 ##########")

#dia = int(input("Introduce el dia de la semana: "))
dia = 2

"""
if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
        print("Es martes")
    else:
        if dia == 3:
            print("Es miercoles")
        else:
            if dia == 4:
                print("Es jueves")
            else:
                if dia == 5:
                    print("Es viernes")
                else:
                    ("Es fin de semana")
"""

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
else:
    print("Es fin de semana")

# Ejemplo 5
print("\n########## EJEMPLO 5 ##########")

edad_minima = 18
edad_maxima = 65
#edad_oficial = int(input("¿Tienes edad de trabajar? Introduce tu edad: "))
edad_oficial = 18

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Esta en edad de trabajar !!")
else:
    print("No esta en edad de trabajar !!")

# Ejemplo 6
print("\n########## EJEMPLO 6 ##########")

pais = "Alemania"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un pais de habla hispana !!")
else:
    print(f"{pais} no es un pais de habla hispana :(")

# Ejemplo 7
print("\n########## EJEMPLO 7 ##########")

pais = "España"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} no es un pais de habla hispana :(")
else:
    print(f"{pais} es un pais de habla hispana !!")

# Ejemplo 8
print("\n########## EJEMPLO 8 ##########")

pais = "Colombia"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} no es un pais de habla hispana :(")
else:
    print(f"{pais} es un pais de habla hispana !!")