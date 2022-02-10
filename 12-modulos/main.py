"""
Modulos: Son funcionalidades ya hechas para reutilizar.
En python hay muchos modulos que los puedes consultar aqui:
https://docs.python.org/3/library/math.html#module-math

Podemos conseguir modulos que ya vienen en el lenguaje,
modulos en internet, y tambien podemos crear nuestros modulos.
"""
# Importar modulo propio
import mimodulo
from mimodulo import holaMundo # Importar una sola funcion de mi modulo
from mimodulo import * # Importar todas las funciones del modulo

print(mimodulo.holaMundo("Michael Ripoll"))
print(mimodulo.calculadora(3, 5, True))

print(holaMundo("Michael Ripoll"))
print(calculadora(3, 5, True))

# Modulo fechas
import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print("Mi fecha personalizada", fecha_personalizada)

print(datetime.datetime.now().timestamp())

# Modulo matematicas
import math

print("Raiz cuadrada de 10: ", math.sqrt(10))
print("Numero pi: ", float(math.pi))
print("Redondear alta: ", math.ceil(6.66798))
print("Redondear baja: ", math.floor(6.66798))

# Modulo random
import random
print("Número aleatorio entre 15 y 67: ", random.randint(15, 67))