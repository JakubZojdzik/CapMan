from win import Win
import pygame

level_grid = []
LVL_WIDTH = 25
LVL_HEIGHT = 24

SPRITE_WIDTH = Win.GRID_SIZE-8
SPRITE_HEIGHT = Win.GRID_SIZE-8

img_pink = pygame.transform.scale(pygame.image.load("../lib/pink.png"), [SPRITE_WIDTH, SPRITE_HEIGHT])

class Ghost(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, color):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.step = 25/6
        self.image = img_pink
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

    @staticmethod
    def loadLevelGrid(grid):
        level_grid = grid.copy()
        LVL_HEIGHT = len(level_grid)-1
        LVL_WIDTH = len(level_grid[0])-1


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
