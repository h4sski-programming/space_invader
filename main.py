import pygame
import math
import random

from settings import *
from enemy import Enemy
from player import Player
from bullet import Bullet
from bonus import Bonus


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
        self.bonuses_list = pygame.sprite.Group()
        self.bullets_list = pygame.sprite.Group()
        self.enemy_cd = 1_000
        self.enemy_spawn()
        self.last_time_fire = 0
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == ENEMY_SPAWN:
                rand_x = random.randint(10, RESOLUTION[0]-30)
                self.enemys_list.add(Enemy(rand_x, -19, self.main_screen,
                                           type=random.randint(1, self.player.level//2 if self.player.level <1 else 1)))
            
        
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
        
        for bonus in pygame.sprite.spritecollide(sprite=self.player, group=self.bonuses_list, dokill=False):
            self.assign_bonus_to_player(bonus)
            bonus.kill()
        
        # fire bullet
        if keys[pygame.K_p] and self.can_fire():
            b_x = self.player.x + (self.player.width/2)
            b_y = self.player.y - 8
            b = Bullet(x=b_x, y=b_y, surface=self.main_screen, angle=math.radians(-90),
                       player=self.player)
            self.bullets_list.add(b)
            self.last_time_fire = pygame.time.get_ticks()
        
    
    def update(self) -> None:
        
        # enemys
        enemys_to_delete = []
        for enemy in self.enemys_list.sprites():
            enemy.update()
            if not self.is_fit_in_surface(enemy.x, enemy.y, enemy.width, enemy.height, 
                                          surface=enemy.surface) or enemy.hp <= 0:
                enemys_to_delete.append(enemy)
            for bullet in pygame.sprite.spritecollide(enemy, self.bullets_list, True):
                enemy.hp -= bullet.power
                self.player.score += enemy.value
        for enemy in enemys_to_delete:
            if enemy.bonus_probability > random.random():
                self.bonus_spawn(enemy)
            enemy.kill()
        # print(len(self.enemys_list))                # debuging
        
        # bonuses
        bonuses_to_delete = []
        for bonus in self.bonuses_list.sprites():
            bonus.update()
            if not self.is_fit_in_surface(bonus.x, bonus.y, bonus.width, bonus.height,
                                          surface=bonus.surface):
                bonuses_to_delete.append(bonus)
        for bonus in bonuses_to_delete:
            bonus.kill()
        # print(len(self.bonuses_list))                # debuging
        
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
        
        # player
        self.player.update()
    
    def draw(self) -> None:
        self.window.fill(0)
        
        ####################
        # top bar
        self.top_bar.fill(TOP_BAR_BG)
        text = pygame.font.SysFont('Comic Sans MS', TOP_BAR_HEIGHT-20).render(f'Score: {self.player.score}', False, TOP_BAR_TEXT)
        self.top_bar.blit(text, (20, 15))
        text = pygame.font.SysFont('Comic Sans MS', TOP_BAR_HEIGHT-20).render(f'Level: {self.player.level}', False, TOP_BAR_TEXT)
        self.top_bar.blit(text, (150, 15))
        # draw stats
        line_1 = f'Bullets max: {self.player.bullets_num_max}  Bullets power: {self.player.bullet_power}    Fire cd: {self.player.fire_cd * 100 // 1 /100}'
        line_2 = f'Bullets speed: {self.player.bullet_speed}    Bullets radius: {self.player.bullet_radius}'
        
        text_bullets_max = pygame.font.SysFont('Comic Sans MS', 
            BONUS_FONT_SIZE).render(f'Bullets max: {self.player.bullets_num_max}', False, BONUS_BULLETS_MAX)
        text_bullet_power = pygame.font.SysFont('Comic Sans MS', 
            BONUS_FONT_SIZE).render(f'Bullet power: {self.player.bullet_power}', False, BONUS_BULLET_POWER)
        text_fire_cd = pygame.font.SysFont('Comic Sans MS', 
            BONUS_FONT_SIZE).render(f'Fire cd: {int(self.player.fire_cd)}', False, BONUS_FIRE_CD)
        first_row_y = 5
        self.top_bar.blit(text_bullets_max, (250, first_row_y))
        self.top_bar.blit(text_bullet_power, (375, first_row_y))
        self.top_bar.blit(text_fire_cd, (500, first_row_y))
        
        text_bullet_speed = pygame.font.SysFont('Comic Sans MS', 
            BONUS_FONT_SIZE).render(f'Bullet speed: {self.player.bullet_speed}', False, BONUS_BULLET_SPEED)
        text_bullet_radius = pygame.font.SysFont('Comic Sans MS', 
            BONUS_FONT_SIZE).render(f'Bullet radius: {self.player.bullet_radius}', False, BONUS_BULLET_RADIUS)
        text_acceleration = pygame.font.SysFont('Comic Sans MS', 
            BONUS_FONT_SIZE).render(f'Acceler.: {self.player.acceleration}', False, BONUS_ACCELERATION)
        second_row_y = 30
        self.top_bar.blit(text_bullet_speed, (250, second_row_y))
        self.top_bar.blit(text_bullet_radius, (375, second_row_y))
        self.top_bar.blit(text_acceleration, (500, second_row_y))
        
                
        ####################
        # main screen
        self.main_screen.fill(MAIN_SCREEN_BG)
        for enemy in self.enemys_list:
            enemy.draw()
        
        for bonus in self.bonuses_list:
            bonus.draw()
        
        for bullet in self.bullets_list:
            bullet.draw()
        
        self.player.draw()
        
        ####################
        # bottom bar
        self.bottom_bar.fill(BOTTOM_BAR_BG_)
        
        progres_bar_ratio = (self.player.score-self.player.prev_level_score) / self.player.next_level_score
        rect = pygame.Rect((0, 0), 
                        #    (100, 10))
                           (RESOLUTION[0] * progres_bar_ratio, BOTTOM_BAR_HEIGHT))
        pygame.draw.rect(surface=self.bottom_bar, rect=rect, color=self.player.color)
        
        
        ####################
        # blit all surfaces into the main window
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
    
    def enemy_spawn(self) -> None:
        pygame.time.set_timer(event=ENEMY_SPAWN , millis=self.enemy_cd)
    
    def bonus_spawn(self, enemy) -> None:
        bonus = Bonus(x=enemy.x, y=enemy.y, surface=self.main_screen,
                      type=random.randint(1,6))
        self.bonuses_list.add(bonus)
    
    def assign_bonus_to_player(self, bonus):
        self.player.fire_cd = self.player.fire_cd * bonus.fire_cd
        self.player.acceleration = self.player.acceleration * bonus.acceleration
        self.player.bullet_power += bonus.bullet_power
        self.player.bullet_speed += bonus.bullet_speed
        self.player.bullet_radius += bonus.bullet_radius
        self.player.bullets_num_max += bonus.bullets_num_max



if __name__ == '__main__':
    game = Game()
    game.run()