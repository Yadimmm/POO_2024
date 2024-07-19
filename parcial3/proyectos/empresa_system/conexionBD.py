import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            database='mi_empresa',
            user='root',
            password=''
        )
        if conexion.is_connected():
            return conexion
        else:
            print("No se pudo conectar a la base de datos")
            return None
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None