#Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario
num1= int(input("Ingrese el primer número: "))


num2= int(input("Ingrese el segundo número: "))


if num1 < num2:
    
    print(f"Los números entre {num1} y {num2} son:")
    for i in range(num1, num2 + 1):
        print(i, end=" ")
    print()  
else:
    print("El primer número debe ser menor que el segundo número.") 