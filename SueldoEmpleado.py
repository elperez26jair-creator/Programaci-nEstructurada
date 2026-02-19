nombre = input("Ingrese el nombre del empleado: ")
horastrabajadas = float(input("Ingrese las horas trabajadas: "))
cuotaporhora = float(input("Ingrese la cuota por hora: "))
horas_extras = 0
sueldo = 0
if horastrabajadas > 40:
    horasnormales = 40
    horasextras = horastrabajadas - 40
    sueldo = (horasnormales * cuotaporhora) + (horasextras * cuotaporhora * 2)
else:
    sueldo = horastrabajadas * cuotaporhora
    print("\n--- Resumen de Nómina ---")
print(f"Nombre del empleado: {nombre}")
print(f"Horas trabajadas: {horastrabajadas}")
print(f"Horas extras: {horasextras}")
print(f"Sueldo total: {sueldo: 2f}")