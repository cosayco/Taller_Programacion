import tkinter as tk
import pyttsx3

# Inicializar el motor de voz
engine = pyttsx3.init()

def hablar():
    texto = entrada.get()
    if texto.strip():
        engine.say(texto)
        engine.runAndWait()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Programa que Habla")
ventana.geometry("400x200")

# Etiqueta
label = tk.Label(ventana, text="Escribe el texto para hablar:", font=("Arial", 12))
label.pack(pady=10)

# Campo de texto
entrada = tk.Entry(ventana, width=40, font=("Arial", 12))
entrada.pack(pady=5)

# Botón para hablar
boton = tk.Button(ventana, text="Hablar", command=hablar, font=("Arial", 12), bg="lightblue")
boton.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()