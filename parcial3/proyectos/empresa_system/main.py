from funciones import *
from empleados import empleados

def menu():
    while True:
        borrarPantalla()
        print("""
        .::  Menu Principal ::.
            1. Crear empleado
            2. Leer empleados
            3. Actualizar empleado
            4. Eliminar empleado
            5. Salir
        """)
        opcion = input("Elige una opción: ").upper()

        if opcion == '1' or opcion == "CREAR EMPLEADO" or opcion == "CREAR":
            borrarPantalla()
            print("\n \t ..:: Crear Empleado ::..")
            nombre = input("Nombre: ")
            puesto = input("Puesto: ")
            salario = input("Salario: ")
            nuevo_empleado = empleados.Empleados(nombre=nombre, puesto=puesto, salario=salario)
            nuevo_empleado.crear_empleado()
            esperarTecla()

        elif opcion == '2' or opcion == "LEER" or opcion == "LEER EMPLEADO":
            borrarPantalla()
            print("\n \t ..:: Empleados en Sistema ::..")
            empleados.Empleados.leer_empleados()
            esperarTecla()

        elif opcion == '3' or opcion == "ACTUALIZAR" or opcion == "ACTUALIZAR EMPLEADO":
            borrarPantalla()
            print("\n \t ..:: Actualizar Empleado ::..")
            id = input("ID del empleado a actualizar: ")
            nombre = input("Nuevo nombre: ")
            puesto = input("Nuevo puesto: ")
            salario = input("Nuevo salario: ")
            empleado_actualizado = empleados.Empleados(id_empleado=id, nombre=nombre, puesto=puesto, salario=salario)
            empleado_actualizado.actualizar_empleado()
            esperarTecla()

        elif opcion == '4' or opcion == "ELIMINAR" or opcion == "ELIMINAR EMPLEADO":
            borrarPantalla()
            print("\n \t ..:: Eliminar Empleado ::..")
            id = input("ID del empleado a eliminar: ")
            empleados.Empleados.eliminar_empleado(id)
            esperarTecla()
            
        elif opcion == '5' or opcion == "SALIR":
            print("Sistema finalizado con éxito...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()