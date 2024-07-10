import pygame


class Character(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, surface: pygame.Surface, width: int = 20, height: int = 20) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.surface = surface
        
        self.color = 'red'
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))
    
    def update(self):
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))
    
    def draw(self) -> None:
        pygame.draw.rect(surface=self.surface, rect=self.rect, color=self.color)