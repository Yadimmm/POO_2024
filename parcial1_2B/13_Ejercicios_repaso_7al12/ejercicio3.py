# 3.-Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir el contenido de la lista en mayusculas

#item es una variable temporal que representa cada elemento de la lista a medida que se itera sobre ella. 
def comprobar_lista():
    lista=[]

    if not lista:
        print("LA LISTA VACIA ESTAR.LLENARLA DEBEMOS.")

        while True:
            elemento = input("INGRESA UNA PALABRA O FRASE O 'salir' PARA CONCLUIR:")
            if elemento.lower() == 'salir':
                break
            lista.append(elemento)

    print("\nCONTENIDO DE LA LISTA EN MAYUSCULAS:")
    for item in lista:
        print(item.upper())

comprobar_lista()