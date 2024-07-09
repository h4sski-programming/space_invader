import pygame
import math

from settings import *
from enemy import Enemy
from player import Player
from bullet import Bullet


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.running = True
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption('Space Invader @ h4sski')
        
        self.player = Player(hp=10, x=RESOLUTION[0]/2, y=RESOLUTION[1]-50, surface=self.window)
        e1 = Enemy(hp=10, x=100, y=50, surface=self.window)
        self.enemys_list = [e1]
        self.bullets_list = []
        self.last_time_fire = 0
        
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
        ### up and down movement diabled, not needed for now.
        # if keys[pygame.K_w]:
        #     self.player.move_up()
        # if keys[pygame.K_s]:
        #     self.player.move_down()
            
        # fire bullet
        if keys[pygame.K_p] and self.can_fire():
            b_x = self.player.x + (self.player.width/2)
            b_y = self.player.y - 8
            b = Bullet(x=b_x, y=b_y, surface=self.window, angle=math.radians(-90))
            self.bullets_list.append(b)
            self.last_time_fire = pygame.time.get_ticks()
        
    
    def update(self) -> None:
        
        enemys_to_delete = []
        for enemy in self.enemys_list:
            enemy.update()
            if not self.is_on_screen(enemy.x, enemy.y, enemy.width, enemy.height):
                enemys_to_delete.append(enemy)
        for enemy in enemys_to_delete:
            self.enemys_list.remove(enemy)
        print(len(self.enemys_list))
        
        # bullets
        bullets_to_delete = []
        for bullet in self.bullets_list:
            bullet.update()
            if not self.is_on_screen(x=bullet.x, y=bullet.y,
                                 width=bullet.radius, height=bullet.radius):
                bullets_to_delete.append(bullet)
                
        for bullet in bullets_to_delete:
            self.bullets_list.remove(bullet)
        # print(len(self.bullets_list))
        
        self.player.update()
    
    def draw(self) -> None:
        self.window.fill(0)
        
        for enemy in self.enemys_list:
            enemy.draw()
        
        for bullet in self.bullets_list:
            bullet.draw()
            
        self.player.draw()
        
        pygame.display.flip()
    
    def run(self) -> None:
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
    
    
    # other methods
    def can_fire(self) -> bool:
        if pygame.time.get_ticks() < self.last_time_fire + self.player.fire_cd:
            return False
        return True
    
    def is_on_screen(self, x:int, y:int, width:int, height:int) -> bool:
        if x > RESOLUTION[0]:
            return False
        if y > RESOLUTION[1]:
            return False
        if x+width < 0:
            return False
        if y+height < 0:
            return False
        return True

if __name__ == '__main__':
    game = Game()
    game.run()