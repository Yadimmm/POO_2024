# opcion1=True
# while opcion1:
#  print("\n\t...:::CALCULADORA BASICA:::...\n 1.-Suma \n 2.-Resta \n 3.-Multiplicacion \n 4.-Division \n 5.-Salir")

#  opcion=input("\t Elige una opcion:").upper()

#  if opcion=="1" or opcion=="+" or opcion=="SUMA":
#   n1=int(input("Numero #1:"))
#   n2=int(input("Numero #2:"))
#   print(f"{n1}+{n2}={n1+n2}")
#  elif opcion=="2" or opcion=="-" or opcion=="RESTA":
#   n1=int(input("Numero #1:"))
#   n2=int(input("Numero #2:"))
#   print(f"{n1}-{n2}={n1-n2}")
#  elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
#   n1=int(input("Numero #1:"))
#   n2=int(input("Numero #2:"))
#   print(f"{n1}*{n2}={n1*n2}")
#  elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
#   n1=int(input("Numero #1:"))
#   n2=int(input("Numero #2:"))
#   print(f"{n1}/{n2}={n1/n2}")
#  else:
#   print("Terminaste la ejecucion del SW")
#   opcion1=False

def solicitarNumeros():
    global n1, n2
    n1 = int(input("Numero #1:"))
    n2 = int(input("Numero #2:"))

def operacionAritmetica(opcion):
    if opcion == "1" or opcion == "+" or opcion == "SUMA":
        solicitarNumeros()
        return f"{n1}+{n2}={n1+n2}"
    elif opcion == "2" or opcion == "-" or opcion == "RESTA":
        solicitarNumeros()
        return f"{n1}-{n2}={n1-n2}"
    elif opcion == "3" or opcion == "*" or opcion == "MULTIPLICACION":
        solicitarNumeros()
        return f"{n1}*{n2}={n1*n2}"
    elif opcion == "4" or opcion == "/" or opcion == "DIVISION":
        solicitarNumeros()
        return f"{n1}/{n2}={n1/n2}"
    else:
        return "Terminaste la ejecucion del SW"

while True:
    print("\n\t...:::CALCULADORA BASICA:::...\n 1.-Suma \n 2.-Resta \n 3.-Multiplicacion \n 4.-Division \n 5.-Salir")
    opcion = input("\t Elige una opcion:").upper()
    
    if opcion=="5" or opcion=="SALIR":
        print("Terminaste la ejecucion del SW")
        break
    
    print(operacionAritmetica(opcion))