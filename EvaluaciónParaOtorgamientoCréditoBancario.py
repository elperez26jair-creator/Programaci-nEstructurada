
ingreso = float(input("Ingrese su ingreso mensual: "))
antiguedad = int(input("Ingrese su antigüedad laboral : "))
historial = int(input("Historial crediticio 1=Bueno, 2=Regular, 3=Malo: "))

resultado = ""
tipo = ""
if ingreso >= 12000:
    if antiguedad >= 2:
        if historial != 3:
            resultado = "Crédito aprobado"
            tipo = "Crédito normal"
        else:
            resultado = "Crédito rechazado"
            tipo = "Sin crédito"
    else:
        resultado = "Crédito rechazado"
        tipo = "Sin crédito"

elif ingreso >= 8000:
    if antiguedad >= 1:
        if historial == 2:
            resultado = "Crédito condicionado"
            tipo = "Crédito condicionado"
        else:
            resultado = "Crédito rechazado"
            tipo = "Sin crédito"
    else:
        resultado = "Crédito rechazado"
        tipo = "Sin crédito"
else:
    resultado = "Crédito rechazado"
    tipo = "Sin crédito"
if ingreso > 25000:
    tipo += " - Cliente candidato a crédito premium"
print("\nResultado:", resultado)
print("Tipo de crédito:", tipo)
