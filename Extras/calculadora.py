import tkinter as tk
import math

class CalculadoraAvanzada:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Avanzada con Memoria")
        self.memoria = 0

        self.entrada = tk.Entry(root, font="Arial 20", bd=10, relief=tk.RIDGE, justify=tk.RIGHT, fg="lime", bg="black", insertbackground="lime")
        self.entrada.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

        self.crear_botones()

    def click(self, valor):
        if valor == "=":
            try:
                resultado = eval(self.entrada.get())
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, resultado)
            except:
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, "Error")
        elif valor == "C":
            self.entrada.delete(0, tk.END)
        elif valor == "MC":
            self.memoria = 0
        elif valor == "MR":
            self.entrada.insert(tk.END, str(self.memoria))
        elif valor == "M+":
            try:
                self.memoria += float(eval(self.entrada.get()))
            except:
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, "Error")
        elif valor == "M-":
            try:
                self.memoria -= float(eval(self.entrada.get()))
            except:
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, "Error")
        elif valor == "%":
            try:
                resultado = float(eval(self.entrada.get())) / 100
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, resultado)
            except:
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, "Error")
        elif valor == "√":
            try:
                resultado = math.sqrt(float(eval(self.entrada.get())))
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, resultado)
            except:
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, "Error")
        else:
            self.entrada.insert(tk.END, valor)

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
                    boton = tk.Button(marco, text=texto, font="Arial 18", relief=tk.GROOVE, bd=5)
                    boton.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
                    boton.config(command=lambda t=texto: self.click(t))

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraAvanzada(root)
    root.mainloop()