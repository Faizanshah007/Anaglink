from anagram_generator import *
import pygame
from pygame.locals import *
import sys
import time
import os

#List of Linked words
lnkdlist = pygame.sprite.Group()
#List of buttons
buttonlist = pygame.sprite.Group()

#Initializing Pygame

pygame.init()

#Path

root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


#Anagram Data

anagpool   = Pre_setup.get()
anagselec  = produce()
multiplier = 0


# Window Dimension

window_width = 1000 #max - 1366
window_height = int(window_width*0.5)#max - 768

# Fonts

txtfont1 = pygame.font.SysFont("Courier New", int((1/20)*window_height), True, True)
txtfont2 = pygame.font.SysFont("Harlow Solid", int((1/20)*window_height), False, True)
txtfont3 = pygame.font.SysFont("Copperplate Gothic", int((1/25)*window_height), True, True)

# Colors

white  = (255,255,255)
cyan   = (0, 255, 255)
blue   = (0,0,255)
black  = (0,0,0)
orange = (255, 165, 0)
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

# Answers

ignorelist = list()

def ansGen():
    ans = list()
    sub = list()
    a = list()
    for tp in anagpool:
        sub.clear()
        for wrd in anagselec:
            if(wrd in tp):
                sub.append(wrd)
        a = sub[:]

        if(len(a)==1):
            ignorelist.append(a)

        if(len(a)>1):
            ans.append(a)

    return(ans)

ans = ansGen()



