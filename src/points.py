import pygame
from win import Win
from score import Score

POINT_WIDTH = int(Win.GRID_SIZE/2)
POINT_HEIGHT = int(Win.GRID_SIZE/2)

img = pygame.transform.scale(pygame.image.load("../lib/point.png"), [POINT_WIDTH, POINT_HEIGHT])

class Points:
    def __init__(self):
        self.lvl = 0
        self.map = [
            [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1],
            [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
            [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
            [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
            [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
            [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
            [0,1,0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0,1],
            [0,1,0,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1,0,1],
            [0,1,0,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1,0,1],
            [0,1,0,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1,0,1],
            [0,1,0,0,0,0,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1,0,1],
            [0,1,0,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1,0,1],
            [0,1,0,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1,0,1],
            [0,1,0,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1,0,1],
            [0,1,0,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1],
            [0,1,0,1,1,1,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1],
            [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
            [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
            [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
            [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]
    
    def is_point(self, x, y):
        return self.map[y][x]
    
    def to_board(self, screen, plr):
        for i in range(25):
            for j in range(24):
                if(plr.rect.collidepoint(Win.MARGIN_LEFT + Win.GRID_SIZE * i + int(Win.GRID_SIZE/2), Win.MARGIN_TOP + Win.GRID_SIZE * j + int(Win.GRID_SIZE/2)) == True):
                    self.map[j][i] = 0
                    Score.score += 10
                if(self.map[j][i] == 1):
                    screen.blit(img, (Win.MARGIN_LEFT + Win.GRID_SIZE * i + Win.GRID_SIZE/2 - POINT_WIDTH/2, Win.MARGIN_TOP + Win.GRID_SIZE * j + Win.GRID_SIZE/2 - POINT_HEIGHT/2))
        