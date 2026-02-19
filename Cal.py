p1 = float(input("Calificación del primer parcial: "))
p2 = float(input("Calificación del segundo parcial: "))
proyecto = float(input("Calificación del proyecto final: "))
promedio = (p1 + p2 + proyecto) / 3
if promedio >= 70 and proyecto >= 60:
    estatus = "Aprobado"
elif promedio >= 50 and promedio <= 69:
    estatus = "Extraordinario"
else:
    estatus = "Reprobado"
print("Promedio final:", promedio)
print("Estatus académico:", estatus)
if promedio >= 95:
    print("Alumno con excelencia académica")
