
import pygame
from caballo import Caballo
from config import ANCHO, ALTO, META_X, FPS
from utils import cargar_sprite

pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Carrera de Caballos Modular")
clock = pygame.time.Clock()

# Cargar sprites
sprites = []
for i in range(1, 5):
    img = cargar_sprite(f"caballos/caballo_{i}.png")
    sprites.append(img)

# Crear caballos
caballos = []
for i, sprite in enumerate(sprites):
    caballo = Caballo(indice=i, sprite=sprite, x=50, y=100 + i * 100)
    caballos.append(caballo)

corriendo = False
fuente = pygame.font.SysFont(None, 48)

# Loop principal
ejecutando = True
while ejecutando:
    dt_ms = clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                corriendo = True

    pantalla.fill((200, 255, 200))

    # Línea de meta
    pygame.draw.line(pantalla, (255, 0, 0), (META_X, 50), (META_X, ALTO - 50), 5)

    # Actualizar y dibujar caballos
    for caballo in caballos:
        caballo.actualizar(dt_ms, corriendo)
        caballo.dibujar(pantalla)

    if not corriendo:
        texto = fuente.render("Presiona ESPACIO para iniciar", True, (0, 0, 0))
        pantalla.blit(texto, (ANCHO//2 - texto.get_width()//2, 20))

    pygame.display.flip()

pygame.quit()
