import pygame
from colors import Colors

WIDTH = 1200
HEIGHT = 800
FPS = 30
BGCOLOR = Colors.CYAN

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CapMan Game")
clock = pygame.time.Clock()
i = 0
main = True
while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('turn left')
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('turn right')
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('turn up')
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                print('turn down')
 

pygame.quit()