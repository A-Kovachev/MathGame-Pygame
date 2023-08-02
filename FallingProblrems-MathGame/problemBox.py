import pygame

color_problem = (41,36,33)
color_pbox_borders = (238,118,0)
color_pbox_inside = (244,164,96)

class Problem():
    def __init__(self,pos_x,pos_y,problem_txt):
        super().__init__()

        font_problem = pygame.font.SysFont(pygame.font.get_default_font(),100)
        self.inside_surf = font_problem.render(problem_txt,True,color_problem)
        self.rect = self.inside_surf.get_rect(topleft=(pos_x,pos_y))
        self.rect_border = pygame.Rect(pos_x-5,pos_y-5,self.rect.width+10,self.rect.height+10)
        
    def Draw(self,screen,speed):
        self.rect.bottom += speed
        self.rect_border.topleft = (self.rect.left-5,self.rect.top-5)
        pygame.draw.rect(screen,color_pbox_borders,self.rect_border,border_radius=9)
        pygame.draw.rect(screen,color_pbox_inside,self.rect,border_radius=7)
        screen.blit(self.inside_surf,self.rect)
        
