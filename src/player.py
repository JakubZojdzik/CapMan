import pygame
from colors import Colors
from win import Win

SPRITE_WIDTH = 50
SPRITE_HEIGHT = 50

img_u = pygame.transform.scale(pygame.image.load("../lib/Player_up.png"), [SPRITE_WIDTH, SPRITE_HEIGHT])
img_r = pygame.transform.scale(pygame.image.load("../lib/Player_right.png"), [SPRITE_WIDTH, SPRITE_HEIGHT])
img_d = pygame.transform.scale(pygame.image.load("../lib/Player_down.png"), [SPRITE_WIDTH, SPRITE_HEIGHT])
img_l = pygame.transform.scale(pygame.image.load("../lib/Player_left.png"), [SPRITE_WIDTH, SPRITE_HEIGHT])

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = img_r
        self.rect = self.image.get_rect()
        self.rect.center = (Win.WIDTH / 2, Win.HEIGHT / 2)
        self.direction = 0 # 0 - none, 1 - up, 2 - right, 3 - down, 4 - left
        self.frame = 0 # count frames
        self.step = 10
    
    def turn(self, dir):
        self.direction = dir

    def update(self):
        if(self.direction == 1):
            self.rect.y = self.rect.y - self.step
            self.image = img_u

        if(self.direction == 2):
            self.rect.x = self.rect.x + self.step
            self.image = img_r

        if(self.direction == 3):
            self.rect.y = self.rect.y + self.step
            self.image = img_d
            
        if(self.direction == 4):
            self.rect.x = self.rect.x - self.step
            self.image = img_l
        