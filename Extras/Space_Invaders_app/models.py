from dataclasses import dataclass
from typing import List
import math, random
from settings import (
    WIDTH, HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPEED, PLAYER_LIVES, FIRE_COOLDOWN,
    BULLET_WIDTH, BULLET_HEIGHT, BULLET_SPEED, MAX_BULLETS,
    ENEMY_WIDTH, ENEMY_HEIGHT, ENEMY_ROWS, ENEMY_COLS, ENEMY_X_SPACING, ENEMY_Y_SPACING,
    ENEMY_INIT_SPEED, ENEMY_STEP_DOWN, ENEMY_SPEED_GROWTH,
    BARRIER_COUNT, BARRIER_WIDTH, BARRIER_HEIGHT, BARRIER_Y,
    SCORE_PER_ENEMY, LEVEL_UP_BONUS
)

@dataclass
class Rect:
    x: float
    y: float
    w: float
    h: float

    def intersects(self, other: "Rect") -> bool:
        return not (self.x + self.w < other.x or other.x + other.w < self.x or
                    self.y + self.h < other.y or other.y + other.h < self.y)

class Bullet:
    def __init__(self, x: float, y: float, speed: float):
        self.rect = Rect(x, y, BULLET_WIDTH, BULLET_HEIGHT)
        self.speed = speed
        self.alive = True

    def update(self, dt: float):
        self.rect.y -= self.speed * dt
        if self.rect.y + self.rect.h < 0:
            self.alive = False

class Player:
    def __init__(self):
        self.rect = Rect(WIDTH / 2 - PLAYER_WIDTH / 2, HEIGHT - PLAYER_HEIGHT - 20, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.speed = PLAYER_SPEED
        self.lives = PLAYER_LIVES
        self.cooldown = 0.0

    def update(self, dt: float, move_dir: float):
        self.rect.x += move_dir * self.speed * dt
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.w))
        if self.cooldown > 0:
            self.cooldown -= dt

    def can_fire(self) -> bool:
        return self.cooldown <= 0

    def fire(self) -> Bullet:
        self.cooldown = FIRE_COOLDOWN
        bx = self.rect.x + self.rect.w / 2 - BULLET_WIDTH / 2
        by = self.rect.y - BULLET_HEIGHT
        return Bullet(bx, by, BULLET_SPEED)

class Enemy:
    def __init__(self, x: float, y: float):
        self.rect = Rect(x, y, ENEMY_WIDTH, ENEMY_HEIGHT)
        self.alive = True

class EnemyFormation:
    def __init__(self, level: int = 1):
        self.enemies: List[Enemy] = []
        self.level = level
        self.speed = ENEMY_INIT_SPEED * (ENEMY_SPEED_GROWTH ** (level - 1))
        self.dir = 1  # 1 derecha, -1 izquierda
        # calculamos el bloque y márgenes
        total_w = ENEMY_COLS * ENEMY_WIDTH + (ENEMY_COLS - 1) * ENEMY_X_SPACING
        start_x = (WIDTH - total_w) / 2
        start_y = 60
        for r in range(ENEMY_ROWS):
            for c in range(ENEMY_COLS):
                x = start_x + c * (ENEMY_WIDTH + ENEMY_X_SPACING)
                y = start_y + r * (ENEMY_HEIGHT + ENEMY_Y_SPACING)
                self.enemies.append(Enemy(x, y))

    def bounds(self):
        xs = [e.rect.x for e in self.enemies if e.alive]
        xe = [e.rect.x + e.rect.w for e in self.enemies if e.alive]
        ys = [e.rect.y for e in self.enemies if e.alive]
        ye = [e.rect.y + e.rect.h for e in self.enemies if e.alive]
        if not xs:
            return Rect(0,0,0,0)
        left = min(xs); right = max(xe); top = min(ys); bottom = max(ye)
        return Rect(left, top, right - left, bottom - top)

    def update(self, dt: float):
        if not any(e.alive for e in self.enemies):
            return
        b = self.bounds()
        # cambio de dirección al tocar bordes
        if (self.dir > 0 and b.x + b.w >= WIDTH - 20) or (self.dir < 0 and b.x <= 20):
            self.dir *= -1
            for e in self.enemies:
                if e.alive:
                    e.rect.y += ENEMY_STEP_DOWN
        else:
            dx = self.dir * self.speed * dt
            for e in self.enemies:
                if e.alive:
                    e.rect.x += dx

    def any_reached_player_line(self) -> bool:
        for e in self.enemies:
            if e.alive and e.rect.y + e.rect.h >= HEIGHT - 80:
                return True
        return False

class Barrier:
    def __init__(self, x: float):
        self.rect = Rect(x, BARRIER_Y, BARRIER_WIDTH, BARRIER_HEIGHT)
        self.hp = 8  # aguante simple

    def hit(self):
        self.hp -= 1

    def alive(self) -> bool:
        return self.hp > 0

class GameState:
    def __init__(self):
        self.player = Player()
        self.bullets: List[Bullet] = []
        self.enemies = EnemyFormation(level=1)
        self.barriers: List[Barrier] = self._spawn_barriers()
        self.level = 1
        self.score = 0
        self.game_over = False
        self.paused = False

    def _spawn_barriers(self) -> List[Barrier]:
        margin = 60
        usable = WIDTH - 2 * margin
        spacing = usable / (BARRIER_COUNT - 1)
        xs = [margin + i * spacing - BARRIER_WIDTH / 2 for i in range(BARRIER_COUNT)]
        return [Barrier(x) for x in xs]

    def update(self, dt: float, move_dir: float, firing: bool):
        if self.game_over or self.paused:
            return
        # jugador
        self.player.update(dt, move_dir)
        # disparo
        if firing and self.player.can_fire() and len(self.bullets) < MAX_BULLETS:
            self.bullets.append(self.player.fire())
        # balas
        for b in self.bullets:
            b.update(dt)
        self.bullets = [b for b in self.bullets if b.alive]
        # enemigos
        self.enemies.update(dt)
        # colisiones bala-enemigo
        for b in self.bullets:
            for e in self.enemies.enemies:
                if e.alive and b.alive and b.rect.intersects(e.rect):
                    e.alive = False
                    b.alive = False
                    self.score += SCORE_PER_ENEMY
                    break
        # colisiones con barreras
        for b in self.bullets:
            for barrier in self.barriers:
                if barrier.alive() and b.alive and b.rect.intersects(barrier.rect):
                    b.alive = False
                    barrier.hit()
                    break
        self.barriers = [bar for bar in self.barriers if bar.alive()]
        # derrota por contacto
        if self.enemies.any_reached_player_line():
            self.player.lives -= 1
            if self.player.lives <= 0:
                self.game_over = True
            else:
                # reubicar formación y limpiar balas
                self.enemies = EnemyFormation(level=self.level)
                self.bullets.clear()
        # nivel completado
        if not any(e.alive for e in self.enemies.enemies):
            self.level += 1
            self.score += LEVEL_UP_BONUS
            self.enemies = EnemyFormation(level=self.level)

    def reset(self):
        self.__init__()