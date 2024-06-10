#Los errores de ejecucion en un lenguaje de programacion se presentan cuando existe una anomalia o error dentro de la ejecucion del codigo lo cual provoca que se detenga la ejecucion del SW. Con el control y manejo de excepciones sera posible minimizar o evitar la interrupcion del programa debido a una excepcion.

#EJEMPLO 1 CUANDO UNA VARIABLE NO SE GENERA
# try:
#  nombre=input("Introduce el nombre completo de una persona:")

#  if len(nombre)>0:
#     nombre_usuario="El nombre completo del usuario es:"+nombre

#  print(nombre_usuario)
# except:
#   print("Es necesaio introducir un nombre de usuario....Verificalo")

# x=3+4
# print("el valor de x es:"+str(x))

#EJEMPLO 2 CUANDO SE SOLICITA UN NUMERO Y SE INGRESA OTRA COSA
# try:
#  numero=int(input("Ingresa un numero entero:"))

#  if numero>0:
#     print("Soy un numero entero positivo")
#  elif numero==0:
#     print("SOY UN NUMERO ENTERO NEUTRO")
#  else:
#     print("SOY UN NUMERO ENTERO NEGATIVO")
# except ValueError:
#    print("INTRODUCE UN NUMERO ENTERO")

#EJEMPLO 3 GENERAN MULTIPLE EXCEPCIONES
try:
 numero=int(input("INTRODUCE UN NUMERO:"))
 print("EL CUADRADO DEL NUMERO ES:"+str(numero*numero))
except ValueError:
  print("INTRODUCE UN NUMERO ENTERO")
except TypeError:
  print("SE DEBE CONVERTIR EL NUMERO A ENTERO")
else:
  print("NO SE PRESENTARON ERRORES DE EJECUCION")
finally:
  print("TERMINE LA EJECUCION")