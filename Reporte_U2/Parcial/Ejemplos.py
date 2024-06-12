# # Definición de una clase llamada "Persona"
# class Persona:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad

#     def saludar(self):
#         print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# # Crear una instancia (objeto) de la clase "Persona"
# mi_persona = Persona(nombre="Juan", edad=30)

# # Llamar al método "saludar" de la instancia
# mi_persona.saludar()  # Salida: "Hola, mi nombre es Juan y tengo 30 años."

# # Definición de una clase llamada "Persona"
# class Persona:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad

#     def saludar(self):
#         print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# # Crear una instancia (objeto) de la clase "Persona"
# mi_persona = Persona(nombre="Juan", edad=30)

# # Llamar al método "saludar" de la instancia
# mi_persona.saludar()  # Salida: "Hola, mi nombre es Juan y tengo 30 años."

class Animal:
    def sonido(self):
        print("Hace algún sonido")

# class Perro(Animal):
#     def sonido(self):
#         print("El perro ladra")

# mi_perro = Perro()
# mi_perro.sonido()  # Salida: "El perro ladra"
class Gato(Animal):
    def sonido(self):
        print("El gato maulla")

def hacer_sonar(animal):
    animal.sonido()

mi_gato = Gato()
hacer_sonar(mi_gato)  # Salida: "El gato maulla"
