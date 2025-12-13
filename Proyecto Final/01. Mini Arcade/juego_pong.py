import pygame
import sys
from config import ANCHO, ALTO, BLANCO, NEGRO, AZUL

def juego_pong(pantalla, clock):

    paleta1_y = ALTO // 2 - 40
    paleta2_y = ALTO // 2 - 40

    pelota_x = ANCHO // 2
    pelota_y = ALTO // 2
    vel_x = 4
    vel_y = 4

    puntos1 = 0
    puntos2 = 0

    fuente = pygame.font.SysFont(None, 40)

    ejecutando = True
    while ejecutando:

        pantalla.fill(NEGRO)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        # Jugador 1: A / Z
        if keys[pygame.K_a] and paleta1_y > 0:
            paleta1_y -= 5
        if keys[pygame.K_z] and paleta1_y < ALTO - 80:
            paleta1_y += 5

        # Jugador 2: ↑ / ↓
        if keys[pygame.K_UP] and paleta2_y > 0:
            paleta2_y -= 5
        if keys[pygame.K_DOWN] and paleta2_y < ALTO - 80:
            paleta2_y += 5

        # Paletas
        pygame.draw.rect(pantalla, BLANCO, (20, paleta1_y, 10, 80))
        pygame.draw.rect(pantalla, BLANCO, (ANCHO - 30, paleta2_y, 10, 80))

        # Pelota
        pygame.draw.circle(pantalla, AZUL, (pelota_x, pelota_y), 8)

        pelota_x += vel_x
        pelota_y += vel_y

        if pelota_y <= 0 or pelota_y >= ALTO:
            vel_y *= -1

        if (pelota_x <= 30 and paleta1_y < pelota_y < paleta1_y + 80):
            vel_x *= -1
        if (pelota_x >= ANCHO - 30 and paleta2_y < pelota_y < paleta2_y + 80):
            vel_x *= -1

        if pelota_x < 0:
            puntos2 += 1
            pelota_x, pelota_y = ANCHO // 2, ALTO // 2
        if pelota_x > ANCHO:
            puntos1 += 1
            pelota_x, pelota_y = ANCHO // 2, ALTO // 2

        texto = fuente.render(f"{puntos1}   -   {puntos2}", True, BLANCO)
        pantalla.blit(texto, (ANCHO // 2 - 40, 20))

        pygame.display.update()
        clock.tick(60)

        # Salir al menú
        if keys[pygame.K_SPACE]:
            ejecutando = False