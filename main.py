import pygame

pygame.init()

window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()