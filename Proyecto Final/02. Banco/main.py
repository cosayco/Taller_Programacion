import tkinter as tk
from tkinter import messagebox, ttk
import os
import sqlite3
from datetime import datetime

# --------------------------------------
# BASE DE DATOS
# --------------------------------------
ruta_directorio = os.path.dirname(os.path.abspath(__file__))
ruta_db = os.path.join(ruta_directorio,"db", "banco_completo.db") 
conn = sqlite3.connect(ruta_db)
cursor = conn.cursor()
import os 
import tkinter as tk

# Tabla de usuarios
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT UNIQUE,
    pin TEXT,
    saldo REAL DEFAULT 0
)
""")

# Tabla de movimientos
cursor.execute("""
CREATE TABLE IF NOT EXISTS movimientos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER,
    tipo TEXT,
    monto REAL,
    destino TEXT,
    fecha TEXT,
    FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)
""")

conn.commit()

usuario_actual = None

# --------------------------------------
# FUNCIONES DEL BANCO
# --------------------------------------
def registrar_usuario():
    nombre = entry_usuario.get().strip()
    pin = entry_pin.get().strip()
    if not nombre or not pin:
        messagebox.showwarning("Error", "Debes ingresar un usuario y un PIN")
        return
    try:
        cursor.execute("INSERT INTO usuarios (nombre, pin, saldo) VALUES (?, ?, 0)", (nombre, pin))
        conn.commit()
        messagebox.showinfo("Éxito", f"Cuenta creada correctamente para {nombre}")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "El usuario ya existe")

def iniciar_sesion():
    global usuario_actual
    nombre = entry_usuario.get().strip()
    pin = entry_pin.get().strip()
    cursor.execute("SELECT * FROM usuarios WHERE nombre=? AND pin=?", (nombre, pin))
    user = cursor.fetchone()
    if user:
        usuario_actual = user
        mostrar_menu_principal()
    else:
        messagebox.showerror("Error", "Usuario o PIN incorrecto")

def consultar_saldo():
    cursor.execute("SELECT saldo FROM usuarios WHERE id=?", (usuario_actual[0],))
    saldo = cursor.fetchone()[0]
    messagebox.showinfo("Saldo actual", f"Tu saldo es: ${saldo:.2f}")

def registrar_movimiento(tipo, monto, destino=""):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO movimientos (usuario_id, tipo, monto, destino, fecha) VALUES (?, ?, ?, ?, ?)",
                   (usuario_actual[0], tipo, monto, destino, fecha))
    conn.commit()

def depositar():
    try:
        monto = float(entry_monto.get())
        if monto <= 0:
            raise ValueError
        cursor.execute("UPDATE usuarios SET saldo = saldo + ? WHERE id=?", (monto, usuario_actual[0]))
        conn.commit()
        registrar_movimiento("Depósito", monto)
        messagebox.showinfo("Depósito", f"Has depositado ${monto:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Monto inválido")

def retirar():
    try:
        monto = float(entry_monto.get())
        cursor.execute("SELECT saldo FROM usuarios WHERE id=?", (usuario_actual[0],))
        saldo = cursor.fetchone()[0]
        if monto <= 0 or monto > saldo:
            raise ValueError
        cursor.execute("UPDATE usuarios SET saldo = saldo - ? WHERE id=?", (monto, usuario_actual[0]))
        conn.commit()
        registrar_movimiento("Retiro", -monto)
        messagebox.showinfo("Retiro", f"Has retirado ${monto:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Monto inválido o saldo insuficiente")

def transferir():
    destino = entry_destino.get().strip()
    try:
        monto = float(entry_transferir.get())
    except ValueError:
        messagebox.showerror("Error", "Monto inválido")
        return
    
    if not destino or monto <= 0:
        messagebox.showerror("Error", "Debes ingresar un usuario y un monto válido")
        return

    cursor.execute("SELECT id, saldo FROM usuarios WHERE nombre=?", (destino,))
    receptor = cursor.fetchone()
    if not receptor:
        messagebox.showerror("Error", "El usuario destino no existe")
        return

    cursor.execute("SELECT saldo FROM usuarios WHERE id=?", (usuario_actual[0],))
    saldo_origen = cursor.fetchone()[0]
    if monto > saldo_origen:
        messagebox.showerror("Error", "Saldo insuficiente")
        return

    cursor.execute("UPDATE usuarios SET saldo = saldo - ? WHERE id=?", (monto, usuario_actual[0]))
    cursor.execute("UPDATE usuarios SET saldo = saldo + ? WHERE id=?", (monto, receptor[0]))
    conn.commit()

    registrar_movimiento("Transferencia enviada", -monto, destino)
    # Registrar también en el destinatario
    cursor.execute("INSERT INTO movimientos (usuario_id, tipo, monto, destino, fecha) VALUES (?, ?, ?, ?, ?)",
                   (receptor[0], "Transferencia recibida", monto, usuario_actual[1], datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()

    messagebox.showinfo("Transferencia", f"Transferencia de ${monto:.2f} a {destino} completada")

def ver_historial():
    ventana = tk.Toplevel(root)
    ventana.title("Historial de movimientos")
    ventana.geometry("600x300")
    ventana.rowconfigure(0, weight=1)
    ventana.columnconfigure(0, weight=1)

    tree = ttk.Treeview(ventana, columns=("tipo", "monto", "destino", "fecha"), show="headings")
    tree.grid(row=0, column=0, sticky="nsew")

    for col in ("tipo","monto","destino","fecha"):
        tree.heading(col, text=col.capitalize())
        tree.column(col, anchor="center")

    cursor.execute("SELECT tipo, monto, destino, fecha FROM movimientos WHERE usuario_id=? ORDER BY id DESC", (usuario_actual[0],))
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

    for col in tree["columns"]:
        max_len = max([len(str(tree.set(item, col))) for item in tree.get_children()] + [len(col)])
        tree.column(col, width=max_len * 10)

def cerrar_sesion():
    global usuario_actual
    usuario_actual = None
    frame_menu.pack_forget()
    frame_login.pack(pady=20)

# --------------------------------------
# INTERFAZ (Tkinter)
# --------------------------------------
root = tk.Tk()
root.title("Banco Nacional con Transferencias e Historial")
root.resizable(False, False)
ancho = 500
alto = 700 
x = (root.winfo_screenwidth() // 2) - (ancho // 2)
y = (root.winfo_screenheight() // 2) - (alto // 2)
root.geometry(f"{ancho}x{alto}+{x}+{y}")

ruta_logo = os.path.join(ruta_directorio, "logo", "OIP2.png")
imagen = tk.PhotoImage(file=ruta_logo)
label = tk.Label(root, image=imagen)
label.pack()

tk.Label(root, text="🦆 Banco estado", font=("Arial", 20, "bold"), fg="#fab700").pack(pady=10)

# LOGIN
frame_login = tk.Frame(root)
frame_login.pack(pady=20)

tk.Label(frame_login, text="Usuario:").pack()
entry_usuario = tk.Entry(frame_login)
entry_usuario.pack()

tk.Label(frame_login, text="PIN:").pack()
entry_pin = tk.Entry(frame_login, show="*")
entry_pin.pack()

tk.Button(frame_login, text="Iniciar sesión", command=iniciar_sesion, bg="#0044aa", fg="white").pack(pady=5)
tk.Button(frame_login, text="Registrar", command=registrar_usuario, bg="#0077cc", fg="white").pack(pady=5)

# MENÚ PRINCIPAL
frame_menu = tk.Frame(root)

def mostrar_menu_principal():
    frame_login.pack_forget()
    frame_menu.pack(pady=10)

    for widget in frame_menu.winfo_children():
        widget.destroy()

    tk.Label(frame_menu, text=f"Bienvenido, {usuario_actual[1]}", font=("Arial", 12, "bold")).pack(pady=10)

    tk.Button(frame_menu, text="Consultar saldo", command=consultar_saldo, bg="#0044aa", fg="white").pack(pady=5)

    tk.Label(frame_menu, text="Monto:").pack()
    global entry_monto
    entry_monto = tk.Entry(frame_menu)
    entry_monto.pack()

    tk.Button(frame_menu, text="Depositar", command=depositar, bg="#0077cc", fg="white").pack(pady=5)
    tk.Button(frame_menu, text="Retirar", command=retirar, bg="#00aaee", fg="white").pack(pady=5)

    tk.Label(frame_menu, text="Transferir a usuario:").pack(pady=5)
    global entry_destino, entry_transferir
    entry_destino = tk.Entry(frame_menu)
    entry_destino.pack()
    tk.Label(frame_menu, text="Monto:").pack()
    entry_transferir = tk.Entry(frame_menu)
    entry_transferir.pack()

    tk.Button(frame_menu, text="Transferir", command=transferir, bg="#009933", fg="white").pack(pady=5)
    tk.Button(frame_menu, text="Ver historial", command=ver_historial, bg="#ffaa00", fg="black").pack(pady=5)
    tk.Button(frame_menu, text="Cerrar sesión", command=cerrar_sesion, bg="#cccccc").pack(pady=10)

root.mainloop()
