import pygame

# Colores
BLANCO = (255, 255, 255)
NEGRO  = (0, 0, 0)
VERDE  = (0, 200, 0)
ROJO   = (200, 30, 30)
AZUL   = (50, 150, 255)

# Pantalla
ANCHO = 600
ALTO  = 400
CELDA = 20

def inicializar_pygame():
    """Crea la pantalla principal y el reloj."""
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Mini Arcade en Python")
    clock = pygame.time.Clock()
    return pantalla, clock