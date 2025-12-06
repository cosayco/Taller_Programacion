import tkinter as tk
from tkinter import messagebox

USUARIO_VALIDO = "admin"
CLAVE_VALIDA = "1234"

def mostrar_login(callback_exito):
    login = tk.Tk()
    login.title("Login")
    login.geometry("300x200")

    tk.Label(login, text="Usuario:").pack(pady=5)
    entrada_usuario = tk.Entry(login)
    entrada_usuario.pack()

    tk.Label(login, text="Contraseña:").pack(pady=5)
    entrada_clave = tk.Entry(login, show="*")
    entrada_clave.pack()

    def validar():
        usuario = entrada_usuario.get()
        clave = entrada_clave.get()
        if usuario == USUARIO_VALIDO and clave == CLAVE_VALIDA:
            login.destroy()
            callback_exito()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    tk.Button(login, text="Ingresar", command=validar).pack(pady=20)
    login.mainloop()