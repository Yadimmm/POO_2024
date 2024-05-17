#Solicitar 2 numeros al usuario y realizar todas las operaciones basicas de una calculadora (+,-,*,/) y mostrar por pantalla el resultado

numero1=int(input("Ingrese el primer numero: "))

numero2=int(input("Ingrese el segundo numero: "))

suma=numero1+numero2
resta=numero1-numero2
multiplicacion=numero1*numero2
division=numero1/numero2

print(f"Suma:{numero1} + {numero2} = {suma}")
print(f"Resta:{numero1} - {numero2} = {resta}")
print(f"Multiplicacion:{numero1} X {numero2} = {multiplicacion}")
print(f"Division:{numero1} / {numero2} = {division}")