import pygame

color_button_txt = (5,5,5)
color_button_background = (255,193,37)
color_bg_onClick = (255,153,18)

class Button():
    def __init__(self,pos_x,answer_txt):
        super().__init__()

        font_size = 150
        txt_length = len(answer_txt)
        self.num_posx = pos_x + 15
        self.num_posy = 585
        #centering the text in the buttons depending on the length
        if txt_length == 1:
            self.num_posx += 33
        elif txt_length == 3:
            font_size = 100
            self.num_posy = 600
        elif txt_length == 4:
            font_size = 70
            self.num_posy = 610
        elif txt_length == 5:
            font_size = 50
            self.num_posx += 10
            self.num_posy = 615
        elif txt_length == 6:
            font_size = 50
            self.num_posy = 615
            
        font_problem = pygame.font.SysFont(pygame.font.get_default_font(),font_size)
        self.surf = font_problem.render(answer_txt,True,color_button_txt)
        self.rect = pygame.rect.Rect(pos_x,570,150,120)

    def Draw(self,screen):
        #if the mouse if hovering over the button the background changes
        mouse_pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen,color_bg_onClick,self.rect,border_radius=5)
        else:
            pygame.draw.rect(screen,color_button_background,self.rect,border_radius=5)

        screen.blit(self.surf,(self.num_posx,self.num_posy))

        

