"""
FUNCIONES: 
Una función es un conjunto de instrucciones agrupadas bajo
un nombre concreto qeu pueden reutilizarse invocando a 
la función tantas veces como sea necesario.

def nombreDeMiFuncion(parametros):
    # BLOQUE / CONJUNTO DE INSTRUCCIONES

nombreDeMiFuncion(mi_parametro)

"""

"""
# Ejemplo 1
print("###### EJEMPLO 1 ######")

def muestraNombre():
    print("Victor")
    print("Paco")
    print("Juan")
    print("Francisco")
    print("Aitor")
    print("Nestor")
    print("\n")

# Invocar función
muestraNombre()


# Ejemplo 2: Parametros
print("###### EJEMPLO 2 ######")

def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print("Y eres mayor de edad")

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
mostrarTuNombre(nombre, edad)
"""

# Ejemplo 3
print("###### EJEMPLO 3 ######")

def tabla(numero):
    print(f"tabla de multiplicar del número: {numero}")

    for contador in range(11):
        operacion = numero * contador
        print(f"{numero} x {contador} = {operacion}")

numero = int(input("Introduce la tabla a obtener: "))
tabla(numero)

# Ejemplo 3.1
print("###### EJEMPLO 3.1 ######")

for numero_tabla in range(1, 11):
    tabla(numero_tabla)

# Ejemplo 4: Parametros opcionales

print("###### EJEMPLO 4 ######")

def getEmpleado(nombre, id = False):
    print("Empleado")
    print(f"{nombre}")

    if id != False:
        print(f"Cedula: {id}")

getEmpleado("Michael Ripoll", 1140860277)

# Ejemplo 5: Parametros opcionales y return o devolver datos
print("###### EJEMPLO 5 ######")

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"

    return saludo

print(saludame("Michael Ripoll"))

# Ejemplo 6: Parametros opcionales y return o devolver datos
print("###### EJEMPLO 6 ######")
def calculadora(numero1, numero2, basicas = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicación: " + str(multi)
        cadena += "\n"
        cadena += "División: " + str(division)

    return cadena

print (calculadora(56,12,True))

# Ejemplo 7
print("###### EJEMPLO 7 ######")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(devuelveTodo("Michael", "Ripoll Puche"))

# Ejemplo 8: Funciones lambda
print("###### EJEMPLO 8 #####")

dime_el_year = lambda year: f"El año es {year}"

print(dime_el_year(2022))