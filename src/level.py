import pygame
from win import Win

# 24x25
img = pygame.transform.scale(pygame.image.load("../lib/ingame_textures/map/block.png"), [Win.GRID_SIZE, Win.GRID_SIZE])

class Level:
    def __init__(self):
        self.lvl = 0
        self.maps = [
            # clean map:
            [
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,1,1,2,1,1,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,1,2,2,2,1,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,1,2,2,2,1,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            ],
            [
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,1,1,0,1,1,1,0,1,0],
                [1,0,1,0,0,0,0,0,0,0,1,3,0,0,1,0,0,1,0,0,1,3,1,0,1,0],
                [1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0],
                [1,0,1,0,0,0,0,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,1,0,1,0],
                [1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0],
                [1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0],
                [1,0,1,1,1,1,1,1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,1,1,2,1,1,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,1,2,2,2,1,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,1,2,2,2,1,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,0,1,0],
                [1,0,1,0,1,1,3,1,0,0,1,0,3,0,1,0,0,1,0,0,0,0,1,0,1,0],
                [1,0,1,0,1,1,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0],
                [1,0,1,0,1,1,0,1,0,0,1,1,1,1,1,0,0,1,0,0,0,0,1,0,1,0],
                [1,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0],
                [1,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0],
                [1,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            ],
            [
                [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0],
                [1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,1,0],
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
                [1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,1,0],
                [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            ],
            [
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,1,0,1,0],
                [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0],
                [1,0,0,0,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,0,0,0,1,0],
                [1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,1,0,1,0],
                [1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,0,0,1,1,2,1,1,0,0,0,1,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,0,0,1,0,1,2,2,2,1,0,1,0,0,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,0,0,1,0,1,2,2,2,1,0,1,0,0,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,0,0,1,1,1,1,1,0,0,0,1,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0],
                [1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0],
                [1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0],
                [1,0,0,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,0,0,1,0],
                [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0],
                [1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,1,0],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            ],
            [
                [1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0],
                [1,0,0,3,1,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,3,0,0,1,0],
                [1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0],
                [1,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,1,0],
                [1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0],
                [1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,1,1,2,1,1,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,1,0,0,0,0,0,1,0,1,2,2,2,1,0,1,0,0,0,0,0,1,0,1,0],
                [1,0,1,0,0,0,0,0,1,0,1,2,2,2,1,0,1,0,0,0,0,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0],
                [1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0],
                [1,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,1,0],
                [1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0],
                [1,3,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,3,0,0,1,0],
                [1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            ],
            [
                [1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0],
                [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0],
                [1,0,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,0,1,0],
                [1,0,1,0,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0],
                [1,0,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0],
                [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0],
                [1,0,1,0,1,1,1,0,1,0,1,1,2,1,1,0,1,0,1,1,1,0,1,0,1,0],
                [1,0,1,0,1,3,1,0,1,0,1,2,2,2,1,0,1,0,1,3,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,1,2,2,2,1,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
                [1,0,1,0,1,0,1,0,1,0,1,1,0,1,1,0,1,0,0,0,0,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
                [1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0],
                [1,0,1,1,1,1,1,0,1,0,1,1,0,1,1,0,1,0,1,1,1,1,1,0,1,0],
                [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0],
                [1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            ],
            [
                [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0],
                [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,1,0,1,1,0,1,0,1,0,1,1,1,1,0,1,1,1,0,0,1,0,0,1,0],
                [1,0,1,0,3,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,3,0,1,0],
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
                [0,0,1,0,0,0,3,1,0,1,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0],
                [1,0,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1,1,0,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,3,1,0],
                [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            ],
            [
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0],
                [1,0,1,3,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,3,1,0,1,0],
                [1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,0,1,0],
                [1,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,1,0],
                [1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0],
                [2,2,2,2,1,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,1,2,2,2,2,0],
                [1,1,1,1,1,0,1,1,0,0,1,1,2,1,1,0,0,1,1,0,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,1,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0],
                [1,1,1,1,1,0,1,1,0,0,1,1,1,1,1,0,0,1,1,0,1,1,1,1,1,0],
                [2,2,2,2,1,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,1,2,2,2,2,0],
                [1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,0],
                [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0],
                [1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,0],
                [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0],
                [1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0],
                [1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,1,0],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            ],
            [
                [1,0,1,1,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,0,1,0],
                [1,0,0,0,0,0,1,3,0,0,1,2,2,2,1,0,0,3,1,0,0,0,0,0,1,0],
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
                [1,1,0,1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1,0,1,1,0],
                [1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0],
                [1,0,1,1,1,0,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,1,1,0,1,0],
                [1,0,1,3,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,3,1,0,1,0],
                [1,0,1,0,1,0,1,1,1,1,0,1,0,1,0,1,1,1,1,0,1,0,1,0,1,0],
                [1,0,1,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,1,0,1,0],
                [1,0,0,0,0,0,1,1,0,1,1,1,0,1,1,1,0,1,1,0,0,0,0,0,1,0],
                [1,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,0,1,0],
                [1,0,1,0,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1,0,1,0],
                [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0],
                [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            ],
            
            # [
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,0,0,0,1,1,2,1,1,0,0,0,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,0,0,0,1,2,2,2,1,0,0,0,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,0,0,0,1,2,2,2,1,0,0,0,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            # ],
            ]
        self.start_maps = self.maps

        self.mapsCfg = [
            [ #easy
                [[2], [3, 2], [10, 30], [12, 24, 36], [4, 6]],
                [[2],[3, 2], [10, 30], [12, 24, 36], [4, 6]],
                [[3],[3, 2], [10, 30], [12, 24, 36], [4, 6]],
                [[3],[3, 2], [10, 35], [12, 24, 34], [4, 6]],
                [[5],[3, 2], [10, 35], [12, 24, 34], [4, 6]],
                [[7],[3, 2], [10, 40], [10, 20, 30], [4, 4]],
                [[7],[3, 2], [8, 40], [10, 20, 30], [4, 4]],
                [[10],[3, 2], [8, 40], [10, 20, 30], [4, 4]],
                [[12],[3, 2], [8, 40], [10, 20, 30], [4, 4]],
            ],
            [  #standard
                [[3], [3, 2], [10, 30], [12, 24, 36], [4, 6]],
                [[3], [3, 2], [10, 30], [12, 24, 36], [4, 6]],
                [[5], [3, 2], [10, 35], [12, 24, 34], [4, 6]],
                [[8], [3, 2], [10, 35], [12, 24, 34], [4, 6]],
                [[10], [3, 2], [8, 40], [12, 24, 36], [4, 4]],
                [[15], [3, 2], [8, 40], [10, 20, 30], [4, 4]],
                [[25], [3, 2], [8, 40], [10, 20, 30], [4, 4]],
                [[1000], [3, 2], [8, 40], [10, 20, 30], [4, 4]],
                [[1000], [3, 3], [7, 45], [10, 20, 30], [4, 4]],
            ],
            [  # hard
                [[10], [3, 2], [10, 35], [12, 24, 34], [4, 6]],
                [[10], [3, 2], [10, 35], [12, 24, 34], [4, 6]],
                [[10], [3, 2], [10, 35], [12, 24, 34], [4, 6]],
                [[15], [3, 2], [8, 40], [12, 24, 36], [4, 4]],
                [[15], [3, 2], [8, 40], [10, 20, 30], [4, 4]],
                [[25], [3, 2], [8, 40], [10, 20, 30], [4, 4]],
                [[40], [3, 2], [8, 40], [10, 20, 30], [4, 4]],
                [[1000], [3, 3], [8, 45], [10, 20, 30], [4, 4]],
                [[1000], [3, 3], [7, 45], [8, 16, 24], [4, 4]],
            ],
            # [[ghosts IQ//10],[chase speed, scary speed], [scary mode length, scatter mode time], [open ghost1, g2, g3], [player speed, player scary speed]]
        ]
    
    def reset(self):
        self.lvl = 0
        self.maps = self.start_maps

    def is_blocked(self, x, y):
        if(self.maps[self.lvl][y][x] == 3):
            return 0
        return self.maps[self.lvl][y][x]
    
    def show_board(self):
        return self.maps[self.lvl].copy()
    
    def to_board(self, screen):
        for i in range(25):
            for j in range(24):
                if(self.maps[self.lvl][j][i] == 1):
                    screen.blit(img, (Win.MARGIN_LEFT + Win.GRID_SIZE * i, Win.MARGIN_TOP + Win.GRID_SIZE * j))
