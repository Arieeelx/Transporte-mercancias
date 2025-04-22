import tkinter as tk
from tkinter import messagebox
import conexion_db
import tkcalendar as DateEntry

tabla = "envios"

def agregar_envio():
    origen_envio = entry_origen.get()
    destino_envio = entry_destino.get()
    fecha_despacho = fecha_despacho_widget.get()
    estado_envio = var_estado_envio.get()

    try:
        conexion = conexion_db.conectar_db()
        cursor = conexion.cursor()

        cursor.execute(f"insert into {tabla} (origen, destino, fecha_despacho, estado) values (%s, %s, %s, %s)", (origen_envio, destino_envio, fecha_despacho, estado_envio))

        conexion.commit()
        conexion.close()

        messagebox.showinfo("Envío agregado", f"Datos del envío:\n --Origen: {origen_envio}\n --Destino: {destino_envio}\n --Fecha despacho: {fecha_despacho}")

    except Exception as e:
        messagebox.showerror("Error: ", f"Ocurrió un problema -- {e}")

def mostrar_informacion():
    try:
        conexion = conexion_db.conectar_db()
        cursor = conexion.cursor()

        consulta = f"select * from {tabla}"

        cursor.execute(consulta)

        resultados = cursor.fetchall()

        mensaje = ""
        for resultado in resultados:
            mensaje += f"ID: {resultado[0]}\n| Origen: {resultado[1]}\n| Destino: {resultado[2]}\n| Fecha despacho: {resultado[3]}\n| Estado del pedido: {resultado[4]}\n\n"

        conexion.commit()
        conexion.close()

        messagebox.showinfo("Pedidos en curso", mensaje)

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un problema:\n{e}")

def eliminar_pedido():
    try:
        id_envio = entry_id_envio.get()

        conexion = conexion_db.conectar_db()
        cursor = conexion.cursor()

        eliminar = f"delete from {tabla} where id = %s"

        cursor.execute(eliminar, (id_envio,))

        conexion.commit()
        conexion.close()

        messagebox.showinfo("Pedido eliminado", "Se ha eliminado el pedido solicitado")

    except Exception as e:
        messagebox.showerror("Error", f"No se ha podido eliminar debido a: {e}")

def actualizar_informacion():
    try:
        id_envio = entry_id_envio.get()
        origen_envio = entry_origen.get()
        destino_envio = entry_destino.get()
        fecha_despacho = fecha_despacho_widget.get()
        estado_envio = var_estado_envio.get()

        if not id_envio:
            messagebox.showerror("Error", "Ingresa un ID correcto, verifica en casilla mostrar información antes de actualizar datos.")
            return

        conexion = conexion_db.conectar_db()
        cursor = conexion.cursor()

        actualizar = f"update {tabla} set origen = %s, destino = %s, fecha_despacho = %s, estado = %s where id = %s"

        cursor.execute(actualizar, (origen_envio, destino_envio, fecha_despacho, estado_envio, id_envio))

        conexion.commit()
        conexion.close()

        messagebox.showinfo("Pedido actualizado", "Se realizan los cambios correspondientes")

    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error\n{e}")

