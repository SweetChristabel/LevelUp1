import pygame

pygame.init()
window = pygame.display.set_mode((1280, 960))

errorbox = pygame.image.load("windowserror.png")
errorsound = pygame.mixer.Sound("win98error.mp3")
easteregg = pygame.mixer.Sound("What Is Love.wav")
hold = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            hold = True
        if event.type == pygame.MOUSEBUTTONUP:
            hold = False
        if hold == True:
            x = event.pos[0]-errorbox.get_width()/2
            y = event.pos[1]-errorbox.get_height()/2
            window.blit(errorbox, (x, y))
            pygame.mixer.Sound.play(errorsound)
        pygame.display.flip()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                window.fill((0,0,0))
                pygame.mixer.Sound.play(easteregg)

        if event.type == pygame.QUIT:
            exit()