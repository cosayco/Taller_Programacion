import tkinter as tk
import pyttsx3
import threading

# Inicializar motor UNA sola vez
engine = pyttsx3.init()

# Configuración inicial
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)
voices = engine.getProperty('voices')

# Función que habla en un hilo
def hablar():
    texto = entrada.get("1.0", tk.END).strip()
    if texto:
        threading.Thread(target=decir, args=(texto,)).start()

def decir(texto):
    # Aplicar propiedades actuales
    engine.setProperty('rate', velocidad.get())
    engine.setProperty('volume', volumen.get())
    seleccion = lista_voces.curselection()
    if seleccion:
        index = seleccion[0]
        engine.setProperty('voice', voices[index].id)
    engine.say(texto)
    engine.runAndWait()
    engine.endLoop

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Programa que Habla")
ventana.geometry("500x400")

label = tk.Label(ventana, text="Escribe el texto para hablar:", font=("Arial", 12))
label.pack(pady=10)

frame_texto = tk.Frame(ventana)
frame_texto.pack(pady=5)

entrada = tk.Text(frame_texto, width=50, height=8, font=("Arial", 12))
entrada.pack(side=tk.LEFT)

scroll = tk.Scrollbar(frame_texto, command=entrada.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
entrada.config(yscrollcommand=scroll.set)

boton_hablar = tk.Button(ventana, text="Hablar", command=hablar, font=("Arial", 12), bg="lightblue")
boton_hablar.pack(pady=5)

velocidad = tk.Scale(ventana, from_=100, to=300, orient="horizontal", label="Velocidad")
velocidad.set(150)
velocidad.pack(pady=5)

volumen = tk.Scale(ventana, from_=0, to=1, resolution=0.1, orient="horizontal", label="Volumen")
volumen.set(0.9)
volumen.pack(pady=5)

label_voces = tk.Label(ventana, text="Selecciona la voz:", font=("Arial", 12))
label_voces.pack(pady=5)

lista_voces = tk.Listbox(ventana, height=4)
for i, v in enumerate(voices):
    lista_voces.insert(i, v.name)
lista_voces.pack(pady=5)

ventana.mainloop()