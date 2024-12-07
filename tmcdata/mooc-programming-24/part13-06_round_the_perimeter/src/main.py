# # WRITE YOUR SOLUTION HERE:
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

def movebot(x, y):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    #probably not the optimal solution in terms of future expandability but hey if it works it ain't stupid
    window.fill((0, 0, 0))
    window.blit(robot,(x, y))
    pygame.display.flip()
    clock.tick(80)

while True:
    while x <= screenw-robotw:
        movebot(x, y)
        x +=1
    while y <= screenh-roboth:
        movebot(x, y)
        y += 1
    while x >= 0:
        movebot(x, y)
        x -= 1
    while y >= 0:
        movebot(x, y)
        y -= 1
    
        

        
    