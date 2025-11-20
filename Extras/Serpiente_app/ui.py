import pygame
from settings import TEXT_COLOR, FOOD_COLOR, WIDTH, HEIGHT

class UI:
    def __init__(self, screen):
        self.font = pygame.font.SysFont("consolas", 20)
        self.big = pygame.font.SysFont("consolas", 36, bold=True)
        self.screen = screen

    def draw_hud(self, score, speed, paused):
        text = f"Puntos: {score}  Velocidad: {speed:.1f}  {'[PAUSA]' if paused else ''}"
        surf = self.font.render(text, True, TEXT_COLOR)
        self.screen.blit(surf, (10, 10))

    def draw_game_over(self, score):
        msg1 = self.big.render("GAME OVER", True, FOOD_COLOR)
        msg2 = self.font.render(f"Puntos: {score}  (Enter: reiniciar, Esc: salir)", True, TEXT_COLOR)
        rect1 = msg1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
        rect2 = msg2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
        self.screen.blit(msg1, rect1)
        self.screen.blit(msg2, rect2)