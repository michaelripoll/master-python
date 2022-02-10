cantantes = ["2pac", "Drake", "Bad Bunny", "Julio Iglesias"]
numeros = [1, 2, 5, 8, 3, 4]

# Ordenar
print(numeros)
numeros.sort()
print(numeros)

# Añadir elementos
cantantes.append("Natos y Waor")
cantantes.insert(1, "David Bisbal")
print(cantantes)

# Eliminar elementos
cantantes.pop(1)
cantantes.remove("Bad Bunny")
print(cantantes)

# Dar la vuelta
print(numeros)
numeros.reverse()
print(numeros)

# Buscar dentro de una lista
print("Drake" in cantantes)

# Contar elementos
print(len(cantantes))

# Cuantas veces aparece un elemento
print(numeros.count(8))

# Conseguir un indice
print(cantantes.index("Drake"))

# Unir listas
cantantes.extend(numeros)
print(cantantes)