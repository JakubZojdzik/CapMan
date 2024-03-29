import pygame
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
from credits import Credits

pygame.init()
pygame.display.set_caption("CapMan")
pygame.display.set_icon(pygame.image.load("../assets/ingame_textures/player/Player_right.png"))
screen_info = pygame.display.Info()

Win.MARGIN_LEFT = int((screen_info.current_w - Win.WIDTH) / 2)
Win.MARGIN_LEFT = Win.GRID_SIZE * round(Win.MARGIN_LEFT / Win.GRID_SIZE)
Win.MARGIN_TOP = int((screen_info.current_h - Win.HEIGHT) / 2)
Win.MARGIN_TOP = Win.GRID_SIZE * round(Win.MARGIN_TOP / Win.GRID_SIZE) - Win.GRID_SIZE

Win.screen = pygame.display.set_mode((screen_info.current_w, screen_info.current_h), pygame.FULLSCREEN)
clock = pygame.time.Clock()

title = pygame.image.load('../assets/menu/capmantitle.png')
game_over = pygame.image.load('../assets/menu/game_over.png')
play_button = pygame.image.load('../assets/menu/play_button.png')
settings_button = pygame.image.load('../assets/menu/settings_button.png')
credits_button = pygame.image.load('../assets/menu/credits_button.png')
paused_screen = pygame.image.load("../assets/ingame_textures/map/play_shade.png")
pause_button = pygame.image.load("../assets/ingame_textures/map/pause.png")
pause_button = pygame.transform.scale(pause_button, (80, 80))
back_button = pygame.image.load("../assets/ingame_textures/map/yellowarrow.png")
back_button = pygame.transform.scale(back_button, (80, 80))

player = Player(Win.MARGIN_LEFT+Win.GRID_SIZE*12.5, Win.MARGIN_TOP+Win.GRID_SIZE*14.5)
player_list = pygame.sprite.Group()
player_list.add(player)

finalscore = 0

blinky = Ghost(Win.MARGIN_LEFT+Win.GRID_SIZE*12.5, Win.MARGIN_TOP+Win.GRID_SIZE*10.5, "chase", "red")
pinky = Ghost(Win.MARGIN_LEFT+Win.GRID_SIZE*11.5, Win.MARGIN_TOP+Win.GRID_SIZE*11.5, "closed", "pink")
inky = Ghost(Win.MARGIN_LEFT+Win.GRID_SIZE*12.5, Win.MARGIN_TOP+Win.GRID_SIZE*12.5, "closed", "blue")
clyde = Ghost(Win.MARGIN_LEFT+Win.GRID_SIZE*13.5, Win.MARGIN_TOP+Win.GRID_SIZE*11.5, "closed", "orange")

inky.auxiliary_variable = 3
scary_time_off = -1

ghost_list = pygame.sprite.Group()
ghost_list.add(blinky)
ghost_list.add(pinky)
ghost_list.add(inky)
ghost_list.add(clyde)
ghost_tab = [blinky, pinky, inky, clyde]

lvl = Level()
options = Bigmap()

font = pygame.font.Font("../assets/fonts/VT323/VT323-Regular.ttf", 48)

pygame.mixer.init()
soundtrack = pygame.mixer.Sound("../assets/sounds/pacmansoundtrack.mp3")
soundtrack.set_volume(Settings.volume)
death_sound = pygame.mixer.Sound('../assets/sounds/pacmandeath.mp3')
death_sound.set_volume(Settings.volume)
ghostDeath = pygame.mixer.Sound('../assets/sounds/eatGhost.mp3')
ghostDeath.set_volume(0)
ouou = pygame.mixer.Sound('../assets/sounds/ouou.mp3')
ouou.set_volume(0)
ouou.play(-1)
ghostBack = pygame.mixer.Sound('../assets/sounds/ghostBackToBase.mp3')
ghostBack.set_volume(0)
ghostBack.play(-1)
ghostScared = pygame.mixer.Sound('../assets/sounds/scaredGhost.mp3')
ghostScared.set_volume(0)
ghostScared.play(-1)

