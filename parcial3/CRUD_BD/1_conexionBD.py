import mysql.connector

try:
    #Conectarse con la base de datos....
    conexion=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bd_python"
    )   

except Exception as e:
    print(f"ERROR:{e}")
    print(f"Tipo de error:{type(e).__name__}")
    print(f"Ocurrio un problema con el servidor.....Por favor intentalo mas tarde....")
else:
     print(f"Se creo la conexion con la base de datos exitosamente")