import pygame

from sprite import Character

class Bonus(Character):
    def __init__(self, x: int, y: int, 
                 surface, width: int = 20, height: int = 20,
                 type:int = 1) -> None:
        super().__init__(x, y, surface, width, height)
        self.type = type
        self.speed = 2
        
        self.assign_type()
    
    def update(self):
        self.y += self.speed
        super().update()
    
    def assign_type(self) -> None:
        self.color = types[self.type]['color']
        self.fire_cd = types[self.type]['fire_cd']
        self.bullets_num_max = types[self.type]['bullets_num_max']
        self.acceleration = types[self.type]['acceleration']
        

# types dictionary
types = {
    1: {'color': (50, 50, 70),
        'fire_cd': 0.2,
        'acceleration': 1,
        'bullets_num_max': 0},
    2: {'color': (50, 50, 130),
        'fire_cd': 1,
        'acceleration': 1,
        'bullets_num_max': 5},
    3: {'color': (50, 50, 170),
        'fire_cd': 1,
        'acceleration': 2,
        'bullets_num_max': 0},
}