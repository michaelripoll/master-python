import mysql.connector

# Conexión
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "",
database = "master_python"
)

# La concexión ha sido correcta?
# print(database)

# Cursor
cursor = database.cursor(buffered=True)


# Crear base de datos
"""
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")


for bd in cursor:
    print(bd)
"""

# Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY (id)
)
""")

cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)

#cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18500)")
coches = [
    ('Seat', 'Ibiza', 5000),
    ('Renault', 'Clio', 15000),
    ('Citroen', 'Saxo', 2000),
    ('Mercedes', 'Clase C', 35000)
]

#cursor.executemany("INSERT INTO vehiculos VALUES(null, %s, %s, %s)", coches)
database.commit()

# Listar
cursor.execute("SELECT * FROM vehiculos")
result = cursor.fetchall()

for coche in result:
    print(coche)

# Borrar
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Renault' ")
database.commit()

print(cursor.rowcount, "borrados!")

# Actualizar
cursor.execute("UPDATE vehiculos SET modelo = 'Léon WHERE marca = 'Seat'")
database.commit()

print(cursor.rowcount, "actualizados!")