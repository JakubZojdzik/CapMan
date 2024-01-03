import pygame
from pygame.locals import Rect, QUIT
from win import Win
import sys
import webbrowser
import time

screen_info = pygame.display.Info()
back_button = pygame.image.load("../assets/ingame_textures/map/yellowarrow.png")
back_button = pygame.transform.scale(back_button, (80, 80))

class Credits:
    @staticmethod
    def credits():
        screen_info = pygame.display.Info()
        width = screen_info.current_w
        height = screen_info.current_h
        if width*9 <= height*16:
            height = width * 9 // 16
        else:
            width = height * 16 // 9
        unit = width//16
        left_margin = (screen_info.current_w - width) / 2
        
        rect_size = [unit*6, unit*2]
        font = pygame.font.Font("../assets/fonts/VT323/VT323-Regular.ttf", unit)
        small_font = pygame.font.Font("../assets/fonts/VT323/VT323-Regular.ttf", unit//2)
        Win.screen.fill(Win.BGCOLOR)
        title = pygame.transform.scale(pygame.image.load("../assets/menu/capman_developers.png"), [unit*12, unit*2])
        Win.screen.blit(title, (unit*2+left_margin, 0))
        Win.screen.blit(back_button, (15, 15))

        SPRITE_WIDTH = unit * 8 // 5
        SPRITE_HEIGHT = unit * 8 // 5
        red_ghost = pygame.transform.scale(pygame.image.load("../assets/ingame_textures/ghosts/redghost/redghostright.png"), [SPRITE_WIDTH, SPRITE_HEIGHT])
        pink_ghost = pygame.transform.scale(pygame.image.load("../assets/ingame_textures/ghosts/pinkghost/pinkghostright.png"), [SPRITE_WIDTH, SPRITE_HEIGHT])
        orange_ghost = pygame.transform.scale(pygame.image.load("../assets/ingame_textures/ghosts/orangeghost/orangeghostright.png"), [SPRITE_WIDTH, SPRITE_HEIGHT])
        blue_ghost = pygame.transform.scale(pygame.image.load("../assets/ingame_textures/ghosts/blueghost/blueghostright.png"), [SPRITE_WIDTH, SPRITE_HEIGHT])
        rects = [
            [unit, unit*3, (161, 6, 15), (245, 115, 115), red_ghost, 'Jakub', 'Żojdzik', 'JakubZojdzik'],
            [unit*9, unit*3, (201, 10, 170), (245, 149, 230), pink_ghost, 'Michał', 'Węgrzyn', 'michal-wegrzyn'],
            [unit, unit*6, (204, 106, 2), (247, 177, 101), orange_ghost, 'Tymon', 'Terczyński', 'PomyslowyZiom'],
            [unit*9, unit*6, (6, 117, 201), (126, 206, 252), blue_ghost, 'Martin', 'Drelichowski', 'MDrel'],
        ]

        for i in range(len(rects)):
            rects[i][0] += left_margin

        rect_padding = unit // 10

        for rect in rects:
            pygame.draw.rect(Win.screen, rect[2], Rect(rect[0], rect[1], rect_size[0], rect_size[1]), border_radius=rect_padding*2)
            pygame.draw.rect(Win.screen, rect[3], Rect(rect[0]+rect_padding, rect[1]+rect_padding, rect_size[0]-rect_padding*2, rect_size[1]-rect_padding*2), border_radius=rect_padding*2)
            Win.screen.blit(rect[4], (rect[0]-unit*4//5, rect[1]+unit//5))
            Win.screen.blit(font.render(rect[5], True, (0,0,0)), Rect(rect[0]+unit, rect[1], rect_size[0]-unit, unit))
            Win.screen.blit(font.render(rect[6], True, (0,0,0)), Rect(rect[0]+unit, rect[1]+unit*9//10, rect_size[0]-unit, unit))
        
        buttons = [[rect[0], rect[1], *rect_size, rect[7]] for rect in rects]
        buttons.append([unit*2, 0, unit*12, unit*2, 'JakubZojdzik/CapMan'])

        open_link_time = 0.0
        opened_link_url = ''
        link_url = ''

        run = True
        while run:
            mouse_pos = pygame.mouse.get_pos()
            link_url = ''
            for button in buttons:
                if button[0] <= mouse_pos[0] <= button[0] + button[2] and button[1] <= mouse_pos[1] <= button[1] + button[3]:
                    link_url = 'github.com/'+button[4]
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if pos[0]<=100 and pos[1]<=100:
                        return
                    if link_url != '':
                        opened_link_url = link_url
                        webbrowser.open(opened_link_url)
                        open_link_time = time.time()
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == ord('q') or event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        return
            
            pygame.draw.rect(Win.screen, Win.BGCOLOR, Rect(0, unit*81/10, unit*16, unit*4/5))
            if link_url != opened_link_url and link_url != '':
                opened_link_url = ''
                open_link_time = time.time()

            if time.time() - open_link_time <= 4 and opened_link_url != '':
                text_img = small_font.render(f'Opened {opened_link_url} in your web browser', True, (255, 255, 255))
                Win.screen.blit(text_img, text_img.get_rect(center = (unit*8, unit*17//2)))
            elif link_url != '':
                text_img = small_font.render(link_url, True, (255, 255, 255))
                Win.screen.blit(text_img, text_img.get_rect(center = (unit*8, unit*17//2)))

            pygame.display.update()