import pygame
from circleshape import CircleShape 
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
       super().__init__(x, y, PLAYER_RADIUS)
       self.rotation = 0
       self.cool_down = 0 

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.cool_down > 0: return
        self.cool_down = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
         
    def update(self, dt):
        self.cool_down -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]: self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]: self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]: self.move(-dt)
        if keys[pygame.K_SPACE]: self.shoot()
