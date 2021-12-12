<<<<<<< HEAD
class Win:
    WIDTH = 960
    HEIGHT = 840
    FPS = 30
    BGCOLOR = (0, 0, 0)
    FPS = 30
    GRID_SIZE = 60
    MARGIN_TOP = 120
    MARGIN_LEFT = 240
=======
from colors import Colors

class Win:
    MENUWIDTH=794
    SETTINSGWIDTH=1195 #sorry Kuba, że wciskam swoje tu ale mam nadzieję że się nie popsuje, a będzie czyściej
    WIDTH = 625
    HEIGHT = 600
    FPS = 30
    BGCOLOR = Colors.BLACK
    FPS = 30
    GRID_SIZE = 25
    MARGIN_TOP = 120
    MARGIN_LEFT = 240

    @staticmethod
    def pixelPos_to_gridPos(x, y):
        x -= Win.MARGIN_LEFT - (Win.GRID_SIZE+1)//2
        y -= Win.MARGIN_TOP - (Win.GRID_SIZE+1)//2
        if x%Win.GRID_SIZE == 0 and y%Win.GRID_SIZE == 0:
            return [x//Win.GRID_SIZE, y//Win.GRID_SIZE, 0]
        if x%Win.GRID_SIZE == 0:
            y1 = y//Win.GRID_SIZE
            y2 = y1 + Win.GRID_SIZE
            if y2 > Win.HEIGHT:
                y2 -= Win.HEIGHT
>>>>>>> Develop
