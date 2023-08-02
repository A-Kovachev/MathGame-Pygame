import pygame

color_background = (191,239,255) #light blue
color_text = (153,153,153)#gray

class StartScreen():
    def __init__(self):
        super().__init__()

        self.backgroud = pygame.Surface((490,700))
        self.backgroud.fill(color_background)
        self.backgroud_rect = self.backgroud.get_rect(topleft=(0,0))

        self.font_txt = pygame.font.SysFont("Helvetica",50)
        self.text_surf = self.font_txt.render("Click anywhere to start",True,color_text)
        self.text_rect = self.text_surf.get_rect(topleft=(35,250))

    def Draw(self, screen):
        screen.blit(self.backgroud,self.backgroud_rect)
        screen.blit(self.text_surf,self.text_rect)
        
        mouse_pos = pygame.mouse.get_pos()
        if self.backgroud_rect.collidepoint(mouse_pos) and\
            pygame.mouse.get_pressed()[0] == 1:
            return True
        else:
            return False







