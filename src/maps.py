import pygame
from win import Win
from highscore import Highscore

pygame.init()
font = pygame.font.Font("../lib/VT323/VT323-Regular.ttf", 48)
screen_info = pygame.display.Info()
ICON_SIZE = (screen_info.current_h - 365) // 4 + 70
class Bigmap:
    def __init__(self):
        self.map1 = pygame.transform.scale(pygame.image.load("../lib/maps/map1.png"), [ICON_SIZE, ICON_SIZE])
        self.map2 = pygame.transform.scale(pygame.image.load("../lib/maps/map2.png"), [ICON_SIZE, ICON_SIZE])
        self.map3 = pygame.transform.scale(pygame.image.load("../lib/maps/map3.png"), [ICON_SIZE, ICON_SIZE])
        self.map4 = pygame.transform.scale(pygame.image.load("../lib/maps/map4.png"), [ICON_SIZE, ICON_SIZE])
        self.map5 = pygame.transform.scale(pygame.image.load("../lib/maps/map1.png"), [ICON_SIZE, ICON_SIZE])
        self.map6 = pygame.transform.scale(pygame.image.load("../lib/maps/map2.png"), [ICON_SIZE, ICON_SIZE])
        self.map7 = pygame.transform.scale(pygame.image.load("../lib/maps/map3.png"), [ICON_SIZE, ICON_SIZE])
        self.map8 = pygame.transform.scale(pygame.image.load("../lib/maps/map4.png"), [ICON_SIZE, ICON_SIZE])
        self.maps = [self.map1, self.map2, self.map3, self.map4, self.map5, self.map6, self.map7, self.map8]

        self.title = pygame.image.load("../lib/capmantitle.png")
        self.title = pygame.transform.rotozoom(self.title, 0, 0.35)

        self.locked = False

    def drawmaps(self, screen):
        run = True
        while run:
            screen.fill(Win.BGCOLOR)
            
            d = int((screen_info.current_w - 4*ICON_SIZE) / 5)
            e = screen_info.current_h // 3 - 50
            screen.blit(self.title, (int((screen_info.current_w - 365) / 2),0))

            for i in range(4):
                score_img = font.render("Lvl: " + str(i+1), True, (0, 255, 255))
                score_rect = score_img.get_rect(center=((i+1) * d + ICON_SIZE * i + ICON_SIZE // 2, e - 30))
                screen.blit(score_img, score_rect)
                screen.blit(self.maps[i], ((i+1) * d + ICON_SIZE * i, e))
                score_img = font.render("Highscore: " + str(Highscore.load_highscore(i+1)), True, (0, 255, 255))
                if(Highscore.load_highscore(i+1) == "-1"):
                    score_img = font.render("Highscore: ?", True, (0, 255, 255))
                score_rect = score_img.get_rect(center=((i+1) * d + ICON_SIZE * i + ICON_SIZE // 2, e + ICON_SIZE + 25))
                screen.blit(score_img, score_rect)

            e += screen_info.current_h - (ICON_SIZE + 60) - screen_info.current_h // 3.2
            for i in range(4):
                score_img = font.render("Lvl: " + str(i+5), True, (0, 255, 255))
                score_rect = score_img.get_rect(center=((i+1) * d + ICON_SIZE * i + ICON_SIZE // 2, e - 30))
                screen.blit(score_img, score_rect)
                screen.blit(self.maps[i+4], ((i+1) * d + ICON_SIZE * i, e))
                score_img = font.render("Highscore: " + str(Highscore.load_highscore(i+5)), True, (0, 255, 255))
                if(str(Highscore.load_highscore(i+5)) == '-1'):
                    score_img = font.render("Highscore: ?", True, (0, 255, 255))
                score_rect = score_img.get_rect(center=((i+1) * d + ICON_SIZE * i + ICON_SIZE // 2, e + ICON_SIZE + 25))
                screen.blit(score_img, score_rect)

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # zakończenie
                    pygame.quit()
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == ord('q'):
                        run = False
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if (pos[0]>=d and pos[0]<=d+225) and (pos[1]>=e and pos[1]<=e+220):
                        return 1
                    if (pos[0]>=2*d+225 and pos[0]<=2*d+450) and (pos[1]>=e and pos[1]<=e+220):
                        return 2
                    if (pos[0]>=3*d+450 and pos[0]<=3*d+675) and (pos[1]>=e and pos[1]<=e+220):
                        return 3
                    if (pos[0]>=4*d+675 and pos[0]<=4*d+900) and (pos[1]>=e and pos[1]<=e+220):
                        return 4
