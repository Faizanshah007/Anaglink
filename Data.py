import anagram_generator
import Pre_setup
import pygame
from pygame.locals import *
import sys
import time

#Initializing Pygame

pygame.init()


#Anagram Data

anagpool   = Pre_setup.get()
anagselec  = anagram_generator.produce()
multiplier = 0


# Window Dimension

window_width = 1000 #max - 1366
window_height = int(window_width*0.5)#max - 768

# Fonts

txtfont1 = pygame.font.SysFont("Copperplate Gothic", int((3/140)*window_height), True, True)
txtfont2 = pygame.font.SysFont("Copperplate Gothic", int((1/14)*window_height), True, True)

# Colors

white  = (255,255,255)
cyan   = (0, 255, 255)
blue   = (0,0,255)
black  = (0,0,0)
green  = (0,255,0)
red    = (255,0,0)
yellow = (255,255,0)

# Wait function

def waitforkey():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                return

# Terminate

def terminate():
    pygame.quit()
    sys.exit()

# Render Text

def drawtext(text,font,surface,x,y,colour = black):
    textobj = font.render(text,1,colour)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)


