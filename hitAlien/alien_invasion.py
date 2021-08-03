import pygame
from setting import Setting
from ship import Ship
import game_function as game_f
from pygame.sprite import Group

def run_game():
    """初始化游戏并建立一个屏幕对象"""
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("Alian Invasion")

    ship = Ship(screen,ai_setting)
    bullets = Group()
    bg_color = (230,230,230)
    while True:
        game_f.check_events(ai_setting, screen, ship, bullets)
        ship.update_location()
        bullets.update()
        game_f.update_screen(ai_setting, screen, ship, bullets)

run_game()
