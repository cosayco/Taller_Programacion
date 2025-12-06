from tkinter import messagebox
from db.db import cargar_productos, guardar_productos

def registrar_ingreso(id_, cantidad):
    df = cargar_productos()

    id_ = str(id_)
    df["ID"] = df["ID"].astype(str)

    if id_ not in df["ID"].values:
        messagebox.showerror("Error", "ID no encontrado")
        return
    
    df.loc[df["ID"] == id_, "Stock"] += int(cantidad)
    guardar_productos(df)
    messagebox.showinfo("Éxito", f"Ingreso registrado para ID: {id_}")