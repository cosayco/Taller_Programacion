import pandas as pd
from tkinter import messagebox
from db.db import cargar_productos, guardar_productos

def agregar_producto(id_, nombre, categoria, unidad, precio):
    df = cargar_productos()
    if id_ in df["ID"].values:
        messagebox.showerror("Error", "ID ya existe")
        return
    nuevo = {"ID": id_, "Nombre": nombre, "Categoría": categoria, "Unidad": unidad, "Precio": float(precio), "Stock": 0}
    #df = df.append(nuevo, ignore_index=True)
    df = pd.concat([df, pd.DataFrame([nuevo])], ignore_index=True)
    guardar_productos(df)
    messagebox.showinfo("Éxito", "Producto agregado")