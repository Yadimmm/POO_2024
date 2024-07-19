import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from conexion import obtener_conexion

class Persona:
    def __init__(self, id_persona, nombre, apellidos, fecha_nacimiento, telefono, correo_electronico):
        self.id_persona = id_persona
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = telefono
        self.correo_electronico = correo_electronico

    def get_nombre_completo(self):
        return f"{self.nombre} {self.apellidos}"

    def actualizar_datos(self, nombre=None, apellidos=None, fecha_nacimiento=None, telefono=None, correo_electronico=None):
        if nombre:
            self.nombre = nombre
        if apellidos:
            self.apellidos = apellidos
        if fecha_nacimiento:
            self.fecha_nacimiento = fecha_nacimiento
        if telefono:
            self.telefono = telefono
        if correo_electronico:
            self.correo_electronico = correo_electronico

class Cliente(Persona):
    def __init__(self, id_cliente, nombre, apellidos, fecha_nacimiento, telefono, correo_electronico):
        super().__init__(id_cliente, nombre, apellidos, fecha_nacimiento, telefono, correo_electronico)
        self.id_cliente = id_cliente

    @staticmethod
    def registrar_cliente():
        def confirmar_registro():
            from main import menu_inicio_sesion

            nombre = entry_nombre.get()
            apellidos = entry_apellidos.get()
            fecha_nacimiento = entry_fecha_nacimiento.get()
            telefono = entry_telefono.get()
            correo_electronico = entry_correo_electronico.get()

            conexion = obtener_conexion()
            cursor = conexion.cursor()

            consulta_persona = """INSERT INTO Persona (nombre, apellidos, fecha_nacimiento, telefono, correo_electronico) 
                              VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(consulta_persona, (nombre, apellidos, fecha_nacimiento, telefono, correo_electronico))
            id_persona = cursor.lastrowid

            consulta_cliente = "INSERT INTO Cliente (id_cliente) VALUES (%s)"
            cursor.execute(consulta_cliente, (id_persona,))
            conexion.commit()

            messagebox.showinfo("Éxito", f"Cliente {nombre} {apellidos} registrado con éxito.")
            registrar_cliente_window.destroy()
            cursor.close()
            conexion.close()

            menu_inicio_sesion()

        def regresar():
            registrar_cliente_window.destroy()
            from main import menu_inicio_sesion
            menu_inicio_sesion()

        registrar_cliente_window = tk.Tk()
        registrar_cliente_window.title("Registrar Nuevo Cliente")

        tk.Label(registrar_cliente_window, text="Nombre").grid(row=0, column=0, padx=10, pady=10)
        entry_nombre = tk.Entry(registrar_cliente_window)
        entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(registrar_cliente_window, text="Apellidos").grid(row=1, column=0, padx=10, pady=10)
        entry_apellidos = tk.Entry(registrar_cliente_window)
        entry_apellidos.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(registrar_cliente_window, text="Fecha de Nacimiento (YYYY-MM-DD)").grid(row=2, column=0, padx=10, pady=10)
        entry_fecha_nacimiento = tk.Entry(registrar_cliente_window)
        entry_fecha_nacimiento.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(registrar_cliente_window, text="Teléfono").grid(row=3, column=0, padx=10, pady=10)
        entry_telefono = tk.Entry(registrar_cliente_window)
        entry_telefono.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(registrar_cliente_window, text="Correo Electrónico").grid(row=4, column=0, padx=10, pady=10)
        entry_correo_electronico = tk.Entry(registrar_cliente_window)
        entry_correo_electronico.grid(row=4, column=1, padx=10, pady=10)

        tk.Button(registrar_cliente_window, text="Registrar", command=confirmar_registro).grid(row=5, columnspan=2, pady=10)
        tk.Button(registrar_cliente_window, text="Regresar", command=regresar).grid(row=6, columnspan=2, pady=10)

        registrar_cliente_window.mainloop()

class Empleado(Persona):
    def __init__(self, id_empleado, nombre, apellidos, fecha_nacimiento, telefono, correo_electronico, password, especialidad):
        super().__init__(id_empleado, nombre, apellidos, fecha_nacimiento, telefono, correo_electronico)
        self.password = password
        self.especialidad = especialidad

    def actualizar_disponibilidad(self, dias_disponibles, hora_inicio, hora_fin):
        """
        Actualiza la disponibilidad del empleado en la base de datos.
        :param dias_disponibles: Lista de días en los que el empleado está disponible, por ejemplo: ['Lunes', 'Martes']
        :param hora_inicio: Hora de inicio de disponibilidad en formato 'HH:MM'
        :param hora_fin: Hora de fin de disponibilidad en formato 'HH:MM'
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
                
                dias_disponibles_str = ','.join(dias_disponibles)
                
                consulta = """
                UPDATE Empleado
                SET dias_disponibles = %s, hora_inicio = %s, hora_fin = %s
                WHERE id_empleado = %s
                """
                
                cursor.execute(consulta, (dias_disponibles_str, hora_inicio, hora_fin, self.id_empleado))
                conexion.commit()
                
                print("Disponibilidad actualizada con éxito.")
        
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
        
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()

    def consultar_reservas(self):
        try:
            conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='spa_system'
            )
            if conexion.is_connected():
                cursor = conexion.cursor(dictionary=True)
                
                consulta = """
                SELECT r.id_reserva, c.nombre AS cliente, s.nombre AS servicio, r.fecha, r.hora
                FROM Reserva r
                JOIN Cliente c ON r.cliente_id = c.id_cliente
                JOIN Servicio s ON r.servicio_id = s.id_servicio
                WHERE r.empleado_id = %s
                ORDER BY r.fecha, r.hora
                """
                
                cursor.execute(consulta, (self.id_empleado,))
                reservas = cursor.fetchall()

                if reservas:
                    print(f"Reservas para el empleado {self.get_nombre_completo()}:")
                    for reserva in reservas:
                        print(f"Reserva ID: {reserva['id_reserva']}, Cliente: {reserva['cliente']}, Servicio: {reserva['servicio']}, Fecha: {reserva['fecha']}, Hora: {reserva['hora']}")
                else:
                    print("No hay reservas para este empleado.")

        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
        
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()