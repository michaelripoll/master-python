nada = None
cadena = "Hola soy Michael Ripoll"
entero = 99
flotante = 4.2
booleano = True
lista = [10, 20, 30, 100, 200]
listaString = [44, "treinta", 30, "cuarenta"]
tuplaNoCambia = ("master", "en", "python")
diccionario = {
    "nombre": "Michael",
    "apellido": "Ripoll",
    "curso": "Master en Python"
}
rango = range(9)
dato_byte = b"Probando"

# Imprimir variable
print(nada)
print(cadena)
print(entero)
print(flotante)
print(booleano)
print(lista)
print(listaString)
print(tuplaNoCambia)
print(diccionario)
print(rango)
print(dato_byte)

print("-----------------")

# Mostrar tipo de dato
print(type(nada))
print(type(cadena))
print(type(entero))
print(type(flotante))
print(type(booleano))
print(type(lista))
print(type(listaString))
print(type(tuplaNoCambia))
print(type(diccionario))
print(type(rango))
print(type(dato_byte))

print("-----------------")
# Convirtiendo tipos de datos
texto = "Hola soy un texto"
numerito = str(776)

print(texto+" "+numerito)