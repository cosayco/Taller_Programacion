import pygame, sys
from settings import WIDTH, HEIGHT, BG_COLOR
from models import Board
from utils import draw_grid, draw_board, draw_next_piece
from ui import UI

def main():
    pygame.init()
    pygame.display.set_caption("Tetris — Pygame modular")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    ui = UI(screen)

    board = Board()
    paused = False

    drop_accum = 0.0  # acumulador de tiempo para gravedad
    soft_drop = False

    while True:
        dt = clock.tick(60) / 1000.0  # delta en segundos

        # --- Eventos ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit(); sys.exit()
                if event.key == pygame.K_p:
                    paused = not paused
                if board.game_over and event.key == pygame.K_r:
                    board = Board()
                    paused = False
                if not board.game_over and not paused:
                    if event.key == pygame.K_LEFT:
                        board.move(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        board.move(1, 0)
                    elif event.key == pygame.K_DOWN:
                        soft_drop = True
                    elif event.key == pygame.K_SPACE:
                        board.hard_drop()
                    elif event.key == pygame.K_z:
                        board.rotate(clockwise=False)
                    elif event.key == pygame.K_x:
                        board.rotate(clockwise=True)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    soft_drop = False

        # --- Lógica de gravedad ---
        if not paused and not board.game_over:
            fall_time = board.drop_time
            if soft_drop:
                fall_time = min(fall_time * 0.15, 0.02)
            drop_accum += dt
            if drop_accum >= fall_time:
                board.tick_gravity()
                drop_accum = 0.0

        # --- Render ---
        screen.fill(BG_COLOR)
        draw_board(screen, board, offset_x=0, offset_y=0)
        draw_grid(screen, offset_x=0, offset_y=0)

        # Panel lateral
        draw_next_piece(screen, board)
        ui.draw_hud(board.score, board.level, board.lines)

        if board.game_over:
            ui.draw_game_over(board.score)

        pygame.display.flip()

if __name__ == "__main__":
    main()