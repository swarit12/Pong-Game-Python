import pygame
import random
from pygame import mixer

pygame.init()
mixer.init()

# Game Specific Variables
screen_width = 700
screen_height = 600
black = (0, 0, 0)
white = (250, 250, 250)
btn_color = (255, 255, 255)
btn_color2= (100, 100, 100)
screen= pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PONG BY SWARIT")
font= pygame.font.SysFont("Comic Sans MS", 20)
font2= pygame.font.SysFont("Comic Sans MS", 30)
font1= pygame.font.SysFont("Comic Sans MS", 30)
welcome = pygame.image.load("C:\\Users\Shashank-dt\Desktop\game sprites\Pong Game\pong-logo.jpg")
welcome = pygame.transform.scale(welcome, (screen_width, screen_height)).convert_alpha()

def display_text(text, color, x, y):
    screen_text=font.render(text, True, color)
    screen.blit(screen_text, [x,y])

def display_text1(text, color, x, y):
    screen_text=font1.render(text, True, color)
    screen.blit(screen_text, [x,y])

def display_text2(text, color, x, y):
    screen_text=font2.render(text, True, color)
    screen.blit(screen_text, [x,y])

def welcome_screen():
    global current_time, button_pressed_time
    exit= False
    current_time = 0
    button_pressed_time = 0
    while not exit:
        screen.fill(white)
        screen.blit(welcome, (0,0))
        display_text("PLAYER 1 : UP ARROW (UP), DOWN ARROW (DOWN)", white, 100, 480)
        display_text("PLAYER 2 : W (UP), S (DOWN)", white, 200, 520)
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                exit=True
            if event.type== pygame.MOUSEBUTTONDOWN:
                if 300<= mouse[0] <= 300+120 and 400<= mouse[1] <= 400+50:
                    start_sound = mixer.Sound("C:\\Users\Shashank-dt\Desktop\game sprites\Pong Game\mixkit-police-short-whistle-615.wav")
                    start_sound.play()
                    game_loop()
        current_time= pygame.time.get_ticks()

        mouse = pygame.mouse.get_pos()

        if 300<= mouse[0] <= 300+120 and 400<= mouse[1] <= 400+50:
            pygame.draw.rect(screen, btn_color2, [300, 400, 120, 50])
            display_text1("Play", white, 330, 400)

        else:
            pygame.draw.rect(screen, btn_color, [300, 400, 120, 50])
            display_text1("Play", black, 330, 400)

        pygame.display.update()
def game_loop():
    exit = False
    game_over = False
    fps= 18
    velocity_y = 15
    velocity_x = 15
    player1_vel = 0
    player2_vel = 0
    ball_x = 350
    ball_y = 280
    ball1_x= 350
    ball1_y= 280
    player1_points= 0
    player2_points= 0
    player1_x = 680
    player1_y = 200
    player1_width= 11
    player1_height= 200
    player2_x = 11
    player2_y = 200
    player2_width= 12
    player2_height= 200
    ball_radius= 20
    sound= mixer.Sound("C:\\Users\Shashank-dt\Desktop\game sprites\Pong Game\paddle.wav")
    clock= pygame.time.Clock()
    start_ticks= pygame.time.get_ticks()

    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

            if event.type== pygame.KEYDOWN:
                if event.key== pygame.K_UP:
                    player1_vel-=12
                if event.key== pygame.K_DOWN:
                    player1_vel+=12
                if event.key== pygame.K_w:
                    player2_vel-=12
                if event.key== pygame.K_s:
                    player2_vel+=12
                if event.key== pygame.K_SPACE:
                    game_loop()
            if event.type== pygame.KEYUP:
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    player1_vel=0
                if event.key in (pygame.K_s, pygame.K_w):
                    player2_vel=0

        seconds = (pygame.time.get_ticks()- start_ticks)/1000
        if seconds>3:
            ball_x += velocity_x
            ball_y += velocity_y
        start_sound = mixer.Sound("C:\\Users\Shashank-dt\Desktop\game sprites\Pong Game\mixkit-police-short-whistle-615.wav")
        player1_y += player1_vel
        player2_y += player2_vel

        screen.fill(black)
        player1=pygame.draw.rect(screen, white, [player1_x, player1_y, player1_width, player1_height], 0, 4)
        player2=pygame.draw.rect(screen, white, [player2_x, player2_y, player2_width, player2_height], 0, 4)
        ball=pygame.draw.ellipse(screen, white,[ball_x/1.024,ball_y, ball_radius, ball_radius])
        ball_outline=pygame.draw.ellipse(screen, white,[ball1_x/1.105, ball1_y-22, ball_radius+50, ball_radius+50], 1)
        game_line= pygame.draw.aaline(screen, white, (screen_width/2, 0), (screen_width/2, screen_height))

        display_text("PLAYER 1: "+ str(player1_points), white, 500, 20)
        display_text("PLAYER 2: "+ str(player2_points), white, 100, 20)

        if player1.top <= 15:
            player1_y = 15
        if player1.bottom >= screen_height-15:
            player1_y = screen_height-(player1_height+15)
        if player2.top <= 15:
            player2_y = 15
        if player2.bottom >= screen_height-15:
            player2_y = screen_height-(player2_height+15)

        if ball.top<=0 or ball.bottom>= screen_height:
            velocity_y*= -1
            mixer.Sound.play(sound)

        if ball.right>=screen_width:
            player2_points+=1
            ball_x= screen_width/2
            ball_y= screen_height/2
            start_sound.play()
            velocity_x *= random.choice((1, -1))
            velocity_y *= random.choice((1, -1))

        if ball.left<= 0:
            player1_points += 1
            ball_x= screen_width/2
            ball_y= screen_height/2
            start_sound.play()
            velocity_x *= random.choice((1, -1))
            velocity_y *= random.choice((1, -1))

        if ball.colliderect(player1) or ball.colliderect(player2):
            velocity_x*=-1
            mixer.Sound.play(sound)

        if player1_points>=10:
            game_over=True

        if player2_points>=10:
            game_over= True

        if game_over:
            ball_x = velocity_x
            ball_y = velocity_y
            screen.fill(black)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = True
                if event.type== pygame.KEYDOWN:
                    if pygame.key== pygame.K_SPACE:
                        game_loop()

            player1 = pygame.draw.rect(screen, white, [player1_x, player1_y, player1_width, player1_height], 0, 4)
            player2 = pygame.draw.rect(screen, white, [player2_x, player2_y, player2_width, player2_height], 0 , 4)
            ball = pygame.draw.ellipse(screen, white, [350 , 330, ball_radius, ball_radius])
            display_text("PLAYER 1: " + str(player1_points), white, 500, 20)
            display_text("PLAYER 2: " + str(player2_points), white, 100, 20)

            if player2_points>=10:
                display_text2("GAME OVER", white, 255, 200)
                display_text2("THE WINNER IS PLAYER 2", white, 155, 250)
            elif player1_points>=10:
                display_text2("GAME OVER", white, 255, 200)
                display_text2("THE WINNER IS PLAYER 1", white, 150, 250)

        clock.tick(fps)
        pygame.display.update()

    pygame.quit()
    quit()

welcome_screen()