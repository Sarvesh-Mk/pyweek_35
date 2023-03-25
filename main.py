import pygame 

pygame.init()
win = pygame.display.set_mode((1620, 880))

def redrawWindow():
    win.fill((255, 255, 255))
    pygame.display.update()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            run = False

    redrawWindow()
