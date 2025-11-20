import random
from dataclasses import dataclass
from settings import GRID_COLS, GRID_ROWS

@dataclass(frozen=True)
class Point:
    x: int
    y: int

def clamp_wrap(p: Point) -> Point:
    return Point(p.x % GRID_COLS, p.y % GRID_ROWS)

class Snake:
    def __init__(self):
        mid = Point(GRID_COLS // 2, GRID_ROWS // 2)
        self.body = [mid, Point(mid.x - 1, mid.y), Point(mid.x - 2, mid.y)]
        self.direction = Point(1, 0)
        self.grow = 0
        self.alive = True

    def set_direction(self, dx, dy):
        new_dir = Point(dx, dy)
        if len(self.body) > 1:
            if Point(self.body[0].x + new_dir.x, self.body[0].y + new_dir.y) == self.body[1]:
                return
        self.direction = new_dir

    def head(self):
        return self.body[0]

    def move(self, wrap=True):
        new_head = Point(self.head().x + self.direction.x, self.head().y + self.direction.y)
        if wrap:
            new_head = clamp_wrap(new_head)
        else:
            if not (0 <= new_head.x < GRID_COLS and 0 <= new_head.y < GRID_ROWS):
                self.alive = False
                return
        if new_head in self.body:
            self.alive = False
            return
        self.body.insert(0, new_head)
        if self.grow > 0:
            self.grow -= 1
        else:
            self.body.pop()

    def eat(self):
        self.grow += 1

class Food:
    def __init__(self, snake: Snake):
        self.pos = self.spawn(snake)

    def spawn(self, snake: Snake) -> Point:
        free = {Point(x, y) for x in range(GRID_COLS) for y in range(GRID_ROWS)}
        free -= set(snake.body)
        return random.choice(list(free)) if free else snake.head()