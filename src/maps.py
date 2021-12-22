import pygame
from win import Win
from highscore import Highscore
from settings import Settings

pygame.init()
font = pygame.font.Font("../lib/fonts/VT323/VT323-Regular.ttf", 48)
screen_info = pygame.display.Info()
ICON_SIZE = (screen_info.current_h - 365) // 4 + 70
lock_img = pygame.transform.scale(pygame.image.load("../lib/menu/maps/lock.png"), [ICON_SIZE, ICON_SIZE])
map1 = pygame.transform.scale(pygame.image.load("../lib/menu/maps/map1.png"), [ICON_SIZE, ICON_SIZE])
map2 = pygame.transform.scale(pygame.image.load("../lib/menu/maps/map2.png"), [ICON_SIZE, ICON_SIZE])
map3 = pygame.transform.scale(pygame.image.load("../lib/menu/maps/map3.png"), [ICON_SIZE, ICON_SIZE])
map4 = pygame.transform.scale(pygame.image.load("../lib/menu/maps/map4.png"), [ICON_SIZE, ICON_SIZE])
map5 = pygame.transform.scale(pygame.image.load("../lib/menu/maps/map5.png"), [ICON_SIZE, ICON_SIZE])
map6 = pygame.transform.scale(pygame.image.load("../lib/menu/maps/map6.png"), [ICON_SIZE, ICON_SIZE])
map7 = pygame.transform.scale(pygame.image.load("../lib/menu/maps/map7.png"), [ICON_SIZE, ICON_SIZE])
map8 = pygame.transform.scale(pygame.image.load("../lib/menu/maps/map8.png"), [ICON_SIZE, ICON_SIZE])

class Bigmap:
    def __init__(self):
        self.maps = [map1, map2, map3, map4, map5, map6, map7, map8]
        self.title = pygame.image.load("../lib/menu/capmantitle.png")
        self.title = pygame.transform.rotozoom(self.title, 0, 0.35)
        self.comeback=pygame.image.load("../lib/ingame_textures/map/yellowarrow.png")
        self.comeback = pygame.transform.scale(self.comeback, [ICON_SIZE//2,ICON_SIZE//2])
        self.locked = [False, True, True, True, True, True, True, True, True]

    def drawmaps(self, screen):
        run = True
        for i in range(1, 8):
            if(Highscore.load_highscore(i, Settings.difficulty) != '-1'):
                self.locked[i] = False
            else:
                break

        while run:
            screen.fill(Win.BGCOLOR)
            
            d = int((screen_info.current_w - 4*ICON_SIZE) / 5)
            e = screen_info.current_h // 3 - 50
            screen.blit(self.title, (int((screen_info.current_w - 365) / 2),0))
            screen.blit(self.comeback, (0, 0))

            for i in range(4):
                score_img = font.render("Lvl: " + str(i+1), True, (0, 255, 255))
                score_rect = score_img.get_rect(center=((i+1) * d + ICON_SIZE * i + ICON_SIZE // 2, e - 30))
                screen.blit(score_img, score_rect)
                screen.blit(self.maps[i], ((i+1) * d + ICON_SIZE * i, e))
                if(self.locked[i]):
                    screen.blit(lock_img, ((i+1) * d + ICON_SIZE * i, e))
                score_img = font.render("Highscore: " + str(Highscore.load_highscore(i+1, Settings.difficulty)), True, (0, 255, 255))
                if(Highscore.load_highscore(i+1, Settings.difficulty) == "-1"):
                    score_img = font.render("Highscore: ?", True, (0, 255, 255))
                score_rect = score_img.get_rect(center=((i+1) * d + ICON_SIZE * i + ICON_SIZE // 2, e + ICON_SIZE + 25))
                screen.blit(score_img, score_rect)

            e2 = e + screen_info.current_h - (ICON_SIZE + 60) - screen_info.current_h // 3.2
            for i in range(4):
                score_img = font.render("Lvl: " + str(i+5), True, (0, 255, 255))
                score_rect = score_img.get_rect(center=((i+1) * d + ICON_SIZE * i + ICON_SIZE // 2, e2 - 30))
                screen.blit(score_img, score_rect)
                screen.blit(self.maps[i+4], ((i+1) * d + ICON_SIZE * i, e2))
                if(self.locked[i+4]):
                    screen.blit(lock_img, ((i+1) * d + ICON_SIZE * i, e2))
                score_img = font.render("Highscore: " + str(Highscore.load_highscore(i+5, Settings.difficulty)), True, (0, 255, 255))
                if(str(Highscore.load_highscore(i+5, Settings.difficulty)) == '-1'):
                    score_img = font.render("Highscore: ?", True, (0, 255, 255))
                score_rect = score_img.get_rect(center=((i+1) * d + ICON_SIZE * i + ICON_SIZE // 2, e2 + ICON_SIZE + 25))
                screen.blit(score_img, score_rect)

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # zakończenie
                    pygame.quit()
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == ord('q'):
                        run = False
                    if event.key == pygame.K_LEFT: #wraca do menu głównego
                        return (-1)

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    for i in range(4):
                        if((not self.locked[i]) and (pos[0] >= (i+1) * d + ICON_SIZE * i - 10 and pos[0] <= (i+1) * d + ICON_SIZE * (i + 1) + 10) and (pos[1] >= e - 10 and pos[1] <= e+10+ICON_SIZE)):
                            return i+1
                    for i in range(4):
                        if((not self.locked[i+4]) and (pos[0] >= (i+1) * d + ICON_SIZE * i - 10 and pos[0] <= (i+1) * d + ICON_SIZE * (i + 1) + 10) and (pos[1] >= e2 - 10 and pos[1] <= e2+10+ICON_SIZE)):
                            return i+5

