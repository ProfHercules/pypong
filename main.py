import sys
import random

import pygame

from constants import *
from objects import Ball, Paddle

pygame.init()
pygame.display.set_caption("PyPong")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Fira Code", 32)


def update_fps():
    fps = str(int(clock.get_fps()))
    fps_text = font.render(fps, True, pygame.Color("coral"))
    return fps_text


# init game objects
left_paddle = Paddle(32, SC_HEIGHT / 2 - 64)
right_paddle = Paddle(SC_WIDTH - 32, SC_HEIGHT / 2 - 96)
ball = Ball(SC_WIDTH / 2, SC_HEIGHT / 2)
ball.change_v(dvx=-2, dvy=2)

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(cl_off_black)
    screen.blit(update_fps(), (16, 5))

    if ball.is_colliding_with(left_paddle) or left_paddle.is_colliding_with(ball):
        print("Colliding left")
        ball.bounce_x()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_paddle.move(dy=-PADDLE_SPEED)
    if keys[pygame.K_s]:
        left_paddle.move(dy=PADDLE_SPEED)
    if keys[pygame.K_UP]:
        left_paddle.move(dy=-PADDLE_SPEED)
    if keys[pygame.K_DOWN]:
        left_paddle.move(dy=PADDLE_SPEED)

    ball.update()
    left_paddle.draw(on=screen)
    right_paddle.draw(on=screen)
    ball.draw(on=screen)

    # --- Limit to 60 frames per second
    clock.tick(FPS)
    pygame.display.flip()
