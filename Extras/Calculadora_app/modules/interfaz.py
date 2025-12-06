import tkinter as tk
from modules.logica import Memoria, calcular_expresion, calcular_porcentaje, calcular_raiz
from modules.estilos import FUENTE, COLOR_FONDO, COLOR_TEXTO, COLOR_CURSOR

class CalculadoraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Modular")
        self.memoria = Memoria()

        self.entrada = tk.Entry(root, font=FUENTE, bd=10, relief=tk.RIDGE, justify=tk.RIGHT,
                                fg=COLOR_TEXTO, bg=COLOR_FONDO, insertbackground=COLOR_CURSOR)
        self.entrada.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

        self.crear_botones()

    def click(self, valor):
        if valor == "=":
            resultado = calcular_expresion(self.entrada.get())
        elif valor == "C":
            self.entrada.delete(0, tk.END)
            return
        elif valor == "MC":
            self.memoria.limpiar()
            return
        elif valor == "MR":
            self.entrada.insert(tk.END, str(self.memoria.obtener()))
            return
        elif valor == "M+":
            resultado = calcular_expresion(self.entrada.get())
            if resultado != "Error":
                self.memoria.agregar(float(resultado))
            return
        elif valor == "M-":
            resultado = calcular_expresion(self.entrada.get())
            if resultado != "Error":
                self.memoria.restar(float(resultado))
            return
        elif valor == "%":
            resultado = calcular_porcentaje(self.entrada.get())
        elif valor == "√":
            resultado = calcular_raiz(self.entrada.get())
        else:
            self.entrada.insert(tk.END, valor)
            return

        self.entrada.delete(0, tk.END)
        self.entrada.insert(tk.END, resultado)

    def crear_botones(self):
        botones = [
            ["MC", "MR", "M+", "M-"],
            ["√", "%", "C", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "=", ""]
        ]

        for fila in botones:
            marco = tk.Frame(self.root)
            marco.pack(expand=True, fill=tk.BOTH)
            for texto in fila:
                if texto:
                    boton = tk.Button(marco, text=texto, font=FUENTE, relief=tk.GROOVE, bd=5)
                    boton.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
                    boton.config(command=lambda t=texto: self.click(t))