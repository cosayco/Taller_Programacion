import pygame
from constantes import TAM_CUADRADO, GRIS

class Ficha:
    def __init__(self, fila, col, color):
        self.fila = fila
        self.col = col
        self.color = color
        self.reina = False
        self.x = 0
        self.y = 0
        self.calcular_pos()

    def calcular_pos(self):
        self.x = TAM_CUADRADO * self.col + TAM_CUADRADO // 2
        self.y = TAM_CUADRADO * self.fila + TAM_CUADRADO // 2
    
    def mover(self, fila, col):
        self.fila = fila
        self.col = col
        self.calcular_pos()

    def dibujar(self, win):
        radio = TAM_CUADRADO // 2 - 10
        pygame.draw.circle(win, GRIS, (self.x, self.y), radio + 2)
        pygame.draw.circle(win, self.color, (self.x, self.y), radio)