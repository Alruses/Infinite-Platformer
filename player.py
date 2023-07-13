import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, images):
        self.images = images
        self.image = images['p1_walk11']
        self.rect = self.image.get_rect()
        self.rect.center = pos
        