from datetime import datetime

def obtener_fecha_cumple():
    while True:
        try:
            fecha_str = input("INGRESA TU FECHA DE CUMPLEANIOS (DD/MM/YYYY)")
            fecha_cumple = datetime.strptime(fecha_str, "%d/%m/%Y")
            return fecha_cumple
        except ValueError:
            print("FORMATO INCORRECTO")

def calcular_dias_faltantes(fecha_cumple):
    hoy = datetime.now()
    dias_faltantes = (fecha_cumple - hoy).days
    return dias_faltantes

def main():
    fecha_cumple = obtener_fecha_cumple()
    dias_faltantes = calcular_dias_faltantes(fecha_cumple)
    
    if dias_faltantes == 0:
        print("HOY ES TU CUMPLEANIOS")
    elif dias_faltantes > 0:
        print(f"FALTAN {dias_faltantes} DIAS PARA TU CUMPLEANIOS")
    else:
        print(f"TU CUMPLEANIOS YA PASO")

if __name__ == "__main__":
    main()
