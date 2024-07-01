from operadores import Cliente, Empleado, Veterinaria, Cita, Animal, Servicio

cliente1 = Cliente("Juan Hernandez Dueñes", "Lago 116", "6183242201", "juan@gmail.com")
animal1 = Animal("Dukii", "perro", 1, cliente1)
servicio1 = Servicio("Vacunación", "Primeras vacunas", 500)
empleado1 = Empleado("Luis Perez", "Calle 123", "5551234567", "luis@veterinaria.com", "Veterinario", 2000)


cliente2 = Cliente("Leonel Gallegos Villa", "lagos 213", "6751009643", "leovilla9@gmail.com")
animal2 = Animal("mali", "gato", 2, cliente2)
servicio2 = Servicio("Análisis clínicos", "Diagnosticar o descartar enfermedades", 550)

cliente1.registrar_mascota(animal1)
cliente2.registrar_mascota(animal2)

veterinaria = Veterinaria("VetCare", "Av. Principal 123", "5559876543")


veterinaria.registrar_cliente(cliente1)
veterinaria.registrar_cliente(cliente2)


veterinaria.asignar_empleados(empleado1)

cita1 = Cita("18-01-2005", "15:00", cliente1.datos_persona(), empleado1.datos_persona(), empleado1.telefono, servicio1.datos_servicio())
cita2 = Cita("17-05-2005", "16:00", cliente2.datos_persona(), empleado1.datos_persona(), empleado1.telefono, servicio2.datos_servicio())

veterinaria.programar_cita(cita1)
veterinaria.programar_cita(cita2)

print(veterinaria.datos_veterinaria())
print(f"\nServicio 1:\n{cita1.agregar_cita()}\n")
print(f"Servicio 2:\n{cita2.agregar_cita()}\n")