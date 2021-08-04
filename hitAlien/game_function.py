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
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_setting, screen, ship, bullets)
    elif event.key == pygame.K_b:
        fire_super_bullet(ai_setting, screen, ship, bullets)
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

def update_bullets(ai_setting, screen, aliens, ship, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    check_bullet_alien_collisions(ai_setting, screen, aliens, ship, bullets)


def check_bullet_alien_collisions(ai_setting, screen, aliens, ship, bullets):
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_setting, screen, aliens, ship)

def fire_bullets(ai_setting, screen, ship, bullets):
    if(len(bullets)<ai_setting.bullet_allowed):
        new_bullte = Bullet(ai_setting,screen,ship)
        bullets.add(new_bullte)

def fire_super_bullet(ai_setting, screen, ship, bullets):
    if(len(bullets)<ai_setting.bullet_allowed):
        ai_setting.bullet_width = 300
        new_bullte = Bullet(ai_setting,screen,ship)
        bullets.add(new_bullte)
        ai_setting.bullet_width = 3

def create_fleet(ai_setting, screen, aliens, ship):
    alien = Alien(ai_setting, screen)
    alien_width = alien.rect.width
    number_col = get_number_aliens_x(ai_setting,alien_width)
    number_row = get_number_aliens_y(ai_setting,alien.rect.height, ship.rect.height)
    for i in range(number_col):
        for j in range(number_row):
            create_alien(ai_setting,screen,i,j,aliens)

def get_number_aliens_x(ai_setting,alien_width)->int:
    available_space_x = ai_setting.screen_width - 2*alien_width
    number_col = int(available_space_x /(2*alien_width))
    return number_col

def get_number_aliens_y(ai_setting,alien_height,ship_height):
    available_space_y = (ai_setting.screen_height - (3*alien_height)-ship_height)
    number_row = int(available_space_y/(2*alien_height))
    return number_row

def create_alien(ai_setting,screen,number_col,number_row,aliens):
    alien = Alien(ai_setting,screen)
    alien_width = alien.rect.width
    alien.x = alien_width+2*alien_width*number_col
    alien.rect.x=alien.x
    alien.y = alien.rect.height+2*alien.rect.height*number_row
    alien.rect.y=alien.y
    aliens.add(alien)

def update_aliens(ai_setting, aliens):
    check_fleet_edges(ai_setting,aliens)
    aliens.update()

def check_fleet_edges(ai_setting,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_setting,aliens)
            break

def change_fleet_direction(ai_setting,alines):
    for alien in alines.sprites():
        alien.rect.y+=ai_setting.fleet_drop_speed
    ai_setting.fleet_direction *= -1