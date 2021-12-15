import pygame
from win import Win
class Bigmap:
    def __init__(self):
        self.map1=pygame.image.load("../lib/maps/map1.png")
        self.map1= pygame.transform.rotozoom(self.map1, 0, 0.3)

        self.map2=map1=pygame.image.load("../lib/maps/map2.png")
        self.map3=map1=pygame.image.load("../lib/maps/map3.png")
        self.map4=map1=pygame.image.load("../lib/maps/map4.png")

    def drawmaps(self):
        run=True
        while run:
            screen.fill(Win.BGCOLOR)

            screen.blit(self.map1, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # zakończenie
                    pygame.quit()
                    run = False
    def choice(self):
        ev = pygame.event.get()

        # proceed events
        for event in ev:

            # handle MOUSEBUTTONUP
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)




pygame.init()
pygame.init()
screen_info = pygame.display.Info()
Win.MARGIN_LEFT = int((screen_info.current_w - Win.WIDTH) / 2)
Win.MARGIN_LEFT = Win.GRID_SIZE * round(Win.MARGIN_LEFT / Win.GRID_SIZE)
Win.MARGIN_TOP = int((screen_info.current_h - Win.HEIGHT) / 2)
Win.MARGIN_TOP = Win.GRID_SIZE * round(Win.MARGIN_TOP / Win.GRID_SIZE) - Win.GRID_SIZE
screen = pygame.display.set_mode((screen_info.current_w, screen_info.current_h), pygame.FULLSCREEN)
plansza=Bigmap()
plansza.drawmaps()
plansza.choice()