"""
Listas (Arrays)
Son colecciones o conjuntos de datos/valores, bajo un unico nombre.
Para acceder a esos valores podemos usar un indice númerico.
"""

pelicula = "Batman"

# Definir lista
peliculas = ["Batman", "Spiderman", "El señor de los anillos"]
cantantes = list(("2pac", "Drake", "Jennifer Lopez")) #Pasar como tupla
years = list(range(2020, 2050))
variada = ["Victor", 30, 4.4, True, "Texto"]

print(peliculas)
print(cantantes)
print(years)
print(variada)

# Indices
peliculas[1] = "Gran Torino"
print(peliculas[0])
print(peliculas[-2])
print(cantantes[1:3])
print(cantantes[0:])

# Añadir elementos a lista
cantantes.append("Kase O")
print(cantantes)

# Recorrer lista
print("\n********** listado Peliculas **********")

nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula: ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")

# Listas multidimensionles
print("\n********** listado de contactos **********")
contactos = [ 
    [
        "Antonio",
        "antonio@antonio.com"
    ],
    [
        "Luis",
        "luis@luis.com"
    ],
    [
        "Salvador",
        "salvador@salvador.com"
    ]
]

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("E-mail: " + elemento)
    print("\n")