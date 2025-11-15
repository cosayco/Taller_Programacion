import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np
import os

# Contadores
usuario_victorias = 0
usuario_derrotas = 0
usuario_empates = 0

# Opciones
opciones = ['piedra', 'papel', 'tijera']
imagenes = {}

# Ruta de imágenes
carpeta_base = os.path.dirname(__file__)
carpeta_img = os.path.join(carpeta_base, "img")
#carpeta_img = "img"

# Funciones del juego
def obtener_eleccion_computador():
    return np.random.choice(opciones)

def determinar_ganador(usuario, computador):
    if usuario == computador:
        return "Empate"
    elif (usuario == 'piedra' and computador == 'tijera') or \
         (usuario == 'papel' and computador == 'piedra') or \
         (usuario == 'tijera' and computador == 'papel'):
        return "¡Ganaste!"
    else:
        return "Perdiste"

def jugar(eleccion_usuario):
    global usuario_victorias, usuario_derrotas, usuario_empates
    eleccion_computador = obtener_eleccion_computador()
    resultado = determinar_ganador(eleccion_usuario, eleccion_computador)

    if resultado == "¡Ganaste!":
        usuario_victorias += 1
    elif resultado == "Perdiste":
        usuario_derrotas += 1
    else:
        usuario_empates += 1

    actualizar_marcador()
    messagebox.showinfo("Resultado", f"Tú elegiste: {eleccion_usuario}\n"
                                     f"La computadora eligió: {eleccion_computador}\n\n{resultado}")

def actualizar_marcador():
    marcador_usuario.config(text=f"👤 Usuario\nGanadas: {usuario_victorias}\nPerdidas: {usuario_derrotas}\nEmpates: {usuario_empates}")
    marcador_computador.config(text=f"💻 Computadora\nGanadas: {usuario_derrotas}\nPerdidas: {usuario_victorias}\nEmpates: {usuario_empates}")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera")
ventana.resizable(False, False)

# Centrar ventana
ancho_ventana = 500
alto_ventana = 420
pantalla_ancho = ventana.winfo_screenwidth()
pantalla_alto = ventana.winfo_screenheight()
x = (pantalla_ancho // 2) - (ancho_ventana // 2)
y = (pantalla_alto // 2) - (alto_ventana // 2)
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

# Cargar imágenes desde carpeta img
for opcion in opciones:
    #ruta = os.path.join(carpeta_img, f"{opcion}.png")
    #ruta = os.path.abspath(os.path.join(carpeta_img, f"{opcion}.png"))
    ruta = os.path.join(carpeta_img, f"{opcion}.png")
    print("Cargando:", ruta)
    img = Image.open(ruta).resize((100, 100))
    imagenes[opcion] = ImageTk.PhotoImage(img)

# Etiqueta de instrucciones
etiqueta = tk.Label(ventana, text="Elige tu opción:", font=("Arial", 16))
etiqueta.pack(pady=10)

# Frame de botones con imágenes
frame_botones = tk.Frame(ventana)
frame_botones.pack()

for opcion in opciones:
    boton = tk.Button(frame_botones, image=imagenes[opcion],
                      command=lambda o=opcion: jugar(o))
    boton.pack(side=tk.LEFT, padx=10)

# Frame de marcador
frame_marcador = tk.Frame(ventana)
frame_marcador.pack(pady=20)

marcador_usuario = tk.Label(frame_marcador, text="", font=("Arial", 12), justify="left")
marcador_usuario.pack(side=tk.LEFT, padx=30)

marcador_computador = tk.Label(frame_marcador, text="", font=("Arial", 12), justify="left")
marcador_computador.pack(side=tk.RIGHT, padx=30)

actualizar_marcador()
ventana.mainloop()