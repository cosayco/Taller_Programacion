
import pygame
from dataclasses import dataclass
from config import META_X

@dataclass
class Caballo:
    indice: int
    sprite: pygame.Surface
    x: float
    y: float
    terminado: bool = False
    tiempo_fin_ms: int = 0

    def actualizar(self, dt_ms: int, corriendo: bool):
        if not corriendo or self.terminado:
            return
        velocidad = 3 + (self.indice % 3) + (dt_ms % 2)  # velocidad variable
        self.x += velocidad * (dt_ms / 16.0)
        if self.x + self.sprite.get_width() >= META_X:
            self.x = META_X - self.sprite.get_width()
            self.terminado = True
            self.tiempo_fin_ms = pygame.time.get_ticks()

    def dibujar(self, surface):
        surface.blit(self.sprite, (int(self.x), int(self.y)))
