import clases

persona = clases.Persona()
persona.setNombre("Michael")
persona.setApellidos("Ripoll")
persona.setAltura("1.73cm")
persona.setEdad("28 años")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()} {persona.getAltura()} {persona.getEdad()}")

informatico = clases.Informatico()
informatico.setNombre("Michael")
informatico.setApellidos("Ripoll")

print(f"El informatico es: {informatico.getNombre()} {informatico.getApellidos()}")

tecnico = clases.TecnicoRedes()
tecnico.setNombre("Michael")
tecnico.setApellidos("Ripoll")

print(f"El tecnico es: {tecnico.getNombre()} {tecnico.getApellidos()}")
