# WRITE YOUR SOLUTION HERE:
import pygame
import datetime
import math
pygame.init
screenw = 640
screenh = 480
display = pygame.display.set_mode((screenw, screenh))
display.fill((0,0,0))
center = screenw/2, screenh/2

def defaultdisplay():
    pygame.draw.circle(display, (255,0,0),(center),200)
    pygame.draw.circle(display, (0,0,0), (center), 195)
    pygame.draw.circle(display, (255,0,0), (center), 10)

def getcoords (angle, radius):
    x = screenw/2+math.cos(angle)*radius
    y = screenh/2+math.sin(angle)*radius
    return x, y

quarter = 6.28/4
secminsector = 6.28/60
hoursector = 6.28/12

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    timenow = datetime.datetime.now()
    pygame.display.set_caption(timenow.strftime("%H:%M:%S"))
    defaultdisplay()

    secangle = -quarter + timenow.second*secminsector
    minangle = -quarter + timenow.minute*secminsector + (timenow.second*secminsector/60)
    hourangle = -quarter + (timenow.hour % 12) * hoursector + (timenow.minute*hoursector/60)

    pygame.draw.line(display,(0,0,255),getcoords(secangle, 180),(center),2)
    pygame.draw.line(display,(0,0,255),getcoords(minangle, 180),(center),3)
    pygame.draw.line(display,(0,0,255),getcoords(hourangle, 120),(center),5)
    pygame.display.flip() 