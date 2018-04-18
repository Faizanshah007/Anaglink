from button import *
#fps = 60
stat = 'None'

#mainClock = pygame.time.Clock()

pygame.display.set_caption("Anaglink")
Canvas = pygame.display.set_mode((window_width,window_height))#,pygame.FULLSCREEN)pygame.HWSURFACE)


subsurface = Canvas.subsurface((0,0,window_width, (1/5)*window_height))

pygame.mixer.music.load(os.path.join(root_dir, "Anagram", "Media", "main.wav"))

loosemusic = pygame.mixer.Sound(os.path.join(root_dir, "Anagram", "Media", "game_over.wav"))
winmusic = pygame.mixer.Sound(os.path.join(root_dir, "Anagram", "Media", "winner.wav"))
linkedmusic = pygame.mixer.Sound(os.path.join(root_dir, "Anagram", "Media", "anaglinked.wav"))
incorrectmusic = pygame.mixer.Sound(os.path.join(root_dir, "Anagram", "Media", "incorrect.wav"))
fewsecsound = pygame.mixer.Sound(os.path.join(root_dir, "Anagram", "Media", "fewsecleft.wav"))

startimage = pygame.image.load(os.path.join(root_dir, "Anagram", "Media", "start.jpg"))
startimage = pygame.transform.scale( startimage, ( window_width, window_height ) )
startimagerect = startimage.get_rect()
startimagerect.centerx = window_width/2
startimagerect.centery = window_height/2

lostimage = pygame.image.load(os.path.join(root_dir, "Anagram", "Media", "lost.jpg"))
lostimage = pygame.transform.scale( lostimage, ( window_width, window_height ) )
lostimagerect = startimage.get_rect()
lostimagerect.centerx = window_width/2
lostimagerect.centery = window_height/2

wonimage = pygame.image.load(os.path.join(root_dir, "Anagram", "Media", "won.jpg"))
wonimage = pygame.transform.scale( wonimage, ( window_width, window_height ) )
wonimagerect = startimage.get_rect()
wonimagerect.centerx = window_width/2
wonimagerect.centery = window_height/2

# Button Plotting

def plotter(lst):
    for i in range(5):
        for j in range(5):
            buttonlist.add( Button( Canvas, int(window_width * (1/20 + j/5)), int(window_height*(1/4 + i*1/7)), lst[j + 5*i]) )

# Timer - 120s

ratio = (0.9)/120

def update_timer():
    global clock
    diff = time.time() - clock
    pygame.draw.rect( subsurface, cyan, ( int(window_width*(1/20)), int(window_height*(15/100)), int(window_width*(0.9)), int(window_width*(1/50))), 2)
    return( pygame.draw.rect( subsurface, red, ( int(window_width*(1/20)), int(window_height*(15/100)), int(window_width*(0.9) - (diff*ratio*window_width)), int(window_width*(1/50))), 0) )
    

Canvas.fill(white)
Canvas.blit(startimage, startimagerect)

pygame.display.flip()

waitforkey()

clock = time.time()

plotter(anagselec)

lnkdlist.empty()

print(ans)
print(ignorelist)

pygame.mixer.music.play(-1,0.0)


while True:
    
    Canvas.fill(black)
    drawtext("SCORE : 12150", txtfont1, subsurface, (0.4)*window_width, window_height/25, white)
    drawtext(" X5 ", txtfont2, subsurface, window_width*(3/4), window_height/30, white)
    a = update_timer().width
    if( a == 1 ):
        fewsecsound.stop()
        stat = 'Lost'
        break
    
    if( a == 100 ):
        fewsecsound.play(-1)
        
    if( ans == [] ):
        stat = 'Won'
        break
    Button.pointing = 0
    buttonlist.update()
    Check_playhover()
    Button.inout.clear()
    clicked()
    if(check_lnk()):
        linkedmusic.play()
        buttonlist.remove(lnkdlist)
        lnkdlist.empty()
    elif(check_lnk() == False):
        incorrectmusic.play()
        for l in lnkdlist:
            l.active = False
            l.wrong = True
            lnkdlist.empty()


    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                terminate()
        if event.type == QUIT :
            terminate()

        #if event.type == pygame.MOUSEMOTION:

    pygame.display.flip()

pygame.mixer.music.stop()

if( stat == 'Lost' ):
    loosemusic.play()
    Canvas.blit(lostimage, lostimagerect)
if( stat == 'Won' ):
    winmusic.play()
    Canvas.blit(wonimage, wonimagerect)
pygame.display.flip()

waitforkey()

time.sleep(1)
    
terminate()
    
