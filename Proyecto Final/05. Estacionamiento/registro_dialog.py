import tkinter as tk
from tkinter import ttk, messagebox

class RegistroDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Registrar Entrada")
        self.grab_set()
        self.result = None

        frm = ttk.Frame(self, padding=10)
        frm.pack()

        ttk.Label(frm, text="Patente:").grid(row=0, column=0, padx=5, pady=5)
        self.patente_var = tk.StringVar()
        ttk.Entry(frm, textvariable=self.patente_var).grid(row=0, column=1)

        ttk.Label(frm, text="Tipo:").grid(row=1, column=0, padx=5, pady=5)
        self.tipo_var = tk.StringVar()

        tipo_combo = ttk.Combobox(
            frm, textvariable=self.tipo_var,
            values=["Auto", "Moto", "Camioneta"],
            state="readonly"
        )
        tipo_combo.grid(row=1, column=1)
        tipo_combo.current(0)

        btns = ttk.Frame(frm)
        btns.grid(row=2, column=0, columnspan=2, pady=10)

        ttk.Button(btns, text="Aceptar", command=self.accept).pack(side="left", padx=5)
        ttk.Button(btns, text="Cancelar", command=self.cancel).pack(side="left", padx=5)

    def accept(self):
        patente = self.patente_var.get().strip()
        tipo = self.tipo_var.get().strip()

        if not patente:
            messagebox.showwarning("Error", "Ingrese la patente.")
            return

        self.result = (patente.upper(), tipo)
        self.destroy()

    def cancel(self):
        self.result = None
        self.destroy()