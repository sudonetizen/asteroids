import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
 
    while running:
        # quit 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # fill screen with color
        screen.fill("black")            

        # refresh screen
        pygame.display.flip()

    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

if __name__ == "__main__":
    main()
