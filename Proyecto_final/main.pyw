import tkinter as tk
from tkinter import messagebox, ttk
from reservas.reserva import Reserva, Servicio
from usuarios.usuario import Empleado, Cliente
from funciones import borrarPantalla, esperar_tecla
from conexion import obtener_conexion
from plyer import notification
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from mysql.connector import Error
from datetime import datetime

def cargar_empleados():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT p.id_persona, p.nombre, p.apellidos, p.correo_electronico FROM Persona p JOIN Empleado e ON p.id_persona = e.id_empleado")
    empleados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return empleados

def cargar_clientes():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT p.id_persona AS id_cliente, p.nombre, p.apellidos 
        FROM Persona p 
        JOIN Cliente c ON p.id_persona = c.id_cliente
    """)
    clientes = cursor.fetchall()
    cursor.close()
    conexion.close()
    return clientes

def menu_inicio_sesion():
    def iniciar_sesion():
        root.destroy()
        iniciar_sesion_empleado()

    def registrar_empleado_fn():
        root.destroy()
        registrar_empleado()

    def registrar_cliente_fn():
        root.destroy()
        Cliente.registrar_cliente()

    def salir():
        root.destroy()

    root = tk.Tk()
    root.title("Sistema Gestión WAVE PARADISE")
    root.state('zoomed') 
    root.configure(bg="#f0f0f0")

    root.option_add("*tearOff", False)
    menu_bar = tk.Menu(root)
    file_menu = tk.Menu(menu_bar)
    file_menu.add_command(label="Minimizar", command=lambda: root.iconify())
    file_menu.add_command(label="Maximizar", command=lambda: root.state('zoomed'))
    file_menu.add_command(label="Salir", command=lambda: root.destroy())
    menu_bar.add_cascade(label="Opciones", menu=file_menu)
    root.config(menu=menu_bar)

    tk.Label(root, text="....::::::  Sistema Gestión WAVE PARADISE  ::::::....", font=("Helvetica", 24), bg="#f0f0f0").pack(pady=50)

    tk.Button(root, text="Iniciar sesión como Empleado", command=iniciar_sesion, width=30, height=2, font=("Helvetica", 18)).pack(pady=20)
    tk.Button(root, text="Registrar nuevo Empleado", command=registrar_empleado_fn, width=30, height=2, font=("Helvetica", 18)).pack(pady=20)
    tk.Button(root, text="Registrar nuevo Cliente", command=registrar_cliente_fn, width=30, height=2, font=("Helvetica", 18)).pack(pady=20)
    tk.Button(root, text="Salir", command=salir, width=30, height=2, font=("Helvetica", 18)).pack(pady=20)

    root.mainloop()

def iniciar_sesion_empleado():
    def seleccionar_empleado(event):
        empleado_seleccionado = combo_empleados.get()
        if empleado_seleccionado:
            id_empleado = empleado_seleccionado.split('-')[0].strip()
            conexion = obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT correo_electronico FROM Persona WHERE id_persona = %s", (id_empleado,))
            correo = cursor.fetchone()
            if correo:
                entry_email.config(state=tk.NORMAL)
                entry_email.delete(0, tk.END)
                entry_email.insert(0, correo[0])
                entry_email.config(state='readonly')
            cursor.close()
            conexion.close()

    def verificar_credenciales():
        empleado_seleccionado = combo_empleados.get()
        if not empleado_seleccionado:
            messagebox.showwarning("Advertencia", "Debe seleccionar un empleado.")
            return
        
        id_empleado = empleado_seleccionado.split('-')[0].strip()
        password = entry_password.get()

        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        consulta = "SELECT e.id_empleado, p.nombre, p.apellidos FROM Empleado e JOIN Persona p ON e.id_empleado = p.id_persona WHERE e.id_empleado = %s AND e.password = %s"
        cursor.execute(consulta, (id_empleado, password))
        empleado = cursor.fetchone()

        if empleado:
            messagebox.showinfo("Éxito", f"Bienvenido {empleado['nombre']} {empleado['apellidos']}")
            root.destroy() 
            menu_gestion_reservas(empleado) 
        else:
            messagebox.showerror("Error", "Credenciales incorrectas.")

        cursor.close()
        conexion.close()

    def regresar():
        root.destroy()
        menu_inicio_sesion()

    root = tk.Tk()
    root.title("Inicio de Sesión - Empleado")
    root.state('zoomed')
    root.configure(bg="#f0f0f0")

    empleados = cargar_empleados()

    frame = tk.Frame(root, bg="#f0f0f0")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Seleccionar Empleado", font=("Helvetica", 18), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=20)
    combo_empleados = ttk.Combobox(frame, font=("Helvetica", 18))
    combo_empleados.grid(row=0, column=1, padx=10, pady=20)
    combo_empleados['values'] = [f"{emp[0]} - {emp[1]} {emp[2]}" for emp in empleados]
    combo_empleados.bind("<<ComboboxSelected>>", seleccionar_empleado)

    tk.Label(frame, text="Correo Electrónico", font=("Helvetica", 18), bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=20)
    entry_email = tk.Entry(frame, font=("Helvetica", 18), state='readonly')
    entry_email.grid(row=1, column=1, padx=10, pady=20)

    tk.Label(frame, text="Contraseña", font=("Helvetica", 18), bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=20)
    entry_password = tk.Entry(frame, show="*", font=("Helvetica", 18))
    entry_password.grid(row=2, column=1, padx=10, pady=20)

    tk.Button(frame, text="Iniciar Sesión", command=verificar_credenciales, font=("Helvetica", 18)).grid(row=3, columnspan=2, pady=20)
    tk.Button(frame, text="Regresar", command=regresar, font=("Helvetica", 18)).grid(row=4, columnspan=2, pady=20)

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
        registrar_empleado_window.destroy()

        cursor.close()
        conexion.close()

        menu_inicio_sesion()

    def regresar():
        registrar_empleado_window.destroy()
        menu_inicio_sesion()

    registrar_empleado_window = tk.Tk()
    registrar_empleado_window.title("Registrar Nuevo Empleado")
    registrar_empleado_window.state('zoomed')
    registrar_empleado_window.configure(bg="#f0f0f0")

    #maximizar, minimizar y cerrar
    registrar_empleado_window.option_add("*tearOff", False)
    menu_bar = tk.Menu(registrar_empleado_window)
    file_menu = tk.Menu(menu_bar)
    file_menu.add_command(label="Minimizar", command=lambda: registrar_empleado_window.iconify())
    file_menu.add_command(label="Maximizar", command=lambda: registrar_empleado_window.state('zoomed'))
    file_menu.add_command(label="Salir", command=lambda: registrar_empleado_window.destroy())
    menu_bar.add_cascade(label="Opciones", menu=file_menu)
    registrar_empleado_window.config(menu=menu_bar)

    frame = tk.Frame(registrar_empleado_window, bg="#f0f0f0")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Nombre", font=("Helvetica", 18), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=20)
    entry_nombre = tk.Entry(frame, font=("Helvetica", 18))
    entry_nombre.grid(row=0, column=1, padx=10, pady=20)

    tk.Label(frame, text="Apellidos", font=("Helvetica", 18), bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=20)
    entry_apellidos = tk.Entry(frame, font=("Helvetica", 18))
    entry_apellidos.grid(row=1, column=1, padx=10, pady=20)

    tk.Label(frame, text="Fecha de Nacimiento (YYYY-MM-DD)", font=("Helvetica", 18), bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=20)
    entry_fecha_nacimiento = tk.Entry(frame, font=("Helvetica", 18))
    entry_fecha_nacimiento.grid(row=2, column=1, padx=10, pady=20)

    tk.Label(frame, text="Teléfono", font=("Helvetica", 18), bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=20)
    entry_telefono = tk.Entry(frame, font=("Helvetica", 18))
    entry_telefono.grid(row=3, column=1, padx=10, pady=20)

    tk.Label(frame, text="Correo Electrónico", font=("Helvetica", 18), bg="#f0f0f0").grid(row=4, column=0, padx=10, pady=20)
    entry_correo_electronico = tk.Entry(frame, font=("Helvetica", 18))
    entry_correo_electronico.grid(row=4, column=1, padx=10, pady=20)

    tk.Label(frame, text="Contraseña", font=("Helvetica", 18), bg="#f0f0f0").grid(row=5, column=0, padx=10, pady=20)
    entry_password = tk.Entry(frame, show="*", font=("Helvetica", 18))
    entry_password.grid(row=5, column=1, padx=10, pady=20)

    tk.Label(frame, text="Especialidad", font=("Helvetica", 18), bg="#f0f0f0").grid(row=6, column=0, padx=10, pady=20)
    entry_especialidad = tk.Entry(frame, font=("Helvetica", 18))
    entry_especialidad.grid(row=6, column=1, padx=10, pady=20)

    tk.Button(frame, text="Registrar", command=confirmar_registro, font=("Helvetica", 18)).grid(row=7, columnspan=2, pady=20)
    tk.Button(frame, text="Regresar", command=regresar, font=("Helvetica", 18)).grid(row=8, columnspan=2, pady=20)

    registrar_empleado_window.mainloop()

def menu_gestion_reservas(empleado):
    def regresar():
        menu.destroy()
        menu_inicio_sesion()

    menu = tk.Tk()
    menu.title(f"Gestión de Reservas - Bienvenido {empleado['nombre']} {empleado['apellidos']}")
    menu.state('zoomed')
    menu.configure(bg="#f0f0f0")

    #maximizar, minimizar y cerrar
    menu.option_add("*tearOff", False)
    menu_bar = tk.Menu(menu)
    file_menu = tk.Menu(menu_bar)
    file_menu.add_command(label="Minimizar", command=lambda: menu.iconify())
    file_menu.add_command(label="Maximizar", command=lambda: menu.state('zoomed'))
    file_menu.add_command(label="Salir", command=lambda: menu.destroy())
    menu_bar.add_cascade(label="Opciones", menu=file_menu)
    menu.config(menu=menu_bar)

    tk.Button(menu, text="Crear Reserva", command=lambda: crear_reserva(empleado), width=30, height=2, font=("Helvetica", 18)).pack(pady=20)
    tk.Button(menu, text="Leer Reservas", command=lambda: leer_reservas(empleado), width=30, height=2, font=("Helvetica", 18)).pack(pady=20)
    tk.Button(menu, text="Actualizar Reserva", command=lambda: actualizar_reserva(empleado), width=30, height=2, font=("Helvetica", 18)).pack(pady=20)
    tk.Button(menu, text="Eliminar Reserva", command=lambda: eliminar_reserva(empleado), width=30, height=2, font=("Helvetica", 18)).pack(pady=20)
    tk.Button(menu, text="Salir", command=regresar, width=30, height=2, font=("Helvetica", 18)).pack(pady=20)

    menu.mainloop()

def crear_reserva(empleado):
    def confirmar_creacion():
        id_cliente = combo_clientes.get().split('-')[0].strip()
        id_servicio = combo_servicios.get().split('-')[0].strip()
        fecha = entry_fecha.get()
        hora = entry_hora.get()

        if not id_cliente or not id_servicio or not fecha or not hora:
            messagebox.showwarning("Advertencia", "Todos los campos deben ser completados.")
            return

        try:
            #fecha y hora
            datetime.strptime(fecha, "%Y-%m-%d")
            datetime.strptime(hora, "%H:%M")
        except ValueError:
            messagebox.showerror("Error", "La fecha o la hora tienen un formato incorrecto.")
            return

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
        registrar_notificacion(conexion, cliente.id_persona, mensaje)

        asunto = "Confirmación de Reserva - SPA"
        cuerpo = f"Estimado {cliente.nombre},\n\nSu reserva para el servicio {nombre_servicio} el día {fecha} a las {hora} ha sido confirmada.\n\nGracias por elegirnos."
        enviar_correo(cliente.correo_electronico, asunto, cuerpo)

        messagebox.showinfo("Éxito", "Reserva creada con éxito.")
        crear_reserva_window.destroy()

        cursor.close()
        conexion.close()

    def cargar_clientes():
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT p.id_persona, p.nombre, p.apellidos FROM Persona p JOIN Cliente c ON p.id_persona = c.id_cliente")
        clientes = cursor.fetchall()
        combo_clientes['values'] = [f"{cliente[0]} - {cliente[1]} {cliente[2]}" for cliente in clientes]
        cursor.close()
        conexion.close()

    def cargar_servicios():
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id_servicio, nombre FROM servicio")
        servicios = cursor.fetchall()
        combo_servicios['values'] = [f"{servicio[0]} - {servicio[1]}" for servicio in servicios]
        cursor.close()
        conexion.close()

    def regresar():
        crear_reserva_window.destroy()
        menu_gestion_reservas(empleado)

    crear_reserva_window = tk.Tk()
    crear_reserva_window.title("Crear Nueva Reserva")
    crear_reserva_window.state('zoomed')
    crear_reserva_window.configure(bg="#f0f0f0")

    frame = tk.Frame(crear_reserva_window, bg="#f0f0f0")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Seleccionar Cliente", font=("Helvetica", 18), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=20, sticky="e")
    combo_clientes = ttk.Combobox(frame, font=("Helvetica", 18), width=30)
    combo_clientes.grid(row=0, column=1, padx=10, pady=20)
    cargar_clientes()

    tk.Label(frame, text="Seleccionar Servicio", font=("Helvetica", 18), bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=20, sticky="e")
    combo_servicios = ttk.Combobox(frame, font=("Helvetica", 18), width=30)
    combo_servicios.grid(row=1, column=1, padx=10, pady=20)
    cargar_servicios()

    tk.Label(frame, text="Fecha (YYYY-MM-DD)", font=("Helvetica", 18), bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=20, sticky="e")
    entry_fecha = tk.Entry(frame, font=("Helvetica", 18), width=30)
    entry_fecha.grid(row=2, column=1, padx=10, pady=20)

    tk.Label(frame, text="Hora (HH:MM)", font=("Helvetica", 18), bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=20, sticky="e")
    entry_hora = tk.Entry(frame, font=("Helvetica", 18), width=30)
    entry_hora.grid(row=3, column=1, padx=10, pady=20)

    tk.Button(frame, text="Registrar", command=confirmar_creacion, font=("Helvetica", 18)).grid(row=4, columnspan=2, pady=20)
    
    tk.Button(frame, text="Regresar", command=regresar, font=("Helvetica", 18)).grid(row=5, columnspan=2, pady=20)

    crear_reserva_window.mainloop()


def leer_reservas(empleado):
    def mostrar_reservas():
        conexion = obtener_conexion()
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

    leer_reservas_window = tk.Tk()
    leer_reservas_window.title("Consultar Reservas")
    leer_reservas_window.state('zoomed')
    leer_reservas_window.configure(bg="#f0f0f0")

    texto_reservas = tk.Text(leer_reservas_window, height=20, width=80, font=("Helvetica", 18))
    texto_reservas.pack(pady=20)

    tk.Button(leer_reservas_window, text="Cerrar", command=leer_reservas_window.destroy, font=("Helvetica", 18)).pack(pady=20)

    mostrar_reservas()

    leer_reservas_window.mainloop()

def actualizar_reserva(empleado):
    def buscar_reserva():
        id_reserva = combo_reservas.get().split('-')[0].strip()

        conexion = obtener_conexion()
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

            entry_servicio_nombre.config(state=tk.NORMAL)
            entry_servicio_nombre.delete(0, tk.END)
            entry_servicio_nombre.insert(0, reserva['servicio_nombre'])
            entry_servicio_nombre.config(state='readonly')

            global reserva_actual
            reserva_actual = reserva
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

        consulta_actualizacion = """
        UPDATE Reserva 
        SET id_cliente = %s, id_servicio = %s, fecha = %s, hora = %s 
        WHERE id_reserva = %s
        """
        cursor.execute(consulta_actualizacion, (nuevo_id_cliente, nuevo_id_servicio, nueva_fecha, nueva_hora, reserva_actual['id_reserva']))
        conexion.commit()

        # Notificación y correo electrónico
        mensaje = f"Reserva actualizada: Cliente {reserva_actual['cliente']}, Servicio {reserva_actual['servicio_nombre']}, Fecha {nueva_fecha}, Hora {nueva_hora}."
        enviar_notificacion("Reserva Actualizada", mensaje)
        registrar_notificacion(conexion, reserva_actual['id_cliente'], mensaje)

        asunto = "Actualización de Reserva - SPA"
        cuerpo = f"Estimado {reserva_actual['cliente']},\n\nSu reserva para el servicio {reserva_actual['servicio_nombre']} ha sido actualizada a la fecha {nueva_fecha} a las {nueva_hora}.\n\nGracias por elegirnos."
        enviar_correo(reserva_actual['correo_electronico'], asunto, cuerpo)

        messagebox.showinfo("Éxito", "Reserva actualizada con éxito.")

        cursor.close()
        conexion.close()

    def cargar_reservas():
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT r.id_reserva, p.nombre
            FROM Reserva r
            JOIN Cliente c ON r.id_cliente = c.id_cliente
            JOIN Persona p ON c.id_cliente = p.id_persona
        """)
        reservas = cursor.fetchall()
        combo_reservas['values'] = [f"{reserva[0]} - {reserva[1]}" for reserva in reservas]
        cursor.close()
        conexion.close()

    def regresar():
        actualizar_reserva_window.destroy()
        menu_gestion_reservas(empleado)

    actualizar_reserva_window = tk.Tk()
    actualizar_reserva_window.title("Actualizar Reserva")
    actualizar_reserva_window.state('zoomed')
    actualizar_reserva_window.configure(bg="#f0f0f0")

    frame = tk.Frame(actualizar_reserva_window, bg="#f0f0f0")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Seleccionar Reserva", font=("Helvetica", 18), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=20)
    combo_reservas = ttk.Combobox(frame, font=("Helvetica", 18))
    combo_reservas.grid(row=0, column=1, padx=10, pady=20)
    cargar_reservas()

    tk.Button(frame, text="Buscar", command=buscar_reserva, font=("Helvetica", 18)).grid(row=0, column=2, padx=10, pady=20)

    tk.Label(frame, text="Cliente ID", font=("Helvetica", 18), bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=20)
    entry_cliente_id = tk.Entry(frame, font=("Helvetica", 18))
    entry_cliente_id.grid(row=1, column=1, padx=10, pady=20)

    tk.Label(frame, text="Servicio ID", font=("Helvetica", 18), bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=20)
    entry_servicio_id = tk.Entry(frame, font=("Helvetica", 18))
    entry_servicio_id.grid(row=2, column=1, padx=10, pady=20)

    tk.Label(frame, text="Servicio Nombre", font=("Helvetica", 18), bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=20)
    entry_servicio_nombre = tk.Entry(frame, state='readonly', font=("Helvetica", 18))
    entry_servicio_nombre.grid(row=3, column=1, padx=10, pady=20)

    tk.Label(frame, text="Fecha (YYYY-MM-DD)", font=("Helvetica", 18), bg="#f0f0f0").grid(row=4, column=0, padx=10, pady=20)
    entry_fecha = tk.Entry(frame, font=("Helvetica", 18))
    entry_fecha.grid(row=4, column=1, padx=10, pady=20)

    tk.Label(frame, text="Hora (HH:MM)", font=("Helvetica", 18), bg="#f0f0f0").grid(row=5, column=0, padx=10, pady=20)
    entry_hora = tk.Entry(frame, font=("Helvetica", 18))
    entry_hora.grid(row=5, column=1, padx=10, pady=20)

    tk.Button(frame, text="Actualizar", command=confirmar_actualizacion, font=("Helvetica", 18)).grid(row=6, columnspan=2, pady=20)
    tk.Button(frame, text="Regresar", command=regresar, font=("Helvetica", 18)).grid(row=7, columnspan=2, pady=20)

    actualizar_reserva_window.mainloop()

