# Dimensiones del tablero estándar de Tetris
COLS = 10
ROWS = 20
CELL = 30

# Ventana
WIDTH = COLS * CELL + 200  # área extra para panel
HEIGHT = ROWS * CELL

# Colores
BG_COLOR = (20, 20, 25)
GRID_COLOR = (40, 40, 50)
TEXT_COLOR = (230, 230, 230)

# Colores por tetromino
COLORS = {
    'I': (0, 240, 240),
    'O': (240, 240, 0),
    'T': (160, 0, 240),
    'S': (0, 240, 0),
    'Z': (240, 0, 0),
    'J': (0, 0, 240),
    'L': (240, 160, 0),
    'X': (90, 90, 90),  # bloque fijo (relleno tablero)
}

# Velocidad de caída (en segundos por celda)
INITIAL_DROP = 0.8
MIN_DROP = 0.08
LEVEL_STEP_LINES = 10  # líneas para subir de nivel

# Puntuación (Guía clásica orientativa)
SCORES = {
    1: 100,
    2: 300,
    3: 500,
    4: 800,  # Tetris
}
SOFT_DROP_SCORE = 1     # por celda
HARD_DROP_SCORE = 2     # por celda

FONT_NAME = "consolas"