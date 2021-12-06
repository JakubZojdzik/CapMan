import pygame
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
        self.trn = 0 # 0 - none, 1 - up, 2 - right, 3 - down, 4 - left
        self.frame = 0 # count frames
        self.step = 10
    
    def turn(self, dir):
        self.trn = dir

    def update(self):
        if(self.trn == 1 or self.trn == 3):
            if(self.direction == 1 or self.direction == 3):
                self.direction = self.trn
                self.trn = 0
            if(self.direction == 2 or self.direction == 0):
                if((self.rect.center[0] % Win.GRID_SIZE) - int(Win.GRID_SIZE / 2) <= 0 and -(self.rect.center[0] % Win.GRID_SIZE) - int(Win.GRID_SIZE / 2) <= int(self.step / 2)):
                    self.rect.center = (int(self.rect.center[0] / Win.GRID_SIZE) * Win.GRID_SIZE + int(Win.GRID_SIZE / 2), self.rect.center[1])
                    self.direction = self.trn
                    self.trn = 0
            if(self.direction == 4 or self.direction == 0):
                if((self.rect.center[0] % Win.GRID_SIZE) - int(Win.GRID_SIZE / 2) >= 0 and (self.rect.center[0] % Win.GRID_SIZE) - int(Win.GRID_SIZE / 2) <= int(self.step / 2)):
                    self.rect.center = (int(self.rect.center[0] / Win.GRID_SIZE) * Win.GRID_SIZE + int(Win.GRID_SIZE / 2), self.rect.center[1])
                    self.direction = self.trn
                    self.trn = 0
            
        if(self.trn == 2 or self.trn == 4):
            if(self.direction == 4 or self.direction == 2):
                self.direction = self.trn
                self.trn = 0
            if(self.direction == 1 or self.direction == 0):
                if((self.rect.center[1] % Win.GRID_SIZE) - int(Win.GRID_SIZE / 2) >= 0 and (self.rect.center[1] % Win.GRID_SIZE) - int(Win.GRID_SIZE / 2) <= int(self.step / 2)):
                    self.rect.center = (self.rect.center[0], int(self.rect.center[1] / Win.GRID_SIZE) * Win.GRID_SIZE + int(Win.GRID_SIZE / 2))
                    self.direction = self.trn
                    self.trn = 0
            if(self.direction == 3 or self.direction == 0):
                if((self.rect.center[1] % Win.GRID_SIZE) - int(Win.GRID_SIZE / 2) <= 0 and -(self.rect.center[1] % Win.GRID_SIZE) - int(Win.GRID_SIZE / 2) <= int(self.step / 2)):
                    self.rect.center = (self.rect.center[0], int(self.rect.center[1] / Win.GRID_SIZE) * Win.GRID_SIZE + int(Win.GRID_SIZE / 2))
                    self.direction = self.trn
                    self.trn = 0
            

        if(self.direction == 1):
            if(self.rect.y - self.step >= 0):
                self.rect.y -= self.step
            self.image = img_u

        if(self.direction == 2):
            if(self.rect.x + self.step + SPRITE_WIDTH <= Win.WIDTH):
                self.rect.x += self.step
            self.image = img_r

        if(self.direction == 3):
            if(self.rect.y + self.step + SPRITE_HEIGHT <= Win.HEIGHT):
                self.rect.y += self.step
            self.image = img_d
            
        if(self.direction == 4):
            if(self.rect.x - self.step >= 0):
                self.rect.x -= self.step
            self.image = img_l
        