# 5.-Crear una lista y un diccionario con el contenido de esta tabla: 
#   ACCION              TERROR        DEPORTES
#   MAXIMA VELOCIDAD    LA MONJA       ESPN
#   ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
#   RAPIDO Y FURIOSO I  LA MALDICION   ACCION
lista=["ACCION","TERROR","DEPORTES"],["MAXIMA VELOCIDAD","LA MONJA","ESPN"],["ARMA MORTAL 4","EL CONJURO","MAS DEPORTES"],["RAPIDOS Y FURIOSO I","LA MALDICION","ACCION"]

diccionario={"ACCION":["MAXIMA VELOCIDAD","ARMA MORTAL 4","RAPIDO Y FURIOSO I"],"TERROR":["LA MONJA","EL CONJURO","LA MALDICION"],"DEPORTES":["ESPN","MAS DEPORTE","ACCION"]}

print("lista:")
for i in lista:
    print(i)

print("\n DICCIONARIO:")
for key,value in diccionario.items():
 print(f"{key}:{value}")


 #Key (clave): Es un identificador único que se utiliza para acceder a un elemento en el diccionario.Es como la etiqueta que se utiliza para identificar un elemento. Las claves en un diccionario deben ser únicas.

 #Value (valor) Es el dato que se almacena bajo una clave en el diccionario.Puede ser cualquier tipo de dato, como un número, una cadena de texto, una lista, otra estructura de datos.