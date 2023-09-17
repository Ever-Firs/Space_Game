import pygame, control
from gun import Gun
from pygame.sprite import Group


def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption('Space')
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()

    while True:
        control.events(screen, gun, bullets)
        gun.update_gun()
        bullets.update()
        control.update(bg_color, screen, gun, bullets)


run()
