import pygame
from settings import TEXT_COLOR, FONT_NAME, WIDTH, HEIGHT, WARNING_COLOR

class UI:
    def __init__(self, screen):
        self.font = pygame.font.SysFont(FONT_NAME, 20)
        self.big = pygame.font.SysFont(FONT_NAME, 36, bold=True)
        self.screen = screen

    def draw_hud(self, score, lives, level):
        self.screen.blit(self.font.render(f"Puntos: {score}", True, TEXT_COLOR), (10, 10))
        self.screen.blit(self.font.render(f"Vidas: {lives}", True, TEXT_COLOR), (10, 35))
        self.screen.blit(self.font.render(f"Nivel: {level}", True, TEXT_COLOR), (10, 60))
        # Controles
        controls_x = WIDTH - 240
        self.screen.blit(self.font.render("Controles:", True, TEXT_COLOR), (controls_x, 10))
        self.screen.blit(self.font.render("←/→ mover", True, TEXT_COLOR), (controls_x, 35))
        self.screen.blit(self.font.render("Espacio: disparar", True, TEXT_COLOR), (controls_x, 55))
        self.screen.blit(self.font.render("P: pausa | R: reiniciar", True, TEXT_COLOR), (controls_x, 75))

    def draw_game_over(self, score):
        msg1 = self.big.render("GAME OVER", True, WARNING_COLOR)
        msg2 = self.font.render(f"Puntos: {score}  (R: reiniciar, Esc: salir)", True, TEXT_COLOR)
        rect1 = msg1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
        rect2 = msg2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
        self.screen.blit(msg1, rect1)
        self.screen.blit(msg2, rect2)