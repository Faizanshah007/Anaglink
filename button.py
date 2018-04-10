from Data import *
bwidth  = 136
bheight = int(bwidth*19/68)
hoversound = pygame.mixer.Sound('C:\\Users\\Raouf\\Desktop\\Python Mini project\\Anagram\\Media\\hover.wav')
clicksound = pygame.mixer.Sound('C:\\Users\\Raouf\\Desktop\\Python Mini project\\Anagram\\Media\\click.wav')

class Button(pygame.sprite.Sprite):

    cntr  = 0
    inout = []
    sound = False
    pointing = 0


    def __init__(self, surface, x, y, wrd):
        global bwidth, bheight
        pygame.sprite.Sprite.__init__(self)
        Button.surface = surface
        #self.image = pygame.Surface((bwidth, bheight)).convert()
        self.rect = pygame.Rect(x, y, bwidth, bheight)
        self.active = False
        self.gid = 0
        self.value = wrd
        

    def checkmouseloc(self, loc):
        
        if(loc[0] >= self.rect.left and loc[0] <= self.rect.right and loc[1] >= self.rect.top and loc[1] <= self.rect.bottom):
            Button.inout.append(1)
            Button.pointing = self
            return True
        else:
            Button.inout.append(0)
            
            

    def clicked(self, loc):

        self.temp = pygame.event.Event(pygame.NOEVENT)
        if(loc[0] >= self.rect.left and loc[0] <= self.rect.right and loc[1] >= self.rect.top and loc[1] <= self.rect.bottom):
            for event in pygame.event.get():
                if( event.type == pygame.MOUSEBUTTONUP or event.type == self.temp.type):
                    clicksound.play()
                    if( not self.active ):
                        self.active = True
                    else:
                        self.active = False
                self.temp = event

    def update(self):

        pygame.draw.rect( Button.surface, cyan, self.rect, 2)
        self.clicked(pygame.mouse.get_pos())
        if( self.active == True ):
            pygame.draw.rect( Button.surface, orange, self.rect, 0)
            pygame.draw.rect( Button.surface, orange, self.rect, 5)
        drawtext( self.value, txtfont3, Button.surface, int(self.rect.left + window_width*1/200), self.rect.top, green )
        self.checkmouseloc(pygame.mouse.get_pos())
        

def Check_playhover():
    if(Button.pointing != 0):
        pygame.draw.rect( Button.surface, cyan, Button.pointing.rect, 5)
    if(1 in Button.inout and Button.sound == False):
        hoversound.play()
        Button.sound = True
    elif(1 not in Button.inout):
        Button.sound = False      
