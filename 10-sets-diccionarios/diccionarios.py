"""
Diccionario:
Un tipo de dato que almacena un conjunto de datos.
En un formato clave > valor.
Es parecid a un array asociativo o un objeto json.
"""

persona  = {
    "Nombre": "Victor",
    "Apellidos": "Robles",
    "Web": "victorroblesweb.es"
}

print(persona)
print(persona["Web"])

# Lista con diccionarios

contactos = [
    {
        "Nombre": "Antonio",
        "E-mail": "antonio@antonio.com"
    },
    {
        "Nombre": "Luis",
        "E-mail": "luis@luis.com"
    },
    {
        "Nombre": "Salvador",
        "E-mail": "salvador@salvador.com"
    }
]

print(contactos)
contactos[0]["nombre"] = "Antoñito"
print(contactos[0]["nombre"])

print("\n********** listado de contactos **********")

for contacto in contactos:
    print("------------------------------")
    print(f"Nombre del contacto: {contacto['Nombre']}")
    print(f"Email del contacto: {contacto['E-mail']}")
    print("------------------------------")