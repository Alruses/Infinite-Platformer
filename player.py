import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, images):
        self.images = images
        self.image = images['p1_walk11']
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.facing = "R"
        self.speed = pygame.math.Vector2(0,0) #remember speed[0] is x speed and speed[1] is y speed
    
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
    def jump():
        #don't worry about being on a platform at the moment, just make the code for jumping


#to-do: add l/r movement to left and right functions
#move_ip function in update
#include gravity somewhere
#make jump function move us upwards