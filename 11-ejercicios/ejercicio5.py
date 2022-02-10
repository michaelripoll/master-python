"""
Ejercicio  5:
Crear una lista con el contenido de esta tabla:
Accion      Aventura            Deportes
Gta         Assins              Fifa 21
Cod         Crash               Pro 21
Pugb        Prince of persia    Moto gp 21

Mostrar esta  informacion ordenada
"""

tabla = [
    {
        "Categoria": "Accion",
        "Juegos":["Gta", "call of Duty", "Pugb"]
    },
    {
        "Categoria": "Aventura",
        "Juegos": ["Assins", "Crash", "Prince of persia"]
    },
    {
        "Categoria": "Deportes",
        "Juegos": ["Fifa 21", "Pro 21", "Moto gp 21"]
    }
]

for categoria in tabla:
    print(f"--------------{categoria['Categoria']}-------------")
    for juego in categoria['Juegos']:
        print(juego)