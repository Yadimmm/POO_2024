#4.-Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico, y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones.
"""
#isinstance  función incorporada que devuelve True si el objeto especificado es una instancia del tipo especificado, de lo contrario devuelve False.
def tipo(variable):
    if isinstance(variable,list):
        return("La variable es una lista")
    elif isinstance(variable,str):
        return("La variable es unn cadena")
    elif isinstance(variable,int):
        return("La variable es un entero")
    elif isinstance(variable,bool):
        return("La variable es un logico")
    else:
        return("Tipo de dato desconocido")
"""
    
lista=[2,3,6,8,4,10]
cadena="Cheves o que"
entero=100
logico=True

def tipoo(variable):
    tipo=type(variable)
    if tipo==list:
        return("La variable es una lista")
    elif tipo==str:
        return("La variable es una cadena")
    elif tipo==int:
        return("La variable es un entero")
    elif tipo==bool:
        return("La variable es un logico")
    else:
        return("Tipo de dato desconocido")
    
print(tipoo(lista))
print(tipoo(cadena))
print(tipoo(entero))
print(tipoo(logico))