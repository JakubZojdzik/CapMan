import pygame, sys
from pygame.locals import *
from win import Win
# set window size
class Settings:
   def init(self):
      self.title=pygame.image.load("../lib/capmantitle.png")

   def sound(self):
      width = 640
      height = 100

      # initilaise pygame
      pygame.init()
      screen_info = pygame.display.Info()
      middle = int((screen_info.current_w - 10) / 2)
      margin_left = int((screen_info.current_w - width) / 2)

      margin_top = 200

      Win.MARGIN_TOP = int((screen_info.current_h - height) / 2)

      screen = pygame.display.set_mode((screen_info.current_w, screen_info.current_h), pygame.FULLSCREEN)
      blackColor = pygame.Color(0, 0, 0)
      yellowColor = pygame.Color(255, 255, 0)
      screen.fill(Win.BGCOLOR)
      # starting position
      x = middle
      pygame.draw.rect(screen, yellowColor, Rect(margin_left, margin_top, width, height))
      pygame.draw.rect(screen, blackColor, Rect(x, margin_top + 5, 10, 90))

      pygame.display.update()

      s = 0
      a = x
      while s == 0:
         button = pygame.mouse.get_pressed()
         if button[0] != 0:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            a = x - 5
            if a < margin_left:
               a = margin_left
            if a > margin_left + width - 10:
               a = margin_left + width - 10
            pygame.draw.rect(screen, yellowColor, Rect(margin_left, margin_top, width, height))
            # pygame.display.update(pygame.Rect(0,0,width,height))
            pygame.draw.rect(screen, blackColor, Rect(a, margin_top + 5, 10, 90))
            pygame.display.update()

         # check for ESC key pressed, or pygame window closed, to quit
         for event in pygame.event.get():
            if event.type == QUIT:

               pygame.quit()
               sys.exit()
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:  # wraca do menu głównego
                  return (a - margin_left) / 630