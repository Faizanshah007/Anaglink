from anagram_generator import *
from pygame.locals import *
import sys, time
import pygame
import os

# "#~" - Variable's value not to be changed


if "Data.py" not in sys.modules :

    # Game Status

    stat = 'None'
    

    # Timer

    timer = 0


    # List of Linked words

    lnkdlist = pygame.sprite.Group()

    # List of buttons

    buttonlist = pygame.sprite.Group()



    # Initializing Pygame

    pygame.init()


    #~Path

    root_dir = os.path.join(os.path.dirname(sys.argv[0]), 'Media') 


    #~Anagram Data

    anagpool   = Pre_setup.get()
    anagselec  = produce()


    #~Window Dimension

    window_width = 1000 #max - 1366
    window_height = int(window_width*0.5)#max - 768


    #~Fonts

    font_dir = os.path.join(os.path.dirname(sys.argv[0]), 'Fonts')
    txtfont1 = pygame.font.Font(os.path.join(font_dir, "Courier New", "COURBI.TTF"), int((1/13)*window_height))
    txtfont2 = pygame.font.Font(os.path.join(font_dir, "Copperplate Gothic", "COPRGTB.TTF"), int((1/25)*window_height))


    #~Colors

    white  = (255,255,255)
    cyan   = (0, 255, 255)
    blue   = (0,0,255)
    black  = (0,0,0)
    orange = (255, 165, 0)
    green  = (0,255,0)
    red    = (255,0,0)
    yellow = (255,255,0)
    purple = (160,32,240)


    # Wait function

    def waitforkey():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type ==  pygame.MOUSEBUTTONUP:
                    return
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

    ignorelist = list() #Stores words which have 0 possible anaglink

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

    ans = ansGen() #Contains all the anaglinks
    ans_copy = ans[:] #~


    # Result

    Score = 0
    TimeBonus = 0


    # Bringing window to foreground

    #CODE IMPORTED FROM:
    #https://www.blog.pythonlibrary.org/2014/10/20/pywin32-how-to-bring-a-window-to-front/'''

    import win32gui, win32com.client

    def foregroundWindow(name):

        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
     
        def windowEnumerationHandler(hwnd, top_windows):
            top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
         
        top_windows = []
        win32gui.EnumWindows(windowEnumerationHandler, top_windows)
        for i in top_windows:
            if name.lower() in i[1].lower():
                win32gui.ShowWindow(i[0],5)
                win32gui.SetForegroundWindow(i[0])
                break
