
import pygame

def cargar_sprite(ruta, ancho=120, alto=80):
    img = pygame.image.load(ruta).convert_alpha()
    return pygame.transform.scale(img, (ancho, alto))
