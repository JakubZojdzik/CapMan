level_grid = []
WIDTH = 25
HEIGHT = 24

class Ghost:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    @staticmethod
    def loadLevelGrid(grid):
        level_grid = grid.copy()
        HEIGHT = len(level_grid)
        WIDTH = len(level_grid[0])


    @staticmethod
    def BFS(x,y):
        visited = level_grid.copy()
        result = level_grid.copy()
        width =
        for i in range(HEIGHT):
            for j in range(WIDTH):
                result[i][j] *= 10000

        queue = [[x, y]]
        while queue:
            vertex = queue.pop(0)
            if visited[(vertex[0]+HEIGHT-1)%HEIGHT][vertex[1]] == 0:
                queue.append()
