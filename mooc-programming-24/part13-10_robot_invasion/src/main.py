# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()

screenw = 640
screenh = 480

window = pygame.display.set_mode((screenw, screenh))
robot = pygame.image.load("robot.png")
roboth = robot.get_height()
robotw = robot.get_width()

bots = []
leavingbots = []

def spawnrobot():
    x = randint(0, screenw-robotw)
    y = -roboth
    return x, y

clock = pygame.time.Clock()

while True:
    newbots = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    spawn = randint(0, 100)
    if spawn == 50:
        bots.append(spawnrobot())
    window.fill((0,0,0))
    for bot in bots:
        window.blit(robot, (bot))
    for bot in leavingbots:
        window.blit(robot, (bot))
    for bot in bots:
        if bot[1] >= screenh-roboth:
            if bot[0] >= screenw/2:
                newbots.append((bot[0]+1, bot[1]))
            else:
                newbots.append((bot[0]-1, bot[1]))
        else:
            newbots.append((bot[0], bot[1]+1))
    bots = newbots

    pygame.display.flip()
    clock.tick(150)