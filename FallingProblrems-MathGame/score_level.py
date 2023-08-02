import pygame

color_score = (72,118,255)#dark blue

class Score():
    def __init__(self):
        super().__init__()

        self.level = 0
        self.score = 1

    def Draw(self,screen):

        font_score = pygame.font.SysFont(pygame.font.get_default_font(),30)
        output_level = "Level:" + str(self.level)
        output_score = "Score:" + str(self.score)
        self.level_surf = font_score.render(output_level,True,color_score)
        self.score_surf = font_score.render(output_score,True, color_score)

        screen.blit(self.score_surf,(400,15))
        screen.blit(self.level_surf,(15,15))


