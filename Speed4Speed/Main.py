# Dena Tayeh - 152885 - Speed4Speed
# Imports
import pygame, sys, time
from pygame.locals import *
from background import Background
from Enemy import *
from Player import *

# Setting up Frames Per Second
FPS = 75
FramePerSec = pygame.time.Clock()

# Creating colors we will use
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (192, 192, 192)

# Other constants used in the program
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Other Variables used in the program
Speed = 5
Score = 0
Lives = 3

# background music player (looped)
pygame.init()
pygame.mixer.music.load('audio/background.wav')
pygame.mixer.music.play(-1)

'''we have three main functions for our game : runHome() which runs our home and controls page, runGame() which runs 
the main game loop including player and enemies , and lose() which handles the game after losing all lives '''




def runHome():
    '''Initializing pygame, and setting Caption and Icon and size for the Game window'''
    pygame.init()
    pygame.display.set_caption("Speed4Speed")
    icon = pygame.image.load('images/Game_Logo.png')
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    '''Creating the Start game button , and setting its primary and secondary colors, font and size respectively,'''
    button_color = WHITE
    button_hover_color = GREY
    button_rect = pygame.Rect(550, 480, 220, 80)
    button_font = pygame.font.SysFont('Verdana', 30)
    button_text = button_font.render("Start Game!", True, (0, 0, 0))
    button_text_rect = button_text.get_rect(center=button_rect.center)
    '''Setting display for home screen  '''
    bk_g = pygame.image.load('images/Main Screen.png')
    bk_g = pygame.transform.scale(bk_g, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(bk_g, (0, 0))
    global Score
    Score = 0
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # seeing whether our event is quiting
                running = False

            # else we Handle mouse events to either changing button color when hovering or going to next screen
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos):  # if the button is clicked :
                    bk_g = pygame.image.load('images/Controls Screen.png')
                    bk_g = pygame.transform.scale(bk_g, (SCREEN_WIDTH, SCREEN_HEIGHT))
                    screen.blit(bk_g, (0, 0))
                    pygame.display.update()  # Displaying controls Screen before starting the game
                    pygame.time.delay(3000)  # giving control screen some time so that user is able to  read it
                    runGame(Speed, Lives)  # running the actual game after waiting for the control screen

            if event.type == pygame.MOUSEMOTION:  # the button reacting to mouse hovering over it by changing its color
                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos):
                    button_color = button_hover_color
                else:
                    button_color = WHITE

        pygame.draw.rect(screen, button_color, button_rect)
        screen.blit(button_text, button_text_rect)  # displaying/drawing the button
        pygame.display.flip()  # updating the screen
    pygame.quit()


