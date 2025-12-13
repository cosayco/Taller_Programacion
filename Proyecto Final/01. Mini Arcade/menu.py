import pygame
import sys
from config import BLANCO, NEGRO, VERDE, ANCHO
from juego_snake import juego_snake
from juego_pong import juego_pong

def menu_principal(pantalla, clock):

    opciones = ["Jugar Snake", "Jugar Pong (2 Jugadores)", "Salir"]
    seleccion = 0

    fuente_titulo = pygame.font.SysFont(None, 55)
    fuente_opciones = pygame.font.SysFont(None, 40)

    ejecutando = True
    while ejecutando:
        pantalla.fill(NEGRO)

        titulo = fuente_titulo.render("MENÚ PRINCIPAL", True, BLANCO)
        pantalla.blit(titulo, (220-40, 50))

        for i, opcion in enumerate(opciones):
            if i == seleccion:
                texto = fuente_opciones.render("> " + opcion, True, VERDE)
            else:
                texto = fuente_opciones.render(opcion, True, BLANCO)

            pantalla.blit(texto, (ANCHO//2 - 180, 150 + i * 60))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    seleccion = (seleccion - 1) % len(opciones)
                elif event.key == pygame.K_DOWN:
                    seleccion = (seleccion + 1) % len(opciones)
                elif event.key == pygame.K_RETURN:
                    if seleccion == 0:
                        juego_snake(pantalla, clock)
                    elif seleccion == 1:
                        juego_pong(pantalla, clock)
                    elif seleccion == 2:
                        pygame.quit()
                        sys.exit()