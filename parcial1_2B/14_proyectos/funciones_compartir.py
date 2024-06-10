lista_peliculas = []

def agregar_pelicula(nombre):
    lista_peliculas.append(nombre)
    print(f"¡La película '{nombre}' ha sido agregada!")

def remover_pelicula(nombre):
    if nombre in lista_peliculas:
        lista_peliculas.remove(nombre)
        print(f"La película '{nombre}' ha sido removida.")
    else:
        print(f"La película '{nombre}' no está en la lista.")

def consultar_peliculas():
    if lista_peliculas:
        print("Películas disponibles:")
        for pelicula in lista_peliculas:
            print(f"- {pelicula}")
    else:
        print("No hay películas en la lista.")

def actualizar_pelicula(nombre_actual, nombre_nuevo):
    if nombre_actual in lista_peliculas:
        indice = lista_peliculas.index(nombre_actual)
        lista_peliculas[indice] = nombre_nuevo
        print(f"La película '{nombre_actual}' ha sido actualizada a '{nombre_nuevo}'.")
    else:
        print(f"La película '{nombre_actual}' no está en la lista.")

def buscar_pelicula(nombre):
    if nombre in lista_peliculas:
        indice = lista_peliculas.index(nombre)
        print(f"La película '{nombre}' está en la posición {indice}.")
    else:
        print(f"La película '{nombre}' no está en la lista.")

def vaciar_lista():
    lista_peliculas.clear()
    print("La lista de películas ha sido vaciada.")

#calculadora con funciones
import math

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no permitida."

def raiz_cuadrada(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Error: Raíz cuadrada de un número negativo no permitida."

def potencia(a, b):
    return math.pow(a, b)



        