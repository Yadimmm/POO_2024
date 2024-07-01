import mysql.connector

#Crear conexion
conexion=mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

#Verificar la conexion
if conexion.is_connected():
    print("Se creo la conexion con exito")
else:
    print("NO fue posible conectarse")

#Crear otro objeto para ejecutar las instrucciones
micursor=conexion.cursor()

#Crear la base de datos desde python
sql="create database bd_python"
micursor.execute(sql)

#verificar que se creo la BD
if micursor:
    print("Se crep la BD exitosamente")

#Mostrar las BD que existen en mi servidor de MySQL
micursor.execute("show databases")

for x in micursor:
    print(x)