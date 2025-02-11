# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint
pygame.init()

clock = pygame.time.Clock()

screenw = 640
screenh = 480

window = pygame.display.set_mode((screenw, screenh))
robot = pygame.image.load("robot.png")

roboth = robot.get_height()
robotw = robot.get_width()
x = randint(0, screenw-robotw)
y = randint(0, screenh-roboth)

def get_hitbox(x,y):
    hitbox = [[x, y],[x+robotw,y+roboth]]
    return hitbox

while True:
    hitbox = get_hitbox(x,y)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] >= hitbox[0][0] and event.pos[0] <= hitbox[1][0] and event.pos[1] >= hitbox[0][1] and event.pos[1] <= hitbox[1][1]:
                x = randint(0, screenw-robotw)
                y = randint(0, screenh-roboth)

        if event.type == pygame.QUIT:
            exit(0)
        
    
    window.fill((0,0,0))
    window.blit(robot, (x, y))
    pygame.display.flip()