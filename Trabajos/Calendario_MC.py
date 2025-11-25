#Este codigo crea un calendario de trabajo de 7x7
import tkinter as tk
import calendar
from datetime import date, timedelta
import locale

try:
    locale.setlocale(locale.LC_TIME, "es_CL.UTF-8")
except:
    locale.setlocale(locale.LC_TIME, "Spanish_Chile")

ventana = tk.Tk()
ventana.title("Calendario Turno 7x7")
ventana.geometry("420x330")

meses = [(2025,m) for m in range(1, 13)]
indice_mes = 0

inicio_turno = date(2025, 1, 1)  
Dias_trabajo = 7
Dias_descanso = 7

def es_dia_trabajo(fecha):
    dif = (fecha - inicio_turno).days
    if dif < 0:
        return False  
    ciclo = (Dias_trabajo + Dias_descanso)
    return (dif % ciclo) < Dias_trabajo

def Mostrar_calendario(year, month):
    for widget in Frame_calendario.winfo_children():
        widget.destroy()

    label_mes.config(text=f"{calendar.month_name[month]} {year}")

    dias = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
    for i, d in enumerate(dias):
        tk.Label(Frame_calendario, text=d, font=("Helvetica", 10, "bold")).grid(row=0, column=i, padx=2, pady=2)
        

    cal = calendar.Calendar(firstweekday=0)
    semanas = cal.monthdatescalendar(year, month)

    for e, semana in enumerate(semanas, start=1):
        for c, dia in enumerate(semana):
            if dia.month == month:
                if es_dia_trabajo(dia):
                    color = "lightgreen"
                else:
                    color = "lightgray"
            else:
                color = ventana.cget("bg")  

            tk.Label(Frame_calendario,text=str(dia.day),width=4,height=2,bg=color,relief="ridge").grid(row=e, column=c, padx=1, pady=1)


def cambiar_mes():
    global indice_mes
    indice_mes = (indice_mes + 1) % len(meses)
    year, month = meses[indice_mes]
    Mostrar_calendario(year, month)

label_mes = tk.Label(ventana, font=("Helvetica", 14, "bold"))
label_mes.pack(pady=5)

Frame_calendario = tk.Frame(ventana)
Frame_calendario.pack()

boton = tk.Button(ventana, text="Cambiar Mes", command=cambiar_mes)
boton.pack(pady=10)

Mostrar_calendario(*meses[indice_mes])


ventana.mainloop()
