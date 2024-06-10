"""
Una funcion es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeno que cumple una funcion especifica. La funcion se puede reutilizar con el simple hecho de invocarlas es decir mandarlas a llamar

Sintaxis:
def nombredeMifuncion(parametros):
    bloqueo o conjunto de instrucciones

nombredeMifuncion(parametros)

Las funciones pueden ser de 4 tipos
1.-Funcion que no recibe parametros y no regresa Valor
2.-Funcion que no recibe parametros y regresa valor 
3.-Funcion que recibe parametros y no regresa valor 
4.-Funcion que recibe parametros y regresa valor
"""
#Ejemplo 1 Crear una funcion para imprimir nombres de personas
#1.-Funcion que no recibe parametros y no regresa Valor
def nombre():
    nombre=input("Ingresa el nombre completo:")

nombre()
#Ejemplo 2 Sumar dos numero 
#2.-Funcion que no recibe parametros y regresa valor 
def suma():
    n1=int(input("Numero #1"))
    n2=int(input("Numero #2"))
    suma=n1+n2
    print(f"{n1} + {n2} = {suma}")
suma()
#Ejemplo 3 Sumar dos numero
#2.-Funcion que recibe parametros y regresa valor 
def suma():
    n1=int(input("Numero #1"))
    n2=int(input("Numero #2"))
    suma=n1+n2
    return suma

resultado=suma()
print(f"La suma es: {resultado}")
#Ejemplo 4 sumar do numeros
#3.-Funcion que recibe parametros y no regresa valor
def suma(num1,num2):
    suma=num1+num2
    print(f"La suma es: {suma}") 

n1=int(input("Numero #1:"))
n2=int(input("Numero #2:"))
suma(n1,n2)
#Ejemplo 5 sumar dos numeros
#4.-Funcion que recibe parametros y regresa valor
def suma(num1,num2):
    suma=num1+num2
    return suma

n1=int(input("Numero #1:"))
n2=int(input("Numero #2:"))
resultado=suma(n1,n2)
print(f"La suma es: {resultado}")
#Ejemplo 6 Crear un programa que solicite atravez de una funcion la siguiente informacion nombre del paciente,edad,estatura,tipo de sangre.Utilizar una funcion que reciba parametros y regrese valor
#1 Funcion no tiene parametros y no regresa valor
def paciente():
    nombre=input("Nombre del paciente:")
    edad=int(input("Edad del paciente:"))
    estatura=float(("Ingresa la estatura:"))
    sangre=input(input("Tipo de sangre"))
    print(f"Nombre del paciente {nombre} \n Edad:{edad} \n Estatura: {estatura} \n Tipo de sangre: {sangre}")

for i in range(1,4):
    paciente()
    
#2 Funcio no tine parametros y regresa valor
def paciente2():
    nombre=input("Nombre del paciente:")
    edad=int(input("Edad del paciente:"))
    estatura=float(("Ingresa la estatura:"))
    sangre=input(input("Tipo de sangre"))
    return f"Nombre del paciente {nombre} \n Edad:{edad} \n Estatura: {estatura} \n Tipo de sangre: {sangre}"

print(paciente2())

#3 Funcion tiene parametros y no regresa valor
def paciente3(nom,ed,est,sang):
    return f"Nombre del paciente {nombre} \n Edad:{edad} \n Estatura: {estatura} \n Tipo de sangre: {sangre}"

nombre=input("Nombre del paciente:")
edad=int(input("Edad del paciente:"))
estatura=float(("Ingresa la estatura:"))
sangre=input(input("Tipo de sangre"))
paciente3(nombre,edad,estatura,sangre)

#4 Funcion tiene parametros y regresa valor
def paciente3(nom,ed,est,sang):
    return f"Nombre del paciente {nombre} \n Edad:{edad} \n Estatura: {estatura} \n Tipo de sangre: {sangre}"

nombre=input("Nombre del paciente:")
edad=int(input("Edad del paciente:"))
estatura=float(("Ingresa la estatura:"))
sangre=input(input("Tipo de sangre"))
print(paciente3(nombre,edad,estatura,sangre))

def info():

    nombre=input("Ingrese el nombre del paciente: ")
    edad=int(input("Ingrese la edad del paciente: "))
    estatura=float(input("Ingrese la estatura del paciente (en metros): "))
    tipo_sangre=input("Ingrese el tipo de sangre del paciente: ")

    informacion=(nombre, edad, estatura, tipo_sangre)

    return informacion

datos_paciente=info()

print("\nInformación del paciente:")
print(f"Nombre: {datos_paciente[0]}")
print(f"Edad: {datos_paciente[1]} años")
print(f"Estatura: {datos_paciente[2]} metros")
print(f"Tipo de sangre: {datos_paciente[3]}")

'''
def saludar(nombre):
    print(f"Hola, {nombre}!")

# Llamada a la función
saludar("Paulina")
'''