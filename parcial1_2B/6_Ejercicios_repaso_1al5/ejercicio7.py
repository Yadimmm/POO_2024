#Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario
num1=int(input("Ingresa el primer numero:"))
num2=int(input("Ingresa el segundo numero:"))

print(f"Los numeros impares entre {num1} y {num2} son:")
for numero in range(num1, num2 +1):
    if numero % 2!=0:
        print(numero)