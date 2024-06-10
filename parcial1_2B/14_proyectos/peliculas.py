import os
import msvcrt
from funciones_compartir import *

def mostrar_menu():
    print("\n\t....::::PeLiCuLaS PiRaTaS 4k::::....\n1. Agregar película\n2. Remover película\n3. Consultar películas\n4. Actualizar Pelicula\n5. Buscar Pelicula\n6. Vaciar lista\n7. Salir")
def pausa():
    print("\nPRESIONA UNA TECLA PARA CONTINUAR...")
    msvcrt.getch()

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("QUE OPCION ELEGIRAS HOY: ")
        if opcion == "1":
            os.system("cls")
            nombre_pelicula = input("Ingresa el nombre de la película: ")
            agregar_pelicula(nombre_pelicula)
            pausa()
        elif opcion == "2":
            os.system("cls")
            nombre_pelicula = input("Ingresa el nombre de la película a remover: ")
            remover_pelicula(nombre_pelicula)
            pausa()
        elif opcion == "3":
            os.system("cls")
            consultar_peliculas()
            pausa()
        elif opcion == "4":
            os.system("cls")
            nombre_actual = input("Ingresa el nombre de la película a actualizar: ")
            nombre_nuevo = input("Ingresa el nuevo nombre de la película: ")
            actualizar_pelicula(nombre_actual, nombre_nuevo)
            pausa()
        elif opcion == "5":
            os.system("cls")
            nombre_buscar = input("Ingresa el nombre de la película a buscar: ")
            buscar_pelicula(nombre_buscar)
            pausa()
        elif opcion == "6":
            os.system("cls")
            vaciar_lista()
            pausa()
        elif opcion == "7":
            print("¡Hasta luego!")
            break