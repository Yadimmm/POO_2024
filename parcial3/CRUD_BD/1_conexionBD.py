import mysql.connector

#Conectarse  con la base de datos
conexion=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bd_python"
)
#Verificar conexion a la BD
if conexion.is_connected():
    print(f"Se creo la conexion con la base de datos exitosamente")
else:
    print(f"No fue posible conectar con la BD.......VERIFIQUE.........")