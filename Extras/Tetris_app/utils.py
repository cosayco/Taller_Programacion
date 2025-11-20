# utils.py
import pygame
from settings import COLS, ROWS, CELL, GRID_COLOR, BG_COLOR, COLORS
from ui import SIDE_X, NEXT_AREA_HEIGHT

def draw_grid(surface, offset_x=0, offset_y=0):
    for x in range(COLS + 1):
        pygame.draw.line(surface, GRID_COLOR, (offset_x + x * CELL, offset_y), (offset_x + x * CELL, offset_y + ROWS * CELL))
    for y in range(ROWS + 1):
        pygame.draw.line(surface, GRID_COLOR, (offset_x, offset_y + y * CELL), (offset_x + COLS * CELL, offset_y + y * CELL))

def draw_board(surface, board, offset_x=0, offset_y=0):
    pygame.draw.rect(surface, BG_COLOR, (offset_x, offset_y, COLS * CELL, ROWS * CELL))
    for r in range(ROWS):
        for c in range(COLS):
            t = board.grid[r][c]
            if t:
                color = COLORS.get(t, COLORS['X'])
                pygame.draw.rect(surface, color, (offset_x + c * CELL, offset_y + r * CELL, CELL, CELL))
    for (cx, cy) in board.current.cells():
        if cy >= 0:
            color = COLORS.get(board.current.type, (200, 200, 200))
            pygame.draw.rect(surface, color, (offset_x + cx * CELL, offset_y + cy * CELL, CELL, CELL))

def draw_next_piece(surface, board):
    # Contenedor del panel "Siguiente"
    panel_y = 20
    pygame.draw.rect(surface, (28, 28, 34), (SIDE_X - 10, panel_y - 10, 180, NEXT_AREA_HEIGHT), border_radius=8)

    font = pygame.font.SysFont("consolas", 20)
    label = font.render("Siguiente:", True, (220, 220, 220))
    surface.blit(label, (SIDE_X, panel_y))

    shape = board.next_type
    color = COLORS.get(shape, (200, 200, 200))
    from models import SHAPES
    mat = SHAPES[shape][0]

    # Centrado dentro del área reservada
    cell = CELL // 2
    origin_x = SIDE_X + 20
    origin_y = panel_y + 30
    for r in range(4):
        for c in range(4):
            if mat[r][c]:
                pygame.draw.rect(surface, color, (origin_x + c * cell, origin_y + r * cell, cell, cell))