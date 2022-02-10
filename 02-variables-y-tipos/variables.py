"""
Una variable es un contenedor de información
que dentro guardará un dato, se pueden crear
much variables y que cada una tenga un dato distinto
"""

#Crear variables y asignarle un valor
texto = "Máster en Python"
texto2 = "Con Víctor Robles"
numero = 45
decimal = 6.7

#Mostrar valor de las variables
print(texto)
print(texto2)
print(numero)
print(decimal)

print("--------------------------------------------")

# Sustituir el valor de algunas variables / reasignando valores
numero = 77
decimal = 8.9

print(numero)
print(decimal)

print("--------------------------------------------")

#Concatenación
nombre = "Michael"
apellido = "Ripoll"
web = "michaelripollweb.com"

print(nombre+" "+apellido+" - "+web)
print(f"{nombre} {apellido} - {web}")
print("Hola me llamo {} {} y mi web es: {}".format(nombre, apellido, web))

print(nombre, apellido, web)