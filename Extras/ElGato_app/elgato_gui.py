import tkinter as tk
from tkinter import messagebox
import numpy as np
import random

def crear_tablero():
    return np.full((3, 3), ' ')

def movimiento_valido(tablero, fila, columna):
    return tablero[fila, columna] == ' '

def realizar_movimiento(tablero, fila, columna, jugador):
    if movimiento_valido(tablero, fila, columna):
        tablero[fila, columna] = jugador
        return True
    return False

def verificar_ganador(tablero, jugador):
    for i in range(3):
        if np.all(tablero[i, :] == jugador) or np.all(tablero[:, i] == jugador):
            return True
    if np.all(np.diag(tablero) == jugador) or np.all(np.diag(np.fliplr(tablero)) == jugador):
        return True
    return False

def tablero_lleno(tablero):
    return not np.any(tablero == ' ')

# IA niveles
def movimiento_pc_facil(tablero):
    posiciones_libres = [(i, j) for i in range(3) for j in range(3) if tablero[i, j] == ' ']
    return random.choice(posiciones_libres) if posiciones_libres else None

def movimiento_pc_medio(tablero):
    # Bloquea jugadas del jugador X si está a punto de ganar
    for jugador in ['O', 'X']:
        for i in range(3):
            for j in range(3):
                if tablero[i, j] == ' ':
                    tablero[i, j] = jugador
                    if verificar_ganador(tablero, jugador):
                        tablero[i, j] = ' '
                        return (i, j)
                    tablero[i, j] = ' '
    return movimiento_pc_facil(tablero)

def movimiento_pc_dificil(tablero):
    # Estrategia simple: intenta ganar, luego bloquear, si no elige centro o esquinas
    for jugador in ['O', 'X']:
        for i in range(3):
            for j in range(3):
                if tablero[i, j] == ' ':
                    tablero[i, j] = jugador
                    if verificar_ganador(tablero, jugador):
                        tablero[i, j] = ' '
                        return (i, j)
                    tablero[i, j] = ' '
    if tablero[1, 1] == ' ':
        return (1, 1)
    for pos in [(0,0),(0,2),(2,0),(2,2)]:
        if tablero[pos] == ' ':
            return pos
    return movimiento_pc_facil(tablero)

# Pantalla inicial
class PantallaInicio:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego del Gato")
        self.root.configure(bg="#2c3e50")

        tk.Label(root, text="Selecciona el modo de juego", font=('Helvetica', 20, 'bold'), fg="white", bg="#2c3e50").pack(pady=20)

        tk.Button(root, text="Jugar contra otra persona", font=('Arial', 16), bg="#27ae60", fg="white", width=25,
                  command=lambda: self.iniciar_juego(False, None)).pack(pady=10)

        tk.Label(root, text="O elige dificultad contra PC", font=('Arial', 16), fg="white", bg="#2c3e50").pack(pady=10)

        tk.Button(root, text="Fácil", font=('Arial', 16), bg="#2980b9", fg="white", width=25,
                  command=lambda: self.iniciar_juego(True, 'facil')).pack(pady=5)
        tk.Button(root, text="Medio", font=('Arial', 16), bg="#f39c12", fg="white", width=25,
                  command=lambda: self.iniciar_juego(True, 'medio')).pack(pady=5)
        tk.Button(root, text="Difícil", font=('Arial', 16), bg="#c0392b", fg="white", width=25,
                  command=lambda: self.iniciar_juego(True, 'dificil')).pack(pady=5)

    def iniciar_juego(self, modo_pc, dificultad):
        self.root.destroy()
        ventana_juego = tk.Tk()
        TicTacToeGUI(ventana_juego, modo_pc, dificultad)
        ventana_juego.mainloop()

class TicTacToeGUI:
    def __init__(self, root, modo_pc, dificultad):
        self.root = root
        self.root.title("Juego del Gato")
        self.root.configure(bg="#2c3e50")

        self.tablero = crear_tablero()
        self.jugador = 'X'
        self.victorias = {'X': 0, 'O': 0}
        self.modo_pc = modo_pc
        self.dificultad = dificultad

        tk.Label(self.root, text="Juego del Gato", font=('Helvetica', 24, 'bold'), fg="white", bg="#2c3e50").pack(pady=10)

        self.frame_tablero = tk.Frame(self.root, bg="#34495e")
        self.frame_tablero.pack(pady=10)

        self.botones = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.frame_tablero, text=' ', font=('Arial', 28, 'bold'), width=5, height=2,
                                bg="#ecf0f1", fg="#2c3e50", activebackground="#bdc3c7",
                                command=lambda fila=i, col=j: self.jugar_turno(fila, col))
                btn.grid(row=i, column=j, padx=5, pady=5)
                self.botones[i][j] = btn

        self.label_info = tk.Label(self.root, text=f"Turno del jugador {self.jugador}", font=('Arial', 16), fg="white", bg="#2c3e50")
        self.label_info.pack(pady=10)

        self.label_victorias = tk.Label(self.root, text=self.obtener_texto_victorias(), font=('Arial', 16), fg="white", bg="#2c3e50")
        self.label_victorias.pack(pady=10)

        tk.Button(self.root, text="Reiniciar Juego", font=('Arial', 14, 'bold'), bg="#e74c3c", fg="white", command=self.reiniciar_juego).pack(pady=10)

    def obtener_texto_victorias(self):
        return f"Victorias - X: {self.victorias['X']} | O: {self.victorias['O']}"

    def jugar_turno(self, fila, col):
        if realizar_movimiento(self.tablero, fila, col, self.jugador):
            self.botones[fila][col]['text'] = self.jugador
            self.botones[fila][col]['state'] = 'disabled'
            if verificar_ganador(self.tablero, self.jugador):
                self.victorias[self.jugador] += 1
                messagebox.showinfo("Fin del juego", f"¡El jugador {self.jugador} ha ganado!")
                self.reiniciar_tablero()
            elif tablero_lleno(self.tablero):
                messagebox.showinfo("Fin del juego", "¡Empate!")
                self.reiniciar_tablero()
            else:
                self.jugador = 'O' if self.jugador == 'X' else 'X'
                self.label_info.config(text=f"Turno del jugador {self.jugador}")
                self.label_victorias.config(text=self.obtener_texto_victorias())

                if self.modo_pc and self.jugador == 'O':
                    self.root.after(500, self.jugar_pc)
        else:
            messagebox.showwarning("Movimiento inválido", "Esa casilla ya está ocupada.")

    def jugar_pc(self):
        if self.dificultad == 'facil':
            movimiento = movimiento_pc_facil(self.tablero)
        elif self.dificultad == 'medio':
            movimiento = movimiento_pc_medio(self.tablero)
        else:
            movimiento = movimiento_pc_dificil(self.tablero)
        if movimiento:
            fila, col = movimiento
            self.jugar_turno(fila, col)

    def reiniciar_tablero(self):
        self.tablero = crear_tablero()
        for i in range(3):
            for j in range(3):
                self.botones[i][j]['text'] = ' '
                self.botones[i][j]['state'] = 'normal'
        self.jugador = 'X'
        self.label_info.config(text=f"Turno del jugador {self.jugador}")

    def reiniciar_juego(self):
        self.victorias = {'X': 0, 'O': 0}
        self.reiniciar_tablero()
        self.label_victorias.config(text=self.obtener_texto_victorias())

root = tk.Tk()
PantallaInicio(root)
root.mainloop()