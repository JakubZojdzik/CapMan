from colors import Colors

class Win:
    MENUWIDTH=794
    GAMEOVERWIDTH=794
    NEWLEVELWIDTH=794
    SETTINSGWIDTH=1195 #sorry Kuba, że wciskam swoje tu ale mam nadzieję że się nie popsuje, a będzie czyściej
    WIDTH = 600
    HEIGHT = 576
    FPS = 30
    BGCOLOR = Colors.BLACK
    FPS = 30
    GRID_SIZE = 24
    MARGIN_TOP = 120
    MARGIN_LEFT = 240

    @staticmethod
    def pixelPos_to_gridPos(pos):
        x = pos[0]
        y = pos[1]
        x -= Win.MARGIN_LEFT - (Win.GRID_SIZE+1)//2
        y -= Win.MARGIN_TOP - (Win.GRID_SIZE+1)//2
        if x%Win.GRID_SIZE == 0 and y%Win.GRID_SIZE == 0:
            return [[x//Win.GRID_SIZE-1, y//Win.GRID_SIZE-1, 0]]
        if x%Win.GRID_SIZE == 0:
            x = x//Win.GRID_SIZE-1
            y1 = y//Win.GRID_SIZE - 1
            y2 = y1 + 1
            length = y % Win.GRID_SIZE
            if y2 >= Win.HEIGHT//Win.GRID_SIZE:
                y2 -= Win.HEIGHT//Win.GRID_SIZE
            if y1 < 0:
                y1 += Win.HEIGHT//Win.GRID_SIZE
            return [[x, y1, length], [x, y2, Win.GRID_SIZE-length]]
        if y%Win.GRID_SIZE == 0:
            y = y//Win.GRID_SIZE - 1
            x1 = x//Win.GRID_SIZE-1
            x2 = x1 + 1
            length = x % Win.GRID_SIZE
            if x2 >= Win.WIDTH//Win.GRID_SIZE:
                x2 -= Win.WIDTH//Win.GRID_SIZE
            if x1 < 0:
                x1 += Win.WIDTH//Win.GRID_SIZE
            return [[x1, y, length], [x2, y, Win.GRID_SIZE-length]]