import pygame

pygame.init()

screenw = 640
screenh = 480

window = pygame.display.set_mode((screenw, screenh))

robot = pygame.image.load("robot.png")
robotw = robot.get_width()
roboth = robot.get_height()

clock = pygame.time.Clock()

x = 0
y = 0
d = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot,(x, y))
    pygame.display.flip()
    if d > 0:
        y += 1
    elif d < 0:
        y -= 1

    if y >= screenh-roboth or y <= 0:
        d = -d

    clock.tick(60)    #The example looked a wee faster but I'm well aware that I'd just need to increase this number a little bit
 