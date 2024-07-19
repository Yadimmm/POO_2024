import mysql.connector
from mysql.connector import Error
from conexion import obtener_conexion

class Servicio:
    def __init__(self, id_servicio, nombre, descripcion, duracion, precio):
        self.id_servicio = id_servicio
        self.nombre = nombre
        self.descripcion = descripcion
        self.duracion = duracion
        self.precio = precio

    def consultar_disponibilidad(self):
        """
        Consulta la disponibilidad del servicio en la base de datos.
        Devuelve los horarios ocupados para el servicio.
        """
        try:
            conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='bd_spa' 
            )
            if conexion.is_connected():
                cursor = conexion.cursor(dictionary=True)
                
                consulta = """
                SELECT fecha, hora
                FROM Reserva
                WHERE servicio_id = %s
                ORDER BY fecha, hora
                """
                
                cursor.execute(consulta, (self.id_servicio,))
                reservas = cursor.fetchall()

                if reservas:
                    print(f"Horarios ocupados para el servicio {self.nombre}:")
                    for reserva in reservas:
                        print(f"Fecha: {reserva['fecha']}, Hora: {reserva['hora']}")
                else:
                    print("No hay reservas para este servicio en este momento.")

        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
        
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()

    def modificar_servicios(self, nombre=None, descripcion=None, duracion=None, precio=None):
        """
        Modifica los detalles del servicio en la base de datos.
        """
        if nombre:
            self.nombre = nombre
        if descripcion:
            self.descripcion = descripcion
        if duracion:
            self.duracion = duracion
        if precio:
            self.precio = precio
        try:
            conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='bd_spa' 
            )
            if conexion.is_connected():
                cursor = conexion.cursor()

                consulta = """
                UPDATE Servicio
                SET nombre = %s, descripcion = %s, duracion = %s, precio = %s
                WHERE id_servicio = %s
                """

                cursor.execute(consulta, (self.nombre, self.descripcion, self.duracion, self.precio, self.id_servicio))
                conexion.commit()

                print("Servicio actualizado con éxito.")

        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")

        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()

class Notificacion:
    def __init__(self, id_notificacion, cliente, mensaje, fecha_envio):
        self.id_notificacion = id_notificacion
        self.cliente = cliente
        self.mensaje = mensaje
        self.fecha_envio = fecha_envio

    def enviar_notificacion(self):
        """
        Envía la notificación al cliente e inserta un registro en la base de datos.
        """
        try:
            conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='bd_spa'
            )
            if conexion.is_connected():
                cursor = conexion.cursor()
                consulta = """
                INSERT INTO Notificacion (cliente_id, mensaje, fecha_envio)
                VALUES (%s, %s, %s)
                """
                cursor.execute(consulta, (self.cliente.id_cliente, self.mensaje, self.fecha_envio))
                conexion.commit()
                print(f"Notificación enviada al cliente {self.cliente.get_nombre_completo()} con éxito.")
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")

        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()

class Reserva:
    def __init__(self, id_reserva, cliente, empleado, servicio, fecha, hora):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.empleado = empleado 
        self.servicio = servicio
        self.fecha = fecha
        self.hora = hora

    def confirmar_reserva(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
    
        consulta = """
        INSERT INTO Reserva (id_cliente, id_servicio, fecha, hora)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(consulta, (self.cliente.id_cliente, self.servicio.id_servicio, self.fecha, self.hora))
        conexion.commit()
    
        print("Reserva confirmada con éxito.")
        cursor.close()
        conexion.close()