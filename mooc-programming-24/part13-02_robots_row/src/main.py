# WRITE YOUR SOLUTION HERE:
import pygame
pygame.init()

window = pygame.display.set_mode((640, 480))

bot = pygame.image.load("robot.png")
width = bot.get_width()
height = bot.get_height()

window.fill((0,0,0))
for i in range (1, 11):
    window.blit(bot,(i * width,height))

pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()