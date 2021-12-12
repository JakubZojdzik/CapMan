import pygame
from win import Win
from player import Player
from level import Level
from points import Points
from ghost import Ghost

from random import randint

pygame.init()
screen_info = pygame.display.Info()
Win.MARGIN_LEFT = int((screen_info.current_w - Win.WIDTH) / 2)
Win.MARGIN_LEFT = Win.GRID_SIZE * round(Win.MARGIN_LEFT / Win.GRID_SIZE)
Win.MARGIN_TOP = int((screen_info.current_h - Win.HEIGHT) / 2)
Win.MARGIN_TOP = Win.GRID_SIZE * round(Win.MARGIN_TOP / Win.GRID_SIZE) - Win.GRID_SIZE
screen = pygame.display.set_mode((screen_info.current_w, screen_info.current_h))
pygame.display.set_caption("CapMan Game")
clock = pygame.time.Clock()
menu = pygame.image.load('../lib/capmenu.png')
credits=pygame.image.load('../lib/credits01.png')
run = True
current=menu
current_width=Win.MENUWIDTH
while run:
    screen.fill(Win.BGCOLOR)
    screen.blit(current, (int((screen_info.current_w - current_width) / 2),0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT: #zakończenie
            pygame.quit()
            run = False
        if event.type == pygame.KEYDOWN: #przejście do gry
            if event.key == ord(' ') or event.key==ord("p"):
                run = False
            if event.key == ord('c'):
                current=credits
                current_width=Win.SETTINSGWIDTH
            if event.key == pygame.K_LEFT:
                current=menu
                current_width = Win.MENUWIDTH
            if event.key == ord('c'):
                pygame.quit()
                run = False

player = Player(Win.MARGIN_LEFT+Win.GRID_SIZE*12.5, Win.MARGIN_TOP+Win.GRID_SIZE*14.5)
player_list = pygame.sprite.Group()
player_list.add(player)

blinky = Ghost(Win.MARGIN_LEFT+Win.GRID_SIZE*12.5, Win.MARGIN_TOP+Win.GRID_SIZE*10.5, "red")
pinky = Ghost(Win.MARGIN_LEFT+Win.GRID_SIZE*11.5, Win.MARGIN_TOP+Win.GRID_SIZE*12.5, "pink")
inky = Ghost(Win.MARGIN_LEFT+Win.GRID_SIZE*12.5, Win.MARGIN_TOP+Win.GRID_SIZE*12.5, "blue")
clyde = Ghost(Win.MARGIN_LEFT+Win.GRID_SIZE*13.5, Win.MARGIN_TOP+Win.GRID_SIZE*12.5, "orange")

ghost_list = pygame.sprite.Group()
ghost_list.add(blinky)
ghost_list.add(pinky)
ghost_list.add(inky)
ghost_list.add(clyde)

lvl = Level()

points = Points()
points.reset_points(lvl)

def next_lvl():
    lvl.lvl += 1
    points.reset_points(lvl)
    player.rect.center = (Win.MARGIN_LEFT+Win.GRID_SIZE*12.5, Win.MARGIN_TOP+Win.GRID_SIZE*14.5)

main = True
temp = 0
while main:
    temp += 1
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
            if event.key == ord('q'):
                pygame.quit()
                main = False

    ghost_list.update(lvl)
    if(temp % 15 == 0):
        blinky.trn = randint(1, 4)
        inky.trn = randint(1, 4)
        pinky.trn = randint(1, 4)
        clyde.trn = randint(1, 4)

    player.update(lvl)
    screen.fill(Win.BGCOLOR)
    #drawGrid()
    lvl.to_board(screen)
    points.to_board(screen, player)
    player_list.draw(screen)
    ghost_list.draw(screen)
    pygame.display.flip()
    clock.tick(Win.FPS)

pygame.quit()
