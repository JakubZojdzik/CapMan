import pygame, sys
from pygame.locals import *
from win import Win
# set window size
class Settings:
   def __init__(self):
      self.title=pygame.image.load("../lib/capmantitle.png")
      self.position=0.1

   def sound(self):


      # initilaise pygame
      pygame.init()
      screen_info = pygame.display.Info()
      screen = pygame.display.set_mode((screen_info.current_w, screen_info.current_h), pygame.FULLSCREEN)
      width = screen_info.current_w/3
      height = screen_info.current_w/10

      margin_top = screen_info.current_h/3
      margin_left = int((screen_info.current_w - width) / 2)
      self.title= pygame.transform.scale(self.title, [(margin_top-20)*2.4, margin_top-20])
      blackColor = pygame.Color(0, 0, 0)
      yellowColor = pygame.Color(255, 255, 0)
      screen.fill(Win.BGCOLOR)
      screen.blit(self.title, (((screen_info.current_w - ((margin_top-20)*2.4)) / 2),0))
      # starting position
      x = margin_left+width*self.position
      pygame.draw.rect(screen, yellowColor, Rect(margin_left, margin_top, width, height))
      pygame.draw.rect(screen, blackColor, Rect(x, margin_top + 5, width/40, height-10))

      pygame.display.update()


      a = x
      while True:
         button = pygame.mouse.get_pressed()
         if button[0] != 0:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            a = x - 5
            if a < margin_left:
               a = margin_left
            if a > margin_left + width - width/40:
               a = margin_left + width - width/40
            pygame.draw.rect(screen, yellowColor, Rect(margin_left, margin_top, width, height))
            # pygame.display.update(pygame.Rect(0,0,width,height))
            pygame.draw.rect(screen, blackColor, Rect(a, margin_top + 5, width/40, height-10))
            pygame.display.update()

         # check for ESC key pressed, or pygame window closed, to quit
         for event in pygame.event.get():
            if event.type == QUIT:

               pygame.quit()
               sys.exit()
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:  # wraca do menu głównego
                  self.position=(a - margin_left) / width
                  return (a - margin_left) / width