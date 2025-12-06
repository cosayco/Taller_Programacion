import tkinter as tk
from tkinter import ttk, messagebox

def mostrar_login(callback_aceptado):
    login_win = tk.Tk()
    login_win.title("Login de Inventario")

    # Tamaño de la ventana
    ancho = 250
    alto = 100

    # Obtener dimensiones de la pantalla
    pantalla_ancho = login_win.winfo_screenwidth()
    pantalla_alto = login_win.winfo_screenheight()

    # Calcular posición centrada
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)

    login_win.geometry(f"{ancho}x{alto}+{x}+{y}")
    login_win.resizable(False, False)

    # Widgets
    ttk.Label(login_win, text="Usuario:").grid(row=0, column=0, padx=10, pady=5)
    ttk.Label(login_win, text="Contraseña:").grid(row=1, column=0, padx=10, pady=5)

    usuario_entry = ttk.Entry(login_win)
    password_entry = ttk.Entry(login_win, show="*")
    usuario_entry.grid(row=0, column=1, padx=10, pady=5)
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    def validar():
        usuario = usuario_entry.get()
        password = password_entry.get()
        if usuario == "admin" and password == "1234":
            login_win.destroy()
            callback_aceptado()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    ttk.Button(login_win, text="Ingresar", command=validar).grid(row=2, column=0, columnspan=2, pady=10)

    login_win.mainloop()