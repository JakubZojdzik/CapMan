import pygame
from colors import Colors
from win import Win

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(Colors.RED) 
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
        if(self.direction == 2):
            self.rect.x = self.rect.x + self.step
        if(self.direction == 3):
            self.rect.y = self.rect.y + self.step
        if(self.direction == 4):
            self.rect.x = self.rect.x - self.step
        