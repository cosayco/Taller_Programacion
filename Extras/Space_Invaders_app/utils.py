import pygame
from settings import (
    WIDTH, HEIGHT, BG_COLOR, PLAYER_COLOR, ENEMY_COLOR, BULLET_COLOR, BARRIER_COLOR
)

def clear_screen(screen):
    screen.fill(BG_COLOR)

def draw_rect(screen, color, rect):
    pygame.draw.rect(screen, color, (rect.x, rect.y, rect.w, rect.h))

def render_game(screen, gs):
    # jugador
    draw_rect(screen, PLAYER_COLOR, gs.player.rect)
    # balas
    for b in gs.bullets:
        draw_rect(screen, BULLET_COLOR, b.rect)
    # enemigos
    for e in gs.enemies.enemies:
        if e.alive:
            draw_rect(screen, ENEMY_COLOR, e.rect)
    # barreras
    for bar in gs.barriers:
        draw_rect(screen, BARRIER_COLOR, bar.rect)