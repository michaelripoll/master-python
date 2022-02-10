# Importar modulo
import sqlite3

# Conexión
conexion= sqlite3.connect('pruebas.db')

# Crear cursor
cursor = conexion.cursor()

# Crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT,"+
"titulo varchar(255), "+
"descripcion text, "+
"precio int(255)"+
")")

# Guardar cambios
conexion.commit()

# Insertar datos
#cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto', 'Descripción de mi producto', 550)")
#conexion.commit()

# Borrar registros
cursor.execute("DELETE FROM productos")
conexion.commit()

# Instar muchos registros de golpe
productos = [
    ("Ordenador portatil", "Buen PC", 700),
    ("Telefono movil", "Buen Telefono", 140),
    ("Placa Base", "Buena Placa", 80),
    ("Tablet 15", "Buena Tablet", 300)
]
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)
conexion.commit()

# Update
cursor.execute("UPDATE productos SET precio=678 WHERE precio=80")

# Listar datos
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()

print(productos)

for producto in productos:
    print("Titulo:", producto[1])
    print("Descripción:", producto[2])
    print("Valor:", producto[3])
    print("\n")

cursor.execute("SELECT * FROM productos")
producto = cursor.fetchone()
print(producto)

# Cerrar conexión
conexion.close()