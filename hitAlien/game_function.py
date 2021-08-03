from bullet import Bullet
import sys
import pygame
from setting import Setting
from ship import Ship
from bullet import Bullet

def check_events(ai_setting, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ai_setting, screen, ship, bullets)
        

def check_keydown_events(event,ai_setting, screen, ship, bullets):
    print(event.type)
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        print('add bullet')
        new_bullte = Bullet(ai_setting,screen,ship)
        bullets.add(new_bullte)

def check_keyup_events(event,ai_setting, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(ai_setting, screen, ship, bullets):
    screen.fill(ai_setting.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()
        print('bullet')
    ship.blitme()

    pygame.display.flip()