# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()

screenw = 640
screenh = 480

window = pygame.display.set_mode((screenw, screenh))

ball = pygame.image.load("ball.png")
ballw = ball.get_width()
ballh = ball.get_height()

x = randint(0, screenw - ballw)
y = randint(0, screenh - ballh)
#make it start from a random spot, otherwise we'll have the exact same execution each time

r = 1
d = 1

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill((0,0,0))
    window.blit(ball, (x, y))
    pygame.display.flip()

    if x >= screenw - ballw or x < 0:
        r = -r
    if y >= screenh - ballh or y < 0:
        d = -d

    x += r
    y += d

    clock.tick(150)