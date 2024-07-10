import pygame
import math

from settings import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, surface: pygame.Surface, angle: float) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.x = x                  # center point
        self.y = y                  # center point
        self.surface = surface
        self.angle = angle
        self.radius = 3
        self.rect = pygame.Rect((self.x-self.radius, self.y-self.radius), 
                                (self.x+self.radius, self.y+self.radius))
        
        self.color = GREEN
        self.speed = 7
        self.power = 1
    
    def update(self) -> None:
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
        self.rect = pygame.Rect((self.x-self.radius, self.y-self.radius), 
                                (self.radius*2, self.radius*2))
      
    def draw(self) -> None:
        pygame.draw.circle(surface=self.surface, color=self.color, 
                           center=(self.x, self.y), radius=self.radius)