# ui.py
import pygame
from settings import TEXT_COLOR, FONT_NAME, WIDTH, HEIGHT, CELL, COLS, ROWS

SIDE_X = COLS * CELL + 20
NEXT_AREA_HEIGHT = 140  # alto reservado para el cuadro "Siguiente"

class UI:
    def __init__(self, screen):
        self.font = pygame.font.SysFont(FONT_NAME, 20)
        self.big = pygame.font.SysFont(FONT_NAME, 36, bold=True)
        self.screen = screen

    def draw_hud(self, score, level, lines):
        hud_y = 20 + NEXT_AREA_HEIGHT + 10  # empieza debajo del área "Siguiente"
        self.screen.blit(self.font.render(f"Puntos: {score}", True, TEXT_COLOR), (SIDE_X, hud_y))
        self.screen.blit(self.font.render(f"Nivel: {level}", True, TEXT_COLOR), (SIDE_X, hud_y + 30))
        self.screen.blit(self.font.render(f"Líneas: {lines}", True, TEXT_COLOR), (SIDE_X, hud_y + 60))

        controls_y = hud_y + 110
        self.screen.blit(self.font.render("Controles:", True, TEXT_COLOR), (SIDE_X, controls_y))
        self.screen.blit(self.font.render("←/→ mover", True, TEXT_COLOR), (SIDE_X, controls_y + 25))
        self.screen.blit(self.font.render("↓ bajar", True, TEXT_COLOR), (SIDE_X, controls_y + 45))
        self.screen.blit(self.font.render("Z/X rotar", True, TEXT_COLOR), (SIDE_X, controls_y + 65))
        self.screen.blit(self.font.render("Espacio: drop", True, TEXT_COLOR), (SIDE_X, controls_y + 85))
        self.screen.blit(self.font.render("P pausa | R reiniciar", True, TEXT_COLOR), (SIDE_X, controls_y + 105))

    def draw_game_over(self, score):
        msg1 = self.big.render("GAME OVER", True, (240, 80, 80))
        msg2 = self.font.render(f"Puntos: {score}  (R: reiniciar, Esc: salir)", True, TEXT_COLOR)
        rect1 = msg1.get_rect(center=(COLS * CELL // 2, HEIGHT // 2 - 20))
        rect2 = msg2.get_rect(center=(COLS * CELL // 2, HEIGHT // 2 + 20))
        self.screen.blit(msg1, rect1)
        self.screen.blit(msg2, rect2)