import pygame

from settings import *
from enemy import Enemy
from player import Player


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.running = True
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption('Space Invader @ h4sski')
        
        self.player = Player(hp=10, x=RESOLUTION[0]/2, y=RESOLUTION[1]-100, surface=self.window)
        e1 = Enemy(hp=10, x=100, y=50, surface=self.window)
        self.enemys_list = [e1]
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        
        keys = pygame.key.get_pressed()
        
        # move the player
        if keys[pygame.K_a]:
            self.player.move_left()
        if keys[pygame.K_d]:
            self.player.move_right()
        if keys[pygame.K_w]:
            self.player.move_up()
        if keys[pygame.K_s]:
            self.player.move_down()
    
    def update(self) -> None:
        
        for enemy in self.enemys_list:
            enemy.update()
        
        self.player.update()
    
    def draw(self) -> None:
        self.window.fill(0)
        
        for enemy in self.enemys_list:
            enemy.draw()
        
        self.player.draw()
        
        pygame.display.flip()
    
    def run(self) -> None:
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
        


if __name__ == '__main__':
    game = Game()
    game.run()