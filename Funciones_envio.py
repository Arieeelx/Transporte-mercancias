import tkinter as tk
from tkinter import messagebox
import conexion_db
import tkcalendar as DateEntry

tabla = "envios"

def agregar_envio():
    origen_envio = entry_origen.get()
    destino_envio = entry_destino.get()
    fecha_despacho = DateEntry.fecha_despacho.get()
    estado_envio = var_estado_envio.get()

    try:
        conexion = conexion_db.conectar_db()
        cursor = conexion.cursor()

        cursor.execute(f"insert into {tabla} (origen, destino, fecha_despacho, estado) values (%s, %s, %s, %s)", (origen_envio, destino_envio, fecha_despacho, estado_envio))

        conexion.commit()
        conexion.close()

        messagebox.showinfo("Envío agregado", f"Datos del envío\n: --Origen: {origen_envio}\n --Destino: {destino_envio}\n --Fecha despacho: {fecha_despacho}")

    except Exception as e:
        messagebox.showerror("Error: ", f"Ocurrió un problema -- {e}")

#def mostrar_informacion():
#def actualizar_informacion():
#def eliminar_registro():