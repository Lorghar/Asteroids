import circleshape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
import pygame
from logger import log_event
import random

#define Asteroid class
class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

#     def rotate(self, dt):
#         self.rotation += PLAYER_TURN_SPEED * dt

#     def move(self, dt):
#         unit_vector = pygame.Vector2(0, 1)
#         rotated_vector = unit_vector.rotate(self.rotation)
#         rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
#         self.position += rotated_with_speed_vector


        
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            new_asteroid_movement = self.velocity.rotate(angle)
            second_asteroid_movement = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid.velocity = new_asteroid_movement * 1.2
            second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            second_asteroid.velocity = second_asteroid_movement * 1.2
            

    