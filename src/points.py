import pygame
from win import Win
from score import Score
from settings import Settings

POINT_WIDTH = int(Win.GRID_SIZE/2)
POINT_HEIGHT = int(Win.GRID_SIZE/2)
BIG_POINT_WIDTH = int(Win.GRID_SIZE * 1.2)
BIG_POINT_HEIGHT = int(Win.GRID_SIZE * 1.2)

img = pygame.transform.scale(pygame.image.load("../lib/ingame_textures/map/point.png"), [POINT_WIDTH, POINT_HEIGHT])
img_big = pygame.transform.scale(pygame.image.load("../lib/ingame_textures/map/point.png"), [BIG_POINT_WIDTH, BIG_POINT_HEIGHT])

class Points:
    def __init__(self):
        self.lvl = 0
        self.map = [[1]*25 for _ in range(24)]
    
    def is_point(self, x, y):
        return self.map[y][x]

    def reset_points(self, mp):
        n = mp.show_board()
        for i in range(24):
            for j in range(25):
                if(n[i][j] == 0):
                    self.map[i][j] = 1
                elif(n[i][j] == 3):
                    self.map[i][j] = 3
                else:
                    self.map[i][j] = 0

    def is_all(self):
        clean = [[0]*25 for _ in range(24)]
        
        return self.map == clean
    
    def to_board(self, plr):
        scary = False
        for i in range(25):
            for j in range(24):
                if(plr.rect.collidepoint(Win.MARGIN_LEFT + Win.GRID_SIZE * i + int(Win.GRID_SIZE/2), Win.MARGIN_TOP + Win.GRID_SIZE * j + int(Win.GRID_SIZE/2)) == True):
                    if (self.map[j][i] == 1):
                        self.map[j][i] = 0
                        pygame.mixer.music.load("../lib/sounds/waka.mp3")
                        pygame.mixer.music.set_volume(Settings.volume)
                        pygame.mixer.music.play(0)
                        Score.score += Score.SCORE_POINT
                    if(self.map[j][i] == 3):
                        scary = True
                        self.map[j][i] = 0
                        pygame.mixer.music.load("../lib/sounds/waka.mp3")
                        pygame.mixer.music.set_volume(Settings.volume)
                        pygame.mixer.music.play(0)
                        Score.score += 2 * Score.SCORE_POINT
                if(self.map[j][i] == 1):
                    Win.screen.blit(img, (Win.MARGIN_LEFT + Win.GRID_SIZE * i + Win.GRID_SIZE/2 - POINT_WIDTH/2, Win.MARGIN_TOP + Win.GRID_SIZE * j + Win.GRID_SIZE/2 - POINT_HEIGHT/2))
                elif(self.map[j][i] == 3):
                    Win.screen.blit(img_big, (Win.MARGIN_LEFT + Win.GRID_SIZE * i + Win.GRID_SIZE/2 - BIG_POINT_WIDTH/2, Win.MARGIN_TOP + Win.GRID_SIZE * j + Win.GRID_SIZE/2 - BIG_POINT_HEIGHT/2))
        return scary


