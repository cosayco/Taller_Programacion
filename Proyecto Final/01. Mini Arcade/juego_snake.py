import pygame
import random
import sys
from config import ANCHO, ALTO, CELDA, BLANCO, NEGRO, VERDE, ROJO

def dibujar_serpiente(pantalla, celda, lista_serpiente):
    for segmento in lista_serpiente:
        pygame.draw.rect(pantalla, VERDE, [segmento[0], segmento[1], celda, celda])

def juego_snake(pantalla, clock):
    x = ANCHO // 2
    y = ALTO // 2

    x_cambio = 0
    y_cambio = 0

    lista_serpiente = []
    largo_serpiente = 1

    manzana_x = round(random.randrange(0, ANCHO - CELDA) / CELDA) * CELDA
    manzana_y = round(random.randrange(0, ALTO - CELDA) / CELDA) * CELDA

    game_over = False

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_cambio == 0:
                    x_cambio = -CELDA
                    y_cambio = 0
                elif event.key == pygame.K_RIGHT and x_cambio == 0:
                    x_cambio = CELDA
                    y_cambio = 0
                elif event.key == pygame.K_UP and y_cambio == 0:
                    y_cambio = -CELDA
                    x_cambio = 0
                elif event.key == pygame.K_DOWN and y_cambio == 0:
                    y_cambio = CELDA
                    x_cambio = 0

        x += x_cambio
        y += y_cambio

        if x >= ANCHO or x < 0 or y >= ALTO or y < 0:
            game_over = True

        pantalla.fill(NEGRO)

        pygame.draw.rect(pantalla, ROJO, [manzana_x, manzana_y, CELDA - 5, CELDA - 5])

        cabeza = [x, y]
        lista_serpiente.append(cabeza)

        if len(lista_serpiente) > largo_serpiente:
            lista_serpiente.pop(0)

        for bloque in lista_serpiente[:-1]:
            if bloque == cabeza:
                game_over = True

        dibujar_serpiente(pantalla, CELDA, lista_serpiente)

        if x == manzana_x and y == manzana_y:
            manzana_x = round(random.randrange(0, ANCHO - CELDA) / CELDA) * CELDA
            manzana_y = round(random.randrange(0, ALTO - CELDA) / CELDA) * CELDA
            largo_serpiente += 1

        pygame.display.update()
        clock.tick(10)

    fuente = pygame.font.SysFont(None, 50)
    texto = fuente.render("GAME OVER - ESPACIO = MENÚ", True, BLANCO)
    pantalla.blit(texto, [ANCHO // 2 - 230, ALTO // 2 - 20])
    pygame.display.update()

    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    esperando = False  # volver al menú