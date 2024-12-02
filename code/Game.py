import pygame

from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Quitting")
                    pygame.quit()
                    quit()