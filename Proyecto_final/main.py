import tkinter as tk
from tkinter import messagebox
from reservas.reserva import Reserva, Servicio
from usuarios.usuario import Empleado, Cliente
from funciones import borrarPantalla, esperar_tecla
from conexion import obtener_conexion
from plyer import notification
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def menu_inicio_sesion():
    def iniciar_sesion():
        root.destroy()  # Cierra la ventana del menú principal
        iniciar_sesion_empleado()

    def registrar_empleado_fn():
        root.destroy()  # Cierra la ventana del menú principal
        registrar_empleado()

    def registrar_cliente_fn():
        root.destroy()  # Cierra la ventana del menú principal
        Cliente.registrar_cliente()

    def salir():
        root.destroy()  # Cierra la ventana del menú principal

    # Configuración de la ventana principal del menú
    root = tk.Tk()
    root.title("Sistema Gestión WAVE PARADISE")
    root.attributes('-fullscreen', True)  # Configuración para pantalla completa
    root.configure(bg="#f0f0f0")  # Color de fondo

    # Etiquetas y botones del menú principal con fuente grande
    tk.Label(root, text="....::::::Sistema Gestión WAVE PARADISE::::::....", font=("Helvetica", 24), bg="#f0f0f0").pack(pady=50)

    tk.Button(root, text="Iniciar sesión como Empleado", command=iniciar_sesion, width=30, height=2, font=("Helvetica", 18)).pack(pady=20)
    tk.Button(root, text="Registrar nuevo Empleado", command=registrar_empleado_fn, width=30, height=2, font=("Helvetica", 18)).pack(pady=20)
    tk.Button(root, text="Registrar nuevo Cliente", command=registrar_cliente_fn, width=30, height=2, font=("Helvetica", 18)).pack(pady=20)
    tk.Button(root, text="Salir", command=salir, width=30, height=2, font=("Helvetica", 18)).pack(pady=20)

    root.mainloop()

def iniciar_sesion_empleado():
   def verificar_credenciales():
    id_empleado = entry_id.get()
    correo_electronico = entry_email.get()
    password = entry_password.get()

    conexion = obtener_conexion()
    if conexion is None:
        messagebox.showerror("Error", "No se pudo conectar a la base de datos.")
        return

        try:
            cursor = conexion.cursor(dictionary=True)
        
            consulta = """
            SELECT p.id_persona, p.nombre, p.apellidos, p.telefono, p.correo_electronico, e.especialidad, e.password
            FROM Persona p
            JOIN Empleado e ON p.id_persona = e.id_empleado
            WHERE e.id_empleado = %s AND p.correo_electronico = %s AND e.password = %s
            """
            cursor.execute(consulta, (id_empleado, correo_electronico, password))
            empleado_data = cursor.fetchone()

            if empleado_data:
                empleado = Empleado(
                empleado_data['id_persona'], 
                empleado_data['nombre'], 
                empleado_data['apellidos'], 
                None, 
                empleado_data['telefono'], 
                empleado_data['correo_electronico'], 
                empleado_data['password'], 
                empleado_data['especialidad']
            )
                messagebox.showinfo("Éxito", f"Bienvenido {empleado.nombre} {empleado.apellidos}")
                root.destroy()  # Cierra la ventana de inicio de sesión
                menu_gestion_reservas(empleado)  # Acceso al menú CRUD
            else:
                messagebox.showerror("Error", "ID, correo electrónico o contraseña incorrectos.")
        
            cursor.close()
            conexion.close()
        except Error as e:
            messagebox.showerror("Error", f"Error al realizar la consulta: {e}")
            if conexion.is_connected():
                conexion.close()


    def regresar():
        root.destroy()
        menu_inicio_sesion()

    # Configuración de la ventana de inicio de sesión
    root = tk.Tk()
    root.title("Inicio de Sesión - Empleado")
    root.attributes('-fullscreen', True)  # Pantalla completa
    root.configure(bg="#f0f0f0")

    # Crear un frame para contener los widgets centrados
    frame = tk.Frame(root, bg="#f0f0f0")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Etiquetas y campos de entrada con fuente grande
    tk.Label(frame, text="ID de Empleado", font=("Helvetica", 18), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=20)
    entry_id = tk.Entry(frame, font=("Helvetica", 18))
    entry_id.grid(row=0, column=1, padx=10, pady=20)

    tk.Label(frame, text="Correo Electrónico", font=("Helvetica", 18), bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=20)
    entry_email = tk.Entry(frame, font=("Helvetica", 18))
    entry_email.grid(row=1, column=1, padx=10, pady=20)

    tk.Label(frame, text="Contraseña", font=("Helvetica", 18), bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=20)
    entry_password = tk.Entry(frame, show="*", font=("Helvetica", 18))
    entry_password.grid(row=2, column=1, padx=10, pady=20)

    # Botón de inicio de sesión
    tk.Button(frame, text="Iniciar Sesión", command=verificar_credenciales, font=("Helvetica", 18)).grid(row=3, columnspan=2, padx=10, pady=20)
    tk.Button(frame, text="Regresar", command=regresar, font=("Helvetica", 18)).grid(row=4, columnspan=2, padx=10, pady=20)

    root.mainloop()
