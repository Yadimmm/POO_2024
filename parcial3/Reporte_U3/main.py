from reservas.reserva import Reserva, Servicio
from usuarios.usuario import Empleado, Cliente
from funciones import borrarPantalla, esperar_tecla
from conexion import obtener_conexion
from plyer import notification
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def menu_inicio_sesion():
    while True:
        borrarPantalla()
        print("....::::::Sistema Gestión WAVE PARADISE::::::....")
        print("1- Iniciar sesión como Empleado")
        print("2- Registrar nuevo Empleado")
        print("3- Registrar nuevo Cliente")
        print("4- Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            iniciar_sesion_empleado()
        elif opcion == "2":
            registrar_empleado()
        elif opcion == "3":
            Cliente.registrar_cliente() 
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")
            esperar_tecla()

def iniciar_sesion_empleado():
    borrarPantalla()
    print("....::::::Inicio de Sesión::::::....")
    id_empleado = input("Ingrese su ID de Empleado: ")
    correo_electronico = input("Ingrese su Correo Electrónico: ")
    password = input("Ingrese su Contraseña: ")

    conexion = obtener_conexion()
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
        print(f"Bienvenido {empleado.nombre} {empleado.apellidos}")
        esperar_tecla()

        menu_gestion_reservas(empleado)
    else:
        print("ID, correo electrónico o contraseña incorrectos. Inténtelo de nuevo.")
        esperar_tecla()

    cursor.close()
    conexion.close()

def registrar_empleado():
    borrarPantalla()
    print("....::::::Registrar Nuevo Empleado::::::....")
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    fecha_nacimiento = input("Fecha de Nacimiento (YYYY-MM-DD): ")
    telefono = input("Teléfono: ")
    correo_electronico = input("Correo Electrónico: ")
    password = input("Contraseña: ")
    especialidad = input("Especialidad: ")
    
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

    print(f"Empleado {nombre} {apellidos} registrado con éxito.")
    esperar_tecla()

    cursor.close()
    conexion.close()

def menu_gestion_reservas(empleado):
    while True:
        borrarPantalla()
        print(f"....::::::Bienvenido {empleado.nombre} {empleado.apellidos}::::::....")
        print("1- Crear Reserva")
        print("2- Leer Reservas")
        print("3- Actualizar Reserva")
        print("4- Eliminar Reserva")
        print("5- Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_reserva(empleado)
        elif opcion == "2":
            leer_reservas()
        elif opcion == "3":
            actualizar_reserva()
        elif opcion == "4":
            eliminar_reserva()
        elif opcion == "5":
            print("Cerrando sesión...")
            break
        else:
            print("Opción no válida, intente de nuevo.")
            esperar_tecla()

def crear_reserva(empleado):
    borrarPantalla()
    print("....::::::Crear Nueva Reserva::::::....")
    id_cliente = input("Ingrese el ID del Cliente: ")
    id_servicio = input("Ingrese el ID del Servicio: ")
    fecha = input("Ingrese la Fecha de la Reserva (YYYY-MM-DD): ")
    hora = input("Ingrese la Hora de la Reserva (HH:MM): ")

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
        print("Cliente no encontrado.")
        esperar_tecla()
        return
    
    consulta_servicio = "SELECT * FROM servicio WHERE id_servicio = %s"
    cursor.execute(consulta_servicio, (id_servicio,))
    servicio_data = cursor.fetchone()
    
    if servicio_data:
        servicio = Servicio(servicio_data[0], servicio_data[1], servicio_data[2], servicio_data[3], servicio_data[4])
        nombre_servicio = servicio.nombre  
    else:
        print("Servicio no encontrado.")
        esperar_tecla()
        return
    
    reserva = Reserva(None, cliente, empleado, servicio, fecha, hora)
    reserva.confirmar_reserva()
    
    mensaje = f"Reserva creada para el cliente {cliente.nombre} {cliente.apellidos} con el servicio {nombre_servicio}."
    
    enviar_notificacion("Reserva Creada", mensaje)
    registrar_notificacion(conexion, cliente.id_cliente, mensaje)

    asunto = "Confirmación de Reserva - SPA"
    cuerpo = f"Estimado {cliente.nombre},\n\nSu reserva para el servicio {nombre_servicio} el día {fecha} a las {hora} ha sido confirmada.\n\nGracias por elegirnos."
    enviar_correo(cliente.correo_electronico, asunto, cuerpo)
    
    esperar_tecla()

    cursor.close()
    conexion.close()

def leer_reservas():
    borrarPantalla()
    print("....::::::Consultar Reservas::::::....")
    
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
            print(f"Reserva ID: {reserva['id_reserva']}, Cliente: {reserva['cliente']}, Servicio: {reserva['servicio']}, Fecha: {reserva['fecha']}, Hora: {reserva['hora']}")
        
        mensaje = "Se han consultado las reservas existentes."
        enviar_notificacion("Consulta de Reservas", mensaje)
        registrar_notificacion(conexion, None, mensaje) 
    else:
        print("No hay reservas registradas.")
        mensaje = "No hay reservas registradas para mostrar."
        enviar_notificacion("Consulta de Reservas", mensaje)
        registrar_notificacion(conexion, None, mensaje)

    esperar_tecla()
    cursor.close()
    conexion.close()

def actualizar_reserva():
    borrarPantalla()
    print("....::::::Actualizar Reserva::::::....")
    id_reserva = input("Ingrese el ID de la Reserva a actualizar: ")
    
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    consulta = """
    SELECT r.*, p.nombre AS cliente, p.correo_electronico, s.nombre AS servicio_nombre 
    FROM Reserva r 
    JOIN Persona p ON r.id_cliente = p.id_persona 
    JOIN servicio s ON r.id_servicio = s.id_servicio
    WHERE id_reserva = %s
    """
    cursor.execute(consulta, (id_reserva,))
    reserva = cursor.fetchone()

    if reserva:
        print(f"Reserva actual: Cliente ID: {reserva['id_cliente']}, Servicio: {reserva['servicio_nombre']}, Fecha: {reserva['fecha']}, Hora: {reserva['hora']}")
        nuevo_id_cliente = input(f"Nuevo ID de Cliente ({reserva['id_cliente']}): ") or reserva['id_cliente']
        nuevo_id_servicio = input(f"Nuevo ID de Servicio ({reserva['id_servicio']}): ") or reserva['id_servicio']
        nueva_fecha = input(f"Nueva Fecha ({reserva['fecha']}): ") or reserva['fecha']
        nueva_hora = input(f"Nueva Hora ({reserva['hora']}): ") or reserva['hora']

        if nuevo_id_servicio != reserva['id_servicio']:
            cursor.execute("SELECT nombre FROM servicio WHERE id_servicio = %s", (nuevo_id_servicio,))
            nuevo_servicio_data = cursor.fetchone()
            nuevo_servicio_nombre = nuevo_servicio_data['nombre'] if nuevo_servicio_data else reserva['servicio_nombre']
        else:
            nuevo_servicio_nombre = reserva['servicio_nombre']

        consulta_actualizacion = """
        UPDATE Reserva 
        SET id_cliente = %s, id_servicio = %s, fecha = %s, hora = %s 
        WHERE id_reserva = %s
        """
        cursor.execute(consulta_actualizacion, (nuevo_id_cliente, nuevo_id_servicio, nueva_fecha, nueva_hora, id_reserva))
        conexion.commit()

        print("Reserva actualizada con éxito.")
        
        mensaje = f"Reserva ID {id_reserva} actualizada para el cliente {reserva['cliente']} con el servicio {nuevo_servicio_nombre}."
        
        enviar_notificacion("Reserva Actualizada", mensaje)
        registrar_notificacion(conexion, nuevo_id_cliente, mensaje)

        asunto = "Actualización de Reserva - SPA"
        cuerpo = f"Estimado {reserva['cliente']},\n\nSu reserva ha sido actualizada. Los nuevos detalles son:\n\nServicio: {nuevo_servicio_nombre}\nFecha: {nueva_fecha}\nHora: {nueva_hora}.\n\nGracias por elegirnos."
        enviar_correo(reserva['correo_electronico'], asunto, cuerpo)
        
    else:
        print("Reserva no encontrada.")
        mensaje = f"Intento fallido de actualizar la reserva ID {id_reserva}."
        enviar_notificacion("Error al Actualizar Reserva", mensaje)
        registrar_notificacion(conexion, None, mensaje)

    esperar_tecla()
    cursor.close()
    conexion.close()

def eliminar_reserva():
    borrarPantalla()
    print("....::::::Eliminar Reserva::::::....")
    id_reserva = input("Ingrese el ID de la Reserva a eliminar: ")
    
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    consulta = """
    SELECT r.*, p.nombre AS cliente, p.correo_electronico, s.nombre AS servicio_nombre 
    FROM Reserva r 
    JOIN Persona p ON r.id_cliente = p.id_persona 
    JOIN servicio s ON r.id_servicio = s.id_servicio
    WHERE id_reserva = %s
    """
    cursor.execute(consulta, (id_reserva,))
    reserva = cursor.fetchone()

    if reserva:
        consulta_eliminar = "DELETE FROM Reserva WHERE id_reserva = %s"
        cursor.execute(consulta_eliminar, (id_reserva,))
        conexion.commit()

        print("Reserva eliminada con éxito.")
        
        nombre_servicio = reserva['servicio_nombre']
        mensaje = f"Reserva ID {id_reserva} eliminada para el cliente {reserva['cliente']} y servicio {nombre_servicio}."
        
        enviar_notificacion("Reserva Eliminada", mensaje)
        registrar_notificacion(conexion, reserva['id_cliente'], mensaje)

        asunto = "Cancelación de Reserva - SPA"
        cuerpo = f"Estimado {reserva['cliente']},\n\nLamentamos informarle que su reserva para el servicio {nombre_servicio} con ID {id_reserva} ha sido cancelada.\n\nGracias por elegirnos."
        enviar_correo(reserva['correo_electronico'], asunto, cuerpo)
    else:
        print("Reserva no encontrada.")
        mensaje = f"Intento fallido de eliminar la reserva ID {id_reserva}."
        enviar_notificacion("Error al Eliminar Reserva", mensaje)
        registrar_notificacion(conexion, None, mensaje)

    esperar_tecla()
    cursor.close()
    conexion.close()

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