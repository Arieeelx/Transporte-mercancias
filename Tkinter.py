import tkinter as tk
import Funciones_envio
import tkcalendar as DateEntry

ventana = tk.Tk()
ventana.title("Registro de mercancías - Transporte ASA")
ventana.minsize(445,300)
ventana.maxsize(475,400)
ventana.configure(bg="DeepSkyBlue3")
ventana.attributes("-alpha", 0.8)

#frames

frame_datos = tk.LabelFrame(ventana, text="Datos envío", pady=10, bg="SlateGray1")
frame_datos.pack(pady=10)

frame_botones = tk.LabelFrame(ventana, text="¿Qué deseas realizar?", pady=10, bg="SlateGray1")
frame_botones.pack(pady=10)

#label, entry y menu

    #frame_datos
label_origen = tk.Label(frame_datos, text="Origen: ", bg="SlateGray1")
label_origen.grid(row=0, column=0, padx=5, sticky="w")
label_destino = tk.Label(frame_datos, text="Destino: ", bg="SlateGray1")
label_destino.grid(row=1, column=0, padx=5, sticky="w")
label_calendario = tk.Label(frame_datos, text="Posible fecha despacho: ", bg="SlateGray1")
label_calendario.grid(row=2, column=0, padx=5, sticky="w")

Funciones_envio.entry_origen = tk.Entry(frame_datos)
Funciones_envio.entry_origen.grid(row=0, column=1, padx=5, sticky="e")
Funciones_envio.entry_destino = tk.Entry(frame_datos)
Funciones_envio.entry_destino.grid(row=1, column=1, padx=5, sticky="e")
DateEntry_fecha_despacho = DateEntry.DateEntry(frame_datos, width=12, background='DeepSkyBlue3', foreground='black', borderwidth=10, date_pattern='dd/mm/yyyy')
DateEntry_fecha_despacho.grid(row=2, column=1, padx=5, sticky="w")

estado_envio = ["Pago procesado", "En bodega", "En tránsito", "Entregado"]
Funciones_envio.var_estado_envio = tk.StringVar()
Funciones_envio.var_estado_envio.set(estado_envio[0])

label_estado_envio = tk.Label(frame_datos, text="Estado del pedido: ", bg="SlateGray1")
label_estado_envio.grid(row=3, column=0, padx=5, sticky="w")

menu_estado_envio = tk.OptionMenu(frame_datos, Funciones_envio.var_estado_envio, *estado_envio)
menu_estado_envio.grid(row=3, column=1, padx=5, sticky="w")

    #botones
btn_agregar_envio = tk.Button(frame_botones, text="Agregar envio", command=Funciones_envio.agregar_envio)
btn_agregar_envio.grid(row=0, column=0, padx=5, pady=5)







ventana.mainloop()
