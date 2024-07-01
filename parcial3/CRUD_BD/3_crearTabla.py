import mysql.connector

conexion=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bd_python"
)

if conexion.is_connected:
    print("Se conecto con la BD")

#Crear una tabla dentro de una BD existente
sql="CREATE TABLE clientes (id INT PRIMARY KEY AUTO_INCREMENT,nombre varchar(60), direccion varchar(120), telefono varchar(10))"

micursor=conexion.cursor()
micursor.execute(sql)

if micursor:
    print("SE CREO LA TABLA CON EXITO")