import pygame
import codecs
import base64
import time
from win import Win
from player import Player
from level import Level
from points import Points
from ghost import Ghost
from score import Score

pygame.init()
screen_info = pygame.display.Info()
Win.MARGIN_LEFT = int((screen_info.current_w - Win.WIDTH) / 2)
Win.MARGIN_LEFT = Win.GRID_SIZE * round(Win.MARGIN_LEFT / Win.GRID_SIZE)
Win.MARGIN_TOP = int((screen_info.current_h - Win.HEIGHT) / 2)
Win.MARGIN_TOP = Win.GRID_SIZE * round(Win.MARGIN_TOP / Win.GRID_SIZE) - Win.GRID_SIZE
screen = pygame.display.set_mode((screen_info.current_w, screen_info.current_h), pygame.FULLSCREEN)
pygame.display.set_caption("CapMan Game")
clock = pygame.time.Clock()
menu = pygame.image.load('../lib/capmenu.png')
game_over = pygame.image.load('../lib/game_over.png')
newlevel = pygame.image.load('../lib/ekranstartowyzapasowy.png')
credits=pygame.image.load('../lib/credits01.png')

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

font = pygame.font.Font("../lib/VT323/VT323-Regular.ttf", 48)

pygame.mixer.init()
death_sound = pygame.mixer.Sound('../lib/pacmandeath.mp3')
death_sound.set_volume(0.3)

start_time = time.time()

points = Points()
points.reset_points(lvl)

def xor_str(a,b):
    xored = []
    for i in range(max(len(a), len(b))):
        xored_value = ord(a[i%len(a)]) ^ ord(b[i%len(b)])
        xored.append(hex(xored_value)[2:])
    return ''.join(xored)

def encode(value):
    value = base64.b64encode(bytes(value, "utf-8"))
    value = str(value)[2:-1]
    value = codecs.encode(value, 'rot_13')
    value = base64.b64encode(bytes(value, "utf-8"))
    value = str(value)[2:-1]
    value = base64.b64encode(bytes(value, "utf-8"))
    value = str(value)[2:-1]
    value = base64.b64encode(bytes(value, "utf-8"))
    value = str(value)[2:-1]
    value = base64.b64encode(bytes(value, "utf-8"))
    value = str(value)[2:-1]
    value = codecs.encode(value, 'rot_13')
    return value

def decode(value):
    value = codecs.encode(value, 'rot_13')
    value = base64.b64decode(value)
    value = str(value)[2:-1]
    value = base64.b64decode(value)
    value = str(value)[2:-1]
    value = base64.b64decode(value)
    value = str(value)[2:-1]
    value = base64.b64decode(value)
    value = str(value)[2:-1]
    value = codecs.encode(value, 'rot_13')
    value = str(value)
    value = base64.b64decode(value)
    return str(value)[2:-1]

def load_highscore():
    f = open('../lib/ExtreamlyNormalFile.png', "r")
    return(decode(str(f.read())))
        

def save_highscore(score):
    file = open('../lib/ExtreamlyNormalFile.png', 'w')
    file.truncate()
    file.write(encode(score))
    file.close()

def next_lvl():
    global start_time
    start_time = time.time()
    lvl.lvl += 1
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

def death():
    Score.lives -= 1
    player.rect.center = Win.MARGIN_LEFT+Win.GRID_SIZE*12.5, Win.MARGIN_TOP+Win.GRID_SIZE*14.5
    global start_time
    global finalscore
    # finalscore = 
    for ghost in ghost_tab:
        ghost.resetPos()
    screen.fill(Win.BGCOLOR)
    #drawGrid()
    lvl.to_board(screen)
    points.to_board(screen, player)
    player_list.draw(screen)
    ghost_list.draw(screen)
    draw_score(start_time)
    pygame.display.flip()
    if(Score.lives <= 0):
        current=game_over
        current_width=Win.GAMEOVERWIDTH
        screen.fill(Win.BGCOLOR)
        screen.blit(current, (int((screen_info.current_w - current_width) / 2),0))
        pygame.display.update()
        time.sleep(5)
        return
    death_sound.play()
    time.sleep(1.8)
    start_time += 3


def menu_loop():
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
                if event.key == ord('q'):
                    pygame.quit()
                    run = False

def main_loop():
    main = True
    scared = False
    global scary_time_off
    global start_time
    start_time = time.time()
    screen.fill(Win.BGCOLOR)
    lvl.lvl -= 1
    next_lvl()
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
            current=newlevel
            current_width=Win.NEWLEVELWIDTH
            screen.fill(Win.BGCOLOR)
            screen.blit(current, (int((screen_info.current_w - current_width) / 2),0))
            pygame.display.update()
            time.sleep(5)
            next_lvl()
        
        '''if(time.time() - scary_time_off >= 0 and time.time() - scary_time_off < 60 / Win.FPS):
            for ghost in ghost_list:
                ghost.mode = "chase"
            scary_time_off = -1
            scared = False'''
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
            #scary_time_off = time.time() + 8
            #scared = True
        player_list.draw(screen)
        ghost_list.draw(screen)
        draw_score(start_time)
        pygame.display.flip()
        clock.tick(Win.FPS)

while(True):
    pygame.mixer.music.load("../lib/pacmansoundtrack.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(0)
    menu_loop()

    main_loop()
