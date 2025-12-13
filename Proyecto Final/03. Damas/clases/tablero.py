import pygame
from constantes import NEGRO, ROJO, FILAS, COLUMNAS, TAM_CUADRADO, AZUL, CREMA
from clases.ficha import Ficha

class Tablero:
    def __init__(self):
        self.board = []
        self.crear_tablero()
        self.fichas_azules = 12
        self.fichas_cremas = 12

    def crear_tablero(self):
        for fila in range(FILAS):
            self.board.append([])
            for col in range(COLUMNAS):
                if col % 2 == ((fila +  1) % 2):
                    if fila < 3:
                        self.board[fila].append(Ficha(fila, col, CREMA))
                    elif fila > 4:
                        self.board[fila].append(Ficha(fila, col, AZUL))
                    else:
                        self.board[fila].append(0)
                else:
                    self.board[fila].append(0)

    def dibujar(self, win):
        self.dibujar_cuadrados(win)
        for fila in range(FILAS):
            for col in range(COLUMNAS):
                ficha = self.board[fila][col]
                if ficha != 0:
                    ficha.dibujar(win)

    def dibujar_cuadrados(self, win):
        win.fill(NEGRO)
        for fila in range(FILAS):
            for col in range(fila % 2, COLUMNAS, 2):
                pygame.draw.rect(win, ROJO, (col*TAM_CUADRADO, fila*TAM_CUADRADO, TAM_CUADRADO, TAM_CUADRADO))

    def mover(self, ficha, fila, col):
        self.board[ficha.fila][ficha.col], self.board[fila][col] = self.board[fila][col], self.board[ficha.fila][ficha.col]
        ficha.mover(fila, col)
        if fila == FILAS - 1 or fila == 0:
            ficha.reina = True

    def obtener_ficha(self, fila, col):
        return self.board[fila][col]

    def eliminar_ficha(self, ficha):
        self.board[ficha.fila][ficha.col] = 0
        if ficha != 0:
            if ficha.color == ROJO:
                self.fichas_cremas -= 1
            else:
                self.fichas_azules -= 1

    def validar_movimiento(self, ficha, fila_dest, col_dest):
        if ficha.fila == fila_dest or ficha.col == col_dest: return False
        
        diferencia_filas = fila_dest - ficha.fila
        diferencia_cols = col_dest - ficha.col
        
        if abs(diferencia_cols) == 1:
            if not ficha.reina:
                if ficha.color == AZUL and diferencia_filas != -1: return False
                if ficha.color == CREMA and diferencia_filas != 1: return False
            elif abs(diferencia_filas) != 1: return False
            return True

        elif abs(diferencia_cols) == 2 and abs(diferencia_filas) == 2:
            fila_media = (ficha.fila + fila_dest) // 2
            col_media = (ficha.col + col_dest) // 2
            ficha_victima = self.board[fila_media][col_media]

            if not ficha.reina:
                if ficha.color == AZUL and diferencia_filas != -2: return False
                if ficha.color == CREMA and diferencia_filas != 2: return False
            
            if ficha_victima == 0: return False
            if ficha_victima.color == ficha.color: return False
            
            return True

        return False
    def hay_captura_posible(self, ficha):
        posibles_destinos = [
            (ficha.fila + 2, ficha.col - 2), (ficha.fila + 2, ficha.col + 2),
            (ficha.fila - 2, ficha.col - 2), (ficha.fila - 2, ficha.col + 2)
        ]
        
        for f, c in posibles_destinos:
            if 0 <= f < FILAS and 0 <= c < COLUMNAS:
                if self.board[f][c] == 0:
                    if self.validar_movimiento(ficha, f, c):
                        return True
        return False