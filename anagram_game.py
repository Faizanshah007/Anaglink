import pygame

fps = 60

window_width = #max - 1366
window_height = #max - 768

white  = (255,255,255)
cyan   = (0, 255, 255)
blue   = (0,0,255)
black  = (0,0,0)
green  = (0,255,0)
red    = (255,0,0)
yellow = (255,255,0)

mainClock = pygame.time.Clock()

pygame.display.set_caption("Anaglink")
Canvas = pygame.display.set_mode((window_width,window_height))#,pygame.FULLSCREEN)



txtfont = pygame.font.SysFont("Copperplate Gothic", int((3/140)*window_height), True, True)

subsurface = Canvas.subsurface((0,0,window_width, (3/28)*window_height))

Canvas.fill(black)
#startimage

allsprites = pygame.sprite.Group()

#while True:

    