def eliminar_reserva(empleado):
    def buscar_reserva():
        id_reserva = combo_reservas.get().split('-')[0].strip()

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
            reserva_actual = reserva
        else:
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

        # Notificación y correo electrónico
        mensaje = f"Reserva eliminada: Cliente {reserva_actual['cliente']}, Servicio {reserva_actual['servicio_nombre']}, Fecha {reserva_actual['fecha']}, Hora {reserva_actual['hora']}."
        enviar_notificacion("Reserva Eliminada", mensaje)
        registrar_notificacion(conexion, reserva_actual['id_cliente'], mensaje)

        asunto = "Eliminación de Reserva - SPA"
        cuerpo = f"Estimado {reserva_actual['cliente']},\n\nLamentamos informarle que su reserva para el servicio {reserva_actual['servicio_nombre']} programada para el {reserva_actual['fecha']} a las {reserva_actual['hora']} ha sido eliminada.\n\nSi tiene alguna duda, por favor contáctenos."
        enviar_correo(reserva_actual['correo_electronico'], asunto, cuerpo)

        messagebox.showinfo("Éxito", "Reserva eliminada con éxito.")

        cursor.close()
        conexion.close()

    def cargar_reservas():
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT r.id_reserva, p.nombre
            FROM Reserva r
            JOIN Cliente c ON r.id_cliente = c.id_cliente
            JOIN Persona p ON c.id_cliente = p.id_persona
        """)
        reservas = cursor.fetchall()
        combo_reservas['values'] = [f"{reserva[0]} - {reserva[1]}" for reserva in reservas]
        cursor.close()
        conexion.close()

    def regresar():
        eliminar_reserva_window.destroy()
        menu_gestion_reservas(empleado)

    eliminar_reserva_window = tk.Tk()
    eliminar_reserva_window.title("Eliminar Reserva")
    eliminar_reserva_window.state('zoomed')
    eliminar_reserva_window.configure(bg="#f0f0f0")

    frame = tk.Frame(eliminar_reserva_window, bg="#f0f0f0")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Seleccionar Reserva", font=("Helvetica", 18), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=20)
    combo_reservas = ttk.Combobox(frame, font=("Helvetica", 18))
    combo_reservas.grid(row=0, column=1, padx=10, pady=20)
    cargar_reservas()

    tk.Button(frame, text="Buscar", command=buscar_reserva, font=("Helvetica", 18)).grid(row=0, column=2, padx=10, pady=20)

    tk.Label(frame, text="Cliente Nombre", font=("Helvetica", 18), bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=20)
    entry_cliente_nombre = tk.Entry(frame, state='readonly', font=("Helvetica", 18))
    entry_cliente_nombre.grid(row=1, column=1, padx=10, pady=20)

    tk.Label(frame, text="Correo Electrónico del Cliente", font=("Helvetica", 18), bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=20)
    entry_correo_cliente = tk.Entry(frame, state='readonly', font=("Helvetica", 18))
    entry_correo_cliente.grid(row=2, column=1, padx=10, pady=20)

    tk.Label(frame, text="Servicio Nombre", font=("Helvetica", 18), bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=20)
    entry_servicio_nombre = tk.Entry(frame, state='readonly', font=("Helvetica", 18))
    entry_servicio_nombre.grid(row=3, column=1, padx=10, pady=20)

    tk.Label(frame, text="Fecha (YYYY-MM-DD)", font=("Helvetica", 18), bg="#f0f0f0").grid(row=4, column=0, padx=10, pady=20)
    entry_fecha = tk.Entry(frame, state='readonly', font=("Helvetica", 18))
    entry_fecha.grid(row=4, column=1, padx=10, pady=20)

    tk.Label(frame, text="Hora (HH:MM:SS)", font=("Helvetica", 18), bg="#f0f0f0").grid(row=5, column=0, padx=10, pady=20)
    entry_hora = tk.Entry(frame, state='readonly', font=("Helvetica", 18))
    entry_hora.grid(row=5, column=1, padx=10, pady=20)

    tk.Button(frame, text="Eliminar", command=confirmar_eliminacion, font=("Helvetica", 18)).grid(row=6, columnspan=2, pady=20)
    tk.Button(frame, text="Regresar", command=regresar, font=("Helvetica", 18)).grid(row=7, columnspan=2, pady=20)

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