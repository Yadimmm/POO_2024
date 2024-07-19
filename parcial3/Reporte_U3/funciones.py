import os
import msvcrt 

def borrarPantalla():
    os.system("cls")

def esperar_tecla():
    print("Presione cualquier tecla para continuar...")
    msvcrt.getch()