from datetime import datetime,timedelta
def obtener_fecha_cumple():
    while True:
        try:
            fecha_str=input("ingresemos la fecha de cumpleanos (dd/mm/yyyy):")
            fecha_cumple=datetime.strptime(fecha_str,"%d/%m/%Y")
            return fecha_cumple
        except ValueError:print("Formato incorrecto")
def calcular_dais_faltantes(fecha_cumple):
    hoy=datetime.now()
    fecha_cumple_anio=fecha_cumple.replace(year=hoy.year)
    if fecha_cumple_anio<hoy:
        fecha_cumple_anio=fecha_cumple_anio.replace(year=hoy.year+1)
        dias_faltantes=(fecha_cumple_anio-hoy).days
        return dias_faltantes
def main():
    fecha_cumple=obtener_fecha_cumple()
    dias_faltantes=calcular_dais_faltantes(fecha_cumple)
    if dias_faltantes==0:
        print("HOY ES TU CUMPLEANOS")
    else:print(f"Faltan {dias_faltantes} dias para tu cumpleanos")
if __name__=="__main__":
    main()