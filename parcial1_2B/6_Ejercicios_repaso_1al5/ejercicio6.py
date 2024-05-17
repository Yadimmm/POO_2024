#Mostrar todas las tablas del 1 al 10. Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10
for tabla in range(1,11):
    print(f"Tabla del {tabla}:")
    for multi in range(1,11):
        res=tabla*multi
        print(f"{tabla} X {multi} = {res}")
    print()
