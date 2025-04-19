import tkinter as tk
import Funciones_envio
import tkcalendar as DateEntry

ventana = tk.Tk()
ventana.title("Registro de mercancías - Transporte ASA")
ventana.minsize(400,200)
ventana.maxsize(445,400)
ventana.configure(bg="DeepSkyBlue3")
ventana.attributes("-alpha", 0.9)

#frames

frame_datos = tk.LabelFrame(ventana, text="Datos envío", pady=10, bg="SlateGray1")
frame_datos.pack(pady=10)

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

#label, entry y menu

    #frame_datos
label_origen = tk.Label(frame_datos, text="Origen: ", bg="SlateGray1")
label_origen.grid(row=0, column=0, padx=5, sticky="w")
label_destino = tk.Label(frame_datos, text="Destino: ", bg="SlateGray1")
label_destino.grid(row=1, column=0, padx=5, sticky="w")
label_calendario = tk.Label(frame_datos, text="Fecha: ", bg="SlateGray1")
label_calendario.grid(row=2, column=0, padx=5, sticky="w")

Funciones_envio.entry_origen = tk.Entry(frame_datos)
Funciones_envio.entry_origen.grid(row=0, column=1, padx=5, sticky="e")
Funciones_envio.entry_destino = tk.Entry(frame_datos)
Funciones_envio.entry_destino.grid(row=1, column=1, padx=5, sticky="e")
DateEntry_fecha = DateEntry.DateEntry(frame_datos, width=12, background='DeepSkyBlue3', foreground='black', borderwidth=10, date_pattern='dd-mm-yyyy')
DateEntry_fecha.grid(row=2, column=1, padx=5, sticky="w")








ventana.mainloop()
