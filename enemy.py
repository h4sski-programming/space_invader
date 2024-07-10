import pygame

from sprite import Character


class Enemy(Character, pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, 
                 surface, width: int = 20, height: int = 20,
                 type:int = 1) -> None:
        super().__init__(x, y, surface, width, height)
        self.type = type
        self.assign_type()
    
    def update(self):
        self.y += self.speed
        super().update()
        # self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))
    
    def assign_type(self):
        self.color = enemy_types[self.type]['color']
        self.hp = enemy_types[self.type]['hp']
        self.speed = enemy_types[self.type]['speed']
        self.value = enemy_types[self.type]['value']
        self.bonus_probability = enemy_types[self.type]['bonus_probability']
    
enemy_types = {
    # Value is 0 is a template, do not change it!
    0: {
        'color': (250, 0, 0),
        'hp': 1,
        'speed': 1,
        'value': 1,
        'bonus_probability': 0.15,
    },
    1: {
        'color': (250, 0, 0),
        'hp': 1,
        'speed': 1,
        'value': 1,
        'bonus_probability': 0.15,
    },
    2: {
        'color': (170, 50, 0),
        'hp': 3,
        'speed': 1,
        'value': 2,
        'bonus_probability': 0.13,
    },
    3: {
        'color': (170, 0, 50),
        'hp': 5,
        'speed': 1,
        'value': 3,
        'bonus_probability': 0.12,
    },
    4: {
        'color': (100, 50, 50),
        'hp': 8,
        'speed': 1,
        'value': 4,
        'bonus_probability': 0.11,
    },
    5: {
        'color': (150, 100, 0),
        'hp': 14,
        'speed': 1,
        'value': 5,
        'bonus_probability': 0.1,
    },
}