import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, pos, path):
        super().__init__()
        self.width = 70
        self.height = 40

        #another new function to mess with size
        self.image = pygame.Surface([self.width, self.height]).convert()
        self.image.blit(pygame.image.load(path).convert(), (0,0), (0,0,self.width, self.height))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    #how do we scroll our platforms?
    #what makes a new platform appear?
    def scroll(self, change):
        self.rect.top += change
        #we probably want to check if we should be making new platforms each time we do this