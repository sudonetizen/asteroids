import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield  import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    # groups 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
 
    dt = 0

    while running:
        # quit 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # updating player before rendering 
        updatable.update(dt)
        # fill screen with color
        screen.fill("black")            
        
        # game 
        for item in drawable:
            item.draw(screen)

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
