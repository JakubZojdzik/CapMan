from io import SEEK_CUR
from numpy import diff
import pygame
import sys
import os
from pygame.locals import *
from win import Win
from data import Data

class Settings:
    difficulty = 1
    volume = 0.25
    title = pygame.image.load("../assets/menu/capmantitle.png")
    mutepicture=pygame.image.load("../assets/menu/mutepac.png")
    loudpicture=pygame.image.load("../assets/menu/soundpac.png")
    hardcolor=pygame.image.load("../assets/menu/hardcolor.png")
    hardfaded=pygame.image.load("../assets/menu/hardfaded.png")
    essacolor=pygame.image.load("../assets/menu/essacolor.png")
    essafaded=pygame.image.load("../assets/menu/fadedessa.png")
    mediumcolor = pygame.image.load("../assets/menu/mediumcolor.png")
    mediumfaded = pygame.image.load("../assets/menu/mediumfaded.png")
    comeback = pygame.image.load("../assets/ingame_textures/map/yellowarrow.png")
    
    @staticmethod
    def set_volume(volume, sounds = [], save=False):
        Settings.volume = volume
        if not sounds is None:
            pygame.mixer.music.set_volume(Settings.volume)
        else:
            sounds = []
        for sound in sounds:
            sound.set_volume(volume)
        
        if save:
            Settings.save_settings()

    @staticmethod
    def settings(sounds=[]):
        screen_info = pygame.display.Info()
        width = screen_info.current_w//3
        height = screen_info.current_h//6
        ICON_SIZE = (screen_info.current_h - 365) // 4 + 70
        Settings.comeback = pygame.transform.scale(Settings.comeback, [ICON_SIZE // 2, ICON_SIZE // 2])
        margin_top = screen_info.current_h/3
        margin_left = int((screen_info.current_w - width) / 2)
        margin_down = int((screen_info.current_h *(2/3)))
        Settings.title = pygame.transform.scale(Settings.title, [int(((7/8) *margin_top)*2.4), int((7/8) *margin_top)])
        Settings.mutepicture= pygame.transform.scale(Settings.mutepicture,[height ,height] )
        Settings.loudpicture= pygame.transform.scale(Settings.loudpicture,[height ,height])
        LEVEL_ICON_SIZE=(width+2*height)//4
        Settings.hardcolor = pygame.transform.scale(Settings.hardcolor, [LEVEL_ICON_SIZE, LEVEL_ICON_SIZE])
        Settings.hardfaded = pygame.transform.scale(Settings.hardfaded, [LEVEL_ICON_SIZE, LEVEL_ICON_SIZE])
        Settings.essacolor = pygame.transform.scale(Settings.essacolor, [LEVEL_ICON_SIZE, LEVEL_ICON_SIZE])
        Settings.essafaded = pygame.transform.scale(Settings.essafaded, [LEVEL_ICON_SIZE, LEVEL_ICON_SIZE] )
        Settings.mediumcolor = pygame.transform.scale(Settings.mediumcolor, [LEVEL_ICON_SIZE, LEVEL_ICON_SIZE])
        Settings.mediumfaded = pygame.transform.scale(Settings.mediumfaded, [LEVEL_ICON_SIZE, LEVEL_ICON_SIZE])

        blackColor = pygame.Color(0, 0, 0)
        yellowColor = pygame.Color(255, 255, 0)
        Win.screen.fill(Win.BGCOLOR)
        Win.screen.blit(Settings.title, (((screen_info.current_w - ((margin_top-20)*2.4)) / 2), 0))
        Win.screen.blit(Settings.mutepicture, (margin_left-height+1, margin_top))
        Win.screen.blit(Settings.loudpicture, (margin_left+width, margin_top))

        # starting volume
        x = margin_left+width*Settings.volume
        pygame.draw.rect(Win.screen, yellowColor, Rect(margin_left, margin_top, width, height))
        pygame.draw.rect(Win.screen, blackColor, Rect(x, margin_top + 5, width/40, height-10))
        Win.screen.blit(Settings.comeback, (0,0))
        pygame.display.update()
        a = x
        difficulty_displayed = -1
        while True:
            if Settings.difficulty != difficulty_displayed:
                if (Settings.difficulty == 0):
                    Win.screen.blit(Settings.essacolor, (margin_left - height + 1, margin_down))
                    Win.screen.blit(Settings.hardfaded, (margin_left + width + height - LEVEL_ICON_SIZE, margin_down))
                    Win.screen.blit(Settings.mediumfaded, (margin_left+(width-LEVEL_ICON_SIZE)//2, margin_down))
                if(Settings.difficulty == 1):
                    Win.screen.blit(Settings.essafaded, (margin_left-height+1, margin_down))
                    Win.screen.blit(Settings.hardfaded, (margin_left+width+height-LEVEL_ICON_SIZE, margin_down))
                    Win.screen.blit(Settings.mediumcolor, (margin_left + (width - LEVEL_ICON_SIZE) // 2, margin_down))
                if (Settings.difficulty == 2):
                    Win.screen.blit(Settings.hardcolor, (margin_left+width+height-LEVEL_ICON_SIZE, margin_down))
                    Win.screen.blit(Settings.essafaded, (margin_left-height+1, margin_down))
                    Win.screen.blit(Settings.mediumfaded, (margin_left + (width - LEVEL_ICON_SIZE) // 2, margin_down))
                difficulty_displayed = Settings.difficulty
                pygame.display.update()

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
                    Settings.set_volume((a - margin_left) / width, sounds)
                    pygame.draw.rect(Win.screen, yellowColor, Rect(
                        margin_left, margin_top, width, height))
                    pygame.draw.rect(Win.screen, blackColor, Rect(
                        a, margin_top + 5, width / 40, height - 10))
                    pygame.display.update()

                if y>margin_down and (x>margin_left-height+1 and x<margin_left-height+1+LEVEL_ICON_SIZE):
                    Settings.difficulty=0
                if y>margin_down and (x>margin_left + (width - LEVEL_ICON_SIZE) // 2 and x<margin_left + (width - LEVEL_ICON_SIZE) // 2+LEVEL_ICON_SIZE):
                    Settings.difficulty=1
                if y>margin_down and (x>margin_left + width + height - LEVEL_ICON_SIZE and x<margin_left + width + height):
                    Settings.difficulty=2

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if pos[0]<ICON_SIZE and pos[1]<ICON_SIZE:
                        Settings.save_settings()
                        return (Settings.volume, Settings.difficulty)
                if event.type == QUIT:
                    Settings.save_settings()
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == ord('q') or event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER or event.key == ord('p'):
                        Settings.save_settings()
                        return (Settings.volume, Settings.difficulty)
    
    @staticmethod
    def create_settings_file():
        Data.create_file('settings.txt', '0.25\n1')

    @staticmethod
    def load_settings():
        settings = Data.read_from_file('settings.txt').split()
        Settings.volume = float(settings[0])
        Settings.difficulty = int(settings[1])
        Settings.set_volume(Settings.volume, None)
        return Settings.volume, Settings.difficulty

    @staticmethod
    def save_settings():
        Data.write_to_file('settings.txt', str(Settings.volume)+'\n'+str(Settings.difficulty))

Settings.create_settings_file()
Settings.load_settings()