import pygame

from sprite import Character


class Enemy(Character, pygame.sprite.Sprite):
    def __init__(self, hp: int, x: int, y: int, 
                 surface, width: int = 20, height: int = 20,
                 value:int = 1) -> None:
        super().__init__(hp, x, y, surface, width, height)
        self.value = value
        
    def update(self):
        self.y += 1
        super().update()
        # self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))