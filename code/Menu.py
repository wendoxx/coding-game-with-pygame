import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/Menu.mp3')  # Carrega a música
        pygame.mixer_music.play(-1)  # toca a música / O (-1) é para ela repetir sempre
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain", (255, 128, 0), ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", (255, 128, 0), ((WIN_WIDTH / 2), 105))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Quitting")
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text:str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center = text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)