import pygame
import sys
from pygame.locals import *
from win import Win

class Settings:


    def __init__(self):
        self.difficulty = 1

        self.title = pygame.image.load("../lib/capmantitle.png")
        self.position = 0.1
        self.mutepicture=pygame.image.load("../lib/mutepac.png")
        self.loudpicture=pygame.image.load("../lib/soundpac.png")

        self.hardcolor=pygame.image.load("../lib/hardcolor.png")
        self.hardfaded=pygame.image.load("../lib/hardfaded.png")

        self.essacolor=pygame.image.load("../lib/essacolor.png")
        self.essafaded=pygame.image.load("../lib/fadedessa.png")

    def sound(self):
        pygame.init()
        screen_info = pygame.display.Info()
        screen = pygame.display.set_mode(
            (screen_info.current_w, screen_info.current_h), pygame.FULLSCREEN)
        width = screen_info.current_w/3
        height = screen_info.current_h/6

        margin_top = screen_info.current_h/3
        margin_left = int((screen_info.current_w - width) / 2)
        margin_down = int((screen_info.current_h *(2/3))) #to działa tak jakby od góry stąd 2/3
        self.title = pygame.transform.scale(self.title, [int(((7/8) *margin_top)*2.4), int((7/8) *margin_top)])
        self.mutepicture= pygame.transform.scale(self.mutepicture,[height ,height] )
        self.loudpicture= pygame.transform.scale(self.loudpicture,[height ,height])
        LEVEL_ICON_SIZE=screen_info.current_h/3
        self.hardcolor = pygame.transform.scale(self.hardcolor, [LEVEL_ICON_SIZE, LEVEL_ICON_SIZE])
        self.hardfaded = pygame.transform.scale(self.hardfaded, [LEVEL_ICON_SIZE, LEVEL_ICON_SIZE])

        self.essacolor = pygame.transform.scale(self.essacolor, [LEVEL_ICON_SIZE, LEVEL_ICON_SIZE])
        self.essafaded= pygame.transform.scale(self.essafaded,[LEVEL_ICON_SIZE, LEVEL_ICON_SIZE] )

        blackColor = pygame.Color(0, 0, 0)
        yellowColor = pygame.Color(255, 255, 0)
        screen.fill(Win.BGCOLOR)
        screen.blit(self.title, (((screen_info.current_w - ((margin_top-20)*2.4)) / 2), 0))
        screen.blit(self.mutepicture, (margin_left-height+1, margin_top))
        screen.blit(self.loudpicture, (margin_left+width, margin_top))
        # starting position
        x = margin_left+width*self.position
        pygame.draw.rect(screen, yellowColor, Rect(margin_left, margin_top, width, height))
        pygame.draw.rect(screen, blackColor, Rect(x, margin_top + 5, width/40, height-10))
        if(self.difficulty==1):
            screen.blit(self.essacolor, (margin_left-height+1, margin_down))
            screen.blit(self.hardfaded, (margin_left+width+height-LEVEL_ICON_SIZE, margin_down))
        else:
            screen.blit(self.hardcolor, (margin_left+width+height-LEVEL_ICON_SIZE, margin_down))
            screen.blit(self.essafaded, (margin_left-height+1, margin_down))

        pygame.display.update()

        a = x
        while True:
            button = pygame.mouse.get_pressed()
            if button[0] != 0:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]

                if y>margin_top and y<margin_top+height:
                    a = x - 5

                    if a < margin_left:
                        a = margin_left
                    if a > margin_left + width - width / 40:
                        a = margin_left + width - width / 40
                    pygame.draw.rect(screen, yellowColor, Rect(
                        margin_left, margin_top, width, height))
                    # pygame.display.update(pygame.Rect(0,0,width,height))
                    pygame.draw.rect(screen, blackColor, Rect(
                        a, margin_top + 5, width / 40, height - 10))
                    pygame.display.update()

                if y>margin_down and (x>margin_left-height+1 and x<margin_left-height+1+LEVEL_ICON_SIZE):
                    self.difficulty=1
                    screen.blit(self.essacolor, (margin_left - height + 1, margin_down))
                    screen.blit(self.hardfaded, (margin_left + width + height - LEVEL_ICON_SIZE, margin_down))
                    pygame.display.update()
                if y>margin_down and (x>margin_left + width + height - LEVEL_ICON_SIZE and x<margin_left + width + height):
                    self.difficulty=2
                    screen.blit(self.hardcolor, (margin_left + width + height - LEVEL_ICON_SIZE, margin_down))
                    screen.blit(self.essafaded, (margin_left - height + 1, margin_down))
                    pygame.display.update()



            # check for ESC key pressed, or pygame window closed, to quit
            for event in pygame.event.get():
                if event.type == QUIT:

                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:  # wraca do menu głównego
                        self.position = (a - margin_left) / width
                        return ((a - margin_left) / width, self.difficulty)
