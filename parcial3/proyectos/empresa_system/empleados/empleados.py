from mysql.connector import Error
from conexionBD import conectar

class Empleados:
    def __init__(self, id_empleado=None, nombre=None, puesto=None, salario=None):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario

    def crear_empleado(self):
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            query = "INSERT INTO empleados (nombre, puesto, salario) VALUES (%s, %s, %s)"
            valores = (self.nombre, self.puesto, self.salario)
            cursor.execute(query, valores)
            conexion.commit()
            print("Empleado creado exitosamente")
        except Error as e:
            print(f"Error al crear empleado: {e}")

    @staticmethod
    def leer_empleados():
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            query = "SELECT * FROM empleados"
            cursor.execute(query)
            resultados = cursor.fetchall()
            for fila in resultados:
                print(f"ID: {fila[0]}, Nombre: {fila[1]}, Puesto: {fila[2]}, Salario: {fila[3]}")
        except Error as e:
            print(f"Error al leer empleados: {e}")
        finally:
            if conexion is not None and conexion.is_connected():
                conexion.close()

    def actualizar_empleado(self):
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            query = "UPDATE empleados SET nombre = %s, puesto = %s, salario = %s WHERE id = %s"
            valores = (self.nombre, self.puesto, self.salario, self.id_empleado)
            cursor.execute(query, valores)
            conexion.commit()
            print("Empleado actualizado exitosamente")
        except Error as e:
            print(f"Error al actualizar empleado: {e}")
        finally:
            if conexion is not None and conexion.is_connected():
                conexion.close()

    @staticmethod
    def eliminar_empleado(id):
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            query = "DELETE FROM empleados WHERE id = %s"
            valor = (id,)
            cursor.execute(query, valor)
            conexion.commit()
            print("Empleado eliminado exitosamente")
        except Error as e:
            print(f"Error al eliminar empleado: {e}")
        finally:
            if conexion is not None and conexion.is_connected():
                conexion.close()