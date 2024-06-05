peliculas_lista=[]

def agregar_peliculas(pelicula):
    #pelicula=input("Ingresa la pelicual que deseas agregar:")
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