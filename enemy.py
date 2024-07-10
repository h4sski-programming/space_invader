import pygame

from sprite import Character


class Enemy(Character, pygame.sprite.Sprite):
    def __init__(self, hp: int, x: int, y: int, 
                 surface, width: int = 20, height: int = 20,
                 value:int = 1, bonus_probability:float = 0.2) -> None:
        super().__init__(x, y, surface, width, height)
        self.hp = hp
        self.speed = 1
        self.value = value
        self.bonus_probability = bonus_probability
    
    def update(self):
        self.y += self.speed
        super().update()
        # self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))