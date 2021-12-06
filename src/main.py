import pygame
from colors import Colors
from win import Win
from player import Player

Win.BGCOLOR = Colors.CYAN

pygame.init()
screen = pygame.display.set_mode((Win.WIDTH, Win.HEIGHT))
pygame.display.set_caption("CapMan Game")
clock = pygame.time.Clock()

player = Player()
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10

main = True
while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.turn(4)
                print('turn left')
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.turn(2)
                print('turn right')
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.turn(1)
                print('turn up')
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.turn(3)
                print('turn down')
    player.update()
    screen.fill(Win.BGCOLOR)
    player_list.draw(screen)
    pygame.display.flip()
    clock.tick(Win.FPS)

pygame.quit()