import tkinter as tk
from tkinter import messagebox
import random

# Configuración del juego
INICIO = 1
FIN = 100

class AdivinaNumeroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Adivina el Número")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f8ff")

        # Variables del juego
        self.numero_secreto = random.randint(INICIO, FIN)
        self.intentos = 0

        # Estilos
        self.font_title = ("Arial", 18, "bold")
        self.font_text = ("Arial", 12)
        self.color_btn = "#4CAF50"
        self.color_btn_text = "white"

        # Título
        self.label_title = tk.Label(root, text="¡Adivina el número!", font=self.font_title, bg="#f0f8ff", fg="#333")
        self.label_title.pack(pady=10)

        # Instrucciones
        self.label_instr = tk.Label(root, text=f"Ingresa un número entre {INICIO} y {FIN}", font=self.font_text, bg="#f0f8ff")
        self.label_instr.pack(pady=5)

        # Entrada
        self.entry_num = tk.Entry(root, font=self.font_text, justify="center")
        self.entry_num.pack(pady=10)

        # Botón para adivinar
        self.btn_adivinar = tk.Button(root, text="Adivinar", font=self.font_text, bg=self.color_btn, fg=self.color_btn_text, command=self.verificar_intento)
        self.btn_adivinar.pack(pady=5)

        # Mensaje
        self.label_msg = tk.Label(root, text="", font=self.font_text, bg="#f0f8ff", fg="#333")
        self.label_msg.pack(pady=10)

        # Contador de intentos
        self.label_intentos = tk.Label(root, text="Intentos: 0", font=self.font_text, bg="#f0f8ff")
        self.label_intentos.pack(pady=5)

        # Botón reiniciar
        self.btn_reiniciar = tk.Button(root, text="Reiniciar", font=self.font_text, bg="#2196F3", fg="white", command=self.reiniciar_juego)
        self.btn_reiniciar.pack(pady=5)

    def animar_color(self, widget, start_color, end_color, steps=20, delay=30):
        # Animación de transición de color
        start_rgb = self.root.winfo_rgb(start_color)
        end_rgb = self.root.winfo_rgb(end_color)
        delta = [(e - s) / steps for s, e in zip(start_rgb, end_rgb)]

        def step(i):
            if i <= steps:
                new_color = "#%04x%04x%04x" % (
                    int(start_rgb[0] + delta[0] * i),
                    int(start_rgb[1] + delta[1] * i),
                    int(start_rgb[2] + delta[2] * i)
                )
                widget.config(bg=new_color)
                self.root.after(delay, lambda: step(i + 1))

        step(0)

    def verificar_intento(self):
        try:
            intento = int(self.entry_num.get())
            self.intentos += 1
            self.label_intentos.config(text=f"Intentos: {self.intentos}")

            if intento < self.numero_secreto:
                self.label_msg.config(text="Demasiado bajo.", fg="orange")
                self.animar_color(self.label_msg, "#f0f8ff", "#fffacd")
            elif intento > self.numero_secreto:
                self.label_msg.config(text="Demasiado alto.", fg="orange")
                self.animar_color(self.label_msg, "#f0f8ff", "#ffe4e1")
            else:
                messagebox.showinfo("¡Felicidades!", f"Adivinaste el número en {self.intentos} intentos.")
                self.animar_color(self.label_msg, "#f0f8ff", "#98fb98")
                self.reiniciar_juego()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número válido.")

    def reiniciar_juego(self):
        self.numero_secreto = random.randint(INICIO, FIN)
        self.intentos = 0
        self.label_intentos.config(text="Intentos: 0")
        self.label_msg.config(text="")
        self.entry_num.delete(0, tk.END)
        self.animar_color(self.root, "#f0f8ff", "#e6f7ff")

# Ejecutar la aplicación
root = tk.Tk()
app = AdivinaNumeroApp(root)
root.mainloop()