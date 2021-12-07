import pygame
from colors import Colors
from win import Win
from player import Player
from ghost import Ghost
from level import Level

Win.BGCOLOR = Colors.DARK_GRAY

pygame.init()
screen_info = pygame.display.Info()
Win.MARGIN_LEFT = int((screen_info.current_w - Win.WIDTH) / 2)
Win.MARGIN_LEFT = Win.GRID_SIZE * round(Win.MARGIN_LEFT / Win.GRID_SIZE)
Win.MARGIN_TOP = int((screen_info.current_h - Win.HEIGHT) / 2)
Win.MARGIN_TOP = Win.GRID_SIZE * round(Win.MARGIN_TOP / Win.GRID_SIZE) - Win.GRID_SIZE
screen = pygame.display.set_mode((screen_info.current_w, screen_info.current_h))
pygame.display.set_caption("CapMan Game")
clock = pygame.time.Clock()

player = Player()
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 8

lvl = Level()

def drawGrid():
    blockSize = Win.GRID_SIZE #Set the size of the grid block
    for x in range(Win.MARGIN_LEFT, Win.WIDTH + Win.MARGIN_LEFT, blockSize):
        for y in range(Win.MARGIN_TOP, Win.HEIGHT + Win.MARGIN_TOP, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, Colors.WHITE, rect, 1)

main = True
while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.turn(4)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.turn(2)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.turn(1)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.turn(3)
    player.update()
    screen.fill(Win.BGCOLOR)
    drawGrid()
    lvl.to_board(screen)
    player_list.draw(screen)
    pygame.display.flip()
    clock.tick(Win.FPS)

pygame.quit()
