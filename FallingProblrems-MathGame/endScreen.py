import pygame

color_button_txt = (5,5,5)#black
color_button_background = (255,193,37)#orange
color_bg_onClick = (255,153,18)#brownish
color_border = (255,69,0)#brown
clicked = False

class EndScreen():
    def __init__(self):
        super().__init__()

        self.backgroud = pygame.Surface((490,700))
        self.backgroud.fill((0,191,255))
        self.font_txt = pygame.font.SysFont("Helvetica",100)

        self.exit_surf = self.font_txt.render(" Exit ",True,color_button_txt)
        self.exit_rect = self.exit_surf.get_rect(topleft = (150,530))

        self.retry_surf = self.font_txt.render(" Retry ",True,color_button_txt)
        self.retry_rect = self.retry_surf.get_rect(topleft = (120,380))

        self.game_over_font = pygame.font.SysFont("John Hubbard",120)
        self.gameOver_surf = self.game_over_font.render("Game Over",True,(255,0,0))
        self.game_over_rect = self.gameOver_surf.get_rect(topleft=(15,55))

    def Draw(self,screen, level, score):
        screen.blit(self.backgroud,(0,0))
        screen.blit(self.gameOver_surf,self.game_over_rect)
        #display final score and level 
        font_score = pygame.font.SysFont("Helvetica",80,bold=True)
        if level < 0: level = 0
        level = "Level: "+str(level)
        if score < 0: score = 0
        score = "Score: "+str(score)
        score_surf = font_score.render(score,True,color_button_txt)
        score_rect = score_surf.get_rect(topleft=(115,260))
        lvl_surf = font_score.render(level,True,color_button_txt)
        lvl_rect = lvl_surf.get_rect(topleft=(125,180))
        screen.blit(lvl_surf,lvl_rect)
        screen.blit(score_surf,score_rect)
        #changes background colors while hovering
        pygame.draw.rect(screen,color_border,(self.retry_rect.left-10,self.retry_rect.top-10,self.retry_rect.width+20,self.retry_rect.height+20),border_radius=5)
        if self.retry_rect.collidepoint(pygame.mouse.get_pos()): color_button_background = color_bg_onClick
        else: color_button_background = (255,193,37)
        pygame.draw.rect(screen,color_button_background,self.retry_rect,border_radius=5)
        
        pygame.draw.rect(screen,color_border,(self.exit_rect.left-10,self.exit_rect.top-10,self.exit_rect.width+20,self.exit_rect.height+20),border_radius=5)
        if self.exit_rect.collidepoint(pygame.mouse.get_pos()): color_button_background = color_bg_onClick
        else: color_button_background = (255,193,37)
        pygame.draw.rect(screen,color_button_background,self.exit_rect,border_radius=5)
        
        screen.blit(self.retry_surf,self.retry_rect)
        screen.blit(self.exit_surf,self.exit_rect)

        
 