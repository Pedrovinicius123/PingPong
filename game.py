#from ai.ping_pong import Machine
from movement import *
import pygame, random

def setup(func):
    # Initializing pygame
    pygame.init()
    pygame.font.init()

    # Initializing screen
    screen = pygame.display.set_mode([900, 600])
    pygame.display.set_caption("Ping Pong")

    # Initializing colors
    white = (255, 255, 255)
    black = (0, 0, 0)   

    func(screen=screen, colors=(white, black))

    pygame.quit()
    return func


@setup
def run(**kwargs):
    # Players score
    player1_points = 0
    player2_points = 0
    sair = False
    
    # Screen config
    screen = kwargs['screen']
    white, black = kwargs['colors']
    clock = pygame.time.Clock() # FPS  
    screen_size_y = 600 # Screen height    

    # Bar objects
    pad1 = pygame.Rect(60, screen_size_y/2 - 10, 10, 70)
    pad2 = pygame.Rect(840, screen_size_y/2 - 10, 10, 70)

    # ball object
    pos_ball_x = 450
    pos_ball_y = screen_size_y/2
    
    #Initial function
    initial_function = initial_random_movement(1.5)

    # Initial screen
    screen.fill(black)
    pygame.draw.rect(screen, white, pad1)
    pygame.draw.rect(screen, white, pad2)

    while not sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True

        pygame.draw.circle(screen, white, (pos_ball_x, pos_ball_y), 5)
        pos_ball_y = initial_function(pos_ball_x)
        pos_ball_x += 13

        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    try:
        run()

    except Exception as err:
        pass
