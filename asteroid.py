import circleshape
from constants import LINE_WIDTH
import pygame

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



    