import pygame
import codecs
import base64
import time
from settings import Settings
from colors import Colors
from win import Win
from player import Player
from level import Level
from points import Points
from ghost import Ghost
from score import Score
from maps import Bigmap
from highscore import Highscore


pygame.init()
screen_info = pygame.display.Info()
Win.MARGIN_LEFT = int((screen_info.current_w - Win.WIDTH) / 2)
Win.MARGIN_LEFT = Win.GRID_SIZE * round(Win.MARGIN_LEFT / Win.GRID_SIZE)
Win.MARGIN_TOP = int((screen_info.current_h - Win.HEIGHT) / 2)
Win.MARGIN_TOP = Win.GRID_SIZE * round(Win.MARGIN_TOP / Win.GRID_SIZE) - Win.GRID_SIZE
screen = pygame.display.set_mode((screen_info.current_w, screen_info.current_h), pygame.FULLSCREEN)
pygame.display.set_caption("CapMan Game")
clock = pygame.time.Clock()
menu = pygame.image.load('../lib/menu/capmenu.png')
game_over = pygame.image.load('../lib/menu/game_over.png')
newlevel = pygame.image.load('../lib/menu/ekranstartowyzapasowy.png')
credits=pygame.image.load('../lib/menu/credits01.png')

player = Player(Win.MARGIN_LEFT+Win.GRID_SIZE*12.5, Win.MARGIN_TOP+Win.GRID_SIZE*14.5)
player_list = pygame.sprite.Group()
player_list.add(player)

finalscore = 0

blinky = Ghost(Win.MARGIN_LEFT+Win.GRID_SIZE*12.5, Win.MARGIN_TOP+Win.GRID_SIZE*10.5, "chase", "red")
pinky = Ghost(Win.MARGIN_LEFT+Win.GRID_SIZE*11.5, Win.MARGIN_TOP+Win.GRID_SIZE*11.5, "closed", "pink")
inky = Ghost(Win.MARGIN_LEFT+Win.GRID_SIZE*12.5, Win.MARGIN_TOP+Win.GRID_SIZE*12.5, "closed", "blue")
inky.auxiliary_variable = 3
clyde = Ghost(Win.MARGIN_LEFT+Win.GRID_SIZE*13.5, Win.MARGIN_TOP+Win.GRID_SIZE*11.5, "closed", "orange")
scary_time_off = -1
ghost_list = pygame.sprite.Group()
ghost_list.add(blinky)
ghost_list.add(pinky)
ghost_list.add(inky)
ghost_list.add(clyde)
ghost_tab = [blinky, pinky, inky, clyde]

lvl = Level()
options=Bigmap()
set=Settings()

font = pygame.font.Font("../lib/fonts/VT323/VT323-Regular.ttf", 48)

pygame.mixer.init()
death_sound = pygame.mixer.Sound('../lib/sounds/pacmandeath.mp3')
death_sound.set_volume(0.3)

ghostDeath = pygame.mixer.Sound('../lib/sounds/eatGhost.mp3')
ghostDeath.set_volume(0)
ouou = pygame.mixer.Sound('../lib/sounds/ouou.mp3')
ouou.set_volume(0)
ouou.play(-1)
ghostBack = pygame.mixer.Sound('../lib/sounds/ghostBackToBase.mp3')
ghostBack.set_volume(0)
ghostBack.play(-1)
ghostScared = pygame.mixer.Sound('../lib/sounds/scaredGhost.mp3')
ghostScared.set_volume(0)
ghostScared.play(-1)

loudness = [0.1, 0]

start_time = time.time()

points = Points()
points.reset_points(lvl)

