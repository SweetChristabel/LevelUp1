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
s = 2 #movement speed

    #My  initial solution, while very much spaghetti, implemented the screen size restriction from the get go, which the model solution, although neater, didn't. 
    #Below is my solution improved after reading the model solution, with a screen size restriction added to it.

positions = [[screenw-robotw, screenh - roboth],[0, screenh-roboth]] #I put them both nicely on the floor and flipped their positions to make them more intuitive

controls = [
    (pygame.K_LEFT, 0, -s, 0),
    (pygame.K_RIGHT, 0, s, 0),
    (pygame.K_UP, 0, 0, -s),
    (pygame.K_DOWN, 0, 0, s),
    (pygame.K_a, 1, -s, 0),
    (pygame.K_d, 1, s, 0),
    (pygame.K_w, 1, 0, -s),
    (pygame.K_s, 1, 0, s)
]

pressedkey = {}

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
           pressedkey[event.key] = True
        if event.type == pygame.KEYUP:
           del pressedkey[event.key]
        if event.type == pygame.QUIT:
            exit()

    for key in controls:
        if key[0] in pressedkey:
            positions[key[1]][0] += key[2]
            positions[key[1]][1] += key[3]
            #keep them within the window
            positions[key[1]][0] = min(positions[key[1]][0],screenw-robotw)
            positions[key[1]][0] = max(positions[key[1]][0], 0)
            positions[key[1]][1] = min(positions[key[1]][1], screenh-roboth)
            positions[key[1]][1] = max(positions[key[1]][1], 0)

    window.fill((0,0,0))
    for i in range(2):
        window.blit(robot, (positions[i][0], positions[i][1]))
    pygame.display.flip()
    clock.tick(60)

#below is my initial solution as it was.


r1 = False
l1 = False
u1 = False
d1 = False

r2 = False
l2 = False
u2 = False
d2 = False

x2 = 0
y2 = screenh - roboth

x1 = screenw - robotw
y1 = screenh - roboth



while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                l1 = True
            if event.key == pygame.K_RIGHT:
                r1 = True
            if event.key == pygame.K_UP:
                u1 = True
            if event.key == pygame.K_DOWN:
                d1 = True
            if event.key == pygame.K_a:
                l2 = True
            if event.key == pygame.K_d:
                r2 = True
            if event.key == pygame.K_w:
                u2 = True
            if event.key == pygame.K_s:
                d2 = True    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                l1 = False
            if event.key == pygame.K_RIGHT:
                r1 = False
            if event.key == pygame.K_UP:
                u1 = False
            if event.key == pygame.K_DOWN:
                d1 = False
            if event.key == pygame.K_a:
                l2 = False
            if event.key == pygame.K_d:
                r2 = False
            if event.key == pygame.K_w:
                u2 = False
            if event.key == pygame.K_s:
                d2 = False    
        if event.type == pygame.QUIT:
            exit()

    if r1 and x1 < screenw-robotw:
        x1 += s
    if l1 and x1 > 0:
        x1 -= s
    if u1 and y1 > 0:
        y1 -= s
    if d1 and y1 < screenh-roboth:
        y1 += s

    if r2 and x2 < screenw-robotw:
        x2 += s
    if l2 and x2 > 0:
        x2 -= s
    if u2 and y2 > 0:
        y2 -= s
    if d2 and y2 < screenh-roboth:
        y2 += s


    window.fill((0,0,0))
    window.blit(robot, (x1, y1))
    window.blit(robot, (x2, y2))
    pygame.display.flip()
    clock.tick(60)