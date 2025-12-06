import tkinter as tk
from login import mostrar_login
from modules.interfaz import CalculadoraApp

def iniciar_calculadora():
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.geometry("400x600")
    root.mainloop()

if __name__ == "__main__":
    mostrar_login(iniciar_calculadora)