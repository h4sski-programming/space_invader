import pygame

from settings import *
from sprite import Character


class Player(Character):
    def __init__(self, hp: int, x: int, y: int, surface, width: int = 20, height: int = 20) -> None:
        super().__init__(x, y, surface, width, height)
        self.hp = hp
        self.color = GREEN
        self.h_speed = 0
        self.v_speed = 0
        self.h_speed_max = 8
        self.v_speed_max = 8
        self.acceleration = 0.4
        
        self.score = 0
        self.fire_cd = 50
        self.bullets_num_max = 5
    
    def update(self) -> None:
        if 0 < self.x + self.h_speed < RESOLUTION[0]-self.width:
            self.x += self.h_speed
        else:
            self.h_speed = 0
        ### up and down movement diabled, not needed for now.
        # if 0 < self.y + self.v_speed < RESOLUTION[1]-self.height:
        #     self.y += self.v_speed
        # else:
        #     self.v_speed = 0
        super().update()
    
    def draw(self) -> None:
        super().draw()
        gun = pygame.Rect((self.x+8, self.y-10), (4,10))
        pygame.draw.rect(surface=self.surface, rect=gun, color=self.color)
        
    def move_left(self) -> None:
        # if True:
        if self.h_speed > -self.h_speed_max:
            self.h_speed -= self.acceleration
    def move_right(self) -> None:  
        if self.h_speed < self.h_speed_max:
            self.h_speed += self.acceleration    
    def move_up(self) -> None:
        if self.v_speed > -self.v_speed_max:
            self.v_speed -= self.acceleration
    def move_down(self) -> None:
        if self.v_speed < self.v_speed_max:
            self.v_speed += self.acceleration
    