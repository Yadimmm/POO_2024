#Hacer un programa que resuelva lo siguiente. ¿Cuanto es el X por ciento de X numero?
porcentaje=int(input("Ingrese el porcentaje a calcular:"))
cantidad=int(input("Ingrese la cantidad:"))

resultado=int((porcentaje*cantidad)/100)
print(f"El {porcentaje} por ciento de {cantidad} es de {resultado}")