from win import Win
import pygame

level_grid = []
LVL_WIDTH = 25
LVL_HEIGHT = 24

SPRITE_WIDTH = Win.GRID_SIZE-8
SPRITE_HEIGHT = Win.GRID_SIZE-8

img_pink = pygame.transform.scale(pygame.image.load("../lib/pinkghost/pinkghostup.png"), [SPRITE_WIDTH, SPRITE_HEIGHT])
img_blue = pygame.transform.scale(pygame.image.load("../lib/blueghost/blueghostup.png"), [SPRITE_WIDTH, SPRITE_HEIGHT])
img_orange = pygame.transform.scale(pygame.image.load("../lib/orangeghost/orangeghostup.png"), [SPRITE_WIDTH, SPRITE_HEIGHT])
img_red = pygame.transform.scale(pygame.image.load("../lib/redghost/redghostup.png"), [SPRITE_WIDTH, SPRITE_HEIGHT])

class Ghost(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, mode, color):
        pygame.sprite.Sprite.__init__(self)
        self.start_pos_x = pos_x
        self.start_pos_y = pos_y
        self.color = color
        self.step = 25/6
        self.mode = mode
        if(color == "pink"):
            self.image = img_pink
        elif(color == "blue"):
            self.image = img_blue
        elif(color == "orange"):
            self.image = img_orange
        elif(color == "red"):
            self.image = img_red
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.trn = 0
        self.direction = 1

    @staticmethod
    def loadLevelGrid(grid):
        level_grid = grid.copy()
        LVL_HEIGHT = len(level_grid)-1
        LVL_WIDTH = len(level_grid[0])-1

    def resetPos(self):
        self.rect.center = (self.start_pos_x, self.start_pos_y)

    @staticmethod
    def BFS(cells):
        visited = level_grid.copy()
        result = level_grid.copy()

        queue = []

        for i in cells:
            queue.append([i[0], i[1]])
            if len(i) == 2:
                i.append(0)
            result[i[1]][i[0]] = i[2]

        while len(queue) > 0:
            prev_cell = queue.pop(0)
            curr_x = prev_cell[0] - 1
            curr_y = prev_cell[1]
            if curr_x == -1:
                curr_x = LVL_WIDTH - 1

            if visited[curr_y][curr_x] == 0:
                queue.append([curr_x, curr_y])
                visited[curr_y][curr_x] = visited[prev_cell[1]][prev_cell[0]]
                result[curr_y][curr_x] = result[prev_cell[1]][prev_cell[0]] + Win.GRID_SIZE

            curr_x = prev_cell[0]
            curr_y = prev_cell[1] - 1
            if curr_y == -1:
                curr_y = LVL_HEIGHT - 1

            if visited[curr_y][curr_x] == 0:
                queue.append([curr_x, curr_y])
                visited[curr_y][curr_x] = visited[prev_cell[1]][prev_cell[0]]
                result[curr_y][curr_x] = result[prev_cell[1]][prev_cell[0]] + Win.GRID_SIZE

            curr_x = prev_cell[0] + 1
            curr_y = prev_cell[1]
            if curr_x == LVL_WIDTH:
                curr_x = 0

            if visited[curr_y][curr_x] == 0:
                queue.append([curr_x, curr_y])
                visited[curr_y][curr_x] = visited[prev_cell[1]][prev_cell[0]]
                result[curr_y][curr_x] = result[prev_cell[1]][prev_cell[0]] + Win.GRID_SIZE

            curr_x = prev_cell[0]
            curr_y = prev_cell[1] + 1
            if curr_y == LVL_HEIGHT:
                curr_y = 0

            if visited[curr_y][curr_x] == 0:
                queue.append([curr_x, curr_y])
                visited[curr_y][curr_x] = visited[prev_cell[1]][prev_cell[0]]
                result[curr_y][curr_x] = result[prev_cell[1]][prev_cell[0]] + Win.GRID_SIZE


    def got_capman(self, capman):
        return self.rect.colliderect(capman.rect)

    def update(self, map):
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
            if(self.rect.y - self.step >= Win.MARGIN_TOP and not map.is_blocked(int((self.rect.x - Win.MARGIN_LEFT) / Win.GRID_SIZE), int((self.rect.y - self.step - Win.MARGIN_TOP) / Win.GRID_SIZE))):
                self.rect.y -= self.step

        if(self.direction == 2):
            if(self.rect.x + self.step + SPRITE_WIDTH <= Win.WIDTH + Win.MARGIN_LEFT and not map.is_blocked(int((self.rect.x + self.step + SPRITE_WIDTH - Win.MARGIN_LEFT) / Win.GRID_SIZE), int((self.rect.y - Win.MARGIN_TOP) / Win.GRID_SIZE))):
                self.rect.x += self.step

        if(self.direction == 3):
            if(self.rect.y + self.step + SPRITE_HEIGHT <= Win.HEIGHT + Win.MARGIN_TOP and not map.is_blocked(int((self.rect.x - Win.MARGIN_LEFT) / Win.GRID_SIZE), int((self.rect.y + self.step + SPRITE_HEIGHT - Win.MARGIN_TOP) / Win.GRID_SIZE))):
                self.rect.y += self.step
            
        if(self.direction == 4):
            if(self.rect.x - self.step >= Win.MARGIN_LEFT and not map.is_blocked(int((self.rect.x - self.step - Win.MARGIN_LEFT) / Win.GRID_SIZE), int((self.rect.y - Win.MARGIN_TOP) / Win.GRID_SIZE))):
                self.rect.x -= self.step
        
