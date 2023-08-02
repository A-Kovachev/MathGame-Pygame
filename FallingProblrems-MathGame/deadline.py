import pygame

color_deadline = (220,20,60)

class Deadline():
    def __init__(self):
        super().__init__()

        self.deadline_surf = pygame.Surface((500,10))
        self.deadline_surf.fill(color_deadline)
        self.deadline_rect = self.deadline_surf.get_rect(topleft=(0,550))

    def Draw(self, screen):
        screen.blit(self.deadline_surf,self.deadline_rect)
