import sys, pygame, random
from pygame.locals import *
from platform import *

pygame.init()
screen_info = pygame.display.Info()
# set the width and height to the size of the screen
size = (width, height) = (screen_info.current_w,screen_info.current_h)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (255, 224, 179)

sprite_list = pygame.sprite.Group()
platforms = pygame.sprite.Group()

player_sprites = {}

def init():
    #make a for loop to instantiate a few platforms
    #for the path, make sure its "images/grassPlat.png"
    for i in range(height // 100):
        for j in range(width // 420):
            plat = Platform((random.randint(35, (width - 50) // 10) * 10, 120 * i), 'images/grassPlat.png')
            platforms.add(plat)


def main():
    game_over = False
    init()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_f:
                    pygame.display.set_mode(size, FULLSCREEN)
                if event.key == K_ESCAPE:
                    pygame.display.set_mode(size)
        screen.fill(color)
        platforms.draw(screen)
        sprite_list.draw(screen)
        pygame.display.flip()
        
if __name__ == "__main__":
    main()


#constantly ascending
#randomly generating platforms that we jump on to ascend
    #make a maximum distance away from previous platform next plat can gernerate
#do we want to jump manually or are we always automically jumping?
#spring platforms?
#new platforms??

#start button - pause?