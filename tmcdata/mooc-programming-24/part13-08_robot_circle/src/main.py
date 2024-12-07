# WRITE YOUR SOLUTION HERE:
import pygame
import math

pygame.init()

screenw = 640
screenh = 480

window = pygame.display.set_mode((screenw, screenh))

bot = pygame.image.load("robot.png")
robotw = bot.get_width()
roboth = bot.get_height()

clock = pygame.time.Clock()

amtofbots = 10
robots = []

for i in range(0, amtofbots):
    robots.append(i*(6.28/amtofbots))
    #Creating a list of initial robot angles

def getcoords (angle):
    x = 320+math.cos(angle)*150-robotw/2
    y = 240+math.sin(angle)*150-roboth/2
    return x, y

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill((0, 0, 0))
    for robot in robots:
        window.blit(bot, (getcoords(robot)))
    robots = [r + 0.01 for r in robots]
    pygame.display.flip()
    clock.tick(60)