def new_lvl(number):
    global start_time
    start_time = time.time()
    lvl.lvl = number
    lvl.lvl %= len(lvl.maps)
    points.reset_points(lvl)
    player.__init__(Win.MARGIN_LEFT+Win.GRID_SIZE*12 + Win.GRID_SIZE//2, Win.MARGIN_TOP+Win.GRID_SIZE*14 + Win.GRID_SIZE//2)
    blinky.__init__(Win.MARGIN_LEFT + Win.GRID_SIZE * 12 + Win.GRID_SIZE//2, Win.MARGIN_TOP + Win.GRID_SIZE * 10 + Win.GRID_SIZE//2, "chase", "red")
    pinky.__init__(Win.MARGIN_LEFT + Win.GRID_SIZE * 11 + Win.GRID_SIZE//2, Win.MARGIN_TOP + Win.GRID_SIZE * 11 + Win.GRID_SIZE//2, "closed", "pink")
    inky.__init__(Win.MARGIN_LEFT + Win.GRID_SIZE * 12 + Win.GRID_SIZE//2, Win.MARGIN_TOP + Win.GRID_SIZE * 12 + Win.GRID_SIZE//2, "closed", "blue")
    inky.auxiliary_variable = 3
    clyde.__init__(Win.MARGIN_LEFT + Win.GRID_SIZE * 13 + Win.GRID_SIZE//2, Win.MARGIN_TOP + Win.GRID_SIZE * 11 + Win.GRID_SIZE//2, "closed", "orange")

def draw_score(start_time):
    score_img = font.render("Score: " + str(Score.score) + "     Lives: " + str(Score.lives) + "     Time: " + str(round(time.time() - start_time)), True, (0, 255, 255))
    score_rect = score_img.get_rect(center=(screen_info.current_w / 2, Win.MARGIN_TOP + Win.HEIGHT + 50))
    screen.blit(score_img, score_rect)

def calculate_score(done):
    s = Score.score + (180 - round(time.time() - start_time)) * 50 + Score.lives * 1500
    if(s > int(Highscore.load_highscore(lvl.lvl, Settings.difficulty)) and done):
        Highscore.save_highscore(str(s), lvl.lvl, Settings.difficulty)
    return Score.score + (180 - round(time.time() - start_time)) * 50 + Score.lives * 1500

def death():
    Score.lives -= 1
    ouou.set_volume(0)
    ghostBack.set_volume(0)
    ghostScared.set_volume(0)
    death_sound.play()
    player.rect.center = Win.MARGIN_LEFT+Win.GRID_SIZE*12.5, Win.MARGIN_TOP+Win.GRID_SIZE*14.5
    global start_time
    global finalscore
    for ghost in ghost_tab:
        ghost.resetPos()
    screen.fill(Win.BGCOLOR)
    lvl.to_board(screen)
    points.to_board(screen, player)
    player_list.draw(screen)
    ghost_list.draw(screen)
    draw_score(start_time)
    pygame.display.flip()
    if(Score.lives <= 0):
        finalscore = calculate_score(False)
        end_lvl(0)
    else:
        time.sleep(1.8)
        start_time += 3

def end_lvl(is_win):
    global finalscore
    ouou.set_volume(0)
    ghostBack.set_volume(0)
    ghostScared.set_volume(0)
    run = True
    if is_win==1:
        end_img = pygame.image.load("../lib/menu/win.png")
    else:
        end_img = pygame.image.load("../lib/menu/game_over.png")
    score_img = font.render("Score: " + str(finalscore), True, Colors.WHITE)
    score_rect = score_img.get_rect(center=(screen_info.current_w / 2, (screen_info.current_h * 3) // 4))
    highscore_img = font.render("Highscore: " + str(Highscore.load_highscore(lvl.lvl, Settings.difficulty)), True, Colors.WHITE)
    if(str(Highscore.load_highscore(lvl.lvl, Settings.difficulty) == '-1')):
        highscore_img = font.render("Highscore: ?", True, Colors.WHITE)
    highscore_rect = highscore_img.get_rect(center=(screen_info.current_w / 2, (screen_info.current_h * 3) // 4 + 60))
    while run:
        screen.fill(Win.BGCOLOR)
        screen.blit(end_img, (((screen_info.current_w - Win.MENUWIDTH) // 2),0))
        screen.blit(score_img, score_rect)
        screen.blit(highscore_img, highscore_rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # zakończenie
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == ord('q') or event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER or event.key == ord('p'):
                    run = False

def menu_loop():
    global loudness
    ouou.set_volume(0)
    ghostBack.set_volume(0)
    ghostScared.set_volume(0)
    run = True
    lvl.reset()
    points.reset_points(lvl)
    player.rect.center = (Win.MARGIN_LEFT+Win.GRID_SIZE*12.5, Win.MARGIN_TOP+Win.GRID_SIZE*14.5)
    for ghost in ghost_tab:
        ghost.resetPos()
    Score.score = -5
    Score.lives = 3
    current=menu
    current_width=Win.MENUWIDTH
    while run:
        screen.fill(Win.BGCOLOR)
        screen.blit(current, (((screen_info.current_w - current_width) // 2),0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT: #zakończenie
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN: #podjęcie działan w zależności od komendy
                if event.key == ord(' ') or event.key==ord("p"): #kończy menu, przechodzi do gry
                    lvl_number=options.drawmaps(screen)
                    if lvl_number!=-1:
                        return(lvl_number)
                if event.key == ord('c'):#przechodzi do twórców
                    current=credits
                    current_width=Win.SETTINSGWIDTH
                if event.key == ord('s'):
                    loudness=set.sound()
                    pygame.mixer.music.set_volume(loudness[0])
                    death_sound.set_volume(loudness[0])
                    points.volume=loudness[0]

                if event.key == pygame.K_LEFT: #wraca do menu głównego
                    current=menu
                    current_width = Win.MENUWIDTH
                if event.key == ord('q'): #wychodzi z gry
                    pygame.quit()
                    run = False
            button = pygame.mouse.get_pressed()
            if button[0] != 0:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                if (x>screen_info.current_w//3 and x<(screen_info.current_w*2)//3):
                    name_bar_h = (screen_info.current_h*2)//5
                    remaining_h = screen_info.current_h - name_bar_h
                    if (y > name_bar_h and y < name_bar_h+(remaining_h//3)):
                        lvl_number=options.drawmaps(screen)
                        if lvl_number!=-1:
                            return(lvl_number)
                    if (y > name_bar_h+(remaining_h//3) and y < name_bar_h+(remaining_h*2)//3):
                        loudness=set.sound()
                        pygame.mixer.music.set_volume(loudness[0])
                        death_sound.set_volume(loudness[0])
                        points.volume=loudness[0]
                    if (y > name_bar_h+(remaining_h*2)//3 and y < name_bar_h+remaining_h):
                        current=credits
                        current_width=Win.SETTINSGWIDTH
                
                

def main_loop(start_lvl):
    main = True
    global scary_time_off
    global start_time
    global finalscore
    start_time = time.time()
    screen.fill(Win.BGCOLOR)
    new_lvl(start_lvl)
    lvl.to_board(screen)
    points.to_board(screen, player)
    player_list.draw(screen)
    ghost_list.draw(screen)
    draw_score(start_time)
    pygame.display.flip()
    time.sleep(2)
    start_time += 2
    state = -1
    temp = 0
    while main:
        temp += 1
        if(Score.lives <= 0):
            main = False
        if(points.is_all()):
            finalscore = calculate_score(True)
            end_lvl(1)
            main = False

        r = False
        for ghost in ghost_tab:
            if(not r):
                ouou.set_volume(loudness[0])
                ghostBack.set_volume(0)
                ghostScared.set_volume(0)
            if(ghost.mode == "scared"):
                ouou.set_volume(0)
                ghostBack.set_volume(0)
                ghostScared.set_volume(loudness[0])
                r = True
            if(ghost.mode == "return"):
                ouou.set_volume(0)
                ghostBack.set_volume(loudness[0])
                ghostScared.set_volume(0)
                break
        
        if int((time.time() - start_time)*Win.FPS) % 10 == 0:
            #inky, pinky, clyde
            if int(time.time() - start_time) == 10:
                inky.mode = "chase"
            if int(time.time() - start_time) == 20:
                pinky.mode = "chase"
            if int(time.time() - start_time) == 30:
                clyde.mode = "chase"

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
                    main = False

        ghost_list.update(player.rect.center, lvl)
        for ghost in ghost_tab:
            if(ghost.got_capman(player)):
                if(ghost.mode == "scared"):
                    Score.score += 250
                    ghostDeath.play()
                    ghost.mode = "return"
                elif(not ghost.mode == "return"):
                    death()

        player.update(lvl, state)
        if temp % 8 == 0:
            state *= -1
        screen.fill(Win.BGCOLOR)
        lvl.to_board(screen)
        if(points.to_board(screen, player)):
            for ghost in ghost_list:
                if ghost.mode != "closed":
                    ghost.mode = "scared"
                    ghost.auxiliary_variable = 8.0
        player_list.draw(screen)
        ghost_list.draw(screen)
        draw_score(start_time)
        pygame.display.flip()
        clock.tick(Win.FPS)

while(True):

    pygame.mixer.music.load("../lib/sounds/pacmansoundtrack.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    start=menu_loop()
    #print(loudness)

    #pygame.mixer.music.load("../lib/ouou.mp3")
    #pygame.mixer.music.set_volume(0.1)
    #pygame.mixer.music.play(-1)
    main_loop(start)


