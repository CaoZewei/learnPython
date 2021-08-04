import pygame
from pygame.sprite import Sprite
import random
class Alien(Sprite):
    def __init__(self, ai_setting, screen) -> None:
        super().__init__()
        self.screen = screen
        self.ai_setting =ai_setting

        self.image = pygame.image.load('res/image/alien.bmp')
        self.rect = self.image.get_rect()
        # x = random.randint(0,self.ai_setting.screen_width)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = self.rect.x
        self.y = self.rect.y

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        self.x+=(self.ai_setting.alien_speed_factor*self.ai_setting.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <=0:
            return True

