"""
Ejercicio 4:
Crear un scripque tenga 4 variables, una lista, un string,
un entero y un booleno y que imprima un ensaje
segun el tipo de dato de cada variable. Usar funciones.
"""

def traducirTipo(tipo):
    result = None
    if tipo == list:
        result = "Lista"
    elif tipo == str:
        result = "Cadena de texto"
    elif tipo == int:
        result = "Numero entero"
    elif tipo == bool:
        result = "Booleano"
    return result

def comprobarTipado(dato, tipo):
    test = isinstance(dato, tipo)

    if test:
        result = f"Este dato es del tipo {traducirTipo(tipo)}"
    else:
        result = None

    return result

lista = ["Hola mundo", 10]
texto = "Es variable string"
entero = 23
booleano = True

def esLista():
    print(lista)
    return esLista

def esTexto():
    print(texto)
    return esTexto

def esEntero():
    print(entero)
    return esEntero

def esBooleano():
    print(booleano)
    return esBooleano

esLista()
esTexto()
esEntero()
esBooleano()
print(comprobarTipado(lista, list))
print(comprobarTipado(texto, str))
print(comprobarTipado(entero, int))
print(comprobarTipado(booleano, bool))