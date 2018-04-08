from button import *

fps = 60

mainClock = pygame.time.Clock()

pygame.display.set_caption("Anaglink")
Canvas = pygame.display.set_mode((window_width,window_height))#,pygame.FULLSCREEN)


subsurface = Canvas.subsurface((0,0,window_width, (1/5)*window_height))

startimage = pygame.image.load('C:\\Users\\Raouf\\Desktop\\Python Mini project\\Anagram\\Media\\start.jpg')
startimage = pygame.transform.scale( startimage, ( window_width, window_height ) )
startimagerect = startimage.get_rect()
startimagerect.centerx = window_width/2
startimagerect.centery = window_height/2

#allsprites = pygame.sprite.Group()
buttonlist = pygame.sprite.Group()

# Button Plotting

def plotter(lst):
    for i in range(5):
        for j in range(5):
            buttonlist.add( Button( Canvas, int(window_width * (1/20 + j/5)), int(window_height*(1/4 + i*1/5)), lst[j + 5*i]) )

# Timer - 120s

clock = time.time()
ratio = (0.9)/120
def update_timer():
    diff = time.time() - clock
    pygame.draw.rect( subsurface, cyan, ( int(window_width*(1/20)), int(window_height*(15/100)), int(window_width*(0.9)), int(window_width*(1/50))), 2)
    pygame.draw.rect( subsurface, red, ( int(window_width*(1/20)), int(window_height*(15/100)), int(window_width*(0.9) - (diff*ratio*window_width)), int(window_width*(1/50))), 0)
    

Canvas.fill(white)
Canvas.blit(startimage, startimagerect)

pygame.display.flip()

waitforkey()

plotter(anagselec)


while True:

    Canvas.fill(white)
    drawtext("SCORE : ", txtfont1, subsurface, (0.4)*window_width, window_height/25, black)
    drawtext(" X5 ", txtfont2, subsurface, window_width*(3/4), window_height/25, black)
    update_timer()
    buttonlist.update()
    Check_playhover()
    Button.inout.clear()
    
    



    for event in pygame.event.get():
        
        if event.type == QUIT:
            terminate()

        #if event.type == pygame.MOUSEMOTION:

    pygame.display.flip()
        
        

    
