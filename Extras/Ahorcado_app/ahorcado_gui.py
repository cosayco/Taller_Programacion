import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

# Palabras del juego
palabras = ['python', 'numpy', 'ahorcado', 'programa', 'matriz', 'vector', 'funcion', 'variable', 'bucle', 'condicional']

# Configuración inicial
total_intentos = 6

class AhorcadoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego del Ahorcado")
        self.root.geometry("600x500")
        
        # Variables del juego
        self.palabra = random.choice(palabras)
        self.letras_adivinadas = set()
        self.intentos = total_intentos
        
        # Cargar imágenes del ahorcado
        self.imagenes = [ImageTk.PhotoImage(Image.new('RGB', (200, 200), (255, 255, 255))) for _ in range(total_intentos+1)]
        # Nota: Aquí deberías cargar imágenes reales desde archivos PNG (ahorcado0.png, ahorcado1.png, etc.)
        # Ejemplo: ImageTk.PhotoImage(Image.open(f"ahorcado{i}.png"))
        self.imagenes = [ImageTk.PhotoImage(Image.open(f"img/ahorcado{i}.png")) for i in range(total_intentos+1)]

        # Widgets
        self.label_imagen = tk.Label(root, image=self.imagenes[0])
        self.label_imagen.pack(pady=10)
        
        self.label_tablero = tk.Label(root, text=self.obtener_tablero(), font=("Arial", 24))
        self.label_tablero.pack(pady=10)
        
        self.label_intentos = tk.Label(root, text=f"Intentos restantes: {self.intentos}", font=("Arial", 14))
        self.label_intentos.pack(pady=10)
        
        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack()
        
        self.crear_botones_letras()
        
        self.boton_reiniciar = tk.Button(root, text="Reiniciar", command=self.reiniciar_juego)
        self.boton_reiniciar.pack(pady=10)
    
    def crear_botones_letras(self):
        letras = 'abcdefghijklmnopqrstuvwxyz'
        for i, letra in enumerate(letras):
            boton = tk.Button(self.frame_botones, text=letra, width=4, command=lambda l=letra: self.adivinar_letra(l))
            boton.grid(row=i//9, column=i%9)
    
    def obtener_tablero(self):
        return ' '.join([l if l in self.letras_adivinadas else '_' for l in self.palabra])
    
    def adivinar_letra(self, letra):
        if letra in self.letras_adivinadas:
            return
        self.letras_adivinadas.add(letra)
        
        if letra not in self.palabra:
            self.intentos -= 1
            self.label_imagen.config(image=self.imagenes[total_intentos - self.intentos])
        
        self.label_tablero.config(text=self.obtener_tablero())
        self.label_intentos.config(text=f"Intentos restantes: {self.intentos}")
        
        if all(l in self.letras_adivinadas for l in self.palabra):
            messagebox.showinfo("¡Ganaste!", f"Has adivinado la palabra: {self.palabra}")
            self.deshabilitar_botones()
        elif self.intentos == 0:
            messagebox.showinfo("¡Perdiste!", f"La palabra era: {self.palabra}")
            self.deshabilitar_botones()
    
    def deshabilitar_botones(self):
        for boton in self.frame_botones.winfo_children():
            boton.config(state=tk.DISABLED)
    
    def reiniciar_juego(self):
        self.palabra = random.choice(palabras)
        self.letras_adivinadas.clear()
        self.intentos = total_intentos
        self.label_tablero.config(text=self.obtener_tablero())
        self.label_intentos.config(text=f"Intentos restantes: {self.intentos}")
        self.label_imagen.config(image=self.imagenes[0])
        for boton in self.frame_botones.winfo_children():
            boton.config(state=tk.NORMAL)

# Crear ventana principal
root = tk.Tk()
juego = AhorcadoGUI(root)
root.mainloop()