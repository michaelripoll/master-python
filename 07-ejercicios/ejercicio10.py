"""
Ejercicio 10. El programa tiene que pedir la nota de 15 alumnos
y sacar por pantalla cuantos han aprobado y cuantos han suspendido.
"""
aprobados = 0
suspendidos = 0

for alumno in range(1, 16):
    nota = float(input("Ingresar nota de alumno: "))
    if nota >= 3.0:
        print("Estudiante aprobado")
        aprobados += 1
    else:
        print("Estudiante suspendido")
        suspendidos += 1
print(f"{aprobados} estudiantes aprobaron")
print(f"{suspendidos} estudiantes no aprobaron ")