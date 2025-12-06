from tkinter import messagebox
from db.db import cargar_productos, guardar_productos

def registrar_salida(id_, cantidad):
    df = cargar_productos()

    id_ = str(id_)
    df["ID"] = df["ID"].astype(str)

    if id_ not in df["ID"].values:
        messagebox.showerror("Error", "ID no encontrado")
        return
    stock_actual = df.loc[df["ID"] == id_, "Stock"].values[0]
    if stock_actual < int(cantidad):
        messagebox.showerror("Error", "Stock insuficiente")
        return
    df.loc[df["ID"] == id_, "Stock"] -= int(cantidad)
    guardar_productos(df)
    messagebox.showinfo("Éxito", "Salida registrada")