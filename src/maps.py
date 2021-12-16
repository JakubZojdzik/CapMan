import pygame
from win import Win
class Bigmap:
    def __init__(self):
        self.map1=pygame.image.load("../lib/maps/map1.png")
        self.map1= pygame.transform.rotozoom(self.map1, 0, 0.3)
        self.map2=pygame.image.load("../lib/maps/map2.png")
        self.map2 = pygame.transform.rotozoom(self.map2, 0, 0.3)
        self.map3=pygame.image.load("../lib/maps/map3.png")
        self.map3 = pygame.transform.rotozoom(self.map3, 0, 0.3)
        self.map4=pygame.image.load("../lib/maps/map4.png")
        self.map4 = pygame.transform.rotozoom(self.map4, 0, 0.3)

        self.title=pygame.image.load("../lib/capmantitle.png")
        self.title=pygame.transform.rotozoom(self.title, 0, 0.5)

        self.locked = False


    def choice(self):
        ev = pygame.event.get()
        # proceed events
        for event in pygame.event.get():
            # handle MOUSEBUTTONUP
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
    def drawmaps(self):
        run = True
        x = 225
        y = 220
        while run:
            screen.fill(Win.BGCOLOR)
            screen_info = pygame.display.Info()
            d=int((screen_info.current_w - 4*225) / 5)
            e=int((screen_info.current_h - 220) / 2)
            screen.blit(self.title, (int((screen_info.current_w - 522) / 2),0))
            screen.blit(self.map1, (d, e))
            screen.blit(self.map2, (2*d+225, e))
            screen.blit(self.map3, (3*d+450, e))
            screen.blit(self.map4, (4*d+675, e))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # zakończenie
                    pygame.quit()
                    run = False
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if (pos[0]>=d and pos[0]<=d+225) and (pos[1]>=e and pos[1]<=e+220):
                        return int(1)
                    if (pos[0]>=2*d+225 and pos[0]<=2*d+450) and (pos[1]>=e and pos[1]<=e+220):
                        return int(2)
                    if (pos[0]>=3*d+450 and pos[0]<=3*d+675) and (pos[1]>=e and pos[1]<=e+220):
                        return int(3)
                    if (pos[0]>=4*d+675 and pos[0]<=4*d+900) and (pos[1]>=e and pos[1]<=e+220):
                        return int(4)








pygame.init()
pygame.init()
screen_info = pygame.display.Info()
Win.MARGIN_LEFT = int((screen_info.current_w - Win.WIDTH) / 2)
Win.MARGIN_LEFT = Win.GRID_SIZE * round(Win.MARGIN_LEFT / Win.GRID_SIZE)
Win.MARGIN_TOP = int((screen_info.current_h - Win.HEIGHT) / 2)
Win.MARGIN_TOP = Win.GRID_SIZE * round(Win.MARGIN_TOP / Win.GRID_SIZE) - Win.GRID_SIZE
screen = pygame.display.set_mode((screen_info.current_w, screen_info.current_h), pygame.FULLSCREEN)
"""
plansza=Bigmap()
a=plansza.drawmaps()
print (a)
print (type(a))
"""