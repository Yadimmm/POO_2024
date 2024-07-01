class Persona:
    def _init_(self, nombre, direccion, telefono, email):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
    
    def datos_persona(self):
        return f"Nombre: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}, Email: {self.email}"

class Cliente(Persona):
    def _init_(self, nombre, direccion, telefono, email):
        super()._init_(nombre, direccion, telefono, email)
        self.mascotas = []
        self.num_mascotas = 0
    
    def registrar_mascota(self, mascota):
        if isinstance(mascota, Animal):
            self.mascotas.append(mascota)
            self.num_mascotas += 1

    
    def registrar_cliente(self):
        return f"Cliente registrado: {self.datos_persona()}"

class Empleado(Persona):
    def _init_(self, nombre, direccion, telefono, email, especialidad, salario):
        super()._init_(nombre, direccion, telefono, email)
        self.especialidad = especialidad
        self.salario = salario
    
    def getEspecialidad(self):
        return self.especialidad
    
    def atender_cita(self):
        return f"Empleado {self.nombre} atendiendo cita"
    
    def obtener_datos(self):
        return f"{self.datos_persona()}, Especialidad: {self.especialidad}, Salario: {self.salario}"

class Veterinaria:
    def _init_(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.empleados = []
        self.clientes = []
        self.fecha_citas = []
    
    def programar_cita(self, cita):
        if isinstance(cita, Cita):
            self.fecha_citas.append(cita)

    
    def registrar_cliente(self, cliente):
        if isinstance(cliente, Cliente):
            self.clientes.append(cliente)

    
    def asignar_empleados(self, empleado):
        if isinstance(empleado, Empleado):
            self.empleados.append(empleado)

    
    def datos_veterinaria(self):
        empleados = ", ".join([empleado.nombre for empleado in self.empleados])
        clientes = ", ".join([cliente.nombre for cliente in self.clientes])
        return (f"Veterinaria: {self.nombre}\n"
                f"Dirección: {self.direccion}\n"
                f"Teléfono: {self.telefono}\n"
                f"Empleados: {empleados}\n"
                f"Clientes: {clientes}\n"
                f"Total de citas programadas: {len(self.fecha_citas)}")

class Cita:
    def _init_(self, fecha, hora, cliente_datos, empleado_datos, telefono_empleado, servicio):
        self.fecha = fecha
        self.hora = hora
        self.cliente_datos = cliente_datos
        self.empleado_datos = empleado_datos
        self.telefono_empleado = telefono_empleado
        self.servicio = servicio
    
    def agregar_cita(self):
        return (f"Cita programada para {self.fecha} a las {self.hora}\n"
                f"Cliente: {self.cliente_datos}\n"
                f"Empleado: {self.empleado_datos}, Teléfono: {self.telefono_empleado}\n"
                f"Servicio: {self.servicio}")

class Animal:
    def _init_(self, nombre, especie, edad, cliente):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.cliente = cliente
    
    def datos_cliente(self):
        return self.cliente.datos_persona()
    
    def registro_animal(self):
        return f"Animal registrado: {self.nombre}, Especie: {self.especie}, Edad: {self.edad}"

class Servicio:
    def _init_(self, nombre_servicio, descripcion, precio):
        self.nombre_servicio = nombre_servicio
        self.descripcion = descripcion
        self.precio = precio
    
    def getPrecio(self):
        return self.precio
    
    def datos_servicio(self):
        return (f"Servicio: {self.nombre_servicio}, Descripción: {self.descripcion}, Precio: {self.precio}")