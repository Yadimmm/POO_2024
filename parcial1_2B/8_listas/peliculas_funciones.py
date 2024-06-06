'''
peliculas_lista=[]

def agregar_peliculas(pelicula):
    peliculas_lista.append(pelicula)
    print(f"La pelicula {pelicula} ha sido agregada")

def remover_pelicula(pelicula):
    if pelicula in peliculas_lista:
        peliculas_lista.remove(pelicula)
        print(f"La pelicula {pelicula} fue removida")
    else:
        print(f"La pelicula {pelicula} no esta en la lista")

def consultar_pelicula():
    print("lista de peliculas:")
    for pelicula in peliculas_lista:
        print(f"-{pelicula}")
'''
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