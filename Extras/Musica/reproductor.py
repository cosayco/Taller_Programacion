import pygame
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import threading

# Inicializar el mezclador de audio
pygame.mixer.init()

# Ruta del archivo de música (coloca tu archivo .mp3 o .wav en el mismo directorio)
music_file = "musica.mp3"  # Cambia esto por el nombre de tu archivo

# Función para reproducir música
def play_music():
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()

# Crear un hilo para reproducir música sin bloquear la visualización
threading.Thread(target=play_music).start()

# Configuración del gráfico animado
fig, ax = plt.subplots()
x = np.linspace(0, 2*np.pi, 100)
line, = ax.plot(x, np.sin(x))
ax.set_ylim(-1.5, 1.5)
ax.set_title("Visualización mientras se reproduce música")

# Función de actualización para la animación
def update(frame):
    line.set_ydata(np.sin(x + frame/10.0))
    return line,

ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)
plt.show()
