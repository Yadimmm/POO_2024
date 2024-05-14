#Esta estructura de control evalua una condicion si la condicion se cumple see ejecuta la o las instruciones contenidas detro de ella

#Esta estructura tiene 4 variantes 
#1.- if simple
#2.-if compuesto
#3.- if anidado
#4.-if con el elif

#Ejemplo 1 if
color="rojo"

if color=="rojo":
   print("Soy el color rojo")

    #Ejemplo 2 if compuesto

color="rojo"

if color=="rojo":
    print("Soy el color rojo")
else:
    print("No soy el color rojo")

    #Ejemplo 3 if anidado

    color="rojo"

if color=="rojo":
    print("Soy el color rojo")
    if color!="rojo":
        print("No soy rojo color rojo")
else:
    print("No soy el color rojo")

    #Ejemplo 4 if y elif

    color=input("Ingresa el color:")

if color=="rojo":
    print("Soy el color rojo")
elif color=="amarillo":
    print("Soy el color amarillo")
elif color=="azul":
    print("Soy el color azul")
elif color=="negro":
    print("Soy el color negro")
else:
    print("No soy ninguno de los colores anteriores")

