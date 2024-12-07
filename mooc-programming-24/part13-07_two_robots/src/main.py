# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

screenw = 640
screenh = 480

window = pygame.display.set_mode((screenw, screenh))

robot = pygame.image.load("robot.png")
robotw = robot.get_width()
roboth = robot.get_height()

clock = pygame.time.Clock()

x1 = 0
y1 = roboth/2
x2 = 0
y2 = roboth * 1.5

r1 = 1
r2 = 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot,(x1, y1))
    window.blit(robot,(x2, y2))
    pygame.display.flip()
    if x1 < 0 or x1 > screenw - robotw:
        r1 = -r1
    if x2 < 0 or x2 > screenw - robotw:
        r2 = -r2    

    x1 += r1
    x2 += r2
    clock.tick(60) 