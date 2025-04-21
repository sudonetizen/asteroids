import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0
 
    while running:
        # quit 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # fill screen with color
        screen.fill("black")            
        
        # game 
        player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
        player.draw(screen) 

        # refresh screen
        pygame.display.flip()

        # fps 60
        dt = clock.tick(60)/1000

    #print("Starting Asteroids!")
    #print("Screen width:", SCREEN_WIDTH)
    #print("Screen height:", SCREEN_HEIGHT)
    
pygame.quit() 

if __name__ == "__main__":
    main()
