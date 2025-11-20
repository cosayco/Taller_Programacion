# Pantalla
WIDTH = 800
HEIGHT = 600
BG_COLOR = (16, 16, 24)

# Colores
TEXT_COLOR = (230, 230, 230)
PLAYER_COLOR = (80, 200, 255)
ENEMY_COLOR = (120, 255, 120)
BULLET_COLOR = (255, 220, 120)
BARRIER_COLOR = (90, 180, 90)
WARNING_COLOR = (240, 80, 80)

# Jugador
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 20
PLAYER_SPEED = 300        # px/s
PLAYER_LIVES = 3
FIRE_COOLDOWN = 0.35      # s entre disparos

# Bala
BULLET_WIDTH = 4
BULLET_HEIGHT = 12
BULLET_SPEED = 450        # px/s
MAX_BULLETS = 3

# Enemigos
ENEMY_WIDTH = 36
ENEMY_HEIGHT = 24
ENEMY_ROWS = 5
ENEMY_COLS = 10
ENEMY_X_SPACING = 16
ENEMY_Y_SPACING = 18
ENEMY_INIT_SPEED = 40     # px/s (movimiento horizontal del bloque)
ENEMY_STEP_DOWN = 20      # px al cambiar de dirección
ENEMY_SPEED_GROWTH = 1.12 # crecimiento por nivel

# Barreras (opcional simple)
BARRIER_COUNT = 4
BARRIER_WIDTH = 70
BARRIER_HEIGHT = 16
BARRIER_Y = HEIGHT - 160

# Puntuación y nivel
SCORE_PER_ENEMY = 50
LEVEL_UP_BONUS = 200

# Fuentes
FONT_NAME = "consolas"