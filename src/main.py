import pygame
from colors import Colors
from win import Win
from player import Player
from level import Level
from points import Points

pygame.init()
screen_info = pygame.display.Info()
Win.MARGIN_LEFT = int((screen_info.current_w - Win.WIDTH) / 2)
Win.MARGIN_LEFT = Win.GRID_SIZE * round(Win.MARGIN_LEFT / Win.GRID_SIZE)
Win.MARGIN_TOP = int((screen_info.current_h - Win.HEIGHT) / 2)
Win.MARGIN_TOP = Win.GRID_SIZE * round(Win.MARGIN_TOP / Win.GRID_SIZE) - Win.GRID_SIZE
screen = pygame.display.set_mode((screen_info.current_w, screen_info.current_h))
pygame.display.set_caption("CapMan Game")
clock = pygame.time.Clock()
moja_grafika = pygame.image.load('../lib/ekranstartowyzapasowy.png')
run = True
while run:
    screen.blit(moja_grafika, (350,0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == ord(' '):
                run = False

player = Player()
player_list = pygame.sprite.Group()
player_list.add(player)

lvl = Level()

points = Points()
points.reset_points(lvl)

def next_lvl():
    lvl.lvl += 1
    points.reset_points(lvl)

main = True
while main:
    if(points.is_all()):
        next_lvl()
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
    player.update(lvl)
    screen.fill(Win.BGCOLOR)
    # drawGrid()
    lvl.to_board(screen)
    points.to_board(screen, player)
    player_list.draw(screen)
    pygame.display.flip()
    clock.tick(Win.FPS)

pygame.quit()
