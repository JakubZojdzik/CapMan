from win import Win
import pygame
import copy
from collections import deque

LVL_WIDTH = Win.WIDTH // Win.GRID_SIZE
LVL_HEIGHT = Win.HEIGHT // Win.GRID_SIZE

SPRITE_WIDTH = Win.GRID_SIZE-8
SPRITE_HEIGHT = Win.GRID_SIZE-8

img_pink = [
    pygame.transform.scale(pygame.image.load("../assets/ingame_textures/ghosts/pinkghost/pinkghostup.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../assets/ingame_textures/ghosts/pinkghost/pinkghostup.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../assets/ingame_textures/ghosts/pinkghost/pinkghostright.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../assets/ingame_textures/ghosts/pinkghost/pinkghostdown.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../assets/ingame_textures/ghosts/pinkghost/pinkghostleft.png"), [SPRITE_WIDTH, SPRITE_HEIGHT])
]
img_blue = [
    pygame.transform.scale(pygame.image.load("../assets/ingame_textures/ghosts/blueghost/blueghostup.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../assets/ingame_textures/ghosts/blueghost/blueghostup.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../assets/ingame_textures/ghosts/blueghost/blueghostright.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../assets/ingame_textures/ghosts/blueghost/blueghostdown.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../assets/ingame_textures/ghosts/blueghost/blueghostleft.png"), [SPRITE_WIDTH, SPRITE_HEIGHT])
]
img_orange = [
    pygame.transform.scale(pygame.image.load("../assets/ingame_textures/ghosts/orangeghost/orangeghostup.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../assets/ingame_textures/ghosts/orangeghost/orangeghostup.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../assets/ingame_textures/ghosts/orangeghost/orangeghostright.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../assets/ingame_textures/ghosts/orangeghost/orangeghostdown.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../assets/ingame_textures/ghosts/orangeghost/orangeghostleft.png"), [SPRITE_WIDTH, SPRITE_HEIGHT])
]
img_red = [
    pygame.transform.scale(pygame.image.load("../assets/ingame_textures/ghosts/redghost/redghostup.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../assets/ingame_textures/ghosts/redghost/redghostup.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../assets/ingame_textures/ghosts/redghost/redghostright.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../assets/ingame_textures/ghosts/redghost/redghostdown.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
    pygame.transform.scale(pygame.image.load("../assets/ingame_textures/ghosts/redghost/redghostleft.png"), [SPRITE_WIDTH, SPRITE_HEIGHT]),
]

ghost_poses = [None, None, None, None]
scatter_poses = [[[9, 9, 0]], [[15, 9, 0]], [[15, 14, 0]], [[9, 14, 0]]]


class Ghost(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, mode, color, step=3, auxiliary_variable=10):
        pygame.sprite.Sprite.__init__(self)
        self.start_pos_x = pos_x
        self.start_pos_y = pos_y
        self.color = color
        self.step = step
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
        self.direction = 0
        self.prev_mode = "chase"
        self.auxiliary_variable = float(auxiliary_variable) # closed -> start_direction , scared -> time_left
        self.img_scared = pygame.transform.scale(pygame.image.load("../assets/ingame_textures/ghosts/scaredghost.png"), [SPRITE_WIDTH, SPRITE_HEIGHT])
        self.img_scared_white = pygame.transform.scale(pygame.image.load("../assets/ingame_textures/ghosts/whiteghost.png"), [SPRITE_WIDTH, SPRITE_HEIGHT])
        self.upgrade_ghost_poses()

    def ghost_number(self):
        if self.color == "red":
            return 0
        elif self.color == "pink":
            return 1
        elif self.color == "blue":
            return 2
        else:
            return 3

    def upgrade_ghost_poses(self):
        if self.mode == "closed":
            ghost_poses[self.ghost_number()] = None
        else:
            ghost_poses[self.ghost_number()] = self.rect.center

    def resetPos(self):
        if self.mode != "closed":
            self.mode = "chase"
        self.rect.center = (self.start_pos_x, self.start_pos_y)
        self.direction = 0
        self.upgrade_ghost_poses()
        self.image = self.img_rot[self.direction]

    def is_mode_changed(self, lvlCfg, time):
        if self.mode != self.prev_mode and len(Win.pixelPos_to_gridPos(self.rect.center)) == 1:
            self.prev_mode = self.mode
            if self.mode == "chase":
                self.step = lvlCfg[1][0]
            elif self.mode == "return":
                self.step = 8
            elif self.mode == "scared":
                self.step = lvlCfg[1][1]
                self.auxiliary_variable = time + lvlCfg[2][0]
            elif self.mode == "scatter":
                self.step = lvlCfg[1][0]
            else:
                self.step = 1

    @staticmethod
    def BFS(pos, map, step, convert_to_gridPos=True, return_length=True):
        if convert_to_gridPos:
            cells = Win.pixelPos_to_gridPos(pos)
        else:
            cells = pos
        visited = copy.deepcopy(map)
        result = copy.deepcopy(map)
        for i in range(LVL_HEIGHT):
            for j in range(LVL_WIDTH):
                result[i][j] = 1000000
        queue = deque()

        it = 10
        for i in cells:
            if map[i[1]][i[0]] != 1:
                queue.append([i[0], i[1]])
                result[i[1]][i[0]] = i[2] * Win.GRID_SIZE // step
                visited[i[1]][i[0]] = it
                it += 1

        while len(queue) > 0:
            prev_cell = queue.popleft()
            curr_x = prev_cell[0] - 1
            curr_y = prev_cell[1]
            if curr_x == -1:
                curr_x = LVL_WIDTH - 1

            if visited[curr_y][curr_x] in [0, 2, 3]:
                queue.append([curr_x, curr_y])
                visited[curr_y][curr_x] = visited[prev_cell[1]][prev_cell[0]]
                result[curr_y][curr_x] = result[prev_cell[1]][prev_cell[0]] + Win.GRID_SIZE * Win.GRID_SIZE // step

            curr_x = prev_cell[0]
            curr_y = prev_cell[1] - 1
            if curr_y == -1:
                curr_y = LVL_HEIGHT - 1

            if visited[curr_y][curr_x] in [0, 2, 3]:
                queue.append([curr_x, curr_y])
                visited[curr_y][curr_x] = visited[prev_cell[1]][prev_cell[0]]
                result[curr_y][curr_x] = result[prev_cell[1]][prev_cell[0]] + Win.GRID_SIZE * Win.GRID_SIZE // step

            curr_x = prev_cell[0] + 1
            curr_y = prev_cell[1]
            if curr_x == LVL_WIDTH:
                curr_x = 0

            if visited[curr_y][curr_x] in [0, 2, 3]:
                queue.append([curr_x, curr_y])
                visited[curr_y][curr_x] = visited[prev_cell[1]][prev_cell[0]]
                result[curr_y][curr_x] = result[prev_cell[1]][prev_cell[0]] + Win.GRID_SIZE * Win.GRID_SIZE // step

            curr_x = prev_cell[0]
            curr_y = prev_cell[1] + 1
            if curr_y == LVL_HEIGHT:
                curr_y = 0

            if visited[curr_y][curr_x] in [0, 2, 3]:
                queue.append([curr_x, curr_y])
                visited[curr_y][curr_x] = visited[prev_cell[1]][prev_cell[0]]
                result[curr_y][curr_x] = result[prev_cell[1]][prev_cell[0]] + Win.GRID_SIZE * Win.GRID_SIZE // step

        if return_length:
            return result
        else:
            return visited

    def got_capman(self, capman):
        return self.rect.colliderect(capman.rect)

    @staticmethod
    def possible_moves(pos, map):
        gridPos = Win.pixelPos_to_gridPos(pos)
        result = []  # 0 - none, 1 - up, 2 - right, 3 - down, 4 - left
        if len(gridPos) == 1:
            if map[(gridPos[0][1]-1) % LVL_HEIGHT][gridPos[0][0]] != 1:
                result.append([gridPos[0][0], (gridPos[0][1]-1) % LVL_HEIGHT, Win.GRID_SIZE, 1])
            if map[gridPos[0][1]][(gridPos[0][0]+1) % LVL_WIDTH] != 1:
                result.append([(gridPos[0][0]+1) % LVL_WIDTH, gridPos[0][1], Win.GRID_SIZE, 2])
            if map[(gridPos[0][1]+1) % LVL_HEIGHT][gridPos[0][0]] != 1:
                result.append([gridPos[0][0], (gridPos[0][1]+1) % LVL_HEIGHT, Win.GRID_SIZE, 3])
            if map[gridPos[0][1]][(gridPos[0][0]-1) % LVL_WIDTH] != 1:
                result.append([(gridPos[0][0]-1) % LVL_WIDTH, gridPos[0][1], Win.GRID_SIZE, 4])
            return result
        else:
            if gridPos[0][0] == gridPos[1][0]:
                gridPos[0].append(1)
                gridPos[1].append(3)
            else:
                gridPos[0].append(4)
                gridPos[1].append(2)
            return gridPos

    def find_next_move(self, pos, map, lvlCfg, time, capstep):
        max_communication_distance = lvlCfg[0][0]
        posibble_moves = Ghost.possible_moves(self.rect.center, map)
        BFSed_map = Ghost.BFS(pos, map, capstep)
        if self.mode == "closed":
            if self.auxiliary_variable <= time:
                self.mode = "chase"
                self.is_mode_changed(lvlCfg, time)
                return self.find_next_move(pos, map, lvlCfg, time, capstep)

            if len(Win.pixelPos_to_gridPos(self.rect.center)) == 1 or self.direction == 0:
                if Win.pixelPos_to_gridPos(self.rect.center)[0][1] == 12:
                    return 1
                else:
                    return 3
            else:
                return self.direction

        elif self.mode == "chase":
            BFSed_map_self = Ghost.BFS(self.rect.center, map, Win.GRID_SIZE)
            ghost_grid_poses = []
            for i in range(len(ghost_poses)):
                if (not ghost_poses[i] is None) and (not i == self.ghost_number()):
                    gridPos = Win.pixelPos_to_gridPos(ghost_poses[i])
                    for j in gridPos:
                        if BFSed_map_self[j[1]][j[0]] <= max_communication_distance*Win.GRID_SIZE:
                            ghost_grid_poses.append(j)
            ghost_grid_poses.append(None)
            if len(Win.pixelPos_to_gridPos(self.rect.center)) == 1:
                min_length = 10000000
                for i in ghost_grid_poses:
                    if i is None:
                        continue
                    if BFSed_map[i[1]][i[0]] < min_length:
                        min_length = BFSed_map[i[1]][i[0]]
                if BFSed_map[Win.pixelPos_to_gridPos(self.rect.center)[0][1]][Win.pixelPos_to_gridPos(self.rect.center)[0][0]] < min_length:
                    min_length = 1000000
                    curr_direction = 1
                    for i in posibble_moves:
                        if BFSed_map[i[1]][i[0]] < min_length:
                            curr_direction = i[3]
                            min_length = BFSed_map[i[1]][i[0]]

                    return curr_direction
                map_copy = copy.deepcopy(map)
                max_number = -10000000000000
                best_optn = [0]
                for optn in range(len(posibble_moves)):
                    ghost_grid_poses[-1] = posibble_moves[optn].copy()
                    BFSed_map2 = Ghost.BFS(ghost_grid_poses, map, 3, False, True)
                    num_of_cells = 0
                    for i in range(LVL_HEIGHT):
                        for j in range(LVL_WIDTH):
                            if BFSed_map[i][j] >= BFSed_map2[i][j]:
                                map_copy[i][j] = 1
                    #BFSed_map3 = Ghost.BFS(pos, map_copy, 4, True, False)
                    BFSed_map3 = Ghost.BFS(pos, map_copy, Win.GRID_SIZE)
                    for i in range(LVL_HEIGHT):
                        for j in range(LVL_WIDTH):
                            if BFSed_map3[i][j] <= 360000:
                                num_of_cells -= 10000000
                                num_of_cells += (10000-BFSed_map2[i][j])*100
                    if num_of_cells > max_number:
                        best_optn = [optn]
                        max_number = num_of_cells
                    elif num_of_cells == max_number:
                        best_optn.append(optn)
                if len(best_optn) == 1:
                    return posibble_moves[best_optn[0]][3]
                else:
                    min_length = 1000000
                    curr_direction = 1
                    for i in posibble_moves:
                        if BFSed_map[i[1]][i[0]] < min_length:
                            curr_direction = i[3]
                            min_length = BFSed_map[i[1]][i[0]]

                    return curr_direction
            else:
                return self.direction

        elif self.mode == "scared":
            if self.auxiliary_variable <= time:
                self.mode = "chase"
                self.is_mode_changed(lvlCfg, time)
                return self.find_next_move(pos, map, lvlCfg, time, capstep)

            if len(Win.pixelPos_to_gridPos(self.rect.center)) == 1:
                BFSed_map = Ghost.BFS(pos, map, Win.GRID_SIZE, True, True)
                BFSed_map2 = Ghost.BFS(posibble_moves, map, 2, False, True)
                BFSed_map3 = Ghost.BFS(posibble_moves, map, 2, False, False)
                num_of_cells = [0, 0, 0, 0, 0]
                max_number = -1
                curr_direction = 1
                for i in range(LVL_HEIGHT):
                    for j in range(LVL_WIDTH):
                        if BFSed_map[i][j] <= BFSed_map2[i][j]:
                            BFSed_map3[i][j] = 9
                        num_of_cells[BFSed_map3[i][j]-9] += 1
                for i in range(1, 5):
                    if num_of_cells[i] > max_number:
                        max_number = num_of_cells[i]
                        curr_direction = posibble_moves[i-1][3]
                return curr_direction
            else:
                return self.direction

        elif self.mode == "scatter":
            if Win.pixelPos_to_gridPos(self.rect.center)[0][0] == scatter_poses[int(self.auxiliary_variable%4)][0][0] and Win.pixelPos_to_gridPos(self.rect.center)[0][1] == scatter_poses[int(self.auxiliary_variable%4)][0][1]:
                if self.auxiliary_variable == self.ghost_number() + 4:
                    self.mode = "chase"
                    self.is_mode_changed(lvlCfg, time)
                    return self.find_next_move(pos, map, lvlCfg, time, capstep)
                else:
                    self.auxiliary_variable += 1
            BFSed_map = Ghost.BFS(scatter_poses[int(self.auxiliary_variable%4)], map, self.step, False, True)
            min_length = 10000.0
            curr_direction = 1
            for i in posibble_moves:
                if BFSed_map[i[1]][i[0]] < min_length:
                    curr_direction = i[3]
                    min_length = BFSed_map[i[1]][i[0]]
            return curr_direction

        else:
            if Win.pixelPos_to_gridPos(self.rect.center)[0] == [12, 12, 0]:
                self.mode = "chase"
                self.is_mode_changed(lvlCfg, time)
                return self.find_next_move(pos, map, lvlCfg, time, capstep)
            BFSed_map = Ghost.BFS([Win.MARGIN_LEFT+Win.GRID_SIZE*12+Win.GRID_SIZE//2, Win.MARGIN_TOP+Win.GRID_SIZE*12+Win.GRID_SIZE//2], map, self.step)
            min_length = 10000.0
            curr_direction = 1
            for i in posibble_moves:
                if BFSed_map[i[1]][i[0]] < min_length:
                    curr_direction = i[3]
                    min_length = BFSed_map[i[1]][i[0]]
            return curr_direction

    def update(self, player_pos, map, time, lvlCfg, capstep):
        if int(time) % lvlCfg[2][1] == 0 and int(time) != 0 and self.mode == "chase":
            self.mode = "scatter"
            self.auxiliary_variable = self.ghost_number()

        level_grid = copy.deepcopy(map.show_board())
        self.is_mode_changed(lvlCfg, time)
        self.direction = self.find_next_move(player_pos, level_grid, lvlCfg, time, capstep)

        if self.direction == 1:
            self.rect.y -= self.step
        if self.direction == 2:
            self.rect.x += self.step
        if self.direction == 3:
            self.rect.y += self.step
        if self.direction == 4:
            self.rect.x -= self.step

        if self.rect.y < Win.MARGIN_TOP:
            self.rect.y += Win.HEIGHT
        if self.rect.y > Win.MARGIN_TOP + Win.HEIGHT:
            self.rect.y -= Win.HEIGHT

        if self.rect.x < Win.MARGIN_LEFT:
            self.rect.x += Win.WIDTH
        if self.rect.x > Win.MARGIN_LEFT + Win.WIDTH:
            self.rect.x -= Win.WIDTH

        if self.mode == "scared":
            if self.auxiliary_variable <= time+3.0:
                if int(time*10) % 10 <= 4:
                    self.image = self.img_scared_white
                else:
                    self.image = self.img_scared
            else:
                self.image = self.img_scared
        elif self.mode == "return":
            self.image = self.img_scared_white
        else:
            self.image = self.img_rot[self.direction]

        self.upgrade_ghost_poses()
