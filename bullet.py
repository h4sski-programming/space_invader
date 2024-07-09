import pygame
import math

from settings import *


class Bullet:
    def __init__(self, x: int, y: int, surface: pygame.Surface, angle: float) -> None:
        self.x = x
        self.y = y
        self.surface = surface
        self.angle = angle
        
        self.color = GREEN
        self.radius = 3
        self.speed = 7
    
    def update(self) -> None:
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
      
    def draw(self) -> None:
        pygame.draw.circle(surface=self.surface, color=self.color, 
                           center=(self.x, self.y), radius=self.radius)