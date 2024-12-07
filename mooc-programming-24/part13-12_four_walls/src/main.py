# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
clock = pygame.time.Clock()

screenw = 640
screenh = 480

window = pygame.display.set_mode((screenw, screenh))
robot = pygame.image.load("robot.png")
roboth = robot.get_height()
robotw = robot.get_width()

r = False
l = False
u = False
d = False

x = 0
y = screenh - roboth

s = 2 #movement speed

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                l = True
            if event.key == pygame.K_RIGHT:
                r = True
            if event.key == pygame.K_UP:
                u = True
            if event.key == pygame.K_DOWN:
                d = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                l = False
            if event.key == pygame.K_RIGHT:
                r = False
            if event.key == pygame.K_UP:
                u = False
            if event.key == pygame.K_DOWN:
                d = False
        if event.type == pygame.QUIT:
            exit()

    if r and x < screenw-robotw:
        x += s
    if l and x > 0:
        x -= s
    if u and y > 0:
        y -= s
    if d and y < screenh-roboth:
        y += s

    window.fill((0,0,0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    clock.tick(60)