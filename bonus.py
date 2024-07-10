import pygame

from settings import *
from sprite import Character

class Bonus(Character):
    def __init__(self, x: int, y: int, 
                 surface, width: int = 20, height: int = 20,
                 type:int = 1) -> None:
        super().__init__(x, y, surface, width, height)
        self.type = type
        
        self.assign_type()
    
    def update(self):
        self.y += self.speed
        super().update()
    
    def assign_type(self) -> None:
        self.color = bonus_types[self.type]['color']
        self.speed = bonus_types[self.type]['speed']
        self.fire_cd = bonus_types[self.type]['fire_cd']
        self.acceleration = bonus_types[self.type]['acceleration']
        self.bullet_power = bonus_types[self.type]['bullet_power']
        self.bullet_speed = bonus_types[self.type]['bullet_speed']
        self.bullet_radius = bonus_types[self.type]['bullet_radius']
        self.bullets_num_max = bonus_types[self.type]['bullets_num_max']
        

# types dictionary
bonus_types = {
    # Value is 0 is a template, do not change it!
    0: {
        'color': (50, 50, 170),
        'speed': 2,
        'fire_cd': 1,
        'acceleration': 1,
        'bullet_power': 0,
        'bullet_speed': 0,
        'bullet_radius': 0,
        'bullets_num_max': 0,
        },
    1: {
        'color': BONUS_FIRE_CD,
        'speed': 2,
        'fire_cd': 0.8,
        'acceleration': 1,
        'bullet_power': 0,
        'bullet_speed': 0,
        'bullet_radius': 0,
        'bullets_num_max': 0,
        },
    2: {
        'color': BONUS_BULLETS_MAX,
        'speed': 2,
        'fire_cd': 1,
        'acceleration': 1,
        'bullet_power': 0,
        'bullet_speed': 0,
        'bullet_radius': 0,
        'bullets_num_max': 2,
        },
    3: {
        'color': BONUS___,
        'speed': 2,
        'fire_cd': 1,
        'acceleration': 1,
        'player_speed': 1,
        'bullet_power': 0,
        'bullet_speed': 0,
        'bullet_radius': 0,
        'bullets_num_max': 0,
        },
    4: {
        'color': BONUS_BULLET_POWER,
        'speed': 2,
        'fire_cd': 1,
        'acceleration': 1,
        'bullet_power': 1,
        'bullet_speed': 0,
        'bullet_radius': 0,
        'bullets_num_max': 0,
        },
    5: {
        'color': BONUS_BULLET_SPEED,
        'speed': 2,
        'fire_cd': 1,
        'acceleration': 1,
        'bullet_power': 0,
        'bullet_speed': 1,
        'bullet_radius': 0,
        'bullets_num_max': 0,
        },
    6: {
        'color': BONUS_BULLET_RADIUS,
        'speed': 2,
        'fire_cd': 1,
        'acceleration': 1,
        'bullet_power': 0,
        'bullet_speed': 0,
        'bullet_radius': 1,
        'bullets_num_max': 0,
        },
    7: {
        'color': BONUS_ACCELERATION,
        'speed': 2,
        'fire_cd': 1,
        'acceleration': 1.1,
        'bullet_power': 0,
        'bullet_speed': 0,
        'bullet_radius': 1,
        'bullets_num_max': 0,
        },
}