start_time = time.time()
pause_time = None

points = Points()
points.reset_points(lvl)

def get_time():
    global start_time
    global pause_time
    if pause_time is None:
        return time.time() - start_time
    return pause_time - start_time

def pause_game():
    global start_time
    global pause_time
    if pause_time is None:
        pause_time = time.time()
    else:
        start_time += time.time() - pause_time
        pause_time = None

def new_lvl(number):
    Score.score = 0
    Score.lives = 3
    Score.bonus = 0
    global start_time
    global pause_time
    start_time = time.time()
    pause_time = None
    lvl.lvl = number
    lvl.lvl %= len(lvl.maps)
    points.reset_points(lvl)
    player.__init__(Win.MARGIN_LEFT+Win.GRID_SIZE*12 + Win.GRID_SIZE//2, Win.MARGIN_TOP+Win.GRID_SIZE*14 + Win.GRID_SIZE//2)
    player.step = lvl.mapsCfg[lvl.lvl][Settings.difficulty][4][0]
    ghost_step = lvl.mapsCfg[lvl.lvl][Settings.difficulty][1][0]
    blinky.__init__(Win.MARGIN_LEFT + Win.GRID_SIZE * 12 + Win.GRID_SIZE//2, Win.MARGIN_TOP + Win.GRID_SIZE * 10 + Win.GRID_SIZE//2, "chase", "red", ghost_step, 0)
    pinky.__init__(Win.MARGIN_LEFT + Win.GRID_SIZE * 11 + Win.GRID_SIZE//2, Win.MARGIN_TOP + Win.GRID_SIZE * 11 + Win.GRID_SIZE//2, "closed", "pink", ghost_step, lvl.mapsCfg[lvl.lvl][Settings.difficulty][3][0])
    inky.__init__(Win.MARGIN_LEFT + Win.GRID_SIZE * 12 + Win.GRID_SIZE//2, Win.MARGIN_TOP + Win.GRID_SIZE * 12 + Win.GRID_SIZE//2, "closed", "blue", ghost_step, lvl.mapsCfg[lvl.lvl][Settings.difficulty][3][1])
    clyde.__init__(Win.MARGIN_LEFT + Win.GRID_SIZE * 13 + Win.GRID_SIZE//2, Win.MARGIN_TOP + Win.GRID_SIZE * 11 + Win.GRID_SIZE//2, "closed", "orange", ghost_step, lvl.mapsCfg[lvl.lvl][Settings.difficulty][3][2])

def draw_score(start_time):
    score_img = font.render("Score: " + str(Score.score) + "     Lives: " + str(Score.lives) + "     Time: " + str(round(get_time())), True, (0, 255, 255))
    score_rect = score_img.get_rect(center=(screen_info.current_w / 2, Win.MARGIN_TOP + Win.HEIGHT + 50))
    Win.screen.blit(score_img, score_rect)

def calculate_score(is_win):
    s = Score.score
    if is_win:
        s += Score.bonus
    return s

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
    Win.screen.fill(Win.BGCOLOR)
    lvl.to_board()
    points.to_board(player)
    player_list.draw(Win.screen)
    ghost_list.draw(Win.screen)
    draw_score(start_time)
    pygame.display.flip()
    pause_game()
    time.sleep(2)
    pause_game()

def end_lvl(is_win):
    global finalscore
    finalscore = calculate_score(is_win)
    if finalscore > Highscore.highscores[lvl.lvl][Settings.difficulty]:
        Highscore.set_highscore(finalscore, lvl.lvl, Settings.difficulty)
    ouou.set_volume(0)
    ghostBack.set_volume(0)
    ghostScared.set_volume(0)
    run = True
    if is_win==1:
        end_img = pygame.image.load("../assets/menu/win.png")
        if lvl.lvl < 7:
            Highscore.unlock(lvl.lvl+1, Settings.difficulty)
    else:
        end_img = pygame.image.load("../assets/menu/game_over.png")
    score_img = font.render("Score: " + str(finalscore), True, Colors.WHITE)
    score_rect = score_img.get_rect(center=(screen_info.current_w / 2, (screen_info.current_h * 3) // 4))
    highscore_img = font.render("Highscore: " + str(Highscore.highscores[lvl.lvl][Settings.difficulty]), True, Colors.WHITE)
    highscore_rect = highscore_img.get_rect(center=(screen_info.current_w / 2, (screen_info.current_h * 3) // 4 + 60))
    while run:
        Win.screen.fill(Win.BGCOLOR)
        Win.screen.blit(end_img, (((screen_info.current_w - Win.MENUWIDTH) // 2),0))
        Win.screen.blit(score_img, score_rect)
        Win.screen.blit(highscore_img, highscore_rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == ord('q') or event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER or event.key == pygame.K_ESCAPE:
                    run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

def main_loop():
    ouou.set_volume(0)
    ghostBack.set_volume(0)
    ghostScared.set_volume(0)
    soundtrack.set_volume(Settings.volume)
    soundtrack.play(-1)
    lvl.reset()
    points.reset_points(lvl)
    player.rect.center = (Win.MARGIN_LEFT+Win.GRID_SIZE*12.5, Win.MARGIN_TOP+Win.GRID_SIZE*14.5)
    for ghost in ghost_tab:
        ghost.resetPos()
    Score.score = 0
    Score.bonus = 0
    Score.lives = 3

    width = screen_info.current_w
    height = screen_info.current_h
    if width*9 <= height*16:
        height = width * 9 // 16
    else:
        width = height * 16 // 9
    unit = width//16
    left_margin = (screen_info.current_w - width) / 2
    global title, play_button, settings_button, credits_button
    title = pygame.transform.scale(title, [unit*15//2, unit*3])
    play_button = pygame.transform.scale(play_button, [unit*4, unit])
    settings_button = pygame.transform.scale(settings_button, [unit*4, unit])
    credits_button = pygame.transform.scale(credits_button, [unit*4, unit])

    run = True
    while run:
        Win.screen.fill(Win.BGCOLOR)
        Win.screen.blit(title, title.get_rect(center=(left_margin+unit*8, unit*3//2)))
        button_play = Win.screen.blit(play_button, play_button.get_rect(center=(left_margin+unit*8, unit*4)))
        button_settings = Win.screen.blit(settings_button, settings_button.get_rect(center=(left_margin+unit*8, unit*6)))
        button_credits = Win.screen.blit(credits_button, credits_button.get_rect(center=(left_margin+unit*8, unit*8)))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == ord(' ') or event.key==ord("p"):
                    lvl_number=options.drawmaps()
                    while lvl_number!=-1:
                        game_loop(lvl_number)
                        lvl_number=options.drawmaps()
                if event.key == ord('c'):
                    Credits.credits()

                if event.key == ord('s'):
                    Settings.settings([soundtrack, death_sound])
                
                if event.key == ord('q') or event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    run = False

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if button_play.collidepoint(pos):
                    lvl_number=options.drawmaps()
                    while lvl_number!=-1:
                        game_loop(lvl_number)
                        lvl_number=options.drawmaps()
                elif button_settings.collidepoint(pos):
                    Settings.settings([soundtrack, death_sound])
                elif button_credits.collidepoint(pos):
                    Credits.credits()

def game_loop(start_lvl):
    main = True
    global scary_time_off
    global start_time
    global finalscore
    global pause_time
    start_time = time.time()
    pause_time = None
    soundtrack.stop()
    new_lvl(start_lvl)
    Win.screen.fill(Win.BGCOLOR)
    lvl.to_board()
    points.to_board(player)
    player_list.draw(Win.screen)
    ghost_list.draw(Win.screen)
    draw_score(start_time)
    pygame.display.flip()
    time.sleep(2)
    start_time += 2
    state = -1
    temp = 0
    while main:
        temp += 1
        while not pause_time is None:
            ouou.set_volume(0)
            ghostBack.set_volume(0)
            ghostScared.set_volume(0)
            Win.screen.fill(Win.BGCOLOR)
            lvl.to_board()
            player_list.draw(Win.screen)
            ghost_list.draw(Win.screen)
            points.to_board(player)
            draw_score(start_time)
            Win.screen.blit(paused_screen, (Win.MARGIN_LEFT, Win.MARGIN_TOP))
            Win.screen.blit(back_button, (15, 15))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    main = False
                    pause_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == ord('p'):
                        pause_game()
                    if event.key == ord('q') or event.key == pygame.K_ESCAPE:
                        pause_game()
                        main = False
                if event.type == pygame.MOUSEBUTTONUP:
                    if(pygame.mouse.get_pos()[0] <= 100 and pygame.mouse.get_pos()[1] <= 100):
                        pause_game()
                        main = False
                    else:
                        pause_game()

        if(Score.lives <= 0):
            end_lvl(False)
            main = False
            break
        if(points.is_all()):
            Score.bonus += max((180 - round(get_time())),0) * Score.SCORE_TIME
            Score.bonus += Score.lives * Score.SCORE_LIFE
            end_lvl(True)
            main = False
            break

        r = False
        for ghost in ghost_tab:
            if(not r):
                ouou.set_volume(Settings.volume)
                ghostBack.set_volume(0)
                ghostScared.set_volume(0)
            if(ghost.mode == "scared"):
                ouou.set_volume(0)
                ghostBack.set_volume(0)
                ghostScared.set_volume(Settings.volume)
                r = True
            if(ghost.mode == "return"):
                ouou.set_volume(0)
                ghostBack.set_volume(Settings.volume)
                ghostScared.set_volume(0)
                break

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
                if event.key == ord('p'):
                    pause_game()
                if event.key == ord('q') or event.key == pygame.K_ESCAPE:
                    main = False
            
            if event.type == pygame.MOUSEBUTTONUP:
                if(120 <= pygame.mouse.get_pos()[0] <= 200 and pygame.mouse.get_pos()[1] <= 100):
                    pause_game()

        ghost_list.update(player.rect.center, lvl, get_time(), lvl.mapsCfg[lvl.lvl][Settings.difficulty], player.step)
        for ghost in ghost_tab:
            if(ghost.got_capman(player)):
                if(ghost.mode == "scared"):
                    Score.score += Score.SCORE_GHOST[0]
                    Score.bonus += Score.SCORE_GHOST[1]
                    ghostDeath.play()
                    ghost.mode = "return"
                elif(not ghost.mode == "return"):
                    death()

        player.update(lvl, state)
        if temp % 8 == 0:
            state *= -1
        Win.screen.fill(Win.BGCOLOR)
        lvl.to_board()
        if(points.to_board(player)):
            for ghost in ghost_list:
                if ghost.mode != "closed":
                    ghost.mode = "scared"
                    ghost.auxiliary_variable = ghost.auxiliary_variable = get_time() + lvl.mapsCfg[lvl.lvl][Settings.difficulty][2][0]

        if len(Win.pixelPos_to_gridPos(player.rect.center)) == 1:
            is_any_ghost_scared = False
            for ghost in ghost_list:
                if ghost.mode == "scared":
                    is_any_ghost_scared = True
            if is_any_ghost_scared:
                player.step = lvl.mapsCfg[lvl.lvl][Settings.difficulty][4][1]
            else:
                player.step = lvl.mapsCfg[lvl.lvl][Settings.difficulty][4][0]
        player_list.draw(Win.screen)
        ghost_list.draw(Win.screen)
        draw_score(start_time)
        Win.screen.blit(pause_button, (120, 15))
        pygame.display.flip()
        clock.tick(Win.FPS)

    ouou.set_volume(0)
    ghostBack.set_volume(0)
    ghostScared.set_volume(0)
    soundtrack.play(-1)

pygame.mixer.music.set_volume(Settings.volume)
main_loop()