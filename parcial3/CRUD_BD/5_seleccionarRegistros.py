from conexionBD import *

try:
    micursor=conexion.cursor()

    sql="select nombre,direccion,tel from clientes"
    micursor.execute(sql)
    resultado=micursor.fetchall() #MANDA A LLAMAR LAS TUPLAS

# print(resultado)
# print(resultado[0])
# print(resultado[1])
# print(resultado[2])

    if len(resultado)>0:
        print(f"Registros de la tabla: {len(resultado)}")
    for x in resultado:
        print(x)
except:
     print(f"Ocurrio un problema con el servidor.....Por favor intentalo mas tarde....")
else:
     print(f"Registro Insertado Correctamente")

