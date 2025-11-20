import pygame
from settings import WIDTH, HEIGHT, CELL_SIZE, GRID_COLOR

def draw_grid(surface):
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(surface, GRID_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(surface, GRID_COLOR, (0, y), (WIDTH, y))

def grid_to_px(p):
    return p.x * CELL_SIZE, p.y * CELL_SIZE