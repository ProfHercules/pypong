import pygame

from constants import *


class GameObject(pygame.sprite.Sprite):
    def __init__(self, w, h, color: (int, int, int), x: float = 0.0, y: float = 0.0):
        super(GameObject, self).__init__()
        self.surf = pygame.Surface((w, h))
        self.surf.fill(color)
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, on: pygame.Surface):
        on.blit(self.surf, self.rect)

    def move(self, dx: float = 0.0, dy: float = 0.0):
        self.rect.x += dx
        self.rect.y += dy

    def is_colliding_with(self, other: pygame.sprite.Sprite) -> bool:
        return pygame.sprite.collide_rect(self, other)


class Paddle(GameObject):
    def __init__(self, x, y):
        super().__init__(32, 128, cl_white, x, y)

    def move(self, dx: float = 0.0, dy: float = 0.0):
        super(Paddle, self).move(dx, dy)

        if self.rect.x <= self.rect.width / 2:
            self.rect.x = self.rect.width / 2
        if self.rect.x >= SC_WIDTH - self.rect.width / 2:
            self.rect.x = SC_WIDTH - self.rect.width / 2
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y >= SC_HEIGHT - self.rect.height:
            self.rect.y = SC_HEIGHT - self.rect.height

    def is_colliding_with(self, other: pygame.sprite.Sprite) -> bool:
        return pygame.sprite.collide_rect(self, other)


class Ball(GameObject):
    def __init__(self, x, y):
        super().__init__(50, 50, cl_white, x, y)
        self.velocity = (0.0, 0.0)

    def bounce_x(self):
        vx, vy = self.velocity
        self.velocity = (vx * -1, vy)

    def bounce_y(self):
        vx, vy = self.velocity
        self.velocity = (vx, vy * -1)

    def update(self):
        self.move(dx=self.velocity[0], dy=self.velocity[1])
        if (self.rect.x <= 25) or (self.rect.x >= SC_WIDTH - 25):
            self.bounce_x()
        if self.rect.y <= 25 or (self.rect.y >= SC_HEIGHT - 25):
            self.bounce_y()

    def change_v(self, dvx: float = 0.0, dvy: float = 0.0):
        vx, vy = self.velocity
        self.velocity = (vx + dvx, vy + dvy)

    def draw(self, on: pygame.Surface):
        pygame.draw.circle(on, cl_white, (self.rect.x, self.rect.y), 25)

    def is_colliding_with(self, other: pygame.sprite.Sprite) -> bool:
        return pygame.sprite.collide_rect(self, other)
