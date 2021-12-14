from win import Win
import pygame
import copy

level_grid = []
LVL_WIDTH = Win.WIDTH // Win.GRID_SIZE
LVL_HEIGHT = Win.HEIGHT // Win.GRID_SIZE

SPRITE_WIDTH = Win.GRID_SIZE-8
SPRITE_HEIGHT = Win.GRID_SIZE-8

img_pink = [
    pygame.transform.scale(pygame.image.load("../lib/pinkghost/pinkghostup.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../lib/pinkghost/pinkghostup.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../lib/pinkghost/pinkghostright.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../lib/pinkghost/pinkghostdown.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../lib/pinkghost/pinkghostleft.png"), [SPRITE_WIDTH, SPRITE_HEIGHT])
]
img_blue = [
    pygame.transform.scale(pygame.image.load("../lib/blueghost/blueghostup.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../lib/blueghost/blueghostup.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../lib/blueghost/blueghostright.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../lib/blueghost/blueghostdown.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../lib/blueghost/blueghostleft.png"), [SPRITE_WIDTH, SPRITE_HEIGHT])
]
img_orange = [
    pygame.transform.scale(pygame.image.load("../lib/orangeghost/orangeghostup.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../lib/orangeghost/orangeghostup.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../lib/orangeghost/orangeghostright.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../lib/orangeghost/orangeghostdown.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../lib/orangeghost/orangeghostleft.png"), [SPRITE_WIDTH, SPRITE_HEIGHT])
]
img_red = [
    pygame.transform.scale(pygame.image.load("../lib/redghost/redghostup.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../lib/redghost/redghostup.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../lib/redghost/redghostright.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../lib/redghost/redghostdown.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../lib/redghost/redghostleft.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
]

class Ghost(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, mode, color):
        pygame.sprite.Sprite.__init__(self)
        self.start_pos_x = pos_x
        self.start_pos_y = pos_y
        self.color = color
        self.step = 5
        self.mode = mode
        self.img_rot = []
        if(color == "pink"):
            self.img_rot = img_pink
            self.image = img_pink[0]
        elif(color == "blue"):
            self.img_rot = img_blue
            self.image = img_blue[0]
        elif(color == "orange"):
            self.img_rot = img_orange
            self.image = img_orange[0]
        elif(color == "red"):
            self.img_rot = img_red
            self.image = img_red[0]
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.trn = 0
        self.direction = 1

    def resetPos(self):
        self.rect.center = (self.start_pos_x, self.start_pos_y)

    @staticmethod
    def BFS(pos, map):
        cells = Win.pixelPos_to_gridPos(pos)
        #level_grid = map.show_board().copy()
        visited = copy.deepcopy(map.show_board())
        result = copy.deepcopy(map.show_board())
        queue = []

        it = 10
        for i in cells:
            queue.append([i[0], i[1]])
            result[i[1]][i[0]] = float(i[2])
            visited[i[1]][i[0]] = it
            it += 1

        while len(queue) > 0:
            prev_cell = queue.pop(0)
            curr_x = prev_cell[0] - 1
            curr_y = prev_cell[1]
            if curr_x == -1:
                curr_x = LVL_WIDTH - 1

            if visited[curr_y][curr_x] == 0 or visited[curr_y][curr_x] == 2:
                queue.append([curr_x, curr_y])
                visited[curr_y][curr_x] = visited[prev_cell[1]][prev_cell[0]]
                result[curr_y][curr_x] = result[prev_cell[1]][prev_cell[0]] + Win.GRID_SIZE

            curr_x = prev_cell[0]
            curr_y = prev_cell[1] - 1
            if curr_y == -1:
                curr_y = LVL_HEIGHT - 1

            if visited[curr_y][curr_x] == 0 or visited[curr_y][curr_x] == 2:
                queue.append([curr_x, curr_y])
                visited[curr_y][curr_x] = visited[prev_cell[1]][prev_cell[0]]
                result[curr_y][curr_x] = result[prev_cell[1]][prev_cell[0]] + Win.GRID_SIZE

            curr_x = prev_cell[0] + 1
            curr_y = prev_cell[1]
            if curr_x == LVL_WIDTH:
                curr_x = 0

            if visited[curr_y][curr_x] == 0 or visited[curr_y][curr_x] == 2:
                queue.append([curr_x, curr_y])
                visited[curr_y][curr_x] = visited[prev_cell[1]][prev_cell[0]]
                result[curr_y][curr_x] = result[prev_cell[1]][prev_cell[0]] + Win.GRID_SIZE

            curr_x = prev_cell[0]
            curr_y = prev_cell[1] + 1
            if curr_y == LVL_HEIGHT:
                curr_y = 0

            if visited[curr_y][curr_x] == 0 or visited[curr_y][curr_x] == 2:
                queue.append([curr_x, curr_y])
                visited[curr_y][curr_x] = visited[prev_cell[1]][prev_cell[0]]
                result[curr_y][curr_x] = result[prev_cell[1]][prev_cell[0]] + Win.GRID_SIZE

        return result

    def got_capman(self, capman):
        return self.rect.colliderect(capman.rect)

    @staticmethod
    def possible_moves(pos, map):
        gridPos = Win.pixelPos_to_gridPos(pos)
        result = [] # 0 - none, 1 - up, 2 - right, 3 - down, 4 - left
        if len(gridPos) == 1:
            if map.is_blocked(gridPos[0][0], (gridPos[0][1]-1)%LVL_HEIGHT) != 1:
                result.append([gridPos[0][0], (gridPos[0][1]-1)%LVL_HEIGHT, Win.GRID_SIZE, 1])
            if map.is_blocked((gridPos[0][0]+1)%LVL_WIDTH, gridPos[0][1]) != 1:
                result.append([(gridPos[0][0]+1)%LVL_WIDTH, gridPos[0][1], Win.GRID_SIZE, 2])
            if map.is_blocked(gridPos[0][0], (gridPos[0][1]+1)%LVL_HEIGHT) != 1:
                result.append([gridPos[0][0], (gridPos[0][1]+1)%LVL_HEIGHT, Win.GRID_SIZE, 3])
            if map.is_blocked((gridPos[0][0]-1)%LVL_WIDTH, gridPos[0][1]) != 1:
                result.append([(gridPos[0][0]-1)%LVL_WIDTH, gridPos[0][1], Win.GRID_SIZE, 4])
            return result
        else:
            if gridPos[0][0] == gridPos[1][0]:
                gridPos[0].append(1)
                gridPos[1].append(3)
            else:
                gridPos[0].append(4)
                gridPos[1].append(2)
            return gridPos


    def find_next_move(self, pos, map):
        posibble_moves = Ghost.possible_moves(self.rect.center, map)
        BFSed_map = Ghost.BFS(pos, map)
        min_length = 10000.0
        curr_direction = 1
        for i in posibble_moves:
            print(i, BFSed_map[i[1]][i[0]])
            if BFSed_map[i[1]][i[0]] < min_length:
                curr_direction = i[3]
                min_length = BFSed_map[i[1]][i[0]]

        print(curr_direction)

        return curr_direction

    def update(self, player_pos, map):
        self.direction = self.find_next_move(player_pos, map)
        if self.direction == 1:
            self.rect.y -= self.step
        if self.direction == 2:
            self.rect.x += self.step
        if self.direction == 3:
            self.rect.y += self.step
        if self.direction == 4:
            self.rect.x -= self.step

        if (self.rect.y < Win.MARGIN_TOP):
            self.rect.y += Win.HEIGHT
        if (self.rect.y > Win.MARGIN_TOP + Win.HEIGHT):
            self.rect.y -= Win.HEIGHT

        if (self.rect.x < Win.MARGIN_LEFT):
            self.rect.x += Win.WIDTH
        if (self.rect.x > Win.MARGIN_LEFT + Win.WIDTH):
            self.rect.x -= Win.WIDTH

