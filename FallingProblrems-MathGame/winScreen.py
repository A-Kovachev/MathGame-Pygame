import pygame

color_back = (255,125,64)
color_shadow = (205,16,118)
color_button_txt = (5,5,5)

class WinScreen():
    def __init__(self):
        super().__init__()

        self.scr_surf = pygame.Surface((490,700))
        self.scr_surf.fill((151,255,255))

        self.font_back = pygame.font.SysFont("Albertus",110,bold=True,italic=True)
        self.surf = self.font_back.render("V i c t o r y !",True,color_back,)
        self.rect = self.surf.get_rect(topleft=(20,150))
        self.font_back = pygame.font.SysFont("Albertus",110,bold=True,italic=True)
        self.surf_1 = self.font_back.render("V i c t o r y !",True,color_shadow)
        self.rect_1 = self.surf.get_rect(topleft=(20,150))

        self.txt_font = pygame.font.SysFont("Helvetica",100)
        self.playAgain_surf = self.txt_font.render("Play Again",True,color_button_txt)
        self.playAgain_rect = self.playAgain_surf.get_rect(topleft=(100,300))

        self.exit_surf = self.txt_font.render(" Exit ",True,color_button_txt)
        self.exit_rect = self.exit_surf.get_rect(topleft = (100,530))

    def Draw(self,screen):
        #display vcitory
        screen.blit(self.scr_surf,(0,0))
        screen.blit(self.surf_1,(self.rect.left+7,self.rect.top+8,self.rect.width,self.rect.height))
        screen.blit(self.surf,self.rect)

        #buttons
        









