# WRITE YOUR SOLUTION HERE:
import random
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

bot = pygame.image.load("robot.png")
width = bot.get_width()
height = bot.get_height()

window.fill((0,0,0))
for i in range (0,1000):
    window.blit(bot,(random.randint(0, 640-width), random.randint(0, 480-height)))


pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()