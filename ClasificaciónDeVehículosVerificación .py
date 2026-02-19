import tkinter as tk
from tkinter import simpledialog, messagebox
root = tk.Tk()
root.withdraw()
año = int(simpledialog.askstring("Entrada", "Ingrese el año del vehículo:"))
tipo = int(simpledialog.askstring(
    "Entrada",
    "Tipo de vehículo:\n"
    "1 = Particular\n"
    "2 = Carga\n"
    "3 = Público"))
emisiones = float(simpledialog.askstring(
    "Entrada",
    "Ingrese el nivel de emisiones contaminantes:"))
if tipo == 1 and emisiones <= 50:
    resultado = "Verificación aprobada"
elif tipo == 2 and emisiones <= 70:
    resultado = "Verificación aprobada"
elif tipo == 3 and emisiones <= 60:
    resultado = "Verificación aprobada"
else:
    resultado = "Verificación rechazada"

messagebox.showinfo("Resultado", resultado)


if año< 2005:
    messagebox.showwarning(
        "Advertencia Carro viejo ",
        "Vehículo antiguo, requiere revisión especial rquiere motor nuevo" )
