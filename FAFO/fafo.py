# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()
screenwidth = 640
screenheight = 480
window = pygame.display.set_mode((screenwidth, screenheight))

robot = pygame.image.load("robot.png")
width = robot.get_width()
height = robot.get_height()

x = randint(0, screenwidth - width)
y = randint(0, screenheight - height)
clock = pygame.time.Clock()



r = True
d = True

red, green, blue = 255, 0, 0

phases = [
    ('blue', +1),
    ('red', -1), 
    ('green', +1),  
    ('blue', -1), 
    ('red', +1), 
    ('green', -1), 
]
currentphase = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    color, direction = phases[currentphase]
    if color == 'red':
        red = max(0, min(255, red + direction))
    elif color == 'green':
        green = max(0, min(255, green + direction))
    elif color == 'blue':
        blue = max(0, min(255, blue + direction))

    if (direction == +1 and locals()[color] == 255) or (direction == -1 and locals()[color] == 0):
            currentphase = (currentphase + 1) % len(phases)
            #the modulo operation will return the currentphase, because the division result is 0 and remainder is currentphase, until it gets to the end, then it'll return 0 and start over.

#locals is a neat way to access the variable with the same name as the value of the current color variable :) 

    window.fill((red, green, blue))
    window.blit(robot, (x, y))
    pygame.display.flip()

    if r:
        x += 1
    else:
        x -= 1
    if d:
        y += 1
    else:
        y -= 1

    if x >= screenwidth - width:
        r = False
    if x == 0:
        r = True
    if y >= screenheight - height:
        d = False
    if y == 0:
        d = True

    clock.tick(150)