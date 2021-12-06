import pygame
from colors import Colors
from win import Win
from player import Player
from ghost import Ghost

Win.BGCOLOR = Colors.DARK_GRAY

pygame.init()
screen = pygame.display.set_mode((Win.WIDTH, Win.HEIGHT))
pygame.display.set_caption("CapMan Game")
clock = pygame.time.Clock()

player = Player()
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 8

def drawGrid():
    blockSize = Win.GRID_SIZE #Set the size of the grid block
    for x in range(0, Win.WIDTH, blockSize):
        for y in range(0, Win.HEIGHT, blockSize):
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
    player_list.draw(screen)
    pygame.display.flip()
    clock.tick(Win.FPS)

pygame.quit()
