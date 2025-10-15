import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt

#Ventana Principal
principal = tk.Tk()
principal.title("Carga archivo CSV")
principal.geometry("600x600")

#Area texto
texto = tk.Text(principal, wrap="none", font=("Courier", 10))
texto.pack(expand=True, fill="both", padx=10, pady=10)

#Dataframe Global
df=pd.DataFrame()

#Funcion carga archivo
def cargar_CSV():
    global df
    ruta = filedialog.askopenfilename(
        title="Selecciona un archivo CSV",
        filetypes=[("Archivos CSV", "*.csv")]
    )
    if ruta:
        try:
            df=pd.read_csv(ruta)
            texto.delete("1.0", tk.END)
            texto.insert(tk.END, df.to_string(index=False))
            messagebox.showinfo("Éxito", f"Archivo cargado correctamente.\n{ruta}")
        except Exception as e:
            messagebox.showerror("Error", f"No se puedo cargar el archivo:\n{e}")

#Grafico de barras
def grafico_barras():
    global df
    if "Material" in df.columns:
        plt.figure(figsize=(8,5))
        plt.bar(df["Material"], df["Densidad"], color="teal")
        plt.title("Densidad de materiales")
        plt.xlabel("Material")
        plt.ylabel("Densidad (g/cm³)")
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    else:
        messagebox.showwarning("Datos insuficientes","El archivo debe tener columnas: Material")

# Grafico circular
def grafico_circular():
    global df
    if "Material" in df.columns:
        plt.figure(figsize=(6,6))
        plt.pie(df["Masa"], labels=df["Material"], autopct="%1.1f%%", startangle=90)
        plt.title("Distribucion masa por material")
        plt.tight_layout()
        plt.show()
    else:
        messagebox.showwarning("Datos insuficientes","El archivo debe tener columnas: Material")

#Grafico de lineas
def grafico_lineas():
    global df
    if "Material" in df.columns:
        plt.figure(figsize=(8,5))
        plt.plot(df["Material"], df["Masa"], marker="o", label="Masa")
        plt.plot(df["Material"], df["Volumen"], marker="s", label="Volumen")
        plt.title("Masa y Volumen por material")
        plt.xlabel("Material")
        plt.ylabel("Valor")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    else:
        messagebox.showwarning("Datos insuficientes","El archivo debe tener columnas: Material")

frame_botones = tk.Frame(principal)
frame_botones.pack(pady=5)

tk.Button(frame_botones, text="Cargar CSV", command=cargar_CSV).grid(row=0, column=0, padx=5)
tk.Button(frame_botones, text="Grafico Barras", command=grafico_barras).grid(row=0, column=1, padx=5)
tk.Button(frame_botones, text="Grafico Circular", command=grafico_circular).grid(row=0, column=2, padx=5)
tk.Button(frame_botones, text="Grafico Lines", command=grafico_lineas).grid(row=0, column=3, padx=5)

principal.mainloop()

