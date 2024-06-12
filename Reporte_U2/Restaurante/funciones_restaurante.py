def registrar_compra():
    producto = input("INTRODUCE EL NOMBRE DEL PRODUCTO: ")
    cantidad = int(input("INTRODUCE LA CANTIDAD COMPRADA: "))
    precio = float(input("INTRODUCE EL PRECIO DEL PRODUCTO: "))
    print(f"COMPRA REGISTRADA: {cantidad} X {producto} A ${precio} CADA UNO.")

def registrar_inventario():
    producto = input("INTRODUCE EL NOMBRE DEL PRODUCTO PARA INVENTARIO: ")
    cantidad = int(input("INTRODUCE LA CANTIDAD EN INVENTARIO: "))
    print(f"Inventario actualizado: {producto}, cantidad: {cantidad}.")

def mostrar_inventario():
    inventario = {'PRODUCTO1': 20, 'PRODUCTO2': 50}
    for producto, cantidad in inventario.items():
        print(f"{producto}: {cantidad}")