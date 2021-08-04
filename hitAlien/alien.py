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

    def blitme(self):
        self.screen.blit(self.image,self.rect)