#Crear un programa que solicite la calificacion de 15 alumnos e imprimir en pantalla cuantos aproboron y cuantos no aprobaron
aprobados=0
reprobados=0

for contador in range(1,16):
    estudiante=float(input("Ingresa la calificacion del estudiante:"))
    if estudiante >=80:
        aprobados +=1
    else:
        if estudiante <80:
            reprobados+=1
print(f"El total de aprobados fue:{aprobados} alumnos")
print(f"El total de reprobados fue: {reprobados} alumnos")