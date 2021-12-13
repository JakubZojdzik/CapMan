import pygame
from win import Win

# 24x25
img = pygame.transform.scale(pygame.image.load("../lib/block.png"), [Win.GRID_SIZE, Win.GRID_SIZE])

class Level:
    def __init__(self):
        self.lvl = 0
        self.maps = [
            [
                [1,0,1,1,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,0,1,0],
                [1,0,0,0,0,0,1,0,0,0,1,2,2,2,1,0,0,0,1,0,0,0,0,0,1,0],
                [1,0,1,1,1,0,0,0,1,0,1,2,2,2,1,0,1,0,0,0,1,1,1,0,1,0],
                [1,0,0,0,1,0,1,1,1,0,1,2,2,2,1,0,1,1,1,0,1,0,0,0,1,0],
                [1,0,1,0,1,0,0,0,1,0,1,1,2,1,1,0,1,0,0,0,1,0,1,0,1,0],
                [1,0,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,0,1,1,1,0,1,0,1,0],
                [1,1,1,0,0,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,0,0,1,1,1,0],
                [1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0],
                [1,0,1,1,1,0,1,1,1,0,0,0,1,0,0,0,1,1,1,0,1,1,1,0,1,0],
                [1,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0],
                [1,0,1,0,1,1,1,0,1,0,1,1,2,1,1,0,1,0,1,1,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,1,2,2,2,1,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,0,0,1,0,1,0,0,0,1,2,2,2,1,0,0,0,1,0,1,0,0,0,1,0],
                [1,1,0,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,1,0,1,1,0],
                [1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0],
                [1,0,1,1,1,0,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,1,1,0,1,0],
                [1,0,1,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,1,1,1,0,1,0,1,0,1,1,1,1,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,1,0,1,0],
                [1,0,0,0,0,0,1,1,0,1,1,1,0,1,1,1,0,1,1,0,0,0,0,0,1,0],
                [1,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,0,1,0],
                [1,0,1,0,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1,0,1,0],
                [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0],
                [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            ],
            # clean map:
            # [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            # [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            # [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            # [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            # [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            # [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            # [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            # [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            # [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            # [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            # [1,0,0,0,0,0,0,0,0,0,1,1,2,1,1,0,0,0,0,0,0,0,0,0,1,0],
            # [1,0,0,0,0,0,0,0,0,0,1,2,2,2,1,0,0,0,0,0,0,0,0,0,1,0],
            # [1,0,0,0,0,0,0,0,0,0,1,2,2,2,1,0,0,0,0,0,0,0,0,0,1,0],
            # [1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0],
            # [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            # [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            # [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            # [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            # [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            # [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            # [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            # [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            # [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            # [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0],
                [1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,0,1,0],
                [1,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,1,0],
                [1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0],
                [2,2,2,2,1,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,1,2,2,2,2,0],
                [1,1,1,1,1,0,1,1,0,1,1,1,2,1,1,1,0,1,1,0,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,1,1,2,2,2,1,1,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,1,1,2,2,2,1,1,0,0,0,0,0,0,0,0,0,0],
                [1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0],
                [2,2,2,2,1,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,1,2,2,2,2,0],
                [1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,0],
                [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0],
                [1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,0],
                [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0],
                [1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            ],
            [
                [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0],
                [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,1,0,1,1,0,1,0,1,0,1,1,1,1,0,1,1,1,0,0,1,0,0,1,0],
                [1,0,1,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0],
                [1,0,1,1,1,1,0,1,1,1,0,0,0,1,0,1,1,0,1,1,1,1,1,0,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0],
                [1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,0,1,1,1,1,1,1,0,1,0],
                [1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,1,0],
                [1,0,1,1,1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,1,1,2,1,1,0,0,1,0,0,1,0,1,0,1,0],
                [1,0,0,0,0,0,1,0,1,0,1,2,2,2,1,0,0,1,0,0,1,0,1,0,1,0],
                [1,0,1,1,1,0,1,0,1,0,1,2,2,2,1,0,0,1,0,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,0,1,0,0,0,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],
                [1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1,0,1,0,0,1,1,0,0,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,1,1,0,0,0],
                [0,0,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,0,1,1,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0],
                [1,0,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1,1,0,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0],
                [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            ],

            [
                [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,1,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,1,1,0,0,1,1,1,1,0,0,1,0,1,1,1,1,0,1,1,1,1,0,1,0],
                [1,0,0,1,1,0,0,0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0],
                [1,0,0,0,1,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,0,0,0,1,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0],
                [1,0,1,0,0,0,1,1,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0],
                [1,0,1,0,1,0,0,1,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0],
                [1,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0],
                [1,0,1,1,1,1,1,0,0,0,1,1,2,1,1,0,1,0,0,0,1,0,1,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,1,2,2,2,1,0,1,1,0,1,1,0,0,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,1,2,2,2,1,0,1,1,0,1,1,0,0,0,1,0],
                [1,0,1,1,1,1,1,0,0,0,1,1,1,1,1,0,1,0,0,0,1,0,1,0,1,0],
                [1,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,0,1,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0],
                [1,0,1,0,0,0,1,1,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0],
                [1,0,0,0,0,1,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0],
                [1,0,0,0,1,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,0,1,1,0,0,0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0],
                [1,0,1,1,0,0,1,1,1,1,0,0,1,0,1,1,1,1,0,1,1,1,1,0,1,0],
                [1,0,1,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            ],
            
            ]
        self.start_maps = self.maps
    
    def reset(self):
        self.lvl = 0
        self.maps = self.start_maps

    def is_blocked(self, x, y):
        return self.maps[self.lvl][y][x]
    
    def show_board(self):
        return self.maps[self.lvl].copy()
    
    def to_board(self, screen):
        for i in range(25):
            for j in range(24):
                if(self.maps[self.lvl][j][i] == 1):
                    screen.blit(img, (Win.MARGIN_LEFT + Win.GRID_SIZE * i, Win.MARGIN_TOP + Win.GRID_SIZE * j))
