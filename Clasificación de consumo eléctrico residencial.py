import tkinter as tk
from tkinter import simpledialog, messagebox
root = tk.Tk()
root.withdraw()
consumo = simpledialog.askfloat(
    "Consumo",
    "Ingrese el consumo mensual en kWh:"
)

tarifa = simpledialog.askinteger(
    "Tipo de tarifa",
    "Seleccione el tipo de tarifa:\n"
    "1 = Básica\n"
    "2 = Intermedia\n"
    "3 = Alta"
)

costo_kwh = 0
recargo = 0
tipo_tarifa = ""
if consumo is None or tarifa is None:
    messagebox.showerror("Error", "Datos incompletos")
    exit()
if tarifa == 1:
    tipo_tarifa = "Básica"
    costo_kwh = 0.85
    if consumo > 250:
        recargo = 0.12
elif tarifa == 2:
    tipo_tarifa = "Intermedia"
    costo_kwh = 1.25
    if 300 <= consumo <= 500:
        recargo = 0.10
    elif consumo > 500:
        recargo = 0.18
elif tarifa == 3:
    tipo_tarifa = "Alta"
    costo_kwh = 2.10
    if consumo > 400:
        recargo = 0.25

else:
    messagebox.showerror("Error", "Tarifa no válida")
    exit()
subtotal = consumo * costo_kwh
total = subtotal + (subtotal * recargo)

mensajes = ""
if total > 1500:
    mensajes += "⚠Consumo elevado: se recomienda ahorro de energía\n"

if consumo < 100:
    mensajes += " Usuario con consumo eficiente\n"
messagebox.showinfo(
    "Recibo de Energía Eléctrica",
    f"RECIBO DE LUZ\n\n"
    f"Tipo de tarifa: {tipo_tarifa}\n"
    f"Consumo registrado: {consumo} kWh\n"
    f"Costo por kWh: ${costo_kwh}\n"
    f"Recargo aplicado: {recargo * 100}%\n"
    f"Total a pagar: ${total:.2f}\n\n"
    f"{mensajes}"
)






