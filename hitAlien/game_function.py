from bullet import Bullet
import sys
import pygame
from setting import Setting
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        fire_bullets(ai_setting, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event,ai_setting, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(ai_setting, screen, ship, bullets,aliens):
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullets(ai_setting, screen, ship, bullets):
    if(len(bullets)<ai_setting.bullet_allowed):
        new_bullte = Bullet(ai_setting,screen,ship)
        bullets.add(new_bullte)

def create_fleet(ai_setting, screen, aliens):
    alien = Alien(ai_setting, screen)
    alien_width = alien.rect.width
    available_space_x = ai_setting.screen_width - 2*alien_width
    number_alien = int(available_space_x /(2*alien_width))

    for i in range(number_alien):
        alien = Alien(ai_setting,screen)
        alien.x = alien_width+2*alien_width*i
        alien.rect.x=alien.x
        aliens.add(alien)