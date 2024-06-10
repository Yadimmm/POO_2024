# 1.-Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 
#  a.- Recorrer la lista y mostrarla
#  b.- hacer una funcion que recorra la lista de numeros y devuelva un string
#  c.- ordenarla y mostrarla
#  d.- mostrar su longitud
#  e.- buscar algun elemento que el usuario pida por teclado
def list_str(list_numeros):
 return ' '.join(str(e) for e in list_numeros)

list_numeros=[2,1,5,6,7,4,3,8]

def buscar_elementos(list_numeros,elemento):
   if list_numeros in elemento:
    print(f"El elemento {elemento} está en la lista.")
   else:
    print(f"El elemento {elemento} no está en la lista.")

print("LISTA ORIGINAL:")
for i in list_numeros:
    print(i)

print("LISTA STRING:")
print(list_str(list_numeros))

list_numeros.sort()
print("LISTA ORDENADA:")
for i in list_numeros:
    print(i)

print("LONGITUD DE LA LISTA:")
print(len(list_numeros))

elemento = int(input("INGRESA EL NUMERO A BUSCAR DEL 1 AL 8:"))
for i,p in enumerate(list_numeros):
 if p == elemento:
         print(f"{elemento} FUE ENCONTRADO EN LA POSICION {i}")
 if not elemento:
  print(f"NO SE ENCONTRO {elemento} EN LA LISTA")
