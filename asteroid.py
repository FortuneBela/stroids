import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH
        )

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_angle = random.uniform(20,50)
        movement_one = self.velocity.rotate(new_angle)
        movement_two = self.velocity.rotate(-new_angle)
        new_size = self.radius - ASTEROID_MIN_RADIUS
        spawn_one = Asteroid(self.position.x, self.position.y, new_size)
        spawn_two = Asteroid(self.position.x, self.position.y, new_size)
        spawn_one.velocity = movement_one * 1.2
        spawn_two.velocity = movement_two * 1.2