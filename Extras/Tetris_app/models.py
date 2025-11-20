import random
from dataclasses import dataclass
from typing import List, Tuple, Optional
from settings import COLS, ROWS, COLORS, SCORES, LEVEL_STEP_LINES, INITIAL_DROP, MIN_DROP, HARD_DROP_SCORE, SOFT_DROP_SCORE

# Definición de formas (matrices 4x4) y rotaciones por índice
SHAPES = {
    'I': [
        [[0,0,0,0],
         [1,1,1,1],
         [0,0,0,0],
         [0,0,0,0]],
        [[0,0,1,0],
         [0,0,1,0],
         [0,0,1,0],
         [0,0,1,0]],
    ],
    'O': [
        [[0,1,1,0],
         [0,1,1,0],
         [0,0,0,0],
         [0,0,0,0]],
    ],
    'T': [
        [[0,1,0,0],
         [1,1,1,0],
         [0,0,0,0],
         [0,0,0,0]],
        [[0,1,0,0],
         [0,1,1,0],
         [0,1,0,0],
         [0,0,0,0]],
        [[0,0,0,0],
         [1,1,1,0],
         [0,1,0,0],
         [0,0,0,0]],
        [[0,1,0,0],
         [1,1,0,0],
         [0,1,0,0],
         [0,0,0,0]],
    ],
    'S': [
        [[0,1,1,0],
         [1,1,0,0],
         [0,0,0,0],
         [0,0,0,0]],
        [[1,0,0,0],
         [1,1,0,0],
         [0,1,0,0],
         [0,0,0,0]],
    ],
    'Z': [
        [[1,1,0,0],
         [0,1,1,0],
         [0,0,0,0],
         [0,0,0,0]],
        [[0,1,0,0],
         [1,1,0,0],
         [1,0,0,0],
         [0,0,0,0]],
    ],
    'J': [
        [[1,0,0,0],
         [1,1,1,0],
         [0,0,0,0],
         [0,0,0,0]],
        [[0,1,1,0],
         [0,1,0,0],
         [0,1,0,0],
         [0,0,0,0]],
        [[0,0,0,0],
         [1,1,1,0],
         [0,0,1,0],
         [0,0,0,0]],
        [[0,1,0,0],
         [0,1,0,0],
         [1,1,0,0],
         [0,0,0,0]],
    ],
    'L': [
        [[0,0,1,0],
         [1,1,1,0],
         [0,0,0,0],
         [0,0,0,0]],
        [[0,1,0,0],
         [0,1,0,0],
         [0,1,1,0],
         [0,0,0,0]],
        [[0,0,0,0],
         [1,1,1,0],
         [1,0,0,0],
         [0,0,0,0]],
        [[1,1,0,0],
         [0,1,0,0],
         [0,1,0,0],
         [0,0,0,0]],
    ],
}

def rotate_matrix(mat: List[List[int]]) -> List[List[int]]:
    # Rotación 90°: transponer y revertir filas
    return [list(row) for row in zip(*mat[::-1])]

@dataclass
class Piece:
    type: str
    rotation: int
    x: int
    y: int

    def shape(self) -> List[List[int]]:
        base = SHAPES[self.type]
        idx = self.rotation % len(base)
        return base[idx]

    def cells(self) -> List[Tuple[int, int]]:
        result = []
        m = self.shape()
        for r in range(4):
            for c in range(4):
                if m[r][c]:
                    result.append((self.x + c, self.y + r))
        return result

class Bag:
    # Generador 7-bag: asegura distribución uniforme
    def __init__(self):
        self.bag = []
        self.refill()

    def refill(self):
        self.bag = list(SHAPES.keys())
        random.shuffle(self.bag)

    def next(self) -> str:
        if not self.bag:
            self.refill()
        return self.bag.pop()

class Board:
    def __init__(self):
        self.grid = [['' for _ in range(COLS)] for _ in range(ROWS)]
        self.bag = Bag()
        self.current = self.spawn_piece()
        self.next_type = self.bag.next()
        self.score = 0
        self.lines = 0
        self.level = 1
        self.drop_time = INITIAL_DROP
        self.game_over = False

    def spawn_piece(self) -> Piece:
        t = self.bag.next()
        # pieza centrada arriba
        return Piece(type=t, rotation=0, x=COLS // 2 - 2, y=0)

    def fits(self, piece: Piece) -> bool:
        for (cx, cy) in piece.cells():
            if cx < 0 or cx >= COLS or cy < 0 or cy >= ROWS:
                return False
            if cy >= 0 and self.grid[cy][cx]:
                return False
        return True

    def lock_piece(self):
        for (cx, cy) in self.current.cells():
            if 0 <= cy < ROWS:
                self.grid[cy][cx] = self.current.type
            else:
                self.game_over = True
        cleared = self.clear_lines()
        if cleared:
            self.score += SCORES.get(cleared, 0)
            self.lines += cleared
            self.update_level()
        # Siguiente pieza
        self.current = Piece(type=self.next_type, rotation=0, x=COLS // 2 - 2, y=0)
        self.next_type = self.bag.next()
        if not self.fits(self.current):
            self.game_over = True

    def clear_lines(self) -> int:
        new_grid = [row for row in self.grid if any(cell == '' for cell in row)]
        cleared = ROWS - len(new_grid)
        # Añadir filas vacías arriba
        for _ in range(cleared):
            new_grid.insert(0, ['' for _ in range(COLS)])
        self.grid = new_grid
        return cleared

    def update_level(self):
        self.level = self.lines // LEVEL_STEP_LINES + 1
        # acelerar caída con límite mínimo
        self.drop_time = max(INITIAL_DROP * (0.9 ** (self.level - 1)), MIN_DROP)

    # Movimientos
    def move(self, dx: int, dy: int) -> bool:
        if self.game_over:
            return False
        test = Piece(self.current.type, self.current.rotation, self.current.x + dx, self.current.y + dy)
        if self.fits(test):
            self.current = test
            # puntuar soft drop
            if dy > 0:
                self.score += SOFT_DROP_SCORE
            return True
        return False

    def hard_drop(self) -> int:
        if self.game_over:
            return 0
        distance = 0
        while self.move(0, 1):
            distance += 1
        self.score += distance * HARD_DROP_SCORE
        self.lock_piece()
        return distance

    def rotate(self, clockwise: bool = True) -> bool:
        if self.game_over:
            return False
        rot = (self.current.rotation + (1 if clockwise else -1))
        test = Piece(self.current.type, rot, self.current.x, self.current.y)
        # Intentar kicks simples (izq/der/arriba)
        kicks = [(0,0), (-1,0), (1,0), (0,-1)]
        for kx, ky in kicks:
            kicked = Piece(test.type, test.rotation, test.x + kx, test.y + ky)
            if self.fits(kicked):
                self.current = kicked
                return True
        return False

    def tick_gravity(self) -> bool:
        # avanza una celda hacia abajo; si no cabe, bloquea
        moved = self.move(0, 1)
        if not moved:
            self.lock_piece()
        return moved