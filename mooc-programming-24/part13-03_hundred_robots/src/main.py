# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
import pygame
pygame.init()

window = pygame.display.set_mode((640, 480))

bot = pygame.image.load("robot.png")
width = 0.8 * bot.get_width()
height = bot.get_height()

window.fill((0,0,0))

r = width
d = height

for i in range (1,11):
    for i in range(0, 10):
        window.blit(bot,(r + i * width, d))
    r += 0.25*width
    d += 0.25*height

#Not precisely the same proportions as in the example, but hopefully good enough. 

pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()