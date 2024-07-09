import pygame

from settings import *
from sprite import Character


class Player(Character):
    def __init__(self, hp: int, x: int, y: int, surface, width: int = 20, height: int = 20) -> None:
        super().__init__(hp, x, y, surface, width, height)
        self.color = GREEN
        self.h_speed = 3
        self.v_speed = 3
        self.fire_cd = 100
    
    def update(self) -> None:
        return super().update()
    
    def draw(self) -> None:
        super().draw()
        gun = pygame.Rect((self.x+8, self.y-10), (4,10))
        pygame.draw.rect(surface=self.surface, rect=gun, color=self.color)
        
    def move_left(self) -> None:
        if self.x > 0:
            self.x -= self.h_speed
    def move_right(self) -> None:
        if self.x + self.width < RESOLUTION[0]:
            self.x += self.h_speed        
    def move_up(self) -> None:
        if self.y > 0:
            self.y -= self.v_speed
    def move_down(self) -> None:
        if self.y + self.height < RESOLUTION[1]:
            self.y += self.v_speed