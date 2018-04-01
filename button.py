import pygame


white  = (255,255,255)
cyan   = (0, 255, 255)
blue   = (0,0,255)
black  = (0,0,0)
green  = (0,255,0)
red    = (255,0,0)
yellow = (255,255,0)

bwidth =
bheight =

class button(pygame.sprite.Sprite):

    def __init__(self, surface, x, y, wrd):

        self.rect = pygame.draw.rect(Surface, cyan, (x, y, bwidth, bheight), 2)
        self.active = False
        self.gid = 0
        
        
