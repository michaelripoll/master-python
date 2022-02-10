import os, shutil

# Crear carpeta

if not os.path.isdir("./14-sistema-archivos/mi_carpeta"):
    os.mkdir("./14-sistema-archivos/mi_carpeta")
else:
    print("Ya existe el directorio")

# Eliminar
# os.rmdir("./mi_carpeta")

"""
# Copiar
ruta_original = "./mi_carpeta"
ruta_nueva = "./mi_carpeta_COPIADA"
shutil.copytree(ruta_original, ruta_nueva)
"""

print("Contenido de mi carpeta: ")
contenido =  os.listdir("./14-sistema-archivos/mi_carpeta")
print(contenido)