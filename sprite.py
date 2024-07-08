import pygame


class Character:
    def __init__(self, hp: int, x: int, y: int, surface, width: int = 20, height: int = 20) -> None:
        self.hp = hp
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.surface = surface
        
        self.color = 'red'
    
    def update(self):
        # self.y += 1
        pass
    
    def draw(self) -> None:
        rect = pygame.Rect((self.x, self.y), (self.width, self.height))
        pygame.draw.rect(surface=self.surface, rect=rect, color=self.color)