import tkinter as tk
from tkinter import messagebox
from modules.interface import iniciar_gui

USUARIO_VALIDO = "admin"
CLAVE_VALIDA = "1234"

def mostrar_login():
    login = tk.Tk()
    login.title("Acceso al Simulador")
    login.geometry("300x200")
    login.resizable(False, False)

    tk.Label(login, text="Usuario:", font=("Arial", 10)).pack(pady=(20, 5))
    usuario_entry = tk.Entry(login, font=("Arial", 12), justify="center")
    usuario_entry.pack()

    tk.Label(login, text="Contraseña:", font=("Arial", 10)).pack(pady=(10, 5))
    clave_entry = tk.Entry(login, font=("Arial", 12), show="*", justify="center")
    clave_entry.pack()

    def validar():
        usuario = usuario_entry.get().strip()
        clave = clave_entry.get().strip()
        if usuario == USUARIO_VALIDO and clave == CLAVE_VALIDA:
            login.destroy()
            iniciar_gui()
        else:
            messagebox.showerror("Acceso denegado", "Usuario o contraseña incorrectos")

    tk.Button(login, text="Ingresar", command=validar, bg="#2196F3", fg="white", width=15).pack(pady=15)
    login.mainloop()