import os
import msvcrt
from funciones_restaurante import *

def mostrar_menu():
    os.system('cls')
    print("\n\t....::::RESTAURANTE JAROCHOS::::....\n1. REGISTRAR COMPRA\n2. REGISTRAR INVENTARIO\n3. MOSTRAR INVENTARIO\n4. SALIR")

def pausa():
    print("\nPRESIONA UNA TECLA PARA CONTINUAR...")
    msvcrt.getch()

def registrar_compra():
    producto = input("Introduce el nombre del producto: ")
    cantidad = int(input("Introduce la cantidad comprada: "))
    precio = float(input("Introduce el precio del producto: "))
    print(f"Compra registrada: {cantidad} x {producto} a ${precio} cada uno.")

def registrar_inventario():
    producto = input("Introduce el nombre del producto para inventario: ")
    cantidad = int(input("Introduce la cantidad en inventario: "))
    print(f"Inventario actualizado: {producto}, cantidad: {cantidad}.")

def mostrar_inventario():
    inventario = {'producto1': 20, 'producto2': 50}
    for producto, cantidad in inventario.items():
        print(f"{producto}: {cantidad}")

if __name__ == "__main__":
    mostrar_menu()
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        registrar_compra()
    elif opcion == "2":
        registrar_inventario()
    elif opcion == "3":
        mostrar_inventario()
    elif opcion == "4":
        print("Saliendo del programa...")
    else:
        print("Opción no válida.")