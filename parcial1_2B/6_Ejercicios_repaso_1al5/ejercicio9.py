#Hacer un programa que solicite numeros indefinidamente hasta que se introduzca el 111 y salir del programa
bandera=111
num=0

while num!=bandera:
    num=int(input("Ingresa un numero:"))
    if num==bandera:
        print("salida")