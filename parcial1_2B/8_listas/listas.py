''''
List(Array)
son collecciones o conjuntos de datos/valores bajo
un mismo nombre,para acceder a los valores se
hace con un indice numerico

Nota:sus valores si son modificables

La lista ees una coleccion ordenada y modificable.
Permite miembors duplicados.
'''
# #Ejemplo 1 crear una lista de numeros e imprimir el contenido
numeros=[23,34]
print("Contenido de la lista")
for numero in numeros:
 print(numero)
#recorrer la lsita con ciclo for
for numero in numeros:
     print(numero)

#Recorrer la lista con el ciclo while
numero=0
tamanio=len(numeros)
print(tamanio)
while numero<=len(numeros)-1:
    print(numeros[numero])
    numero+=1
#Ejemplo 2 Crear una lista de palabras y psoteriormente buscar la coincidencia de una palabra
palabras=['hola','como','estas','mamaica']
palabra_buscar=input("INGRESA LA PALABRA A BUSCAR:")
for i in palabras:
 if i==palabra_buscar:
    print(f"{palabra_buscar} está en la lista y se encontro en la posicion {palabras.index()}.")
 else:
    print(f"{palabra_buscar} no está en la lista.")