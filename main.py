import pygame
import math
import random

from settings import *
from enemy import Enemy
from player import Player
from bullet import Bullet


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.font.init()
        self.running = True
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption('Space Invader @ h4sski')
        
        # create 3 surfaces
        self.top_bar = pygame.Surface((RESOLUTION[0], TOP_BAR_HEIGHT))
        self.main_screen = pygame.Surface((RESOLUTION[0], MAIN_SCREEN_HEIGHT))
        self.bottom_bar = pygame.Surface((RESOLUTION[0], BOTTOM_BAR_HEIGHT))
        
        self.player = Player(hp=10, x=RESOLUTION[0]/2, y=MAIN_SCREEN_HEIGHT-50, surface=self.main_screen)
        self.enemys_list = pygame.sprite.Group()
        self.bullets_list = pygame.sprite.Group()
        self.enemy_cd = 200
        # e1 = Enemy(hp=10, x=100, y=50, surface=self.main_screen)
        # self.enemys_list.add(e1)
        self.last_time_fire = 0
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type ==ENEMY_SPAWN:
                rand_x = random.randint(10, RESOLUTION[0]-30)
                self.enemys_list.add(Enemy(10, rand_x, -19, self.main_screen))
            print(event.type)
        
        
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
            b = Bullet(x=b_x, y=b_y, surface=self.main_screen, angle=math.radians(-90))
            self.bullets_list.add(b)
            self.last_time_fire = pygame.time.get_ticks()
        
    
    def update(self) -> None:
        
        # enemys
        enemys_to_delete = []
        for enemy in self.enemys_list.sprites():
            enemy.update()
            if not self.is_fit_in_surface(enemy.x, enemy.y, enemy.width, enemy.height, 
                                          surface=enemy.surface):
                enemys_to_delete.append(enemy)
            for bullet in pygame.sprite.spritecollide(enemy, self.bullets_list, True):
                enemy.kill()
                self.player.score += enemy.value
        for enemy in enemys_to_delete:
            enemy.kill()
        pygame.time.set_timer(event=ENEMY_SPAWN , millis=100)
        # print(len(self.enemys_list))                # debuging
        
        # bullets
        bullets_to_delete = []
        for bullet in self.bullets_list.sprites():
            bullet.update()
            if not self.is_fit_in_surface(x=bullet.x, y=bullet.y,
                                 width=bullet.radius, height=bullet.radius, 
                                 surface=bullet.surface):
                bullets_to_delete.append(bullet)
                
        for bullet in bullets_to_delete:
            bullet.kill()
        # print(len(self.bullets_list))                # debuging
        
        self.player.update()
    
    def draw(self) -> None:
        self.window.fill(0)
        
        ####################
        # top bar
        self.top_bar.fill(TOP_BAR_BG)
        text = pygame.font.SysFont('Comic Sans MS', TOP_BAR_HEIGHT-20).render(f'Score: {self.player.score}', False, TOP_BAR_TEXT)
        self.top_bar.blit(text, (50, 15))
                
        ####################
        # main screen
        self.main_screen.fill(MAIN_SCREEN_BG)
        for enemy in self.enemys_list:
            enemy.draw()
        
        for bullet in self.bullets_list:
            bullet.draw()
        
        self.player.draw()
        
        ####################
        # bottom bar
        self.bottom_bar.fill(BOTTOM_BAR_BG_)
        
        self.window.blit(self.top_bar, (0, 0))
        self.window.blit(self.main_screen, (0, TOP_BAR_HEIGHT))
        self.window.blit(self.bottom_bar, (0, RESOLUTION[1] - BOTTOM_BAR_HEIGHT))
            
        
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
        if len(self.bullets_list) >= self.player.bullets_num_max:
            return False
        return True
    
    def is_fit_in_surface(self, x:int, y:int, width:int, height:int, surface:pygame.Surface) -> bool:
        surface_rect = surface.get_rect()
        # print(surface_rect)
        if x > surface_rect[2]:
            return False
        if y > surface_rect[3]:
            return False
        if x+width < surface_rect[0]:
            return False
        if y+height < surface_rect[1]:
            return False
        return True

if __name__ == '__main__':
    game = Game()
    game.run()