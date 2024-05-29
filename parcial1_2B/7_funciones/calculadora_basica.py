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
 global n1,n2
 n1=int(input("Numero #1:"))
 n2=int(input("Numero #2:"))
 

def operacionAritmetica(num1,num2):
 if opcion=="1" or opcion=="+" or opcion=="SUMA":
  return(f"{n1}+{n2}={n1+n2}")
 elif opcion=="2" or opcion=="-" or opcion=="RESTA":
  return(f"{n1}-{n2}={n1-n2}")
 elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
  return(f"{n1}*{n2}={n1*n2}")
 elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
  return(f"{n1}/{n2}={n1/n2}")
 else:
  opcion=False
  return "Terminaste la ejecucion del SW"

opcion=True
while opcion:
 print("\n\t...:::CALCULADORA BASICA:::...\n 1.-Suma \n 2.-Resta \n 3.-Multiplicacion \n 4.-Division \n 5.-Salir")
 opcion=input("\t Elige una opcion:").upper() 

 solicitarNumeros()
 print(operacionAritmetica(n1,n2))