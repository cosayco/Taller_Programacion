import pygame, sys
from settings import WIDTH, HEIGHT
from models import GameState
from utils import clear_screen, render_game
from ui import UI

def main():
    pygame.init()
    pygame.display.set_caption("Space Invaders — Pygame modular")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    ui = UI(screen)

    gs = GameState()
    move_dir = 0.0
    firing = False

    while True:
        dt = clock.tick(60) / 1000.0

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit(); sys.exit()
                if event.key == pygame.K_p:
                    gs.paused = not gs.paused
                if gs.game_over and event.key == pygame.K_r:
                    gs.reset()
                    move_dir = 0.0
                    firing = False
                # controles en juego
                if not gs.game_over:
                    if event.key == pygame.K_LEFT:
                        move_dir = -1.0
                    elif event.key == pygame.K_RIGHT:
                        move_dir = 1.0
                    elif event.key == pygame.K_SPACE:
                        firing = True
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    # si suelta una flecha, comprobar la otra
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                        move_dir = -1.0
                    elif keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
                        move_dir = 1.0
                    else:
                        move_dir = 0.0
                elif event.key == pygame.K_SPACE:
                    firing = False

        # Lógica
        gs.update(dt, move_dir, firing)

        # Render
        clear_screen(screen)
        render_game(screen, gs)
        ui.draw_hud(gs.score, gs.player.lives, gs.level)
        if gs.game_over:
            ui.draw_game_over(gs.score)

        pygame.display.flip()

if __name__ == "__main__":
    main()