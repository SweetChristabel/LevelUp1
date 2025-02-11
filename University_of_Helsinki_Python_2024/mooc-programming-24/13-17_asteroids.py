# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint
pygame.init()
screenw = 640
screenh = 480
display = pygame.display.set_mode((screenw, screenh))
robot = pygame.image.load("robot.png")
rock = pygame.image.load("rock.png")

rocks = []
clock = pygame.time.Clock()
gamefont = pygame.font.SysFont("Comic Sans MS", 24)     #it wasn't explicitly stated that we must use Arial!
points = 0

moveleft = False
moveright = False
rx = screenw/2 - robot.get_width()/2
ry = screenh - robot.get_height()



def get_hitbox(x,y,object):
    hitbox = [(x, y),(x+object.get_width(),y+object.get_height())]
    return hitbox

def spawnsteroid():
    x = randint(0, screenw-rock.get_width())
    y = -rock.get_height()
    return x, y

def checkoverlap():
    return not (hitbox[1][1] < rhitbox[0][1] or rhitbox[1][0] < hitbox[0][0] or rhitbox[0][0] > hitbox[1][0])


while True:
    newrocks = []
    display.fill((0,0,0))
    display.blit(robot, (rx, ry))
    pointcounter = gamefont.render(f"Points: {points}", True, (255, 0, 0))
    display.blit(pointcounter, (screenw - 120, 0))
    spawn = randint(0, 150)
    if spawn == 50:
        rocks.append(spawnsteroid())
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveleft = True
            if event.key == pygame.K_RIGHT:
                moveright = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moveleft = False
            if event.key == pygame.K_RIGHT:
                moveright = False
        if event.type == pygame.QUIT:
            exit(0)

    if moveleft:
        rx -= 2     #making the game a little more playable by increasing the speed of the robot
    if moveright:   #since a bad spawn is likely to end the game quickly anyway
        rx += 2     #and I'm too lazy to tinker with the spawn randomness right now, will save that energy for the big one
    for asteroid in rocks:
        display.blit(rock, (asteroid))
    rhitbox = get_hitbox(rx, ry, robot)
    for asteroid in rocks:
        hitbox = get_hitbox(asteroid[0], asteroid[1], rock)
        if hitbox[1][1] > screenh:
            points = 0
            rx = screenw/2 - robot.get_width()/2
            ry = screenh - robot.get_height()
            break   #choosing to just reset the game rather than exit entirely
        if checkoverlap():
            points += 1
        else:
            newrocks.append((asteroid[0],asteroid[1]+1))
            

    rocks = newrocks
    pygame.display.flip()
    clock.tick(150) 