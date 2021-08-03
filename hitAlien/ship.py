import pygame

class Ship():
    """初始化飞船"""
    def __init__(self,screen,ai_setting) -> None:
        self.screen = screen
        self.image = pygame.image.load('res/image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.ai_setting = ai_setting

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False
        self.moving_bottom = False
        self.moving_top = False

    def blitme(self):
        """指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def update_location(self):
        """更新飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center+=self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center-=self.ai_setting.ship_speed_factor

        self.rect.centerx = self.center