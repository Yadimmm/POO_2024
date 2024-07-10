#1er forma

# import conexionBD #cuando quieres usar el archivo llamado dentro del archivo

# micursor=conexionBD.conexion.cursor() 

# sql="INSERT INTO clientes (id, nombre, direccion, tel) VALUES (NULL, 'Daniel Contreras', 'Col. centro', '6181234567')"
# micursor.execute(sql)
# #Es necesario para que al final se complete el Execute(sql) y finalice la consulta SQL
# conexionBD.conexion.commit() 

# if micursor:
# print(f"Registro Insertado con Exito")


#2da forma

from conexionBD import * #Mas especifico para paquetes y modulos

try:
    micursor=conexion.cursor()

    sql="INSERT INTO clientes (id, nombre, direccion, tel) VALUES (NULL, 'Daniel Contreras', 'Col. centro', '6181234567')"
    micursor.execute(sql)
    #Es necesario para que al final se complete el Execute(sql) y finalice la consulta SQL
    conexion.commit() 
except:
     print(f"Ocurrio un problema con el servidor.....Por favor intentalo mas tarde....")
else:
     print(f"Registro Insertado Correctamente")