def registrar_empleado():
    def confirmar_registro():
        nombre = entry_nombre.get()
        apellidos = entry_apellidos.get()
        fecha_nacimiento = entry_fecha_nacimiento.get()
        telefono = entry_telefono.get()
        correo_electronico = entry_correo_electronico.get()
        password = entry_password.get()
        especialidad = entry_especialidad.get()

        conexion = obtener_conexion()
        cursor = conexion.cursor()
        
        consulta_persona = """INSERT INTO Persona (nombre, apellidos, fecha_nacimiento, telefono, correo_electronico) 
                              VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(consulta_persona, (nombre, apellidos, fecha_nacimiento, telefono, correo_electronico))
        id_persona = cursor.lastrowid
        
        consulta_empleado = """INSERT INTO Empleado (id_empleado, password, especialidad) 
                               VALUES (%s, %s, %s)"""
        cursor.execute(consulta_empleado, (id_persona, password, especialidad))
        conexion.commit()

        messagebox.showinfo("Éxito", f"Empleado {nombre} {apellidos} registrado con éxito.")
        registrar_empleado_window.destroy()  # Cierra la ventana después de registrar al empleado

        cursor.close()
        conexion.close()

        menu_inicio_sesion()

    def regresar():
        registrar_empleado_window.destroy()
        menu_inicio_sesion()

    # Configuración de la ventana de registro de empleado
    registrar_empleado_window = tk.Tk()
    registrar_empleado_window.title("Registrar Nuevo Empleado")
    registrar_empleado_window.attributes('-fullscreen', True)  # Pantalla completa
    registrar_empleado_window.configure(bg="#f0f0f0")

    # Etiquetas y campos de entrada con fuente grande
    tk.Label(registrar_empleado_window, text="Nombre", font=("Helvetica", 18), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=20)
    entry_nombre = tk.Entry(registrar_empleado_window, font=("Helvetica", 18))
    entry_nombre.grid(row=0, column=1, padx=10, pady=20)

    tk.Label(registrar_empleado_window, text="Apellidos", font=("Helvetica", 18), bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=20)
    entry_apellidos = tk.Entry(registrar_empleado_window, font=("Helvetica", 18))
    entry_apellidos.grid(row=1, column=1, padx=10, pady=20)

    tk.Label(registrar_empleado_window, text="Fecha de Nacimiento (YYYY-MM-DD)", font=("Helvetica", 18), bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=20)
    entry_fecha_nacimiento = tk.Entry(registrar_empleado_window, font=("Helvetica", 18))
    entry_fecha_nacimiento.grid(row=2, column=1, padx=10, pady=20)

    tk.Label(registrar_empleado_window, text="Teléfono", font=("Helvetica", 18), bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=20)
    entry_telefono = tk.Entry(registrar_empleado_window, font=("Helvetica", 18))
    entry_telefono.grid(row=3, column=1, padx=10, pady=20)

    tk.Label(registrar_empleado_window, text="Correo Electrónico", font=("Helvetica", 18), bg="#f0f0f0").grid(row=4, column=0, padx=10, pady=20)
    entry_correo_electronico = tk.Entry(registrar_empleado_window, font=("Helvetica", 18))
    entry_correo_electronico.grid(row=4, column=1, padx=10, pady=20)

    tk.Label(registrar_empleado_window, text="Contraseña", font=("Helvetica", 18), bg="#f0f0f0").grid(row=5, column=0, padx=10, pady=20)
    entry_password = tk.Entry(registrar_empleado_window, show="*", font=("Helvetica", 18))
    entry_password.grid(row=5, column=1, padx=10, pady=20)

    tk.Label(registrar_empleado_window, text="Especialidad", font=("Helvetica", 18), bg="#f0f0f0").grid(row=6, column=0, padx=10, pady=20)
    entry_especialidad = tk.Entry(registrar_empleado_window, font=("Helvetica", 18))
    entry_especialidad.grid(row=6, column=1, padx=10, pady=20)

    # Botón para confirmar el registro
    tk.Button(registrar_empleado_window, text="Registrar", command=confirmar_registro, font=("Helvetica", 18)).grid(row=7, columnspan=2, pady=20)
    tk.Button(registrar_empleado_window, text="Regresar", command=regresar, font=("Helvetica", 18)).grid(row=8, columnspan=2, pady=20)

    registrar_empleado_window.mainloop()

def menu_gestion_reservas(empleado):
    def regresar():
        menu.destroy()
        menu_inicio_sesion()

    menu = tk.Tk()
    menu.title(f"Gestión de Reservas - Bienvenido {empleado.nombre} {empleado.apellidos}")
    menu.attributes('-fullscreen', True)  # Pantalla completa
    menu.configure(bg="#f0f0f0")

    # Botones del menú CRUD con fuente grande
    tk.Button(menu, text="Crear Reserva", command=lambda: crear_reserva(empleado), width=30, height=2, font=("Helvetica", 18)).pack(pady=20)
    tk.Button(menu, text="Leer Reservas", command=leer_reservas, width=30, height=2, font=("Helvetica", 18)).pack(pady=20)
    tk.Button(menu, text="Actualizar Reserva", command=actualizar_reserva, width=30, height=2, font=("Helvetica", 18)).pack(pady=20)
    tk.Button(menu, text="Eliminar Reserva", command=eliminar_reserva, width=30, height=2, font=("Helvetica", 18)).pack(pady=20)
    tk.Button(menu, text="Salir", command=regresar, width=30, height=2, font=("Helvetica", 18)).pack(pady=20)

    menu.mainloop()

def crear_reserva(empleado):
    def confirmar_creacion():
        id_cliente = entry_id_cliente.get()
        id_servicio = entry_id_servicio.get()
        fecha = entry_fecha.get()
        hora = entry_hora.get()

        conexion = obtener_conexion()
        cursor = conexion.cursor()
        
        consulta_cliente = """
        SELECT p.id_persona, p.nombre, p.apellidos, p.correo_electronico
        FROM Persona p
        JOIN Cliente c ON p.id_persona = c.id_cliente
        WHERE c.id_cliente = %s
        """
        cursor.execute(consulta_cliente, (id_cliente,))
        cliente_data = cursor.fetchone()
        
        if cliente_data:
            cliente = Cliente(cliente_data[0], cliente_data[1], cliente_data[2], None, None, cliente_data[3])
        else:
            messagebox.showerror("Error", "Cliente no encontrado.")
            return
        
        consulta_servicio = "SELECT * FROM servicio WHERE id_servicio = %s"
        cursor.execute(consulta_servicio, (id_servicio,))
        servicio_data = cursor.fetchone()
        
        if servicio_data:
            servicio = Servicio(servicio_data[0], servicio_data[1], servicio_data[2], servicio_data[3], servicio_data[4])
            nombre_servicio = servicio.nombre  
        else:
            messagebox.showerror("Error", "Servicio no encontrado.")
            return
        
        reserva = Reserva(None, cliente, empleado, servicio, fecha, hora)
        reserva.confirmar_reserva()
        
        mensaje = f"Reserva creada para el cliente {cliente.nombre} {cliente.apellidos} con el servicio {nombre_servicio}."
        
        enviar_notificacion("Reserva Creada", mensaje)
        registrar_notificacion(conexion, cliente.id_cliente, mensaje)

        asunto = "Confirmación de Reserva - SPA"
        cuerpo = f"Estimado {cliente.nombre},\n\nSu reserva para el servicio {nombre_servicio} el día {fecha} a las {hora} ha sido confirmada.\n\nGracias por elegirnos."
        enviar_correo(cliente.correo_electronico, asunto, cuerpo)
        
        messagebox.showinfo("Éxito", "Reserva creada con éxito.")
        crear_reserva_window.destroy()

        cursor.close()
        conexion.close()

    def regresar():
        crear_reserva_window.destroy()
        menu_gestion_reservas(empleado)

    crear_reserva_window = tk.Tk()
    crear_reserva_window.title("Crear Nueva Reserva")
    crear_reserva_window.attributes('-fullscreen', True)  # Pantalla completa
    crear_reserva_window.configure(bg="#f0f0f0")

    # Etiquetas y campos de entrada con fuente grande
    tk.Label(crear_reserva_window, text="ID Cliente", font=("Helvetica", 18), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=20)
    entry_id_cliente = tk.Entry(crear_reserva_window, font=("Helvetica", 18))
    entry_id_cliente.grid(row=0, column=1, padx=10, pady=20)

    tk.Label(crear_reserva_window, text="ID Servicio", font=("Helvetica", 18), bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=20)
    entry_id_servicio = tk.Entry(crear_reserva_window, font=("Helvetica", 18))
    entry_id_servicio.grid(row=1, column=1, padx=10, pady=20)

    tk.Label(crear_reserva_window, text="Fecha (YYYY-MM-DD)", font=("Helvetica", 18), bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=20)
    entry_fecha = tk.Entry(crear_reserva_window, font=("Helvetica", 18))
    entry_fecha.grid(row=2, column=1, padx=10, pady=20)

    tk.Label(crear_reserva_window, text="Hora (HH:MM)", font=("Helvetica", 18), bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=20)
    entry_hora = tk.Entry(crear_reserva_window, font=("Helvetica", 18))
    entry_hora.grid(row=3, column=1, padx=10, pady=20)

    # Botón para confirmar la creación de la reserva
    tk.Button(crear_reserva_window, text="Confirmar", command=confirmar_creacion, font=("Helvetica", 18)).grid(row=4, columnspan=2, pady=20)
    tk.Button(crear_reserva_window, text="Regresar", command=regresar, font=("Helvetica", 18)).grid(row=5, columnspan=2, pady=20)

    crear_reserva_window.mainloop()

def leer_reservas():
    def mostrar_reservas():
        conexion = obtener_conexion()  # Asegúrate de que esta función esté definida en tu código
        cursor = conexion.cursor(dictionary=True)
        
        consulta = """
        SELECT r.id_reserva, p.nombre AS cliente, s.nombre AS servicio, r.fecha, r.hora 
        FROM Reserva r 
        JOIN Cliente c ON r.id_cliente = c.id_cliente 
        JOIN Persona p ON c.id_cliente = p.id_persona
        JOIN servicio s ON r.id_servicio = s.id_servicio
        """
        
        cursor.execute(consulta)
        reservas = cursor.fetchall()

        if reservas:
            for reserva in reservas:
                texto_reservas.insert(tk.END, f"Reserva ID: {reserva['id_reserva']}, Cliente: {reserva['cliente']}, Servicio: {reserva['servicio']}, Fecha: {reserva['fecha']}, Hora: {reserva['hora']}\n")
            
            mensaje = "Se han consultado las reservas existentes."
            enviar_notificacion("Consulta de Reservas", mensaje)
            registrar_notificacion(conexion, None, mensaje) 
        else:
            texto_reservas.insert(tk.END, "No hay reservas registradas.\n")
            mensaje = "No hay reservas registradas para mostrar."
            enviar_notificacion("Consulta de Reservas", mensaje)
            registrar_notificacion(conexion, None, mensaje)

        cursor.close()
        conexion.close()

    def regresar():
        leer_reservas_window.destroy()
        menu_gestion_reservas(Empleado)

    # Configuración de la ventana para mostrar las reservas
    leer_reservas_window = tk.Tk()
    leer_reservas_window.title("Consultar Reservas")
    leer_reservas_window.attributes('-fullscreen', True)  # Pantalla completa
    leer_reservas_window.configure(bg="#f0f0f0")

    # Crear un cuadro de texto para mostrar las reservas con fuente grande
    texto_reservas = tk.Text(leer_reservas_window, height=20, width=80, font=("Helvetica", 18))
    texto_reservas.pack(pady=20)

    # Botón para cerrar la ventana
    tk.Button(leer_reservas_window, text="Cerrar", command=leer_reservas_window.destroy, font=("Helvetica", 18)).pack(pady=20)
    tk.Button(leer_reservas_window, text="Regresar", command=regresar, font=("Helvetica", 18)).pack(pady=20)

    mostrar_reservas()  # Llamar a la función para mostrar las reservas

    leer_reservas_window.mainloop()

def actualizar_reserva():
    def buscar_reserva():
        id_reserva = entry_id_reserva.get()
        
        conexion = obtener_conexion()  # Asegúrate de que esta función esté definida en tu código
        cursor = conexion.cursor(dictionary=True)
        consulta = """
        SELECT r.*, p.nombre AS cliente, p.correo_electronico, s.nombre AS servicio_nombre 
        FROM Reserva r 
        JOIN Persona p ON r.id_cliente = p.id_persona 
        JOIN servicio s ON r.id_servicio = s.id_servicio
        WHERE r.id_reserva = %s
        """
        cursor.execute(consulta, (id_reserva,))
        reserva = cursor.fetchone()

        if reserva:
            entry_cliente_id.delete(0, tk.END)
            entry_cliente_id.insert(0, reserva['id_cliente'])

            entry_servicio_id.delete(0, tk.END)
            entry_servicio_id.insert(0, reserva['id_servicio'])

            entry_fecha.delete(0, tk.END)
            entry_fecha.insert(0, reserva['fecha'])

            entry_hora.delete(0, tk.END)
            entry_hora.insert(0, reserva['hora'])

            entry_servicio_nombre.config(state=tk.NORMAL)  # Permitir la edición temporal para actualizar el texto
            entry_servicio_nombre.delete(0, tk.END)
            entry_servicio_nombre.insert(0, reserva['servicio_nombre'])
            entry_servicio_nombre.config(state='readonly')  # Volver a solo lectura

            global reserva_actual
            reserva_actual = reserva  # Guarda la reserva actual para referencia en la actualización
        else:
            messagebox.showerror("Error", "Reserva no encontrada.")
            conexion.close()

    def confirmar_actualizacion():
        nuevo_id_cliente = entry_cliente_id.get()
        nuevo_id_servicio = entry_servicio_id.get()
        nueva_fecha = entry_fecha.get()
        nueva_hora = entry_hora.get()

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        # Obtener el nuevo nombre del servicio basado en el ID del servicio
        cursor.execute("SELECT nombre FROM servicio WHERE id_servicio = %s", (nuevo_id_servicio,))
        nuevo_servicio_data = cursor.fetchone()
        nuevo_servicio_nombre = nuevo_servicio_data[0] if nuevo_servicio_data else reserva_actual['servicio_nombre']

        consulta_actualizacion = """
        UPDATE Reserva 
        SET id_cliente = %s, id_servicio = %s, fecha = %s, hora = %s 
        WHERE id_reserva = %s
        """
        cursor.execute(consulta_actualizacion, (nuevo_id_cliente, nuevo_id_servicio, nueva_fecha, nueva_hora, reserva_actual['id_reserva']))
        conexion.commit()

        messagebox.showinfo("Éxito", "Reserva actualizada con éxito.")

        mensaje = f"Reserva ID {reserva_actual['id_reserva']} actualizada para el cliente {reserva_actual['cliente']} con el servicio {nuevo_servicio_nombre}."
        enviar_notificacion("Reserva Actualizada", mensaje)
        registrar_notificacion(conexion, nuevo_id_cliente, mensaje)

        asunto = "Actualización de Reserva - SPA"
        cuerpo = f"Estimado {reserva_actual['cliente']},\n\nSu reserva ha sido actualizada. Los nuevos detalles son:\n\nServicio: {nuevo_servicio_nombre}\nFecha: {nueva_fecha}\nHora: {nueva_hora}.\n\nGracias por elegirnos."
        enviar_correo(reserva_actual['correo_electronico'], asunto, cuerpo)

        actualizar_reserva_window.destroy()
        cursor.close()
        conexion.close()

    def regresar():
        actualizar_reserva_window.destroy()
        menu_gestion_reservas(Empleado)

    # Configuración de la ventana para actualizar la reserva
    actualizar_reserva_window = tk.Tk()
    actualizar_reserva_window.title("Actualizar Reserva")
    actualizar_reserva_window.attributes('-fullscreen', True)  # Pantalla completa
    actualizar_reserva_window.configure(bg="#f0f0f0")

    # Etiquetas y campos de entrada con fuente grande
    tk.Label(actualizar_reserva_window, text="ID de la Reserva", font=("Helvetica", 18), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=20)
    entry_id_reserva = tk.Entry(actualizar_reserva_window, font=("Helvetica", 18))
    entry_id_reserva.grid(row=0, column=1, padx=10, pady=20)

    tk.Button(actualizar_reserva_window, text="Buscar", command=buscar_reserva, font=("Helvetica", 18)).grid(row=0, column=2, padx=10, pady=20)

    tk.Label(actualizar_reserva_window, text="Cliente ID", font=("Helvetica", 18), bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=20)
    entry_cliente_id = tk.Entry(actualizar_reserva_window, font=("Helvetica", 18))
    entry_cliente_id.grid(row=1, column=1, padx=10, pady=20)

    tk.Label(actualizar_reserva_window, text="Servicio ID", font=("Helvetica", 18), bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=20)
    entry_servicio_id = tk.Entry(actualizar_reserva_window, font=("Helvetica", 18))
    entry_servicio_id.grid(row=2, column=1, padx=10, pady=20)

    tk.Label(actualizar_reserva_window, text="Servicio Nombre", font=("Helvetica", 18), bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=20)
    entry_servicio_nombre = tk.Entry(actualizar_reserva_window, state='readonly', font=("Helvetica", 18))
    entry_servicio_nombre.grid(row=3, column=1, padx=10, pady=20)

    tk.Label(actualizar_reserva_window, text="Fecha (YYYY-MM-DD)", font=("Helvetica", 18), bg="#f0f0f0").grid(row=4, column=0, padx=10, pady=20)
    entry_fecha = tk.Entry(actualizar_reserva_window, font=("Helvetica", 18))
    entry_fecha.grid(row=4, column=1, padx=10, pady=20)

    tk.Label(actualizar_reserva_window, text="Hora (HH:MM)", font=("Helvetica", 18), bg="#f0f0f0").grid(row=5, column=0, padx=10, pady=20)
    entry_hora = tk.Entry(actualizar_reserva_window, font=("Helvetica", 18))
    entry_hora.grid(row=5, column=1, padx=10, pady=20)

    # Botón para confirmar la actualización
    tk.Button(actualizar_reserva_window, text="Actualizar", command=confirmar_actualizacion, font=("Helvetica", 18)).grid(row=6, columnspan=2, pady=20)
    tk.Button(actualizar_reserva_window, text="Regresar", command=regresar, font=("Helvetica", 18)).grid(row=7, columnspan=2, pady=20)

    actualizar_reserva_window.mainloop()

def eliminar_reserva():
    def buscar_reserva():
        id_reserva = entry_id_reserva.get()
        print(f"Buscando la reserva con ID: {id_reserva}")
        
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        consulta = """
        SELECT r.id_reserva, r.id_cliente, r.fecha, r.hora, p.nombre AS cliente, p.correo_electronico, s.nombre AS servicio_nombre
        FROM Reserva r
        JOIN Persona p ON r.id_cliente = p.id_persona
        JOIN servicio s ON r.id_servicio = s.id_servicio
        WHERE r.id_reserva = %s
        """
        cursor.execute(consulta, (id_reserva,))
        reserva = cursor.fetchone()

        if reserva:
            print(f"Reserva encontrada: {reserva}")
            # Muestra los datos en los campos correspondientes
            entry_cliente_nombre.config(state=tk.NORMAL)
            entry_cliente_nombre.delete(0, tk.END)
            entry_cliente_nombre.insert(0, reserva['cliente'])
            entry_cliente_nombre.config(state='readonly')

            entry_correo_cliente.config(state=tk.NORMAL)
            entry_correo_cliente.delete(0, tk.END)
            entry_correo_cliente.insert(0, reserva['correo_electronico'])
            entry_correo_cliente.config(state='readonly')

            entry_servicio_nombre.config(state=tk.NORMAL)
            entry_servicio_nombre.delete(0, tk.END)
            entry_servicio_nombre.insert(0, reserva['servicio_nombre'])
            entry_servicio_nombre.config(state='readonly')

            entry_fecha.config(state=tk.NORMAL)
            entry_fecha.delete(0, tk.END)
            entry_fecha.insert(0, reserva['fecha'].strftime('%Y-%m-%d'))
            entry_fecha.config(state='readonly')

            entry_hora.config(state=tk.NORMAL)
            entry_hora.delete(0, tk.END)
            entry_hora.insert(0, str(reserva['hora']))
            entry_hora.config(state='readonly')

            global reserva_actual
            reserva_actual = reserva  # Guarda la reserva actual para referencia en la eliminación
        else:
            print("Reserva no encontrada.")
            messagebox.showerror("Error", "Reserva no encontrada.")
            conexion.close()

    def confirmar_eliminacion():
        if not reserva_actual:
            messagebox.showerror("Error", "No se encontró la reserva. Por favor, búsquela antes de intentar eliminarla.")
            return

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        consulta_eliminar = "DELETE FROM Reserva WHERE id_reserva = %s"
        cursor.execute(consulta_eliminar, (reserva_actual['id_reserva'],))
        conexion.commit()

        messagebox.showinfo("Éxito", "Reserva eliminada con éxito.")
        
        nombre_servicio = reserva_actual['servicio_nombre']
        mensaje = f"Reserva ID {reserva_actual['id_reserva']} eliminada para el cliente {reserva_actual['cliente']} y servicio {nombre_servicio}."
        
        enviar_notificacion("Reserva Eliminada", mensaje)
        registrar_notificacion(conexion, reserva_actual['id_cliente'], mensaje)

        asunto = "Cancelación de Reserva - SPA"
        cuerpo = f"Estimado {reserva_actual['cliente']},\n\nLamentamos informarle que su reserva para el servicio {nombre_servicio} con ID {reserva_actual['id_reserva']} ha sido cancelada.\n\nGracias por elegirnos."
        enviar_correo(reserva_actual['correo_electronico'], asunto, cuerpo)

        eliminar_reserva_window.destroy()
        cursor.close()
        conexion.close()

    def regresar():
        eliminar_reserva_window.destroy()
        menu_gestion_reservas(Empleado)

    # Configuración de la ventana para eliminar la reserva
    eliminar_reserva_window = tk.Tk()
    eliminar_reserva_window.title("Eliminar Reserva")
    eliminar_reserva_window.attributes('-fullscreen', True)  # Pantalla completa
    eliminar_reserva_window.configure(bg="#f0f0f0")

    # Etiquetas y campos de entrada con fuente grande
    tk.Label(eliminar_reserva_window, text="ID de la Reserva", font=("Helvetica", 18), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=20)
    entry_id_reserva = tk.Entry(eliminar_reserva_window, font=("Helvetica", 18))
    entry_id_reserva.grid(row=0, column=1, padx=10, pady=20)

    tk.Button(eliminar_reserva_window, text="Buscar", command=buscar_reserva, font=("Helvetica", 18)).grid(row=0, column=2, padx=10, pady=20)

    tk.Label(eliminar_reserva_window, text="Cliente Nombre", font=("Helvetica", 18), bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=20)
    entry_cliente_nombre = tk.Entry(eliminar_reserva_window, state='readonly', font=("Helvetica", 18))
    entry_cliente_nombre.grid(row=1, column=1, padx=10, pady=20)

    tk.Label(eliminar_reserva_window, text="Correo Electrónico del Cliente", font=("Helvetica", 18), bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=20)
    entry_correo_cliente = tk.Entry(eliminar_reserva_window, state='readonly', font=("Helvetica", 18))
    entry_correo_cliente.grid(row=2, column=1, padx=10, pady=20)

    tk.Label(eliminar_reserva_window, text="Servicio Nombre", font=("Helvetica", 18), bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=20)
    entry_servicio_nombre = tk.Entry(eliminar_reserva_window, state='readonly', font=("Helvetica", 18))
    entry_servicio_nombre.grid(row=3, column=1, padx=10, pady=20)

    tk.Label(eliminar_reserva_window, text="Fecha (YYYY-MM-DD)", font=("Helvetica", 18), bg="#f0f0f0").grid(row=4, column=0, padx=10, pady=20)
    entry_fecha = tk.Entry(eliminar_reserva_window, state='readonly', font=("Helvetica", 18))
    entry_fecha.grid(row=4, column=1, padx=10, pady=20)

    tk.Label(eliminar_reserva_window, text="Hora (HH:MM:SS)", font=("Helvetica", 18), bg="#f0f0f0").grid(row=5, column=0, padx=10, pady=20)
    entry_hora = tk.Entry(eliminar_reserva_window, state='readonly', font=("Helvetica", 18))
    entry_hora.grid(row=5, column=1, padx=10, pady=20)

    # Botón para confirmar la eliminación
    tk.Button(eliminar_reserva_window, text="Eliminar", command=confirmar_eliminacion, font=("Helvetica", 18)).grid(row=6, columnspan=2, pady=20)
    tk.Button(eliminar_reserva_window, text="Regresar", command=regresar, font=("Helvetica", 18)).grid(row=7, columnspan=2, pady=20)

    eliminar_reserva_window.mainloop()

def enviar_notificacion(titulo, mensaje):
    notification.notify(
        title=titulo,
        message=mensaje,
        app_name='Sistema de Gestión SPA',
        timeout=10 
    )

def registrar_notificacion(conexion, id_cliente, mensaje):
    cursor = conexion.cursor()
    consulta = """
    INSERT INTO notificacion (id_cliente, mensaje, fecha_envio)
    VALUES (%s, %s, NOW())
    """
    cursor.execute(consulta, (id_cliente, mensaje))
    conexion.commit()
    cursor.close()

def enviar_correo(destinatario, asunto, cuerpo):
    remitente = "w4v3paradise@gmail.com"  
    password = "xyaq ljue liir ywaa"  

    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(remitente, password)
        texto = mensaje.as_string()
        servidor.sendmail(remitente, destinatario, texto)
        servidor.quit()

        print(f"Correo enviado con éxito a {destinatario}")

    except Exception as e:
        print(f"Error al enviar el correo: {e}")

if __name__ == "__main__":
    menu_inicio_sesion()