def runGame(SPEED, L):
    # speed and lives are given to make them global , not losing their values even if the game is run again after losing
    global Score  # to make score global/shared across elements
    pygame.init()

    # Creating our screen
    DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Setting up Sprites
    P1 = Player()  # our player
    E1 = Enemy1()  # the orange cars - provided with parameters to move it automatically
    E2 = Enemy2()  # the green cars - provided with parameters to move it automatically
    back_ground = Background(SCREEN_WIDTH, SCREEN_HEIGHT)
    # background created in a class, so it can be scrolled through continuously

    # Creating Sprites Groups while separating each type of enemy of the other
    enemies1 = pygame.sprite.Group()
    enemies1.add(E1)
    enemies2 = pygame.sprite.Group()
    enemies2.add(E2)

    # Combining moving Sprites Groups
    all_sprites = pygame.sprite.Group()
    all_sprites.add(P1)
    all_sprites.add(enemies1)
    all_sprites.add(enemies2)

    # Adding a new User event -Speeding-
    INC_SPEED = pygame.USEREVENT + 1
    # giving lives initial image
    lives = pygame.transform.scale(pygame.image.load('images/3_Lives.png'), (100, 33.3))

    # Game Loop
    while True:

        # Cycles through all occurring events
        for event in pygame.event.get():
            if event.type == INC_SPEED and SPEED < 10:
                SPEED += 0.70  # incrementing speed gradually
            if event.type == QUIT:
                pygame.quit()  # quitting if user wants to exit
                sys.exit()

        # updating screen
        back_ground.update()
        back_ground.render(DISPLAYSURF)

        # Setting up Fonts for score and displaying it, and displaying lives
        font_small = pygame.font.SysFont("Verdana", 20)
        scores = font_small.render(str(Score), True, WHITE)
        DISPLAYSURF.blit(scores, (10, 10))
        DISPLAYSURF.blit(lives, (700, 10))

        # Moving and Re-drawing all Sprites
        for entity in all_sprites:
            DISPLAYSURF.blit(entity.image, entity.rect)
            Score = entity.move(Speed, SCREEN_WIDTH, Score)
            # moving sprites and updating scores

        # To be run if collision occurs between Player and Enemy to update lives or end the game
        if pygame.sprite.spritecollideany(P1, enemies1) or pygame.sprite.spritecollideany(P1,
                                                                                          enemies2) or P1.rect.right > SCREEN_WIDTH - 275 or P1.rect.left < 265:
            pygame.mixer.Sound('audio/crash.wav').play()  # playing crash sound
            if L == 3:  # reduce number of lives and change the number of lives displayed
                lives = pygame.transform.scale(pygame.image.load('images/2_Lives.png'), (67, 33.3))
                DISPLAYSURF.blit(lives, (700, 10))
                L = 2
            elif L == 2:  # reduce number of lives and change the number of lives displayed
                lives = pygame.transform.scale(pygame.image.load('images/1_Lives.png'), (34, 33.3))
                DISPLAYSURF.blit(lives, (700, 10))
                L = 1
            else:  # ending game
                pygame.time.delay(300)
                Lose()

            time.sleep(0.8)

            # recreating player and enemies so when player hits an enemy it doesn't get stuck to it
            # so lives only decreases by one

            P1 = Player()
            E1 = Enemy1()
            E2 = Enemy2()
            back_ground = Background(SCREEN_WIDTH, SCREEN_HEIGHT)

            # Creating Sprites Groups
            enemies1 = pygame.sprite.Group()
            enemies1.add(E1)
            enemies2 = pygame.sprite.Group()
            enemies2.add(E2)

            all_sprites = pygame.sprite.Group()
            all_sprites.add(P1)
            all_sprites.add(enemies1)
            all_sprites.add(enemies2)
        pygame.display.update()
        FramePerSec.tick(FPS)


def Lose():
    # initializing
    pygame.init()

    # Creating the Play again button , and setting its primary and secondary colors, font and size respectively
    button1_color = WHITE
    button1_hover_color = GREY
    button1_rect = pygame.Rect(250, 220, 300, 100)
    button1_font = pygame.font.SysFont('Verdana', 36)
    button1_text = button1_font.render("Play again", True, BLACK)
    button1_text_rect = button1_text.get_rect(center=button1_rect.center)

    # Creating the Quit button , and setting its primary and secondary colors, font and size respectively
    button2_color = WHITE
    button2_hover_color = GREY
    button2_rect = pygame.Rect(250, 340, 300, 100)
    button2_font = pygame.font.SysFont('Verdana', 36)
    button2_text = button2_font.render("Quit", True, BLACK)
    button2_text_rect = button2_text.get_rect(center=button2_rect.center)

    # Setting the exit screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    bk_g = pygame.image.load('images/Exit Screen.png')
    bk_g = pygame.transform.scale(bk_g, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(bk_g, (0, 0))

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # we Handle mouse events to either changing buttons color when hovering or going to next screen or quitting
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button1_rect.collidepoint(mouse_pos):
                    runHome()
                if button2_rect.collidepoint(mouse_pos):
                    sys.exit()

            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                if button1_rect.collidepoint(mouse_pos):
                    button1_color = button1_hover_color
                else:
                    button1_color = WHITE

                if button2_rect.collidepoint(mouse_pos):
                    button2_color = button2_hover_color
                else:
                    button2_color = WHITE

        # drawing the buttons with their labels
        pygame.draw.rect(screen, button1_color, button1_rect)
        screen.blit(button1_text, button1_text_rect)
        pygame.draw.rect(screen, button2_color, button2_rect)
        screen.blit(button2_text, button2_text_rect)

        pygame.display.flip()  # updating screen
    pygame.quit()


runHome()
