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
#Ejemplo2
#crear una lista de palabras, posteriormente buscar la coincidencia de una palabra
palabra = ["hola","utd", "como", "estas", "ok", "ok", "naranja"]
palabra_buscar = input("inserta palabra a buscar: ")

if palabra_buscar in palabra:
    for i, p in enumerate(palabra):
        if p == palabra_buscar:
            print(f"Encontré la palabra en la posición {i}")
else:
    print("No encontré la palabra en la lista")
#EJEMPLO # AGREGAR Y ELIMINAR ELEMENTOS DE UNA LISTA
#OS.SYSTEM("CLEAR")
numeros=[23,24,23]
print(numeros)
#agregar un elemento
numeros.append(100)
print(numeros)
numeros.insert(3,200)
print(numeros)
#Eliminar un elemento
numeros.remove(100)#indicar el elemento a borrar
print(numeros)
numeros.pop(2)#Indicar la posicion del elemento a borrar
print(numeros)