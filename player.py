import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, images):
        self.images = images
        self.image = images['p1_walk11']
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.facing = "R"

    def update(self):
        #what do we need to update?
        self.image = self.images['p1_walk11']

        #facing different directions - we only need to change it if he's facing left because the images are facing right by default
        #couple of functions to change the value of facing
        if self.facing == "L":
            self.image = pygame.transform.flip(self.image, True, False)

    def left(self):
        self.facing = "L"
    def right(self):
        self.facing = "R"