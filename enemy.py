import pygame

from sprite import Character


class Enemy(Character):
    def __init__(self, hp: int, x: int, y: int, surface, width: int = 20, height: int = 20) -> None:
        super().__init__(hp, x, y, surface, width, height)
        
    def update(self):
        super().update()
        self.y += 1