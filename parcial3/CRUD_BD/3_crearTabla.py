import mysql.connector

try:
    conexion=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bd_python"
    )
except:
    print(f"Ocurrio un problema con el servidor.....Por favor intentalo mas tarde....")
else:
    #Crear una tabla dentro de una BD existente........
    sql="CREATE TABLE clientes (id INT PRIMARY KEY AUTO_INCREMENT,nombre varchar(60), direccion varchar(120), telefono varchar(10))"

    micursor=conexion.cursor()
    micursor.execute(sql)

    print("SE CREO LA TABLA CON EXITO")