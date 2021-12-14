import pygame
from win import Win

SPRITE_WIDTH = Win.GRID_SIZE-8
SPRITE_HEIGHT = Win.GRID_SIZE-8

img = pygame.transform.scale(pygame.image.load("../lib/player/Player.png"), [SPRITE_WIDTH, SPRITE_HEIGHT])
img_u = pygame.transform.scale(pygame.image.load("../lib/player/Player_up.png"), [SPRITE_WIDTH, SPRITE_HEIGHT])
img_r = pygame.transform.scale(pygame.image.load("../lib/player/Player_right.png"), [SPRITE_WIDTH, SPRITE_HEIGHT])
img_d = pygame.transform.scale(pygame.image.load("../lib/player/Player_down.png"), [SPRITE_WIDTH, SPRITE_HEIGHT])
img_l = pygame.transform.scale(pygame.image.load("../lib/player/Player_left.png"), [SPRITE_WIDTH, SPRITE_HEIGHT])

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img_r
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        #self.rect.center = (Win.WIDTH / 2 + Win.MARGIN_LEFT + ((Win.WIDTH / 2 + Win.MARGIN_LEFT + (Win.GRID_SIZE/2)) % Win.GRID_SIZE), Win.HEIGHT / 2 + Win.MARGIN_TOP + ((Win.HEIGHT / 2 + Win.MARGIN_TOP + (Win.GRID_SIZE/2)) % Win.GRID_SIZE))
        self.direction = 0 # 0 - none, 1 - up, 2 - right, 3 - down, 4 - left
        self.trn = 0 # 0 - none, 1 - up, 2 - right, 3 - down, 4 - left
        self.frame = 0 # count frames
        self.step = 5
    
    def turn(self, dir):
        self.trn = dir

    def get_coords(self):
        return (round((self.rect.center[0] - Win.MARGIN_LEFT) / Win.GRID_SIZE), round((self.rect.center[1] - Win.MARGIN_TOP) / Win.GRID_SIZE))

    def update(self, map, state):
        stand = True
        if(self.trn == 1 or self.trn == 3):
            x = int(self.rect.center[0] / Win.GRID_SIZE) * Win.GRID_SIZE + int(Win.GRID_SIZE / 2)
            y = self.rect.center[1]
            if(self.direction == 1 or self.direction == 3):
                self.direction = self.trn
                self.trn = 0
            if(self.direction == 2 or self.direction == 0):
                if((self.rect.center[0] % Win.GRID_SIZE) - int(Win.GRID_SIZE / 2) >= 0 and (self.rect.center[0] % Win.GRID_SIZE) - int(Win.GRID_SIZE / 2) <= int(self.step / 2)):
                    if(self.trn == 1):
                        if(map.is_blocked(int((x - Win.MARGIN_LEFT) / Win.GRID_SIZE), int((y - Win.MARGIN_TOP) / Win.GRID_SIZE - 1)) == 0):
                            self.rect.center = (x, y)
                            self.direction = self.trn
                            self.trn = 0
                    if(self.trn == 3):
                        if(map.is_blocked(int((x - Win.MARGIN_LEFT) / Win.GRID_SIZE), int((y - Win.MARGIN_TOP) / Win.GRID_SIZE + 1)) == 0):
                            self.rect.center = (x, y)
                            self.direction = self.trn
                            self.trn = 0

            if(self.direction == 4 or self.direction == 0):
                if((self.rect.center[0] % Win.GRID_SIZE) - int(Win.GRID_SIZE / 2) >= 0 and (self.rect.center[0] % Win.GRID_SIZE) - int(Win.GRID_SIZE / 2) <= int(self.step / 2)):
                    if(self.trn == 1):
                        if(map.is_blocked(int((x - Win.MARGIN_LEFT) / Win.GRID_SIZE), int((y - Win.MARGIN_TOP) / Win.GRID_SIZE) - 1) == 0):
                            self.rect.center = (x, y)
                            self.direction = self.trn
                            self.trn = 0
                    if(self.trn == 3):
                        if(map.is_blocked(int((x - Win.MARGIN_LEFT) / Win.GRID_SIZE), int((y - Win.MARGIN_TOP) / Win.GRID_SIZE + 1)) == 0):
                            self.rect.center = (x, y)
                            self.direction = self.trn
                            self.trn = 0
            
        if(self.trn == 2 or self.trn == 4):
            x = self.rect.center[0]
            y = int(self.rect.center[1] / Win.GRID_SIZE) * Win.GRID_SIZE + int(Win.GRID_SIZE / 2)
            if(self.direction == 4 or self.direction == 2):
                self.direction = self.trn
                self.trn = 0
            if(self.direction == 1 or self.direction == 0):
                if((self.rect.center[1] % Win.GRID_SIZE) - int(Win.GRID_SIZE / 2) >= 0 and (self.rect.center[1] % Win.GRID_SIZE) - int(Win.GRID_SIZE / 2) <= int(self.step / 2)):
                    if(self.trn == 2):
                        if(map.is_blocked(int((x - Win.MARGIN_LEFT) / Win.GRID_SIZE) + 1, int((y - Win.MARGIN_TOP) / Win.GRID_SIZE)) == 0):
                            self.rect.center = (x, y)
                            self.direction = self.trn
                            self.trn = 0
                    if(self.trn == 4):
                        if(map.is_blocked(int((x - Win.MARGIN_LEFT) / Win.GRID_SIZE) - 1, int((y - Win.MARGIN_TOP) / Win.GRID_SIZE)) == 0):
                            self.rect.center = (x, y)
                            self.direction = self.trn
                            self.trn = 0
            if(self.direction == 3 or self.direction == 0):
                if((self.rect.center[1] % Win.GRID_SIZE) - int(Win.GRID_SIZE / 2) >= 0 and (self.rect.center[1] % Win.GRID_SIZE) - int(Win.GRID_SIZE / 2) <= int(self.step / 2)):
                    if(self.trn == 2):
                        if(map.is_blocked(int((x - Win.MARGIN_LEFT) / Win.GRID_SIZE) + 1, int((y - Win.MARGIN_TOP) / Win.GRID_SIZE)) == 0):
                            self.rect.center = (x, y)
                            self.direction = self.trn
                            self.trn = 0
                    if(self.trn == 4):
                        if(map.is_blocked(int((x - Win.MARGIN_LEFT) / Win.GRID_SIZE) - 1, int((y - Win.MARGIN_TOP) / Win.GRID_SIZE)) == 0):
                            self.rect.center = (x, y)
                            self.direction = self.trn
                            self.trn = 0
            

        if(self.direction == 1):
            if(not map.is_blocked(int((self.rect.x - Win.MARGIN_LEFT) / Win.GRID_SIZE), int((self.rect.y - self.step - Win.MARGIN_TOP) / Win.GRID_SIZE))):
                self.rect.y -= self.step
                stand = False
            self.image = img_u

        if(self.direction == 2):
            if(not map.is_blocked(int((self.rect.x + self.step + SPRITE_WIDTH - Win.MARGIN_LEFT) / Win.GRID_SIZE), int((self.rect.y - Win.MARGIN_TOP) / Win.GRID_SIZE))):
                self.rect.x += self.step
                stand = False
            self.image = img_r

        if(self.direction == 3):
            if(not map.is_blocked(int((self.rect.x - Win.MARGIN_LEFT) / Win.GRID_SIZE), int((self.rect.y + self.step + SPRITE_HEIGHT - Win.MARGIN_TOP) / Win.GRID_SIZE))):
                self.rect.y += self.step
                stand = False
            self.image = img_d
            
        if(self.direction == 4):
            if(not map.is_blocked(int((self.rect.x - self.step - Win.MARGIN_LEFT) / Win.GRID_SIZE), int((self.rect.y - Win.MARGIN_TOP) / Win.GRID_SIZE))):
                self.rect.x -= self.step
                stand = False
            self.image = img_l
        
        if(self.rect.y < Win.MARGIN_TOP):
            self.rect.y += Win.HEIGHT
            stand = False
        if(self.rect.y > Win.MARGIN_TOP + Win.HEIGHT):
            self.rect.y -= Win.HEIGHT
            stand = False

        if(self.rect.x < Win.MARGIN_LEFT):
            self.rect.x += Win.WIDTH
            stand = False
        if(self.rect.x > Win.MARGIN_LEFT + Win.WIDTH):
            self.rect.x -= Win.WIDTH
            stand = False

        if state == -1 and not stand:
            self.image = img
        