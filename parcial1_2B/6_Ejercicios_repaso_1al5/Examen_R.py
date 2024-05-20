while True:
 nombre=input("Ingresa el nombre del trabajador:")
 horas_t=float(input("Ingrese las horas trabajadas por el trabajador:"))
 dias_t=int(input("Ingrese los dias trabajados del trabajador:"))
 suel_h=float(input("Cual es el sueldo por hora del trabajador:"))

 sueldo=horas_t*dias_t*suel_h
 sueldo_m=sueldo*4

 print(f"El sueldo de {nombre} es {sueldo}")
 print(f"El sueldo de {nombre} es {sueldo_m}")

 if sueldo_m <= 10000:
    print(f"{nombre} es un obrero de tipo A")
 elif 10000 < sueldo_m <= 15000:
    print(f"{nombre} es un obrero de tipo B")
 else:
    print(f"{nombre} es un empleado sin categoria")
 salir=str(input("Desea agregar otro trabajador (Si/No):"))
 if salir == "si":
    break
