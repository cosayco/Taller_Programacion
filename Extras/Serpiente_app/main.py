import pygame, sys
from settings import WIDTH, HEIGHT, BG_COLOR, INITIAL_SPEED, SPEED_STEP, FOOD_COLOR, SNAKE_COLOR, HEAD_COLOR
from models import Snake, Food
from utils import draw_grid, grid_to_px
from ui import UI

def main():
    pygame.init()
    pygame.display.set_caption("Snake — Modular Pygame")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    ui = UI(screen)

    def reset():
        nonlocal speed, score, snake, food, paused
        snake = Snake()
        food = Food(snake)
        score = 0
        speed = INITIAL_SPEED
        paused = False

    snake = Snake()
    food = Food(snake)
    score = 0
    speed = INITIAL_SPEED
    paused = False

    while True:
        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit(); sys.exit()
                if event.key == pygame.K_RETURN and not snake.alive:
                    reset()
                if event.key == pygame.K_p and snake.alive:
                    paused = not paused
                if event.key in (pygame.K_UP, pygame.K_w):
                    snake.set_direction(0, -1)
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    snake.set_direction(0, 1)
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    snake.set_direction(-1, 0)
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    snake.set_direction(1, 0)

        # Lógica
        if snake.alive and not paused:
            snake.move(wrap=True)
            if snake.head() == food.pos:
                snake.eat()
                score += 10
                speed = min(speed + SPEED_STEP, 25)
                food = Food(snake)

        # Render
        screen.fill(BG_COLOR)
        draw_grid(screen)

        # Comida
        fx, fy = grid_to_px(food.pos)
        pygame.draw.rect(screen, FOOD_COLOR, (fx, fy, 20, 20))

        # Serpiente
        for i, segment in enumerate(snake.body):
            x, y = grid_to_px(segment)
            color = HEAD_COLOR if i == 0 else SNAKE_COLOR
            pygame.draw.rect(screen, color, (x, y, 20, 20))

        ui.draw_hud(score, speed, paused)
        if not snake.alive:
            ui.draw_game_over(score)

        pygame.display.flip()
        clock.tick(speed)

if __name__ == "__main__":
    main()