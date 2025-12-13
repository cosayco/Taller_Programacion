import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

from config import CAPACIDAD_MAX
from logic import generar_ticket, calcular_total_por_minutos
from database import (
    contar_vehiculos_dentro,
    insertar_entrada,
    obtener_vehiculos_dentro,
    registrar_salida,
    obtener_historial
)

from registro_dialog import RegistroDialog

class ParkingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Control de Estacionamiento")
        self.root.geometry("920x600")
        self.user = None
        self.login_screen()

    # PANTALLA DE LOGIN
    def login_screen(self):
        for w in self.root.winfo_children():
            w.destroy()

        frm = ttk.Frame(self.root, padding=20)
        frm.pack(expand=True)

        ttk.Label(
            frm,
            text="Ingreso - Control de Estacionamiento",
            font=("Helvetica", 16)
        ).grid(row=0, column=0, columnspan=2, pady=12)

        ttk.Label(frm, text="Usuario:").grid(row=1, column=0, sticky="e")
        self.username_var = tk.StringVar()
        ttk.Entry(frm, textvariable=self.username_var).grid(row=1, column=1, pady=5)

        ttk.Label(frm, text="Contraseña:").grid(row=2, column=0, sticky="e")
        self.password_var = tk.StringVar()
        ttk.Entry(frm, textvariable=self.password_var, show="*").grid(row=2, column=1, pady=5)

        ttk.Button(frm, text="Entrar", command=self.check_login).grid(
            row=3, column=0, columnspan=2, pady=10
        )

        ttk.Label(
            frm,
            text="Usuario: Felipe | Contraseña: 2005",
            foreground="gray"
        ).grid(row=4, column=0, columnspan=2)

    def check_login(self):
        u = self.username_var.get().strip()
        p = self.password_var.get().strip()

        if u == "Felipe" and p == "2005":
            self.user = u
            self.main_screen()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    # PANTALLA PRINCIPAL
    def main_screen(self):
        for w in self.root.winfo_children():
            w.destroy()

        # Barra superior
        top = ttk.Frame(self.root, padding=10)
        top.pack(side="top", fill="x")

        ttk.Label(
            top, text=f"Usuario: {self.user}", font=("Helvetica", 12)
        ).pack(side="left")

        ttk.Button(top, text="Cerrar sesión", command=self.logout).pack(side="right")

        # Barra de botones y capacidad
        mid = ttk.Frame(self.root, padding=10)
        mid.pack(fill="x")

        self.cap_label = ttk.Label(
            mid, text=self._cap_text(), font=("Helvetica", 12)
        )
        self.cap_label.pack(side="left", padx=10)

        ttk.Button(
            mid, text="Registrar Entrada", command=self.registrar_entrada_dialog
        ).pack(side="left", padx=5)

        ttk.Button(
            mid, text="Registrar Salida", command=self.registrar_salida_dialog
        ).pack(side="left", padx=5)

        ttk.Button(
            mid, text="Ver Historial", command=self.ver_historial
        ).pack(side="left", padx=5)

        ttk.Button(
            mid, text="Refrescar", command=self.refresh
        ).pack(side="left", padx=5)

        # Tabla de vehículos dentro
        frame = ttk.Frame(self.root, padding=10)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Vehículos dentro:").pack(anchor="w")

        self.tree = ttk.Treeview(
            frame,
            columns=("ticket", "patente", "tipo", "entrada"),
            show="headings"
        )
        self.tree.heading("ticket", text="Ticket")
        self.tree.heading("patente", text="Patente")
        self.tree.heading("tipo", text="Tipo")
        self.tree.heading("entrada", text="Entrada")
        self.tree.pack(fill="both", expand=True)

        self.refresh()

    def _cap_text(self):
        dentro = contar_vehiculos_dentro()
        return f"Capacidad: {dentro}/{CAPACIDAD_MAX} ocupadas"

    def refresh(self):
        # actualizar etiqueta capacidad
        self.cap_label.config(text=self._cap_text())

        # limpiar tabla
        for i in self.tree.get_children():
            self.tree.delete(i)

        # volver a cargar
        for row in obtener_vehiculos_dentro():
            rid, ticket, patente, tipo, entrada = row
            # mostrar fecha formateada bonita
            try:
                entrada_dt = datetime.fromisoformat(entrada)
                entrada_str = entrada_dt.strftime("%Y-%m-%d %H:%M:%S")
            except Exception:
                entrada_str = entrada

            self.tree.insert(
                "", "end", iid=rid,
                values=(ticket, patente, tipo, entrada_str)
            )

    def logout(self):
        if messagebox.askyesno("Salir", "¿Desea cerrar sesión?"):
            self.login_screen()

    # REGISTRAR ENTRADA
    def registrar_entrada_dialog(self):
        if contar_vehiculos_dentro() >= CAPACIDAD_MAX:
            messagebox.showwarning("Lleno", "No hay espacio disponible.")
            return

        dlg = RegistroDialog(self.root)
        self.root.wait_window(dlg)

        if not dlg.result:
            return

        patente, tipo = dlg.result
        ticket = generar_ticket()
        entrada_dt = datetime.now().isoformat()

        insertar_entrada(ticket, patente, tipo, entrada_dt)

        messagebox.showinfo(
            "Entrada registrada",
            f"Ticket: {ticket}\nPatente: {patente}"
        )
        self.refresh()

    # REGISTRAR SALIDA
    def registrar_salida_dialog(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Error", "Seleccione un vehículo")
            return

        rid = int(sel[0])
        ticket, patente, tipo, entrada_str = self.tree.item(sel, "values")

        salida_dt = datetime.now()

        total, minutos, subtotal, aplicado_minimo = calcular_total_por_minutos(
            entrada_str, salida_dt
        )

        mensaje = (
            f"Ticket: {ticket}\n"
            f"Patente: {patente}\n"
            f"Tipo: {tipo}\n"
            f"Tiempo estacionado: {minutos} minutos\n\n"
            f"Detalle cobro:\n"
            f"  Subtotal: {subtotal}\n"
        )
        if aplicado_minimo:
            mensaje += "  (Se aplica mínimo)\n"

        mensaje += f"\nTotal a cobrar: {total}\n\n¿Confirmar salida?"

        if messagebox.askyesno("Confirmar salida", mensaje):
            registrar_salida(rid, salida_dt.isoformat(), total)
            messagebox.showinfo(
                "Salida registrada",
                f"Salida registrada. Total cobrado: {total}"
            )
            self.refresh()

    # HISTORIAL
    def ver_historial(self):
        rows = obtener_historial()

        win = tk.Toplevel(self.root)
        win.title("Historial")
        win.geometry("900x400")

        tree = ttk.Treeview(
            win,
            columns=("ticket", "patente", "tipo", "entrada", "salida", "total"),
            show="headings"
        )

        for col, txt in [
            ("ticket", "Ticket"),
            ("patente", "Patente"),
            ("tipo", "Tipo"),
            ("entrada", "Entrada"),
            ("salida", "Salida"),
            ("total", "Total")
        ]:
            tree.heading(col, text=txt)

        for r in rows:
            t_ticket, t_patente, t_tipo, t_entrada, t_salida, t_total = r

            try:
                ent_fmt = datetime.fromisoformat(t_entrada).strftime("%Y-%m-%d %H:%M:%S")
            except Exception:
                ent_fmt = t_entrada

            if t_salida:
                try:
                    sal_fmt = datetime.fromisoformat(t_salida).strftime("%Y-%m-%d %H:%M:%S")
                except Exception:
                    sal_fmt = t_salida
            else:
                sal_fmt = ""

            tree.insert(
                "", "end",
                values=(t_ticket, t_patente, t_tipo, ent_fmt, sal_fmt, t_total)
            )

        tree.pack(fill="both", expand=True)