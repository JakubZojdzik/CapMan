import pygame
from win import Win

# 16x14
img = pygame.transform.scale(pygame.image.load("../lib/block.jpg"), [Win.GRID_SIZE, Win.GRID_SIZE])

class Level:
    def __init__(self):
        self.lvl = 0
        self.maps = [[
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
            [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]]
    
    def is_blocked(self, x, y):
        return self.maps[self.lvl][y][x]

    def change_lvl(self, new_lvl):
        self.lvl = new_lvl - 1
    
    def to_board(self, screen):
        for i in range(16):
            for j in range(14):

                if(self.maps[self.lvl][j][i] == 1):
                    screen.blit(img, (Win.MARGIN_LEFT + Win.GRID_SIZE * i, Win.MARGIN_TOP + Win.GRID_SIZE * j))
