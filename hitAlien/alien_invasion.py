from game_stats import GameStats
import pygame
from setting import Setting
from ship import Ship
import game_function as game_f
from pygame.sprite import Group
from game_stats import GameStats
from Button import Button
from scoreboard import Scoreboard
def run_game():
    """初始化游戏并建立一个屏幕对象"""
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("Alian Invasion")
    aliens = Group()
    ship = Ship(screen,ai_setting)
    bullets = Group()
    game_f.create_fleet(ai_setting, screen, aliens, ship)
    stats = GameStats(ai_setting)
    button = Button(ai_setting,screen,"Play")
    score = Scoreboard(ai_setting,screen,stats)
    while True:
        game_f.check_events(ai_setting, screen, ship, aliens, bullets, button, stats,score)
        if stats.game_active:
            ship.update_location()
            game_f.update_bullets(ai_setting, screen, aliens, ship, bullets,stats,score)
            game_f.update_aliens(ai_setting, screen, aliens, ship, bullets, stats,score)
        game_f.update_screen(ai_setting, screen, ship, bullets,aliens,button,stats,score)

run_game()
