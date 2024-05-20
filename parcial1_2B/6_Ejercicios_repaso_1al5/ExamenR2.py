cal_imc=0
while True:
    peso=float(input("Ingresa el peso en KG:"))
    altura=float(input("Ingresa la alturs en CM:"))

    imc=peso/altura*2

    if imc < 18.5:
        composicion = "Peso inferior al normal"
    elif 18.5 <= imc <= 24.9:
        composicion = "Normal"
    elif 25.0 <= imc <= 29.9:
        composicion = "Peso superior al normal"
    else:
        composicion = "Obesidad"
        
    pregunta = input("¿Quiere calcular otro IMC? (si/no): ")

    if pregunta == "si":
        print("Tu IMC es:", imc)
        print("Composición corporal:", composicion)
        cal_imc +=1
    else:
        print("Tu IMC es:",imc)
        print("Composición corporal:", composicion)
        break

print("Se realizaron", cal_imc, "cálculos de IMC.")